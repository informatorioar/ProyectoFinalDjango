# Proyecto Final Informatorio Etapa II Desarrollo Web Django - CineClub

## Descripción
CineClub es una plataforma web desarrollada con Django para amantes del cine, donde los usuarios pueden explorar películas, leer reseñas y participar en una comunidad cinéfila. El diseño está inspirado en plataformas como Letterboxd, con un enfoque en la crítica cinematográfica profesional.

## Características principales
- Sistema de reseñas con calificación por estrellas (★ ★ ★ ★ ★)
- Catálogo de películas organizado por géneros (#Clásicos, #Indie, #Oscar, #Culto)
- Sección "Comunidad" para interacción entre usuarios
- Página "Sobre Nosotros" con la filosofía del proyecto
- Diseño responsive con Bootstrap 4
- Iconografía con Font Awesome

## Tecnologías utilizadas
- Backend: Django (Python)
- Frontend: 
  - HTML5, CSS3
  - Bootstrap 4.6
  - JavaScript
- Otros:
  - Font Awesome 6 (iconos)
  - jQuery (funcionalidades JS)

## Estructura del proyecto
ProyectoFinalDjango/

├── static/

│ ├── css/ # Estilos CSS personalizados

│ ├── js/ # JavaScript personalizado

│ ├── images/ # Imágenes del sitio (logo, banners)

│ └── fontawesomefree/ # Iconos Font Awesome

├── templates/ # Plantillas HTML

│ └── (estructura de templates Django)

└── (otros archivos Django)


## Instalación y configuración
1. Clonar el repositorio:
   git clone https://github.com/WilsonLombardo/ProyectoFinalDjango.git

2. Crear y activar entorno virtual (recomendado):
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   ./venv/Scripts/activate     # Windows

3. Instalar dependencias:
   pip install -r requirements.txt

4. Configurar base de datos (SQLite por defecto)

5. Ejecutar migraciones:
   python manage.py migrate

6. Crear superusuario:
   python manage.py createsuperuser

7. Iniciar servidor de desarrollo:
   python manage.py runserver

## Diseño destacado
- Barra de navegación negra con logo personalizado
- Secciones con estilo cinematográfico (fondo negro, acentos amarillos)
- Sistema de rating visual con estrellas amarillas (#ffc107)
- Diseño responsive para móviles (navbar toggler personalizado)
- Footer con redes sociales y créditos

## Autores
Daniela Fleitas, Luciano Bottegoni, Marcelo Escalante y Wilson Lombardo

## Contribución
Las contribuciones son bienvenidas. Por favor:
1. Haz un fork del proyecto
2. Crea una rama para tu feature (git checkout -b feature/AmazingFeature)
3. Haz commit de tus cambios (git commit -m 'Add some AmazingFeature')
4. Haz push a la rama (git push origin feature/AmazingFeature)
5. Abre un Pull Request

## Licencia
Distribuido bajo la licencia MIT. Ver `LICENSE` para más información.

## Contacto
Wilson Lombardo - [@tuusuario](https://github.com/WilsonLombardo)  
Proyecto del Informatorio Chaco 2025 - [Sitio web](https://campus-informatorio.chaco.gob.ar)
