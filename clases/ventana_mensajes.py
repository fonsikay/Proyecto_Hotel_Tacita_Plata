# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE DE IMPORTACIONES DE LIBRERIAS
# ----------------------------------------------------------------------------------------------------------------------

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon


# ----------------------------------------------------------------------------------------------------------------------
#   BLOQUE DE MÉTODOS DE LOS MENSAJES POR PANTALLA.
# ----------------------------------------------------------------------------------------------------------------------

# Método para mostrar una ventana de mensaje que contiene el botón "Aceptar".
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
                                  '4px 8px;border-radius: 3px;min-width: 14px;min-height: 14px;}QPushButton:hover, '
                                  'QPushButton:focus{color: white;background-color: qlineargradient(spread:pad, '
                                  'x1:1, y1:0.545, x2:1, y2:0, stop:0 #2eae35, stop:1 #cae44a);}QPushButton:pressed'
                                  ' {background-color: #2eae35;}')
    # Se muestra la ventana de aviso.
    w_ventana_mensaje.exec_()


# Método para mostrar una ventana de mensaje que contiene el botón "Aceptar" y "Cancelar".
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
                                  '4px 8px;border-radius: 3px;min-width: 14px;min-height: 14px;}QPushButton:hover, '
                                  'QPushButton:focus{color: white;background-color: qlineargradient(spread:pad, '
                                  'x1:1, y1:0.545, x2:1, y2:0, stop:0 #2eae35, stop:1 #cae44a);}QPushButton:pressed'
                                  ' {background-color: #2eae35;}')
    w_boton_cancelar = w_ventana_mensaje.addButton(self.tr("Cancelar"), QMessageBox.RejectRole)
    w_boton_cancelar.setStyleSheet('QPushButton {color: #ffffff; text-align: center; background-color: '
                                   'qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0, stop:0 #b6b6b6, stop:1 '
                                   '#e6e6e6); border: 1px solid #828282; padding: 5px 12px 5px 12px; margin: 4px '
                                   '8px 4px 8px; border-radius: 3px; min-width: 14px; min-height: 14px;}'
                                   'QPushButton:hover, QPushButton:focus{color: white;background-color: '
                                   'qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0, stop:0 #95050d, stop:1'
                                   ' #ea0a20);} QPushButton:pressed {background-color: #95050d;}')

    # Se muestra la ventana de aviso.
    w_ventana_mensaje.exec_()

    # Si se ha pulsado el botón de aceptar, pues se cierra la aplicación y si pulsa el de cancenlar, pues no hace
    # nada.
    if w_ventana_mensaje.clickedButton() == w_boton_aceptar:
        return 'Aceptar'
    elif w_ventana_mensaje.clickedButton() == w_boton_cancelar:
        return 'Cancelar'
