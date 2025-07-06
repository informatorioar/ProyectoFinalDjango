# Proyecto Final - Curso Desarrollo Web Python y Django 🐍 INFORMATORIO

## Tienda online - Impresion 3D

El proyecto consiste en la base de una **tienda online** de venta de productos e insumos para impresión 3D.



---
_Link de repositorio_:
[Github](https://github.com/WilsonLombardo/ProyectoFinalDjango)

***

### _Authors_:

| Apellido    |  Nombre   |
|------------ |-----------|
|👩 Fleitas   | Daniela   |
|🧑 Bottegani | Luciano   |
|🧑 Escalante | Marcelo   |
|🧑 Lombardo  | Wilson    |
---
### Fleitas, Daniela
Lider FrontEnd

Funciones:

Maquetar templates HTML con Bootstrap/CSS.

Implementar diseño responsive.

Integrar archivos estáticos (JS, CSS, imágenes).

Tareas específicas:
✔ Mejorar index.html y padre.html (carrusel, navbar).
✔ Crear formularios con django-crispy-forms.
✔ Optimizar carga de imágenes en static/.
---
...
### Escalante, Marcelo
---
Autenticación & Base de Datos
Funciones:

Implementar login/registro (Django allauth o custom).

Gestionar perfiles de usuario.

Configurar PostgreSQL/MySQL (si no usa SQLite).

Tareas específicas:
✔ Extender el modelo User con Profile.
✔ Crear vistas de login/logout.
✔ Migrar datos de prueba con fixtures.
---
...
Bottegani, Marcelo
---
Testing & Deployment
Funciones:

Escribir tests unitarios (pytest).

Configurar despliegue (Render, Vercel, Railway).

Monitorear errores en producción.

Tareas específicas:
✔ Testear vistas y modelos (test_models.py).
✔ Configurar settings.py para producción (DEBUG=False).
✔ Dockerizar la app (opcional).

---
...
Lombardo, Wilson

BackEnd

Funciones:

Gestionar la arquitectura de Django (models, views, URLs).

Implementar lógica de negocio (ej.: carrito de compras, autenticación).

Coordinar merges en Git y resolver conflictos.

Revisar PRs (Pull Requests) y asegurar consistencia en el código.

Tareas específicas:
✔ Configurar models.py (Producto, Cliente, Pedido).
✔ Crear vistas basadas en clases (ListView, CreateView).
✔ Integrar Django REST Framework (si hay API).
---

### _Applied Technologies_:
* Python 
* Django (v.4.0.1)
* Django-environ (v.0.8.1)
* Html 
* Css
* Pillow (v.10.0.0)
* Fontawesome (v.6.0.0)
* Crispy forms (v.1.14.0)

---

### _Getting start_:

1. Instalación:
    * _**Clonar repositorio**_.
    
2. Ejecución:
    * Instalar requirements.txt
    * Iniciar servidor:

        _Ubicarse en carpeta de proyecto (terminal) y ejecutar **"python manage.py runsever"**_

3. Navegando por la app
    * La aplicación se inicia en el "home". Desde allí podemos navegar hacia:

        - Nosotros: información (estilo "about us" de la tienda.)
        - Productos: allí vemos listado de productos (donde podemos modificar/borrar productos existentes, así como también crear nuevos producto).
        - Clientes: vemos el listado de clientes (estos se generan desde admin/django - BBDD sqlite3).
        - Contacto: aquí podemos enviar mensaje a la tienda (completando el formulario, este se guarda en la BBDD y además nos responde con el envío de un mail confirmando recepción del mensaje).

