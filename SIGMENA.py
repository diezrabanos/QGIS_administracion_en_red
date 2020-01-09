#este archivo es llamado desde startup.py que tiene cada usuario en su carpeta C:\Users\usuario_x\AppData\Roaming\QGIS\QGIS3 y se ejecuta cada vez que se abre el qgis 3.
#inspirado desde https://boundless-desktop.readthedocs.io/en/latest/system_admins/globalsettings.html
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSettings
from qgis.utils import iface,home_plugin_path, loadPlugin, startPlugin, plugins
from qgis.core import QgsApplication
import zipfile
import os
import shutil

#lista de complementos a tener instalados
complementos=['sigpac','alidadas','gpsDescargaCarga','hectareas','silvilidar','zoomSigmena','puntossigmena']
#lista de servicios wms a tener cargados
lista_WMS_URL=["http://ovc.catastro.meh.es/Cartografia/WMS/ServidorWMS.aspx","http://www.idee.es/wms/pnoa/pnoa?"]
lista_WMS_NAME=["Catastro","Ortofoto_reciente"]

# esta funcion es la que va a ejecutar siempre
def sigmena():
    #lo que pongamos aqui se va a reproducir cada vez que se abra un qgis en forma de ventana a la que hay que dar a aceptar, vale para informacion muy importante pero es un toston
    #QMessageBox.information(None, "SIGMENA", "Abres un QGIS configurado por SIGMENA") 
    iface.messageBar().pushMessage("SIGMENA", "Acabas de abrir una instancia de QGIS configurada por SIGMENA", duration=15)
    
#respecto a los sistemas de referencia con ello lo definimos por defecto a nivel usuario.
    crs = 'EPSG:25830'
    QSettings().setValue('/Projections/layerDefaultCrs', crs)
    QSettings().setValue("/app/projections/defaultProjectCrs", crs )
    QSettings().setValue("/app/projections/unknownCrsBehavior","UseProjectCrs")
    QSettings().setValue("/app/projections/newProjectCrsBehavior","UsePresetCrs")
    QSettings().setValue("/Projections/EPSG:23030//EPSG:25830_coordinateOp","+proj=pipeline +step +inv +proj=utm +zone=30 +ellps=intl +step +proj=hgridshift +grids=SPED2ETV2.gsb +step +proj=utm +zone=30 +ellps=GRS80")
    #Projections/showDatumTransformDialog
    
#informacion nueva en sigmena
    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20191201/title',"NOVEDAD SIGMENA 4 DICIEMBRE")
    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20191201/content',"<p>Tenemos posibilidad de tener novedades de Sigmena de esta manera, asi que ire poniendo todas las novedades de esta manera. Pincha en este texto para saber mas</p>")
    #QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20191201/image',"O:/sigmena/logos/LogoSIGMENA.jpg")
    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20191201/link','O:/sigmena/notas/Sigmena.htm')
    #QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/1000/sticky','true')
#repositorio de complementos sigmena  
    QSettings().setValue('/app/plugin_installer/checkOnStart','false')
    QSettings().setValue('/app/plugin_repositories/SIGMENA/url','https://raw.githubusercontent.com/diezrabanos/qgis_plugins/master/servidor_descargas_sigmena.xml')
    QSettings().setValue('/app/plugin_repositories/SIGMENA/authcfg','')
    QSettings().setValue('/app/plugin_repositories/Repositorio%20oficial%20de%20complementos%20de%20QGIS\enabled','false')
    QSettings().setValue('/app/plugin_repositories/SIGMENA/enabled','true')

#para instalar complementos interesantes si no estan cargados
    for elemento in complementos:
        if elemento not in plugins: 
            # Installing
            zip_ref = zipfile.ZipFile('O:/sigmena/utilidad/PROGRAMA/QGIS/Complementos/'+elemento+'.zip', 'r')
            zip_ref.extractall(home_plugin_path)
            zip_ref.close()
            loadPlugin(elemento)
            startPlugin(elemento)
        
