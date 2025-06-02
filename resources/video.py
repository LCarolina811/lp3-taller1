"""
Recursos y rutas para la API de videos
"""
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from models.video import VideoModel
from models import db

# Campos para serializar respuestas
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

# Parser para los argumentos en solicitudes PUT (crear video)
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Nombre del video es requerido", required=True)
video_put_args.add_argument("views", type=int, help="Número de vistas del video", required=True)
video_put_args.add_argument("likes", type=int, help="Número de likes del video", required=True)

# Parser para los argumentos en solicitudes PATCH (actualizar video)
video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Nombre del video")
video_update_args.add_argument("views", type=int, help="Número de vistas del video")
video_update_args.add_argument("likes", type=int, help="Número de likes del video")

def abort_if_video_doesnt_exist(video_id):
    """
    Verifica si un video existe, y si no, aborta la solicitud
    
    Args:
        video_id (int): ID del video a verificar
    """
    video = VideoModel.query.filter_by(id=video_id).first()
    if not video:
        abort(404, message=f"No se encontró un video con el ID {video_id}")
    return video

class Video(Resource):
    """
    Recurso para gestionar videos individuales
    
    Métodos:
        get: Obtener un video por ID
        put: Crear un nuevo video
        patch: Actualizar un video existente
        delete: Eliminar un video
    """
    
    @marshal_with(resource_fields)
    def get(self, video_id):
        """
        Obtiene un video por su ID
        
        Args:
            video_id (int): ID del video a obtener
            
        Returns:
            VideoModel: El video solicitado
            ---
        parameters:
          - name: video_id
            in: path
            type: integer
            required: true
            description: ID del video a obtener
        responses:
          200:
            description: Video encontrado
            schema:
              id: Video
              properties:
                id:
                  type: integer
                  example: 1
                name:
                  type: string
                  example: "Mi primer video"
                views:
                  type: integer
                  example: 100
                likes:
                  type: integer
                  example: 10
          404:
            description: No se encontró un video con el ID especificado
        """
        # TODO
        video = abort_if_video_doesnt_exist(video_id)
        return video
        pass
    
    @marshal_with(resource_fields)
    def put(self, video_id):
        """
        Crea un nuevo video con un ID específico
        
        Args:
            video_id (int): ID para el nuevo video
            
        Returns:
            VideoModel: El video creado
            ---
        parameters:
          - name: video_id
            in: path
            type: integer
            required: true
            description: ID para el nuevo video
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                name:
                  type: string
                  example: "Mi primer video"
                views:
                  type: integer
                  example: 100
                likes:
                  type: integer
                  example: 10
        responses:
          201:
            description: Video creado exitosamente
            schema:
              id: Video
              properties:
                id:
                  type: integer
                name:
                  type: string
                views:
                  type: integer
                likes:
                  type: integer
          409:
            description: Ya existe un video con ese ID
        """
        # TODO
        existing_video = VideoModel.query.filter_by(id=video_id).first()
        if existing_video:
            abort(409, message=f"Ya existe un video con el ID {video_id}")
    
        args = video_put_args.parse_args()
        
        new_video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        
        db.session.add(new_video)
        db.session.commit()
        
        return new_video
        pass
    
    @marshal_with(resource_fields)
    def patch(self, video_id):
        """
        Actualiza un video existente
        
        Args:
            video_id (int): ID del video a actualizar
            
        Returns:
            VideoModel: El video actualizado
            ---
        parameters:
          - name: video_id
            in: path
            type: integer
            required: true
            description: ID del video a actualizar
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                name:
                  type: string
                  example: "Nuevo nombre"
                views:
                  type: integer
                  example: 200
                likes:
                  type: integer
                  example: 20
        responses:
          200:
            description: Video actualizado exitosamente
            schema:
              id: Video
              properties:
                id:
                  type: integer
                name:
                  type: string
                views:
                  type: integer
                likes:
                  type: integer
          404:
            description: No se encontró un video con el ID especificado
        """
        # TODO
        video = abort_if_video_doesnt_exist(video_id)
        
        args = video_update_args.parse_args()
    
        if args['name'] is not None:
            video.name = args['name']
        if args['views'] is not None:
            video.views = args['views']
        if args['likes'] is not None:
            video.likes = args['likes']
    
        db.session.commit()
    
        return video
        pass
    
    def delete(self, video_id):
        """
        Elimina un video existente
        
        Args:
            video_id (int): ID del video a eliminar
            
        Returns:
            str: Mensaje vacío con código 204
            ---
        parameters:
          - name: video_id
            in: path
            type: integer
            required: true
            description: ID del video a eliminar
        responses:
          204:
            description: Video eliminado exitosamente
          404:
            description: No se encontró un video con el ID especificado
        """
        # TODO
        video = abort_if_video_doesnt_exist(video_id)

        db.session.delete(video)
        db.session.commit()

        return '', 204
        pass

