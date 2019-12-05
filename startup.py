#llama a un script (SIGMENA.PY)en la ruta O:/sigmena/utilidad/PROGRAMA/QGIS/ para ejecutarlo cada vez que se abre el qgis.
#este archivo debe estar para cada usuario en C:\Users\usuario_x\AppData\Roaming\QGIS\QGIS3\startup.py
#inspirado desde https://boundless-desktop.readthedocs.io/en/latest/system_admins/globalsettings.html
import sys
ruta='O:/sigmena/utilidad/PROGRAMA/QGIS/'
if ruta not in sys.path:
    sys.path.append(ruta)
import SIGMENA
SIGMENA.sigmena()

