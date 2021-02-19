# -*- coding: cp1252 -*-
#este archivo es llamado desde startup.py que tiene cada usuario en su carpeta C:\Users\usuario_x\AppData\Roaming\QGIS\QGIS3 y se ejecuta cada vez que se abre el qgis 3.
#inspirado desde https://boundless-desktop.readthedocs.io/en/latest/system_admins/globalsettings.html
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QToolBar, QDockWidget, QMenuBar
from qgis.utils import iface,home_plugin_path, loadPlugin, startPlugin, plugins,unloadPlugin,findPlugins
from qgis.core import QgsApplication, QgsStyle
import zipfile
import os
import shutil
#import qgis
#import configparser

#para debug
# Code for printing to a file 
#debug = open('O:/sigmena/utilidad/PROGRAMA/QGIS/Complementos/errores.txt', 'w') 
  




#lista de complementos a tener instalados
complementos_con_version=[['impresion_sigmena',"1.0.0"],['sigpac',"1.20.93"],['alidadas',"1.0.6"],['gpsDescargaCarga',"1.0.10"],['hectareas',"1.0.3"],['silvilidar',"1.0.9"],['puntossigmena',"1.0.3"],['ptos2pol',"1.0.3"],['zoomSigmena',"1.1.1"],['censosPuntos',"1.0.0"]]
#ruta archivos de estilo xml
archivosestilos=r"O:\sigmena\leyendas\QGIS_Estilo_SIGMENA/SIGMENA_SIMBOLOGIA.xml"
estilosfavoritos=['dNBR','Parcela','Recinto','MUP','Comarca Forestal', 'Cortafuego 12 m', 'Cortafuegos 3 m', 'Cortafuegos 6 m', 'Cortafuegos 9 m', 'Cotos pesca', 'Fauna Censos Itinerario', 'IMENAS', 'Incendios Puntos de Inicio', 'Incendios Quemado', 'Intrusiones', 'MUP', 'Mojon 1Orden', 'Mojon 2Orden', 'Mojon Monte', 'Monte Certificado', 'Monte Ordenado', 'Montes Gestionados', 'Municipio', 'Ocupaciones', 'Pista Incidencia', 'Pista L1', 'Pista L2', 'Pista L3', 'Pista Sin Clasificar', 'Regeneracion Muy Dificil',  'Rodales', 'Senderos GR', 'Termino Municipal', 'Tratamiento selvicola', 'Vias Pecurias Clasificación Trazado',  'ZEC', 'ZEPA','NDVI','Cotos Pesca Refugio de Pesca','Cotos Pesca Escenario Deportivo Social','Cotos Pesca Coto de Pesca','Cotos Pesca Aguas de Acceso Libre: Excepciones','Cotos Pesca Aguas de Acceso Libre','Cotos Pesca Agua en Régimen Especial con Extracción Controlada','Cotos Pesca Agua en Régimen Especial'] 
#lista de servicios wms a tener cargados
lista_WMS_URL=["http://ovc.catastro.meh.es/Cartografia/WMS/ServidorWMS.aspx","http://www.idee.es/wms/pnoa/pnoa?","https://services.sentinel-hub.com/ogc/wms/0796fba8-667c-4f5f-8596-9d4d18c058e5","https://www.ign.es/wms/pnoa-historico"]
lista_WMS_NAME=["Catastro","Ortofoto_reciente","Sentinel por meses","Ortofotos antiguas"]
#teselas xyz a tener cargadas
lista_xyz_name=["Bing_Satelite","Google_Satelite","Stamen Terrain","Google Hybrid","Carto Positron","ESRI Topo"]
lista_xyz_url=[r"http://ecn.t3.tiles.virtualearth.net/tiles/a{q}.jpeg?g=0&dir=dir_n\x2019","http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}","http://a.tile.stamen.com/terrain/{z}/{x}/{y}.png","https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}","https://cartodb-basemaps-a.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png","https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}"]
listatoolbars=['mLabelToolBar']




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
    QSettings().setValue('/core/NewsFeed\httpsfeedqgisorg\disabled','false')

    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20210219/title',"Visor MACOTE")
    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20210219/content',"<p> Tragsa ha generado un visor para tratar de estimar las zonas con en las que es posible la <b>extración de madera con Teleferico</b>. Pincha en este texto para ampliar</p>")
    #QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20191201/image',"O:/sigmena/logos/LogoSIGMENA.jpg")
    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20210219/link',"O:/sigmena/notas/blog_sigmena/TODOS_LOS_ARTICULOS.html")

    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20210212/title',"Estado vuelos LiDAR - PNOA")
    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20210212/content',"<p> Hay en el Blog información nueva respecto al estado del vuelo <b>LiDAR</b>. Pincha en este texto para ampliar</p>")
    #QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20191201/image',"O:/sigmena/logos/LogoSIGMENA.jpg")
    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20210212/link',"O:/sigmena/notas/blog_sigmena/LIDAR.html")

    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20210209/title',"CARTOGRAFÍA FORESTACIÓN DE TIERRAS AGRÁRIAS")
    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20210209/content',"<p> En el Blog he añadido una entrada referente a la cartografía que han recopilado desde Tragsa del programa de <b>forestación</b> de tierras agrárias. Pincha en este texto para ampliar</p>")
    #QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20191201/image',"O:/sigmena/logos/LogoSIGMENA.jpg")
    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20210209/link',"O:/sigmena/notas/blog_sigmena/FORESTACION.html")

    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20210211/title',"PERÍMETRO INCENDIOS 2020")
    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20210211/content',"<p> En el Blog he añadido una entrada para que sepais que ya está la capa de perímetros de incendios 2020. Pincha en este texto para ampliar</p>")
    #QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20191201/image',"O:/sigmena/logos/LogoSIGMENA.jpg")
    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20210211/link',"O:/sigmena/notas/Blog_Sigmena/INCENDIOS.html")
    
    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20210202/title',"IMAGENES DE SENTINEL")
    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20210202/content',"<p> En el Blog he añadido una entrada referente a como cargar imagenes de Sentinel que he descargado del 2020. Pincha en este texto para ampliar</p>")
    #QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20191201/image',"O:/sigmena/logos/LogoSIGMENA.jpg")
    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20210202/link',"O:/sigmena/notas/Blog_Sigmena/SENTINEL.html")
    
    

    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20210124/title',"Blog SIGMENA")
    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20210124/content',"<p>He creado un blog para teneros informados de las novedades que vayamos teniendo en SIGMENA. Haz click aquí para acceder.</p>")
    #QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20200124/image',"file:///o:/sigmena/logos/LogoSIGMENA.jpg")
    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20210124/link',"O:/sigmena/notas/Blog_Sigmena/TODOS_LOS_ARTICULOS.html")
    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20210124/sticky','true')


    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20200124/title',"MANUAL COMPLEMENTOS SIGMENA")
    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20200124/content',"<p>Animacion para ver como funcionan los complementos SIGMENA. Pincha en este texto para saber mas</p>")
    #QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20200124/image',"file:///o:/sigmena/logos/LogoSIGMENA.jpg")
    QSettings().setValue('/core/NewsFeed/httpsfeedqgisorg/20200124/link',r"O:/sigmena/utilidad/PROGRAMA/QGIS/Complementos/Manual/Manual_complementos_SIGMENA.htm")
    
