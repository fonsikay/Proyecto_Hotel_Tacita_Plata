# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE DE IMPORTACIONES DE LIBRERIAS.
# ----------------------------------------------------------------------------------------------------------------------

from PyQt5.QtWidgets import QPushButton

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

    # Se deshabilitan todos los botones del menú lateral de forma inicial hasta que no se loguee el usuario en la
    # pestaña de "Cuenta".
    self.uiVentana.btnInicio.setEnabled(False)
    self.uiVentana.btnClientes.setEnabled(False)

    # Se indica el color de fondo de los botones deshabilitados.
    self.uiVentana.btnInicio.setStyleSheet('background-color: #173757;')
    self.uiVentana.btnClientes.setStyleSheet('background-color: #173757;')

    # Se indica la pestaña inicial que se carga en la ventana.
    self.uiVentana.tablaContenido.setCurrentWidget(self.uiVentana.tabCuenta)

    # Se indica que el botón "Cuenta" que es el que se muestra la pestaña de forma inicial, aparezca con la línea de
    # estar activo dicho botón, simulando a si lo hubieran marcado.
    self.uiVentana.btnCuenta.setStyleSheet('border-left: 3px solid #f5cc3d;')


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
