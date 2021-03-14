# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from ventanas.principalUi import venPrincipal


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
        # Se llama al método "setupUi" que esta en la clase "venPrincipal" del archivo "principalUi.py".
        self.uiVentana.setupUi(self)
        # Se indica un icono para la ventana principal.
        self.setWindowIcon(QIcon(u':/imagenes/imagenes/logo.png'))

        # Declaración de los controladores de eventos (Event Handler).
        self.uiVentana.btnMinimizar.clicked.connect(self.pro_minimizar)
        self.uiVentana.btnMaximizar.clicked.connect(self.pro_maximizar)
        self.uiVentana.btnCerrar.clicked.connect(self.pro_cerrar)
        # Se llama al método para abrir o cerrar el menú lateral cuando se pulsa el botón "Menú".
        self.uiVentana.btnMenu.clicked.connect(self.pro_mostrar_menu_izquierda)

        # Se guarda en una variable el tamaño de la ventana para saber si esta minimizada o maximizada.
        # Como se va a iniciar maximizada por defecto, se indica el valor 1.
        self.w_tamano_ventana = 1

        # Se crea una variable para almacenar la posición del ratón donde realiza el click para cambiar el tamaño de
        # la ventana según sea el caso.
        self.w_posicion_clic = None

        # Se crea una variable para almacenar la animación del menú lateral izquierdo de la ventana.
        self.w_animacion = None

        # Se llama al método que permite mover la ventana si se pulsa con el botón izquierdo del ratón la barra de
        # título de la aplicación.
        self.pro_funcionalidad_ventana()

        # Se muestra la pantalla de forma maximizada.
        self.showMaximized()

    # Se crea el método que abre o cierra el menú lateral.
    def pro_mostrar_menu_izquierda(self):

        # Se obtiene el valor del ancho del frame del menú izquierdo.
        w_ancho = self.uiVentana.frmMenuIzq.width()

        # Si el ancho del bloque es el mínimo, es que está el menú cerrado.
        if w_ancho == 50:

            # Se abre el menú indicando el valor final.
            w_nuevo_ancho = 140

        # Si el ancho del bloque es el máximo, es que está el menú abierto.
        else:

            # Se cierra el menú indicando el valor inicial.
            w_nuevo_ancho = 50

        # Se crea la animación del menú.
        self.w_animacion = QtCore.QPropertyAnimation(self.uiVentana.frmMenuIzq, b"minimumWidth")
        # Se indica el tiempo que tarda en abrirse o cerrarse el menú lateral.
        self.w_animacion.setDuration(250)
        # Se indica que se inicia en el valor minímo del ancho del bloque del menú.
        self.w_animacion.setStartValue(w_ancho)
        # Se indica que finaliza en el valor máximo del ancho del bloque del menú.
        self.w_animacion.setEndValue(w_nuevo_ancho)
        self.w_animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        # Se inicia la animación del menú lateral.
        self.w_animacion.start()

    # Se crea el método que realiza la funcionalidad de la barra de titulo de la aplicación.
    def pro_funcionalidad_ventana(self):

        # Se indica el método que se lanza cuando se mueve el ratón.
        self.uiVentana.frmCabecera.mouseMoveEvent = self.pro_movimiento_ventana

        # Se indica el método que se lanza cuando se hace doble click en la barra de título de la ventana.
        self.uiVentana.frmCabecera.mouseDoubleClickEvent = self.pro_cambiar_tamano_ventana

    # Se crea el método que se lanza cuando se hace doble click en la barra de titulo de la aplicación para maximizar
    # o mostrar la pantalla de forma normal.
    def pro_cambiar_tamano_ventana(self, w_evento_raton):

        # Si se ha origido el evento de doble click pulsando el botón izquierdo.
        if w_evento_raton.buttons() == QtCore.Qt.LeftButton:

            # Se llama al método que cambia el tamaño de la ventana según sea su estado actual.
            self.pro_maximizar()

    # Se crea el método del evento de presionar el ratón para cuando se quiera mover la ventana estándo en tamaño
    # normal.
    def mousePressEvent(self, event):

        # Se obtiene la posición actual del ratón para usarlo en el movimiento de la ventana al estar en tamaño normal.
        self.w_posicion_clic = event.globalPos()

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

    # Se crea el método que se lanza al pulsar el botón de minimizar.
    def pro_minimizar(self):
        # Se minimiza la ventana.
        self.showMinimized()

    # Se crea el método que se lanza al pulsar el botón de maximizar.
    def pro_maximizar(self):

        # Si la ventana no esta máximizada.
        if self.w_tamano_ventana == 0:

            # Se pone el contador a 1 indicando que está maximizada.
            self.w_tamano_ventana = 1
            # Se muestra la ventana maximizada.
            self.showMaximized()
            # Se muestra el icono de restaurar la ventana al tamaño normal.
            self.uiVentana.btnMaximizar.setIcon(QIcon(u':/iconos/iconos/cil-window-restore.png'))

        # Si la ventana ya esta máximizada, pues se pone con el tamaño normal.
        else:
            # Se pone el contador a 0 indicando que no está maximizada.
            self.w_tamano_ventana = 0
            # Se muestra la ventana en el tamaño normal.
            self.showNormal()
            # Se muestra el icono de maximizar la ventana.
            self.uiVentana.btnMaximizar.setIcon(QIcon(u':/iconos/iconos/cil-window-maximize.png'))

    # Se crea el método que se lanza al pulsar el botón de cerrar.
    def pro_cerrar(self):
        # Se cierra la ventana.
        self.close()

    # Se crea un método para mostrar una ventana de mensaje que contiene el botón "Aceptar".
    def pro_mensaje_un_boton(self, w_tipo_ventana, w_mensaje, w_titulo, w_mensaje_secundario):

        # Se crea un objeto de tipo ventana de mensaje.
        w_ventana_mensaje = QMessageBox()
        # Se muestra el mensaje al usuario indicado.
        w_ventana_mensaje.setText(w_mensaje)

        # Según sea el tipo de mensaje indicado, se elige un tipo de icono para la ventana.
        if w_tipo_ventana == 'Consulta':
            w_ventana_mensaje.setIcon(QMessageBox.Question)
        elif w_tipo_ventana == 'Información':
            w_ventana_mensaje.setIcon(QMessageBox.Information)
        elif w_tipo_ventana == 'Advertencia':
            w_ventana_mensaje.setIcon(QMessageBox.Warning)
        elif w_tipo_ventana == 'Error':
            w_ventana_mensaje.setIcon(QMessageBox.Critical)
        else:
            w_ventana_mensaje.setIcon(QMessageBox.NoIcon)

        # Se indica el titulo de la ventana indicado.
        w_ventana_mensaje.setWindowTitle(w_titulo)
        # Se indica el icono de la ventana.
        w_ventana_mensaje.setWindowIcon(QIcon('icono.ico'))
        # Se indica el mensaje secundario indicado.
        w_ventana_mensaje.setInformativeText(w_mensaje_secundario)

        # Se añade el botón de "Aceptar" con el estilo de la aplicación.
        w_boton_aceptar = w_ventana_mensaje.addButton(self.tr("Aceptar"), QMessageBox.AcceptRole)
        w_boton_aceptar.setStyleSheet('QPushButton {color: #ffffff;text-align: center;background-color: '
                                      'qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0, stop:0 #b6b6b6, stop:1 '
                                      '#e6e6e6);border: 1px solid #828282;padding: 5px 12px 5px 12px;margin: 4px 8px '
                                      '4px 8px;border-radius: 3px;min-width: 14px;min-height: 14px;}QPushButton:hover{'
                                      'color: white;background-color: qlineargradient(spread:pad, x1:1, y1:0.545, x2:1,'
                                      ' y2:0, stop:0 #2eae35, stop:1 #cae44a);}QPushButton:pressed {background-color: '
                                      '#2eae35;}')
        # Se muestra la ventana de aviso.
        w_ventana_mensaje.exec_()

    # Se crea un método para mostrar una ventana de mensaje que contiene el botón "Aceptar" y "Cancelar".
    def fun_mensaje_dos_botones(self, w_tipo_ventana, w_mensaje, w_titulo, w_mensaje_secundario):

        # Se crea un objeto de tipo ventana de mensaje.
        w_ventana_mensaje = QMessageBox()
        # Se muestra el mensaje al usuario indicado.
        w_ventana_mensaje.setText(w_mensaje)

        # Según sea el tipo de mensaje indicado, se elige un tipo de icono para la ventana.
        if w_tipo_ventana == 'Consulta':
            w_ventana_mensaje.setIcon(QMessageBox.Question)
        elif w_tipo_ventana == 'Información':
            w_ventana_mensaje.setIcon(QMessageBox.Information)
        elif w_tipo_ventana == 'Advertencia':
            w_ventana_mensaje.setIcon(QMessageBox.Warning)
        elif w_tipo_ventana == 'Error':
            w_ventana_mensaje.setIcon(QMessageBox.Critical)
        else:
            w_ventana_mensaje.setIcon(QMessageBox.NoIcon)

        # Se indica el titulo de la ventana indicado.
        w_ventana_mensaje.setWindowTitle(w_titulo)
        # Se indica el icono de la ventana.
        w_ventana_mensaje.setWindowIcon(QIcon('icono.ico'))
        # Se indica el mensaje secundario indicado.
        w_ventana_mensaje.setInformativeText(w_mensaje_secundario)

        # Se añade los botones de Aceptar y Cancelar con el estilo de la aplicación.
        w_boton_aceptar = w_ventana_mensaje.addButton(self.tr("Aceptar"), QMessageBox.AcceptRole)
        w_boton_aceptar.setStyleSheet('QPushButton {color: #ffffff;text-align: center;background-color: '
                                      'qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0, stop:0 #b6b6b6, stop:1 '
                                      '#e6e6e6);border: 1px solid #828282;padding: 5px 12px 5px 12px;margin: 4px 8px '
                                      '4px 8px;border-radius: 3px;min-width: 14px;min-height: 14px;}QPushButton:hover{'
                                      'color: white;background-color: qlineargradient(spread:pad, x1:1, y1:0.545, x2:1,'
                                      ' y2:0, stop:0 #2eae35, stop:1 #cae44a);}QPushButton:pressed {background-color: '
                                      '#2eae35;}')
        w_boton_cancelar = w_ventana_mensaje.addButton(self.tr("Cancelar"), QMessageBox.RejectRole)
        w_boton_cancelar.setStyleSheet('QPushButton {color: #ffffff; text-align: center; background-color: '
                                       'qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0, stop:0 #b6b6b6, stop:1 '
                                       '#e6e6e6); border: 1px solid #828282; padding: 5px 12px 5px 12px; margin: 4px '
                                       '8px 4px 8px; border-radius: 3px; min-width: 14px; min-height: 14px;}'
                                       'QPushButton:hover{color: white;background-color: qlineargradient(spread:pad, '
                                       'x1:1, y1:0.545, x2:1, y2:0, stop:0 #95050d, stop:1 #ea0a20);} '
                                       'QPushButton:pressed {background-color: #95050d;}')

        # Se muestra la ventana de aviso.
        w_ventana_mensaje.exec_()

        # Si se ha pulsado el botón de aceptar, pues se cierra la aplicación y si pulsa el de cancenlar, pues no hace
        # nada.
        if w_ventana_mensaje.clickedButton() == w_boton_aceptar:
            return 'Aceptar'
        elif w_ventana_mensaje.clickedButton() == w_boton_cancelar:
            return 'Cancelar'


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
