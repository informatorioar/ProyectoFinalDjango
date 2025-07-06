# Proyecto Final - Curso Python 🐍 CoderHouse

## Tienda online - Impresion 3D

El proyecto consiste en la base de una **tienda online** de venta de productos e insumos para impresión 3D.

---

[![video_ProyectoFinal](/static/images/Video_YouTube.png)](https://www.youtube.com/embed/6qYGL0aBFus)

---
_Link de repositorio_:
[Github](https://github.com/yamilb87/lambda3d.git)

***

### _Authors_:

| Apellido    |  Nombre   |
|------------ |-----------|
|👩 Ramos     | Xareni   |
|👩 Castro    | Yanina   |
|🧑 Bongioanni| Yamil    |
---
### Ramos, Xareni
---
...
### Castro, Yanina
---
Responsable en mayor medida de realizar el maquetado y revisar que las vistas del proyecto tengan la funcionalidad que se pretende.
### Bongioanni, Yamil
---
Responsable mayormente de realizar la creación de models.py, lógica de formularios y escritura/edición de BBDD mediante los views.py.


---

### _Applied Technologies_:
* Python 
* Django (v.4.0.1)
* Django-environ (v.0.8.1)
* Html 
* Css
* Pillow (v.8.4.0)
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

