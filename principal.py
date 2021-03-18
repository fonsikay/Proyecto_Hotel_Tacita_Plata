# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE DE IMPORTACIONES DE LIBRERIAS
# ----------------------------------------------------------------------------------------------------------------------

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from ventanas.principalUi import venPrincipal

# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE DE IMPORTACIONES DE OTROS ARCHIVOS CREADOS PARA LA APLICACIÓN
# ----------------------------------------------------------------------------------------------------------------------

import clases.menu_lateral as menu_lateral
import clases.funcionalidad_ventana as funcionalidad_ventana
import clases.opciones_menu as opciones_menu

# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE DE CREACION DE LA CLASE PRINCIPAL
# ----------------------------------------------------------------------------------------------------------------------


# Se crea la clase Aplicación.
class Principal(QMainWindow):

    # Se crea el método del constructor inicializador.
    def __init__(self, parent=None):

        # Se invoca el constructor padre.
        super().__init__(parent)
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = venPrincipal()
        # Se elimina la barra de titulo predeterminada de Windows.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # Se indica un icono para la ventana principal.
        self.setWindowIcon(QIcon(u':/imagenes/imagenes/logo.png'))
        # Se llama al método "setupUi" que esta en la clase "venPrincipal" del archivo "principalUi.py".
        self.uiVentana.setupUi(self)
        # Se llama al método que realiza la funcionalidad de la ventana que está en el archivo
        # "funcionalidad_ventana.py" de la carpeta "clases".
        funcionalidad_ventana.pro_funcionalidad_ventana(self)
        # Se llama al método que realiza la funcionalidad del menú lateral izquierdo que está en el archivo
        # "menu_lateral.py" de la carpeta "clases".
        menu_lateral.pro_funcionalidad_menu(self)
        # Se llama al método que realiza la funcionalidad de los distintos opciones de menú del menú lateral que está
        # en el archivo "opciones_menu.py" de la carpeta "clases".
        opciones_menu.pro_opciones_menu(self)
        # Se muestra la pantalla de forma maximizada.
        self.showMaximized()

# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE DE MÉTODOS.
# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE SOBRE EL MOVIMIENTO DE LA VENTANA.
# ----------------------------------------------------------------------------------------------------------------------

    # Se crea el método que realiza el movimiento de la ventana.
    def pro_movimiento_ventana(self, w_evento_raton):

        # Se comprueba que la pantalla no esté maximizada.
        if not self.isMaximized():

            # Si se ha origido el evento pulsando el botón izquierdo.
            if w_evento_raton.buttons() == QtCore.Qt.LeftButton:
                # Se realiza el movimiento de la ventana.
                self.move(self.pos() + w_evento_raton.globalPos() - self.w_posicion_clic)
                self.w_posicion_clic = w_evento_raton.globalPos()
                w_evento_raton.accept()

    # Se crea el método del evento de presionar el ratón para cuando se quiera mover la ventana estándo en tamaño
    # normal.
    def mousePressEvent(self, event):

        # Se obtiene la posición actual del ratón para usarlo en el movimiento de la ventana al estar en tamaño normal.
        self.w_posicion_clic = event.globalPos()

# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE SOBRE MAXIMIZAR O RESTAURAR EL TAMAÑO DE LA VENTANA CUANDO SE HACE DOBLE CLICK EN LA BARRA DE TITULO.
# ----------------------------------------------------------------------------------------------------------------------

    # Se crea el método que se lanza cuando se hace doble click en la barra de titulo de la aplicación para maximizar
    # o mostrar la pantalla de forma normal.
    def pro_cambiar_tamano_ventana(self, w_evento_raton):

        # Si se ha origido el evento de doble click pulsando el botón izquierdo.
        if w_evento_raton.buttons() == QtCore.Qt.LeftButton:
            # Se llama al método que cambia el tamaño de la ventana según sea su estado actual.
            funcionalidad_ventana.pro_maximizar(self)


# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE DE EJECUCIÓN DE LA VENTANA PRINCIPAL.
# ----------------------------------------------------------------------------------------------------------------------

# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "Principal()".
    ventana = Principal()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
