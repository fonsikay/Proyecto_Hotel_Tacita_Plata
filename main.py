# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from pantalla_inicio import ven_Inicio


# Se crea la clase Aplicación.
class PantallaInicio_Aplicacion(QMainWindow):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = ven_Inicio()
        # Se llama al método "setupUi" que esta en la clase "ven_Inicio" del archivo "pantalla_inicio.py".
        self.uiVentana.setupUi(self)
        # Se indica un icono para la ventana principal.
        self.setWindowIcon(QIcon('icono.ico'))
        # Se indica el tamaño de la ventana para que no se pueda modificar su tamaño.
        self.setFixedSize(571, 423)
        # Se muestra la pantalla.
        self.show()


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "PantallaInicio_Aplicacion()".
    ventana = PantallaInicio_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
