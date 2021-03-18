# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE DE IMPORTACIONES DE OTROS ARCHIVOS CREADOS PARA LA APLICACIÓN
# ----------------------------------------------------------------------------------------------------------------------

import clases.login_usuario as login_usuario

# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE DE MÉTODOS DE LAS DISTINTAS OPCIONES DEL MENÚ LATERAL
# ----------------------------------------------------------------------------------------------------------------------


# Método que tiene las distintas funcionalidades de las opciones del menú lateral.
def pro_opciones_menu(self):

    # Se llama al método que realiza la funcionalidad de la opción de menú "Cuenta" donde se realiza el login del
    # usuario.
    login_usuario.pro_click_login_usuario(self)
