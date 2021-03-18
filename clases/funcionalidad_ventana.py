# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE DE IMPORTACIONES DE LIBRERIAS
# ----------------------------------------------------------------------------------------------------------------------

from PyQt5.QtGui import QIcon

# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE DE IMPORTACIONES DE OTROS ARCHIVOS CREADOS PARA LA APLICACIÓN
# ----------------------------------------------------------------------------------------------------------------------

from clases.menu_lateral import pro_mostrar_menu_izquierda


# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE DE MÉTODOS DE LA FUNCIONALIDAD DE LA VENTANA.
# ----------------------------------------------------------------------------------------------------------------------

# Método principal que llama a los demás métodos para crear la funcionalidad de la ventana.
def pro_funcionalidad_ventana(self):

    # Se llama al método que tiene los Event Handler de los botones de la barra de título de la ventana.
    pro_botonera_titulo(self)
    # Se llama al método que carga las variables fijas necesarias que se utilizan en los métodos de éste bloque.
    pro_carga_variables_fijas(self)
    # Se llama al método que permite mover la ventana si se pulsa con el botón izquierdo del ratón la barra de
    # título de la aplicación.
    pro_mover_ventana(self)


# Método que tiene la declaración de los controladores de eventos (Event Handler) de los botones de la barra de título.
def pro_botonera_titulo(self):

    # Botones de la ventana.
    self.uiVentana.btnMinimizar.clicked.connect(lambda: pro_minimizar(self))
    self.uiVentana.btnMaximizar.clicked.connect(lambda: pro_maximizar(self))
    self.uiVentana.btnCerrar.clicked.connect(lambda: pro_cerrar(self))
    # Botón de abrir o cerrar la barra de menú lateral.
    self.uiVentana.btnMenu.clicked.connect(lambda: pro_mostrar_menu_izquierda(self))


# Método que se lanza al pulsar el botón de Minimizar la ventana.
def pro_minimizar(self):

    # Se minimiza la ventana.
    self.showMinimized()


# Método que se lanza al pulsar el botón de maximizar la ventana.
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


# Método que se lanza al pulsar el botón de cerrar la ventana.
def pro_cerrar(self):

    # Se cierra la ventana.
    self.close()


# Método donde se guardan las variables fijas necesarias.
def pro_carga_variables_fijas(self):

    # Se guarda en una variable el tamaño de la ventana para saber si esta minimizada o maximizada.
    # Como se va a iniciar maximizada por defecto, se indica el valor 1.
    self.w_tamano_ventana = 1
    # Se crea una variable para almacenar la posición del ratón donde realiza el click para cambiar el tamaño de
    # la ventana según sea el caso.
    self.w_posicion_clic = None
    # Se crea una variable para almacenar la animación del menú lateral izquierdo de la ventana.
    self.w_animacion = None


# Método que se lanza cuando se intenta mover la pantalla pulsando en la barra de titulo de la ventana.
def pro_mover_ventana(self):

    # Se indica el método que se lanza cuando se mueve el ratón.
    # El método "pro_movimiento_ventana" se encuentra en el fichero "principal.py"  ya que no es posible importarlo.
    self.uiVentana.frmCabecera.mouseMoveEvent = self.pro_movimiento_ventana

    # Se indica el método que se lanza cuando se hace doble click en la barra de título de la ventana.
    # El método "pro_cambiar_tamano_ventana" se encuentra en el fichero "principal.py" ya que no es posible importarlo.
    self.uiVentana.frmCabecera.mouseDoubleClickEvent = self.pro_cambiar_tamano_ventana
