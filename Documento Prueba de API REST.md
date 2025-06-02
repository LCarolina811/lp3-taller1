## Pruebas de la API REST

A continuación se describen pruebas básicas para cada uno de los métodos del recurso Video (`resources/video.py`). 

### 1. Obtener un video (GET)

**Solicitud:**
```
GET http://localhost:5000/api/videos/922
```

**Respuesta esperada (200 OK):**
```json
{
  "id": 922,
  "name": "Test",
  "views": 1500,
  "likes": 120
}
```

**Caso de error (video no existe, 404):**
```json
{
  "message": "No se encontró un video con el ID 922"
}
```

---

### 2. Crear un nuevo video (PUT)

**Solicitud:**
```
PUT http://localhost:5000/api/videos/922
Content-Type: application/json

{
  "name": "Nuevo Video",
  "views": 10,
  "likes": 1
}
```

**Respuesta esperada (201 Created o 200 OK):**
```json
{
  "id": 922,
  "name": "Nuevo Video",
  "views": 10,
  "likes": 1
}
```

**Caso de error (ID ya existe, 409):**
```json
{
  "message": "Ya existe un video con el ID 922"
}
```

---

### 3. Actualizar un video (PATCH)

**Solicitud:**
```
PATCH http://localhost:5000/api/videos/922
Content-Type: application/json

{
  "views": 100,
  "likes": 10
}
```

**Respuesta esperada (200 OK):**
```json
{
  "id": 922,
  "name": "Nuevo Video",
  "views": 100,
  "likes": 10
}
```

**Caso de error (video no existe, 404):**
```json
{
  "message": "No se encontró un video con el ID 922"
}
```

---

### 4. Eliminar un video (DELETE)

**Solicitud:**
```
DELETE http://localhost:5000/api/videos/922
```

**Respuesta esperada (204 No Content):**
```
[Sin contenido]
```

**Caso de error (video no existe, 404):**
```json
{
  "message": "No se encontró un video con el ID 922"
}
```

---
