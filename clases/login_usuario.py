# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE DE IMPORTACIONES DE LIBRERIAS
# ----------------------------------------------------------------------------------------------------------------------

import pymysql
import re
from pymysql import Error
from passlib.hash import pbkdf2_sha256

# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE DE IMPORTACIONES DE OTROS ARCHIVOS CREADOS PARA LA APLICACIÓN
# ----------------------------------------------------------------------------------------------------------------------

from clases.menu_lateral import pro_activar_botones_menu
from clases.ventana_mensajes import pro_mensaje_un_boton as pro_mensaje_un_boton


# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE DE MÉTODOS DE LA FUNCIONALIDAD DE LA VENTANA.
# ----------------------------------------------------------------------------------------------------------------------

# Método que tiene la declaración de los controladores de eventos (Event Handler) del botón de logueo del usuario.
def pro_click_login_usuario(self):

    self.uiVentana.btnLogin.clicked.connect(lambda: pro_login_usuario(self))
    self.uiVentana.txtUsuario.textChanged.connect(lambda: pro_validar_texto_usuario(self))
    self.uiVentana.txtPassword.textChanged.connect(lambda: pro_validar_texto_password(self))


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
            pro_comprobar_usuario_bbdd(self, w_email=w_usuario, w_contrasena=w_pass)

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


# Método que valida que el texto de la caja de texto del usuario corresponda al formato correcto de un Email.
def pro_validar_texto_usuario(self):

    # Se obtiene el texto del usuario.
    w_usuario = self.uiVentana.txtUsuario.text().strip()
    # Se aplica el patrón de validación para los campos de Email.
    w_patron = '^[a-zA-Z0-9\._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{2,4}$'
    # Se indica que el campo a comprobar es el email y se guarda en una variable.
    w_validar_usuario = re.match(w_patron, w_usuario, re.I)

    # Si el texto del email está vacío o si el texto del email no ha sido validado por el patrón de emails.
    if w_usuario == '' or not w_validar_usuario:

        # Se modifica el color del borde de la caja de texto.
        self.uiVentana.txtUsuario.setStyleSheet('border: 2px solid red')

    # Si el usuario ha sido rellenado y validado.
    else:

        # Se modifica el color del borde de la caja de texto.
        self.uiVentana.txtUsuario.setStyleSheet('border: 2px solid green')


# Método que valida que el texto de la caja de texto de la contraseña tenga algun valor.
def pro_validar_texto_password(self):

    # Se obtiene el texto de la contraseña.
    w_contrasena = self.uiVentana.txtPassword.text().strip()

    # Si la contraseña esta vacía.
    if w_contrasena == '':

        # Se modifica el color del borde de la caja de texto.
        self.uiVentana.txtContrasena.setStyleSheet('border: 2px solid red')

    # Si la contraseña ha sido rellenada.
    else:

        # Se modifica el color del borde de la caja de texto.
        self.uiVentana.txtPassword.setStyleSheet('border: 2px solid green')


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

                    # Se indica en la etiqueta el nombre y el primer apellido de la persona logueada.
                    self.uiVentana.lblBarraUsuario.setText('Usuario: {} {}'.format(w_datos_usuarios[1],
                                                                                   w_datos_usuarios[2]))

                    # Se activan los botones del menú lateral.
                    pro_activar_botones_menu(self, w_estado=True)

                # Si la validación de la contraseña encriptada no es correcta, se muestra un mensaje de error por
                # pantalla.
                else:

                    pro_mensaje_un_boton(self,
                                         w_tipo_ventana='Error',
                                         w_mensaje='La clave introducida es incorrecta',
                                         w_titulo='Acceso Denegado',
                                         w_mensaje_secundario=None)

            # Si no ha recuperado registros, es que el usuario no existe en la BBDD.
            else:

                # Se indica en la etiqueta del usuario, que el actual es el usuario "Invitado".
                self.uiVentana.lblBarraUsuario.setText('Usuario: Invitado')

                # Se desactivan los botones del menú lateral.
                pro_activar_botones_menu(self, w_estado=False)

                # Se muestra un mensaje de error por pantalla.
                pro_mensaje_un_boton(self,
                                     w_tipo_ventana='Error',
                                     w_mensaje='El usuario {} no existe en el sistema.'.format(w_email),
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


