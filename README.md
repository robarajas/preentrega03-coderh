# PRE-ENTREGA #03-CODERHOUSE - ECOMMERCE
Pre-entrega #03 ecommerce - Django, modelos, templates y base de datos

## Estructura del proyecto

## Temática del proyecto
Este proyecto simula una tienda en linea donde encontrarás listado de productos y direcciones que se pueden registrar desde el sitio o módulo Admin.

### Aplicaciones
* **productos** - Aqui se administran lo relacionado a los productos de la tienda en línea.
* **direcciones** - Aquí se administran las direcciones en envío que el usuario dará de alta.

### Templates
Se crea una carpeta en raíz llamada **templates** en la cual, se crearon subcarpetas que hacen referencias a las aplicaciones del proyecto, a las vistas iniciales y al archivo base (**index.html**)

### Recursos
Se descargó una plantilla inicial desde el sitio **Start Bootstarp** (https://startbootstrap.com/template/shop-homepage#google_vignette) y los recursos descargados se pusieron en una carpeta en raíz llamada **static** (el archivo **index.html** se puso en carpeta **templates** para mejor entendimiento y organización).

## ¿Cómo usarlo?
Sigue los siguientes pasos para llevar a cabo las acciones permitidas dentro del sitio

### Productos
* **Ver productos** - En la parte superior se encuantra el NAV VAR en donde verás la opción de productos,
esta opción te redirecciona a la vista en donde se muestran los artículos registrados en base de datos. Si no hay ningún registro, solo se mostrará un mensaje avisando.
* **Registrar Producto** - Dentro del listado de productos, verás un botón que dice "Agregar producto", este botón te redirecciona al formulario, en donde tendrás que completar los campos solicitados, presionar el botón "Guardar" y se registrará el Producto. Al registrarlo te manda al listado de productos.

### Direcciones
### Productos
* **Ver Direcciones** - En la parte superior se encuantra el NAV VAR en donde verás la opción de "sirecciones",esta opción te redirecciona a la vista en donde se muestran las direcciones registradas en base de datos. Si no hay ningún registro, solo se mostrará un mensaje avisando.
* **Registrar Dirección** - Dentro del listado de direcciones, verás un botón que dice "Agregar dirección", este botón te redirecciona al formulario, en donde tendrás que completar los campos solicitados, presionar el botón "Guardar" y se registrará la nueva Dirección. Al registrarlo te manda al listado de direcciones.

## NOTAS
* Se trabajó con un entorno virtual, el archivo **requirements.txt.** contiene el listado de dependencias utilizadas en el proyecto.
* Se omite la carga de la carpeta de entorno (venv) y la base de datos (db.sqlite3) desde el archivo **.gitignore**.