#esto es para que si estan instalados los active    
    try:  
        QSettings().setValue('/PythonPlugins/zoomSigmena','true')
        QSettings().setValue('/PythonPlugins/alidadas','true')
        QSettings().setValue('/PythonPlugins/gpsDescargaCarga','true')
        QSettings().setValue('/PythonPlugins/hectareas','true')
        QSettings().setValue('/PythonPlugins/sigpac','true')
        QSettings().setValue('/PythonPlugins/silvilidar','true')
        QSettings().setValue('/PythonPlugins/puntossigmena','true')
    except:
        pass
#para que no pierda tiempo buscando si hay actualizaciones de los complementos instalados
    QSettings().setValue("/app/plugin_installer/checkOnStart","false")

#para anadir los wms que sean interesantes, TIRA DE LAS DOS LISTAS DE ARRIBA

    for WMS_URL, WMS_NAME in zip(lista_WMS_URL,lista_WMS_NAME):
        if "Qgis/WMS/%s/authcfg" % WMS_NAME not in QSettings().allKeys():
            QSettings().setValue("/qgis/WMS/%s/authcfg" % WMS_NAME, "")
            QSettings().setValue("/qgis/WMS/%s/username" % WMS_NAME, "")
            QSettings().setValue("/qgis/WMS/%s/password" % WMS_NAME, "")
            QSettings().setValue("/qgis/connections-wms/%s/dpiMode" % WMS_NAME, 7)
            QSettings().setValue("/qgis/connections-wms/%s/ignoreAxisOrientation" % WMS_NAME, False)
            QSettings().setValue("/qgis/connections-wms/%s/ignoreGetFeatureInfoURI" % WMS_NAME, False)
            QSettings().setValue("/qgis/connections-wms/%s/ignoreGetMapURI" % WMS_NAME, False)
            QSettings().setValue("/qgis/connections-wms/%s/invertAxisOrientation" % WMS_NAME, False)
            QSettings().setValue("/qgis/connections-wms/%s/referer" % WMS_NAME, "")
            QSettings().setValue("/qgis/connections-wms/%s/smoothPixmapTransform" % WMS_NAME, "")
            QSettings().setValue("/qgis/connections-wms/%s/url" % WMS_NAME, WMS_URL)

#para anadir las imagenes de bing,
    #QSettings().setValue("/qgis/connections-xyz/Bing%20Sat%E9lite/url","http://ecn.t3.tiles.virtualearth.net/tiles/a{q}.jpeg?g=0&dir=dir_n\x2019")
            

#para que por defecto coja la ruta donde estan las plantillas de mapas, composiciones de mapas en formato qpt
    QSettings().setValue("/app/LastComposerTemplateDir","O:/sigmena/leyendas")

#para evitar problemas con la codificacion de las capas, caracteres extranos
    QSettings().setValue("/UI/encoding","latin1")

#para establecer colores por defecto, la seleccion si no dice otra cosa el proyecto se hace en amarillo y semitransparente.
    QSettings().setValue("/qgis/default_selection_color_red","255")
    QSettings().setValue("/qgis/default_selection_color_green","255")
    QSettings().setValue("/qgis/default_selection_color_blue","0")
    QSettings().setValue("/qgis/default_selection_color_alpha","120")

#para hacer que las mediciones sean planimetricas, evitando el error por medir sobre el elipsoide
    QSettings().setValue("/qgis/measure/planimetric","true")

#copiar el archivo de rejilla necesario, no me deja por los permisos de usuario
    
    #shutil.copy('O:/sigmena/utilidad/PROGRAMA/QGIS/SPED2ETV2.gsb', 'C:/Program Files/QGIS 3.10/share/proj/SPED2ETV2.gsb')

#copiar el archivo de configuracion visual de qgis
    usuario= QgsApplication.qgisSettingsDirPath()
    shutil.copy('O:/sigmena/utilidad/PROGRAMA/QGIS/QGISCUSTOMIZATION3.ini', os.path.join(usuario,'QGIS/QGISCUSTOMIZATION3.ini'))
    

        
