# QGIS_administracion_en_red
Permite tener varios equipos en red con la misma configuración y personalización de QGIS

El qgis cada vez que se abre, busca un script de python concreto startup.py en y si existe en C:\Users\usuario_x\AppData\Roaming\QGIS\QGIS3 lo ejecuta. Su única función es llamar a otro script SIGMENA.PY este ya en una unidad de red con todas las ordenes que queramos meter. Podemos cambiar este último script que está en red y que comprueban todos los usuarios al arrancar y siempre estarán actualizados. 

TAREAS QUE EJECUTA

1.Comprueba si están instalados y activados los complementos que se consideren interesantes, si no lo están los instala. (sigpac, alidadas, gpsdescargacarga, hectáreas, silvilidar, zoomSigmena).

2.Añade si no lo están los wms que consideremos (catastro y ortofotos).

3.Pone los sistemas de referencia por defecto de capas y proyectos en edtr89.

4.Configura el paso de ed50 a etrs89 con la rejilla del IGN, (de momento hay que poner el archivo de la rejilla en c, a mano para darle permisos de administrador).

5.En la versión 3.10 muestra los avisos que queramos mostrar, con nueva información y acceso a la web que nos interese mostrar.

6.Configura el repositorio de complementos que queramos, Sigmena en este caso.

7.Configura la ruta con las plantillas para los mapas O:Sigmena/leyendas.

8.Establece la codificación de caracteres a Latin por defecto.

9. Establece la semitransparencia para las selección de capas.

10.	Establece que las mediciones se hagan en planimétricas.

11.Establece una personalización del programa, ocultando botones que no se suelen utilizar para hacer el manejo más sencillo.


INSTRUCCIONES DE INSTALACION

  startup.py hay que ponerlo en C:\Users\usuario_x\AppData\Roaming\QGIS\QGIS3  en cada equipo en el que queremos que funcione.

  SIGMENA.py hay que ponerlo en O:/sigmena/utilidad/PROGRAMA/QGIS/

  SPED2ETv2.gsb hay que ponerlo en O:/sigmena/utilidad/PROGRAMA/QGIS/ , aunque de momento no funciona por un tema de permisos y hay que pegarlo a mano en C:/Program Files/QGIS 3.10/share/proj/SPED2ETV2.gsb. 

  QGISCUSTOMIZATION3.ini hay que ponerlo en O:/sigmena/utilidad/PROGRAMA/QGIS/ , y después él se autocopia en cada equipo si se actualiza.


Los complementos los coge de O:/sigmena/utilidad/PROGRAMA/QGIS/Complementos/ , comprimidos en zip.