#repositorio de complementos sigmena  
    QSettings().setValue('/app/plugin_installer/checkOnStart','false')
    QSettings().setValue('/app/plugin_repositories/SIGMENA/url','https://raw.githubusercontent.com/diezrabanos/qgis_plugins/master/servidor_descargas_sigmena.xml')
    QSettings().setValue('/app/plugin_repositories/SIGMENA/authcfg','')
    QSettings().setValue('/app/plugin_repositories/Repositorio%20oficial%20de%20complementos%20de%20QGIS\enabled','false')
    QSettings().setValue('/app/plugin_repositories/SIGMENA/enabled','true')

#compruebo que existe la carpeta con los complementos
    directorio = home_plugin_path
    #try:
    #print("empiezo",file=debug)
    if os.path.isdir(directorio):
        os.stat(directorio)
        #print(len(complementos_con_version),file=debug)
        #if len(complementos_con_version)==0:
        versioninstalada="0.0.0"
        #para desinstalar si no la version correcta de un complemento
        for i in range(0,len(complementos_con_version)):
                #print("todos los complementos de la lista", file=debug)
                #print(complementos_con_version[i][0], file=debug)
                
                for x in findPlugins(home_plugin_path):
                    #print("todos los complementos que encuentra", file=debug)
                    #print(x[0], file=debug)
                    #print(x[0], file=debug)       
                    if x[0]==complementos_con_version[i][0]:
                         
                        
                        versioninstalada=str(x[1].get('general',"version"))
                        #print(versioninstalada, file=debug)
                        
                    #else:
                        #versioninstalada="0.0.0"
                        #print("pongo version 0.0.0", file=debug)
                        

                if versioninstalada==complementos_con_version[i][1]:
                    #print("no deberia hacer nada porque no hay ninguna actualziacion", file=debug)
                    
                
                    continue
                else:
                    #print ("se supone que desinstalo",complementos_con_version[i][0], file = debug)
                    #print(versioninstalada,complementos_con_version[i][1], file = debug)
                    unloadPlugin(complementos_con_version[i][0])#desinstala si version antigua de un complemento instalado
                    #print("plugins a instalar ",complementos_con_version[i][0], file = debug)
                    #para instalar un complemento                
                    # Installing
                    zip_ref = zipfile.ZipFile('O:/sigmena/utilidad/PROGRAMA/QGIS/Complementos/'+complementos_con_version[i][0]+'.zip', 'r')
                    zip_ref.extractall(home_plugin_path)
                    zip_ref.close()
                    loadPlugin(complementos_con_version[i][0])
                    startPlugin(complementos_con_version[i][0])
                    #print("desinstalo e instalo",file=debug)
     

    else:
        os.mkdir(directorio)
        for i in range(0,len(complementos_con_version)):
        #para instalar un complemento                
                        # Installing
                        zip_ref = zipfile.ZipFile('O:/sigmena/utilidad/PROGRAMA/QGIS/Complementos/'+complementos_con_version[i][0]+'.zip', 'r')
                        zip_ref.extractall(home_plugin_path)
                        zip_ref.close()
                        loadPlugin(complementos_con_version[i][0])
                        startPlugin(complementos_con_version[i][0])

     

  
    
    #esto es para que si estan instalados los active    
    try:  
        QSettings().setValue('/PythonPlugins/zoomSigmena','true')
        QSettings().setValue('/PythonPlugins/alidadas','true')
        QSettings().setValue('/PythonPlugins/gpsDescargaCarga','true')
        QSettings().setValue('/PythonPlugins/hectareas','true')
        QSettings().setValue('/PythonPlugins/sigpac','true')
        QSettings().setValue('/PythonPlugins/silvilidar','true')
        QSettings().setValue('/PythonPlugins/puntossigmena','true')
        QSettings().setValue('/PythonPlugins/ptos2pol','true')
        QSettings().setValue('/PythonPlugins/censosPuntos','true')
    except:
        pow
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

