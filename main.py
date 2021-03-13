# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect
from PyQt5 import QtCore
from PyQt5.QtGui import QColor
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
        # Se indica el tamaño de la ventana para que no se pueda modificar su tamaño.
        self.setFixedSize(837, 601)

        # Se elimina la barra de titulo y la botonera.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # Se elimina el fondo de la ventana para que sólo muestre la imagen.
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # Se crea un efecto de sombreado para la ventana.
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(98, 97, 98, 150))
        # Se aplica el efecto sombreado al QWidget centralwidget.
        self.uiVentana.centralwidget.setGraphicsEffect(self.shadow)

        # Se crea una variable global para almacenar el valor de la barra de progreso.
        self.w_valor_barra_progreso = 0
        # Se crea un objeto de tipo Timer para ejecutar la barra de desplazamiento.
        self.w_timer = QtCore.QTimer()
        # Se indica el método que se lanza cuando se ejecute el timer.
        self.w_timer.timeout.connect(self.pro_barra_progreso)
        # Se indica el intervalo del timer que serán 100 milisegundos para que vaya avanzando la barra de progreso.
        self.w_timer.start(100)

        # Se muestra la pantalla.
        self.show()

    # Se define el método "pro_barra_progreso()" que se lanza cuando cambia el valor del timer.
    def pro_barra_progreso(self):

        # Se indica que la barra de progreso tome el valor de la variable que guarda el avance de la barra de progreso.
        self.uiVentana.barra_progreso.setValue(self.w_valor_barra_progreso)

        # Si el valor de la barra es menor o igual al 30%, se muestra un mensaje de información.
        if self.w_valor_barra_progreso <= 30:

            QtCore.QTimer.singleShot(0, lambda: self.uiVentana.lblEstado.setText("Conectado con el servidor. . ."))

        # Si el valor de la barra es menor o igual al 50%, se muestra un mensaje de información.
        elif self.w_valor_barra_progreso <= 50:

            QtCore.QTimer.singleShot(0, lambda: self.uiVentana.lblEstado.setText("Obteniendo credenciales. . ."))

        # Si el valor de la barra es menor o igual al 90%, se muestra un mensaje de información y se modifica el texto
        # principal de la aplicación.
        elif self.w_valor_barra_progreso <= 90:

            self.uiVentana.lblTitulo.setText('Accediendo a Hotel Spa La Tacita de Plata App')
            QtCore.QTimer.singleShot(0, lambda: self.uiVentana.lblEstado.setText("Iniciando aplicación. . ."))

        # Si el valor es menor o igual al 100%, se muestra un mensaje de información.
        elif self.w_valor_barra_progreso <= 100:

            QtCore.QTimer.singleShot(0, lambda: self.uiVentana.lblEstado.setText("Carga completa. . ."))

        # Si el valor es mayor al 125%, se para el timer y se cierra la ventana.
        elif self.w_valor_barra_progreso > 120:

            # Se para el timer.
            self.w_timer.stop()

            # Se cierra la pantalla de inicio cuando se termina la carga de la pantalla.
            self.close()

        # Se incrementa el valor de la barra de progreso en 2 cada vez que pasa 100 milisegundos.
        self.w_valor_barra_progreso = self.w_valor_barra_progreso + 2


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
