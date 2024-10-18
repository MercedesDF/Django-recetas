
# Aplicación de Gestión de Recetas

Esta es una aplicación simple de gestión de recetas escrita en Django. Permite agregar, eliminar y buscar recetas de manera eficiente.

## Características

- **Agregar recetas**: Permite a los usuarios añadir nuevas recetas con nombre, ingredientes e instrucciones.
- **Eliminar recetas**: Los usuarios pueden eliminar recetas existentes.
- **Buscar recetas**: Los usuarios pueden buscar recetas por nombre, ingredientes o instrucciones, utilizando palabras clave.
- **Clasificación de recetas**: Las recetas se pueden clasificar en diferentes categorías como carne, pescado, verduras, pastas y postres.

## Requisitos

- Python 3.10 o superior
- Django 5.1.2 o superior

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Navega a la carpeta del proyecto:
   ```bash
   cd ruta/a/tu/proyecto
   ```
3. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv env
   source env/bin/activate  # En Linux o macOS
   env\Scriptsctivate     # En Windows
   ```
4. Instala las dependencias:
   ```bash
   pip install django
   ```
   y los requerimientos del archivo `requirements.txt`.
   pip install -r requirements.txt
   
5. Realiza las migraciones de la base de datos:
   ```bash
   python manage.py migrate
   ```
6. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```
7. Accede a la aplicación en tu navegador en `http://127.0.0.1:8000/`.

## Uso

- **Agregar receta**: Navega a `/recetas/agregar/` para añadir una nueva receta.
- **Ver lista de recetas**: La lista de recetas se muestra en la página principal.
- **Eliminar receta**: Haz clic en el enlace de eliminar junto a la receta que deseas quitar.
- **Buscar receta**: Usa el campo de búsqueda en la página principal para buscar recetas específicas.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar la aplicación, siéntete libre de hacer un fork del repositorio y enviar un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
