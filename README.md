# Proyecto Final Curso Coderhouse - ECOMMERCE
Este proyecto es un MINI ECOMMERCE con manejo de usuarios, direcciones, productos y un chat entre usuarios. Se continuo tomando como base la **Pre-entrega #03 ecommerce - Django, modelos, templates y base de datos**

## Temática del proyecto
Este proyecto simula una tienda en linea donde encontrarás listado de productos y cuando eres un usuario registrado tienes acceso a las direcciones de envío y Chat entre usuarios; así como la administración de los diferentes apartados.

### Aplicaciones
* **productos** - Aqui se administran lo relacionado a los productos de la tienda en línea.
* **direcciones** - Aquí se administran las direcciones en envío que el usuario dará de alta.
* **usuarios** - Aquí se administran las cuentas de usuario registrados así como su actualización de datos
* **mensajeria** - Chat entre usuarios registrados

### Templates
Se crea una carpeta en raíz llamada **templates** en la cual, se crearon subcarpetas que hacen referencias a las aplicaciones del proyecto, a las vistas iniciales y al archivo base (**index.html**)

### Recursos
Se descargó una plantilla inicial desde el sitio **Start Bootstarp** (https://startbootstrap.com/template/shop-homepage#google_vignette) y los recursos descargados se pusieron en una carpeta en raíz llamada **static** (el archivo **index.html** se puso en carpeta **templates** para mejor entendimiento y organización).

## ¿Cómo usarlo el sitio?
Te dejaré por aqui un **video** colgado en una URL de acceso público donde especifica las funcionalidades del sitio, así como algunas restricciones.

* **VIDEO**: "[Da clic AQUI para ir al video en la NUBE](https://drive.google.com/file/d/1FD4-WxJnsM2Ew12l_Ay_Tdlq92RQ_7d1/view?usp=drive_link)"

## ¿Cómo correr el sitio en mi computadora? (Detalles técnicos)
* Necesitas Clonar el proyecto usando la URL del repositorio en GITHUB. Ejecuta el comando "git clone https://github.com/robarajas/preentrega03-coderh.git"
* Posicionate dentro del proyecto y crea tu entorno virtual. Ejecuta el comando "**python -m venv venv**" 
* Activa tu entorno Virtual. Ejecuta el comando ""**. venv/Scripts/activate**"
* Instala las dependencias necesarias del proyecto. Ejecuta el comando: "**pip install -r requirements.txt**"
* Una vez instaladas, solo corre la aplicación. Ejecuta el comando: "python manage.py runserver**
* Listo! Accede a la URL que te aparecerá en consola.

## NOTAS
* Se trabajó con un entorno virtual, el archivo **requirements.txt.** contiene el listado de dependencias utilizadas en el proyecto.
* Se omite la carga de la carpeta de entorno (venv) y la base de datos (db.sqlite3) desde el archivo **.gitignore**.