#para anadir las imagenes de teselas

    for xyz_name, xyz_url in zip(lista_xyz_name,lista_xyz_url):
        if "qgis/connections-xyz/%s/url" % xyz_name not in QSettings().allKeys():
            #QSettings().setValue("/qgis/connections-xyz/Bing%20Sat%E9lite/url","http://ecn.t3.tiles.virtualearth.net/tiles/a{q}.jpeg?g=0&dir=dir_n\x2019")
            #QSettings().setValue("/qgis/connections-xyz/relieve/url","https://mt1.google.com/vt/lyrs=t&x={x}&y={y}&z={z}")
            QSettings().setValue("/qgis/connections-xyz/%s/url" % xyz_name, "%s" % xyz_url)
# Remove a QGIS toolbar (e.g., the File toolbar)
    #fileToolBar = self.iface.fileToolBar()
    #self.iface.mainWindow().removeToolBar( fileToolBar )
            
#para importar estilos de un archivo xml

    style=QgsStyle.defaultStyle()
    style.importXml(archivosestilos)
    for estilo in estilosfavoritos:
        print (estilo)
        style.addFavorite(QgsStyle.SymbolEntity, estilo)
#style.addFavorite(QgsStyle.SymbolEntity, 'vvpp')

#para que por defecto coja la ruta donde estan las plantillas de mapas, composiciones de mapas en formato qpt
    QSettings().setValue("/app/LastComposerTemplateDir","O:/sigmena/leyendas")

#para evitar problemas con la codificacion de las capas, caracteres extranos
    QSettings().setValue("/UI/encoding","UTF-8")
    QSettings().setValue("/qgis/ignoreShapeEncoding","false")

#para establecer colores por defecto, la seleccion si no dice otra cosa el proyecto se hace en amarillo y semitransparente.
    QSettings().setValue("/qgis/default_selection_color_red","255")
    QSettings().setValue("/qgis/default_selection_color_green","255")
    QSettings().setValue("/qgis/default_selection_color_blue","0")
    QSettings().setValue("/qgis/default_selection_color_alpha","120")

#para hacer que las mediciones sean planimetricas, evitando el error por medir sobre el elipsoide
    #QSettings().setValue("/qgis/measure/planimetric","true")
    QSettings().setValue("/core/measure/planimetric","true")

