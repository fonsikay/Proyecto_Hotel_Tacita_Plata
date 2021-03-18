# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE DE IMPORTACIONES DE LIBRERIAS
# ----------------------------------------------------------------------------------------------------------------------

import pymysql
from pymysql import Error
from passlib.hash import pbkdf2_sha256
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon

# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE DE IMPORTACIONES DE OTROS ARCHIVOS CREADOS PARA LA APLICACIÓN
# ----------------------------------------------------------------------------------------------------------------------

from clases.menu_lateral import pro_activar_botones_menu


# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE DE MÉTODOS DE LA FUNCIONALIDAD DE LA VENTANA.
# ----------------------------------------------------------------------------------------------------------------------

# Método que tiene la declaración de los controladores de eventos (Event Handler) del botón de logueo del usuario.
def pro_click_login_usuario(self):

    self.uiVentana.btnLogin.clicked.connect(lambda: pro_login_usuario(self))


# Método que se lanza cuando se pulsa el botón de "Acceder" en la pestaña de logueo y comprueba si el usuario y la
# contraseña son correctos y si es así, se activan los botones de la aplicación.
def pro_login_usuario(self):

    # Se obtiene el valor del usuario y la contraseña introducida.
    w_usuario = self.uiVentana.txtUsuario.text().strip()
    w_pass = self.uiVentana.txtPassword.text().strip()

    # Si se ha rellenado el usuario.
    if len(w_usuario) > 0:

        # Si se ha rellenado la contraseña.
        if len(w_pass) > 0:

            # Se comprueba si el usuario es correcto y se loguea al usuario.
            pro_comprobar_usuario_bbdd(self, w_usuario, w_pass)

        # Si no se ha rellenado la contraseña, pues se muestra un mensaje de error por pantalla.
        else:

            pro_mensaje_un_boton(self,
                                 w_tipo_ventana='Advertencia',
                                 w_mensaje='No ha introducido la contraseña.',
                                 w_titulo='Contraseña vacía',
                                 w_mensaje_secundario=None)

    # Si no se ha rellenado el usuario, pues se muestra un mensaje de error por pantalla.
    else:

        pro_mensaje_un_boton(self,
                             w_tipo_ventana='Advertencia',
                             w_mensaje='No ha introducido el usuario.',
                             w_titulo='Usuario vacío',
                             w_mensaje_secundario=None)


# Método que realiza el logín del usuario en la aplicación.
def pro_comprobar_usuario_bbdd(self, w_email, w_contrasena):

    # Se crea un bloque de excepciones para controlar los fallos de conexión con BBDD.
    try:

        # Se crea la conexión con la BBDD y se comprueba si existe el usuario y contraseña introducido en la pantalla de
        # "Cuenta" del menú lateral.
        w_conexion = fun_conexion_bbdd()

        # Si la conexión ha sido correcta y w_conexion no esta vacía.
        if w_conexion is not None:

            # Se realiza el cursor con la consulta para obtener si existe el usuario y contraseña en la tabla Usuarios.
            w_cursor = w_conexion.cursor()
            w_consulta = '''(SELECT * FROM usuarios WHERE email = '{}')'''.format(w_email)
            w_cursor.execute(w_consulta)
            w_datos_usuarios = w_cursor.fetchone()

            # Si la consulta ha recuperado los datos del usuario, es que existe.
            if w_datos_usuarios is not None:

                # Se obtiene la contraseña del usuario que está encriptada en la tabla de usuarios.
                w_hash_bbdd = w_datos_usuarios[4]

                # Se comprueba si la contraseña encriptada fuera la misma que la contraseña indicada por el usuario
                # encriptada.
                if pbkdf2_sha256.verify(w_contrasena, w_hash_bbdd):

                    # Se muestra un mensaje de información de sesión al usuario.
                    pro_mensaje_un_boton(self,
                                         w_tipo_ventana='Información',
                                         w_mensaje='Bienvenido/a {} {} {}.'.format(w_datos_usuarios[1],
                                                                                   w_datos_usuarios[2],
                                                                                   w_datos_usuarios[3]),
                                         w_titulo='Conexión establecida',
                                         w_mensaje_secundario=None)

                    # Se activan los botones del menú lateral.
                    pro_activar_botones_menu(self, True)

                # Si la validación de la contraseña encriptada no es correcta, se muestra un mensaje de error por
                # pantalla.
                else:

                    pro_mensaje_un_boton(self,
                                         w_tipo_ventana='Error',
                                         w_mensaje='La clave introducida es incorrecta',
                                         w_titulo='Acceso Denegado',
                                         w_mensaje_secundario=None)

            # Si no ha recuperado registros, es que el usuario no existe en la BBDD y se muestra un mensaje de error
            # por pantalla.
            else:

                pro_mensaje_un_boton(self,
                                     w_tipo_ventana='Error',
                                     w_mensaje='El usuario es incorrecto',
                                     w_titulo='Acceso Denegado',
                                     w_mensaje_secundario=None)

    # Si se ha producido un error en la conexión a la BBDD, se muestra un mensaje de error.
    except Error as w_error:

        pro_mensaje_un_boton(self,
                             w_tipo_ventana='Error',
                             w_mensaje='Error Conexión: {}'.format(w_error),
                             w_titulo='Error de conexión',
                             w_mensaje_secundario=None)


# Método que realiza la conexión a la BBDD "Hotel" de MySQL.
def fun_conexion_bbdd():

    # Se crea la conexión con los parámetros de conexión a MySQL.
    w_conexion = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='hotel')

    # Se devuelve la conexión realizada.
    return w_conexion


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
    w_ventana_mensaje.setWindowIcon(QIcon(u':/imagenes/imagenes/logo.png'))
    # Se indica el mensaje secundario indicado.
    w_ventana_mensaje.setInformativeText(w_mensaje_secundario)

    # Se añade el botón de "Aceptar" con el estilo de la aplicación.
    w_boton_aceptar = w_ventana_mensaje.addButton(self.tr("Aceptar"), QMessageBox.AcceptRole)
    w_boton_aceptar.setStyleSheet('QPushButton {color: #ffffff;text-align: center;background-color: '
                                  'qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0, stop:0 #b6b6b6, stop:1 '
                                  '#e6e6e6);border: 1px solid #828282;padding: 5px 12px 5px 12px;margin: 4px 8px '
                                  '4px 8px;border-radius: 3px;min-width: 14px;min-height: 14px;}QPushButton:hover, '
                                  'QPushButton:focus{color: white;background-color: qlineargradient(spread:pad, '
                                  'x1:1, y1:0.545, x2:1, y2:0, stop:0 #2eae35, stop:1 #cae44a);}QPushButton:pressed'
                                  ' {background-color: #2eae35;}')
    # Se muestra la ventana de aviso.
    w_ventana_mensaje.exec_()
