# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE DE IMPORTACIONES DE LIBRERIAS.
# ----------------------------------------------------------------------------------------------------------------------

from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtCore

# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE DE MÉTODOS DE LA FUNCIONALIDAD DEL MENÚ LATERAL IZQUIERDO.
# ----------------------------------------------------------------------------------------------------------------------


# Método principal que llama a los demás métodos para crear la funcionalidad del menú lateral.
def pro_funcionalidad_menu(self):

    # Se llama al método que inicializa los botones de la barra de menú lateral.
    pro_inicializacion_botones_menu(self)

    # Se llama al método que tiene los Event Handler de los botones del menú lateral.
    pro_click_menu_izquierdo(self)

    # Se llama al método que poner el fondo dorado al botón del menú cuando se haya pulsado en un botón de dicho menú
    # para indicar que pestaña se está mostrando en el bloque central de la ventana.
    pro_estilo_boton_menu(self)


# Método que inicializa los botones de la barra de menú lateral.
def pro_inicializacion_botones_menu(self):

    # Se desactivan todos los botones del menú lateral de forma inicial hasta que no se loguee el usuario en la
    # pestaña de "Cuenta" y para ello se indica el estado a valor "False".
    pro_activar_botones_menu(self, w_estado=False)

    # Se indica el color de fondo de los botones deshabilitados.
    self.uiVentana.btnInicio.setStyleSheet('background-color: #173757;')
    self.uiVentana.btnClientes.setStyleSheet('background-color: #173757;')

    # Se indica la pestaña inicial que se carga en la ventana.
    self.uiVentana.tablaContenido.setCurrentWidget(self.uiVentana.tabCuenta)

    # Se indica que el botón "Cuenta" que es el que se muestra la pestaña de forma inicial, aparezca con la línea de
    # estar activo dicho botón, simulando a si lo hubieran marcado.
    self.uiVentana.btnCuenta.setStyleSheet('border-left: 3px solid #f5cc3d;')


# Método que activa o desactiva los botones del menú lateral.
def pro_activar_botones_menu(self, w_estado):

    # Se habilitan o deshabilitan todos los botones del menú lateral según sea el valor de "w_estado" que puede ser
    # "True" o "False".
    self.uiVentana.btnInicio.setEnabled(w_estado)
    self.uiVentana.btnClientes.setEnabled(w_estado)


# Método que tiene la declaración de los controladores de eventos (Event Handler) de los botones del menú lateral.
def pro_click_menu_izquierdo(self):

    # Se indica las pestaña que se muestra en la sección central de la ventana cuando un botón del menú es presionado.
    self.uiVentana.btnInicio.clicked.connect(lambda: self.uiVentana.tablaContenido.setCurrentWidget(self.uiVentana.
                                                                                                    tabInicio))
    self.uiVentana.btnCuenta.clicked.connect(lambda: self.uiVentana.tablaContenido.setCurrentWidget(self.uiVentana.
                                                                                                    tabCuenta))
    self.uiVentana.btnClientes.clicked.connect(lambda: self.uiVentana.tablaContenido.setCurrentWidget(self.uiVentana.
                                                                                                      tabClientes))
    self.uiVentana.btnAjustes.clicked.connect(lambda: self.uiVentana.tablaContenido.setCurrentWidget(self.uiVentana.
                                                                                                     tabAjustes))


# Método para poner el fondo dorado al botón del menú cuando se haya pulsado en un botón de dicho menú para indicar
# que pestaña se está mostrando en el bloque central de la ventana.
def pro_estilo_boton_menu(self):

    # Se recorren todos los botones que tiene el menú lateral izquierdo.
    for w in self.uiVentana.frmMenuIzq.findChildren(QPushButton):
        # Se indica el método que se lanza cuando en el botón indicado se hace click para cambiar su estilo.
        w.clicked.connect(lambda: pro_aplicar_estilo_botones_menu(self))


# Método para cambiar el fondo del botón que ha sido presionado.
def pro_aplicar_estilo_botones_menu(self):

    # Se reinicia el estilo de los otros botones.
    for w in self.uiVentana.frmMenuIzq.findChildren(QPushButton):

        # Si el nombre del botón no es igual al nombre del botón que se ha pulsado.
        if w.objectName() != self.sender().objectName():

            # Se indica que el estilo predeterminado con el color del fondo dorado para dejar el botón marcado.
            w_estilo_por_defecto = w.styleSheet().replace("border-left: 3px solid #f5cc3d;", "")
            # Se aplica como estilo por defecto.
            w.setStyleSheet(w_estilo_por_defecto)

    # Se aplica el nuevo estilo cuando se hace click en el botón.
    # sender(): Botón clicado.
    # Se obtiene el estilo que tiene el botón y se le agrega el fondo dorado.
    w_nuevo_estilo = self.sender().styleSheet() + ("border-left: 3px solid #f5cc3d;")

    # Se aplica el nuevo estilo al botón.
    self.sender().setStyleSheet(w_nuevo_estilo)
    return


# Método que se lanza al pulsar el botón de "Menú" lateral para abrir o cerrar el menú.
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