#para que no compruebe si hay nuevas versiones
    QSettings().setValue("/qgis/checkVersion","false")

#para que el snapping este desactivado por defecto porque ralentiza mucho la edicion
    QSettings().setValue("/qgis/digitizing/default_snap_enabled","false")


#copiar el archivo de rejilla necesario, no me deja por los permisos de usuario lo hago con un bat
    
    #shutil.copy('O:/sigmena/utilidad/PROGRAMA/QGIS/SPED2ETV2.gsb', 'C:/Program Files/QGIS 3.10/share/proj/SPED2ETV2.gsb')


#activo la personalizacion de la visualizacion
    QSettings().setValue("/UI/Customization/enabled","true")
#copiar el archivo de configuracion visual de qgis
    usuario= QgsApplication.qgisSettingsDirPath()
    shutil.copy('O:/sigmena/utilidad/PROGRAMA/QGIS/QGISCUSTOMIZATION3.ini', os.path.join(usuario,'QGIS/QGISCUSTOMIZATION3.ini'))


    


#desabilito el snapping
    #iface.mainWindow().findChild(QDockWidget, 'Snapping and Digitizing Options').findChild(QDialog).findChild(QComboBox,'mSnapModeComboBox').setCurrentIndex(0) #0 = current layer 1 = all layers 2 = advanced
    #for item in QgsMapLayerRegistry.instance().mapLayers().values():
        #QgsProject.instance().setSnapSettingsForLayer(item.id(), False, 2, 0, 2, True)
    
    #iface.mapCanvas().snappingUtils().toggleEnabled()

#para incluir un decorador 
    from qgis.PyQt.Qt import QTextDocument
    from qgis.PyQt.QtGui import QFont
    mQFont = "Sans Serif"

    mQFontsize = 10
    mLabelQString = "SIGMENA"
    mMarginHorizontal = 0
    mMarginVertical = 0
    mLabelQColor = "#006600"
    mLabelQColor2 = "#FFFFFF"
    INCHES_TO_MM = 0.0393700787402 # 1 millimeter = 0.0393700787402 inches
    case = 3
    def add_copyright(p, text, xOffset, yOffset):
        p.translate( xOffset , yOffset )
        text.drawContents(p)
        p.setWorldTransform( p.worldTransform() )
    def _on_render_complete(p):
        deviceHeight = p.device().height() # Get paint device height on which this painter is currently painting
        deviceWidth = p.device().width() # Get paint device width on which this painter is currently painting
        # Create new container for structured rich text
        text = QTextDocument()
        font = QFont()
        font.setFamily(mQFont)
        font.setPointSize(int(mQFontsize))
        text.setDefaultFont(font)
        style = "<style type=\"text/css\"> p { color: " + mLabelQColor + " ; background: " + mLabelQColor2 + " }</style>" 
        text.setHtml( style + "<p>" + mLabelQString + "</p>" )
        # Text Size
        size = text.size()
        # RenderMillimeters
        pixelsInchX = p.device().logicalDpiX()
        pixelsInchY = p.device().logicalDpiY()
        xOffset = pixelsInchX * INCHES_TO_MM * int(mMarginHorizontal)
        yOffset = pixelsInchY * INCHES_TO_MM * int(mMarginVertical)
        # Calculate positions
        if case == 0:
            # Top Left
            add_copyright(p, text, xOffset, yOffset)
        elif case == 1:
            # Bottom Left
            yOffset = deviceHeight - yOffset - size.height()
            add_copyright(p, text, xOffset, yOffset)
        elif case == 2:
            # Top Right
            xOffset = deviceWidth - xOffset - size.width()
            add_copyright(p, text, xOffset, yOffset)
        elif case == 3:
            # Bottom Right
            yOffset = deviceHeight - yOffset - size.height()
            xOffset = deviceWidth - xOffset - size.width()
            add_copyright(p, text, xOffset, yOffset)
        elif case == 4:
            # Top Center
            xOffset = deviceWidth / 2
            add_copyright(p, text, xOffset, yOffset)
        else:
            # Bottom Center
            yOffset = deviceHeight - yOffset - size.height()
            xOffset = deviceWidth / 2
            add_copyright(p, text, xOffset, yOffset)
    # Emitted when the canvas has rendered
    iface.mapCanvas().renderComplete.connect(_on_render_complete)
    # Repaint the canvas map
    iface.mapCanvas().refresh()
    
    #debug.close()

