# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from galeria_imagenes import icono


class venPrincipal(object):
    def setupUi(self, venPrincipal):
        venPrincipal.setObjectName("venPrincipal")
        venPrincipal.resize(1300, 700)
        venPrincipal.setMinimumSize(QtCore.QSize(1300, 700))
        venPrincipal.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(venPrincipal)
        self.centralwidget.setStyleSheet("/* ------------------------- SECCIONES DE LA APLICACION --------------------------*/\n"
"\n"
"/* Color de fondo de las secciones */\n"
"QFrame#frmCabecera, #frmBotonera, #frmMenu, #frmMenuDer, #frmMenuIzq, #frmBarraEstado\n"
"{\n"
"    background-color:qlineargradient(spread:pad, x1:0.528, y1:0.858,                         x2:0.517409, y2:0.159, stop:0 rgba(23, 55, 87, 255), stop:1 rgba(42, 100,             165, 255));\n"
"}\n"
"\n"
"/* --------------- SECCIÓN DE LA CABECERA DE LA APLICACION -----------------*/\n"
"\n"
"/* Color de la linea inferior */\n"
"QFrame#frmCabecera\n"
"{\n"
"    border-bottom: 1px solid rgb(171, 135, 10);\n"
"}\n"
"\n"
"/* - SECCIÓN DE LA BOTONERA DE MENU E ICONO DE LA BARRA DE TITULO -*/\n"
"\n"
"/* Se elimina los bordes */\n"
"QFrame#frmMenu \n"
"{\n"
"    border-bottom: none;\n"
"}\n"
"\n"
"/* Color del botón Minimizar cuando se posiciona el cursor */\n"
"QPushButton#btnMenu:hover\n"
"{\n"
"      background-color:qlineargradient(spread:pad, x1:0.528409, y1:0.733,                     x2:0.5, y2:0.17, stop:0 #b28d0b, stop:1 #f5cc3d);\n"
"}\n"
"\n"
"/* Color del botón Minimizar cuando se pulsa el botón */\n"
"QPushButton#btnMenu:pressed\n"
"{\n"
"    background-color: #b28d0b\n"
"}\n"
"\n"
"/* Imágen de la barra de título */\n"
"QFrame#frmLogo\n"
"{\n"
"    image: url(:/imagenes/imagenes/logo.png);\n"
"    border:none;\n"
"}\n"
"\n"
"/* Titulo de la barra de título */\n"
"QLabel#lblLogo\n"
"{\n"
"    color: rgb(198, 160, 30);\n"
"    font: 25 18pt \"Gabriola\";\n"
"}\n"
"\n"
"QLabel#lblBarraUsuario\n"
"{\n"
"    color: #ffffff;\n"
"    font: 25 9pt \"Bahnschrift Light\";\n"
"}\n"
"\n"
"/* ------------ SECCIÓN DE LA BOTONERA DE LA BARRA DE TITULO -------------*/\n"
"\n"
"/* Color de la botonera de la barra de título */\n"
"QPushButton#btnMinimizar, #btnMaximizar, #btnCerrar, #btnMenu\n"
"{\n"
"    border: 1px solid rgb(171, 135, 10);\n"
"    border-radius: 13px;\n"
"}\n"
"\n"
"/* Color del botón Minimizar cuando se posiciona el cursor */\n"
"QPushButton#btnMinimizar:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0,             stop:0 #2eae35, stop:1 #cae44a);\n"
"}\n"
"\n"
"/* Color del botón Minimizar cuando se pulsa el botón */\n"
"QPushButton#btnMinimizar:pressed \n"
"{\n"
"    background-color: #2eae35;\n"
"}\n"
"\n"
"/* Color del botón Maximizar cuando se posiciona el cursor */\n"
"QPushButton#btnMaximizar:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0,             stop:0 #FF7100, stop:1 #FFDB34);\n"
"}\n"
"\n"
"/* Color del botón Maximizar cuando se pulsa el botón */\n"
"QPushButton#btnMaximizar:pressed \n"
"{\n"
"    background-color: #FF7100;\n"
"}\n"
"\n"
"/* Color del botón Cerrar cuando se posiciona el cursor */\n"
"QPushButton#btnCerrar:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0,             stop:0 #95050d, stop:1 #ea0a20);\n"
"}\n"
"\n"
"/* Color del botón Cerrar cuando se pulsa el botón */\n"
"QPushButton#btnCerrar:pressed \n"
"{\n"
"    background-color: #95050d;\n"
"}\n"
"\n"
"/* --------------------- SECCIÓN DEL CUERPO DE LA VENTANA ---------------------*/\n"
"\n"
"/* Se elimina los bordes */\n"
"QFrame#frmCuerpo \n"
"{\n"
"    border:none;\n"
"}\n"
"\n"
"/* ---------------- SECCIÓN DE LA BARRA DE MENÚ IZQUIERDA ------------------ */\n"
"\n"
"/* Se elimina los bordes de la sección del menú menos el derecho que se indica con el color dorado */\n"
"QFrame#frmMenuIzq\n"
"{\n"
"    border-left: none;\n"
"    border-top: none;\n"
"    border-bottom: none;\n"
"    border-right: 1px solid #b28d0b;\n"
"}\n"
"\n"
"/* Estilo de los botones del menú izquierdo */\n"
"QPushButton#btnInicio, #btnCuenta, #btnAjustes, #btnClientes\n"
"{\n"
"    border-left: none;\n"
"    border-top: none;\n"
"    border-right: none;\n"
"    color: #ffffff;\n"
"    padding-left: 60px;\n"
"    padding-top: 10px;\n"
"    padding-bottom: 10px;\n"
"    font: 25 13pt \"Bahnschrift Light\";\n"
"    background-repeat: none;\n"
"    text-align: left;\n"
"    background-position: center left;\n"
"}\n"
"\n"
"/* Borde inferior en los botones */\n"
"QPushButton#btnInicio, #btnCuenta, #btnClientes\n"
"{\n"
"    border-bottom: 1px solid rgb(171, 135, 10);\n"
"}\n"
"\n"
"/* Borde superior en el boton */\n"
"QPushButton#btnAjustes\n"
"{\n"
"    border-top: 1px solid rgb(171, 135, 10);\n"
"}\n"
"\n"
"/* Color del botón Minimizar cuando se posiciona el cursor */\n"
"QPushButton#btnInicio:hover, #btnCuenta:hover, #btnAjustes:hover, #btnClientes:hover\n"
"{\n"
"      background-color:qlineargradient(spread:pad, x1:0.528409, y1:0.733,                     x2:0.5, y2:0.17, stop:0 #b28d0b, stop:1 #f5cc3d);\n"
"}\n"
"\n"
"/* Color del botón Minimizar cuando se pulsa el botón */\n"
"QPushButton#btnInicio:pressed, #btnCuenta:pressed, #btnAjustes:pressed, #btnClientes:pressed\n"
"{\n"
"    background-color: #b28d0b\n"
"}\n"
"\n"
"/* Icono para el botón Inicio */\n"
"QPushButton#btnInicio\n"
"{\n"
"    background-image: url(:/iconos/iconos/cil-home2.png);\n"
"}\n"
"\n"
"/* Icono para el botón Cuenta */\n"
"QPushButton#btnCuenta\n"
"{\n"
"    background-image: url(:/iconos/iconos/cil-user2.png);\n"
"}\n"
"\n"
"/* Icono para el botón Ajustes */\n"
"QPushButton#btnAjustes\n"
"{\n"
"    background-image: url(:/iconos/iconos/cil-settings3.png);\n"
"}\n"
"\n"
"/* Icono para el botón Clientes */\n"
"QPushButton#btnClientes\n"
"{\n"
"    background-image: url(:/iconos/iconos/cil-user-female.png);\n"
"}\n"
"\n"
"/* ------------------ SECCIÓN DE LA BARRA DE MENÚ DERECHA ------------------ */\n"
"\n"
"/* Color del borde izquierdo */\n"
"QFrame#frmMenuDer\n"
"{ \n"
"    border-left: 1px solid rgb(171, 135, 10);\n"
"}\n"
"\n"
"/* --------------------- SECCIÓN DEL CUERPO DE LA VENTANA -------------------- */\n"
"\n"
"/* Se elimina los bordes */\n"
"QFrame#frmCuerpo \n"
"{\n"
"    border:none;\n"
"}\n"
"\n"
"/* ----------------------- SECCIÓN CENTRAL DE CONTENIDO ---------------------- */\n"
"\n"
"/* Color de fondo de la sección y eliminar el borde */\n"
"QFrame#frmContenido \n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"/* --------------------------- SECCIÓN BARRA DE ESTADO -------------------------- */\n"
"\n"
"/* Color del borde superior */\n"
"QFrame#frmBarraEstado\n"
"{ \n"
"    border-top: 1px solid rgb(171, 135, 10);\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frmCabecera = QtWidgets.QFrame(self.centralwidget)
        self.frmCabecera.setMaximumSize(QtCore.QSize(16777215, 43))
        self.frmCabecera.setStyleSheet("")
        self.frmCabecera.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmCabecera.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmCabecera.setObjectName("frmCabecera")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frmCabecera)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frmTituloContenedor = QtWidgets.QFrame(self.frmCabecera)
        self.frmTituloContenedor.setStyleSheet("")
        self.frmTituloContenedor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmTituloContenedor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmTituloContenedor.setObjectName("frmTituloContenedor")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frmTituloContenedor)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frmMenu = QtWidgets.QFrame(self.frmTituloContenedor)
        self.frmMenu.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frmMenu.setStyleSheet("")
        self.frmMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmMenu.setObjectName("frmMenu")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frmMenu)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnMenu = QtWidgets.QPushButton(self.frmMenu)
        self.btnMenu.setMinimumSize(QtCore.QSize(0, 0))
        self.btnMenu.setMaximumSize(QtCore.QSize(30, 26))
        self.btnMenu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMenu.setStyleSheet("")
        self.btnMenu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconos/iconos/cil-menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMenu.setIcon(icon)
        self.btnMenu.setIconSize(QtCore.QSize(16, 16))
        self.btnMenu.setObjectName("btnMenu")
        self.horizontalLayout_4.addWidget(self.btnMenu)
        self.horizontalLayout_5.addWidget(self.frmMenu)
        self.frmTitulo = QtWidgets.QFrame(self.frmTituloContenedor)
        self.frmTitulo.setMinimumSize(QtCore.QSize(0, 50))
        self.frmTitulo.setStyleSheet("")
        self.frmTitulo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmTitulo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmTitulo.setObjectName("frmTitulo")
        self.frmLogo = QtWidgets.QFrame(self.frmTitulo)
        self.frmLogo.setGeometry(QtCore.QRect(8, -4, 51, 41))
        self.frmLogo.setStyleSheet("")
        self.frmLogo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmLogo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmLogo.setObjectName("frmLogo")
        self.lblLogo = QtWidgets.QLabel(self.frmTitulo)
        self.lblLogo.setGeometry(QtCore.QRect(68, 2, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.lblLogo.setFont(font)
        self.lblLogo.setWordWrap(False)
        self.lblLogo.setObjectName("lblLogo")
        self.horizontalLayout_5.addWidget(self.frmTitulo)
        self.horizontalLayout_2.addWidget(self.frmTituloContenedor)
        self.frmBotonera = QtWidgets.QFrame(self.frmCabecera)
        self.frmBotonera.setMaximumSize(QtCore.QSize(275, 16777215))
        self.frmBotonera.setStyleSheet("")
        self.frmBotonera.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmBotonera.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmBotonera.setObjectName("frmBotonera")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frmBotonera)
        self.horizontalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblBarraUsuario = QtWidgets.QLabel(self.frmBotonera)
        self.lblBarraUsuario.setWordWrap(False)
        self.lblBarraUsuario.setObjectName("lblBarraUsuario")
        self.horizontalLayout_3.addWidget(self.lblBarraUsuario)
        self.btnMinimizar = QtWidgets.QPushButton(self.frmBotonera)
        self.btnMinimizar.setMaximumSize(QtCore.QSize(30, 26))
        self.btnMinimizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMinimizar.setStyleSheet("")
        self.btnMinimizar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconos/iconos/cil-window-minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMinimizar.setIcon(icon1)
        self.btnMinimizar.setIconSize(QtCore.QSize(16, 16))
        self.btnMinimizar.setObjectName("btnMinimizar")
        self.horizontalLayout_3.addWidget(self.btnMinimizar)
        self.btnMaximizar = QtWidgets.QPushButton(self.frmBotonera)
        self.btnMaximizar.setMaximumSize(QtCore.QSize(30, 26))
        self.btnMaximizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMaximizar.setStyleSheet("")
        self.btnMaximizar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconos/iconos/cil-window-restore.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMaximizar.setIcon(icon2)
        self.btnMaximizar.setIconSize(QtCore.QSize(16, 16))
        self.btnMaximizar.setObjectName("btnMaximizar")
        self.horizontalLayout_3.addWidget(self.btnMaximizar)
        self.btnCerrar = QtWidgets.QPushButton(self.frmBotonera)
        self.btnCerrar.setMaximumSize(QtCore.QSize(30, 26))
        self.btnCerrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCerrar.setStyleSheet("")
        self.btnCerrar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/iconos/iconos/cil-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCerrar.setIcon(icon3)
        self.btnCerrar.setIconSize(QtCore.QSize(16, 16))
        self.btnCerrar.setObjectName("btnCerrar")
        self.horizontalLayout_3.addWidget(self.btnCerrar)
        self.horizontalLayout_2.addWidget(self.frmBotonera)
        self.verticalLayout.addWidget(self.frmCabecera)
        self.frmCuerpo = QtWidgets.QFrame(self.centralwidget)
        self.frmCuerpo.setStyleSheet("")
        self.frmCuerpo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmCuerpo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmCuerpo.setObjectName("frmCuerpo")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frmCuerpo)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frmMenuIzq = QtWidgets.QFrame(self.frmCuerpo)
        self.frmMenuIzq.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frmMenuIzq.setStyleSheet("")
        self.frmMenuIzq.setFrameShape(QtWidgets.QFrame.Box)
        self.frmMenuIzq.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmMenuIzq.setLineWidth(0)
        self.frmMenuIzq.setObjectName("frmMenuIzq")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frmMenuIzq)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frmBotonesTop = QtWidgets.QFrame(self.frmMenuIzq)
        self.frmBotonesTop.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmBotonesTop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmBotonesTop.setLineWidth(0)
        self.frmBotonesTop.setObjectName("frmBotonesTop")
        self.formLayout = QtWidgets.QFormLayout(self.frmBotonesTop)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.btnInicio = QtWidgets.QPushButton(self.frmBotonesTop)
        self.btnInicio.setMinimumSize(QtCore.QSize(140, 0))
        self.btnInicio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnInicio.setObjectName("btnInicio")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.btnInicio)
        self.btnCuenta = QtWidgets.QPushButton(self.frmBotonesTop)
        self.btnCuenta.setMinimumSize(QtCore.QSize(140, 0))
        self.btnCuenta.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCuenta.setObjectName("btnCuenta")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.btnCuenta)
        self.btnClientes = QtWidgets.QPushButton(self.frmBotonesTop)
        self.btnClientes.setMinimumSize(QtCore.QSize(140, 0))
        self.btnClientes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnClientes.setObjectName("btnClientes")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.btnClientes)
        self.verticalLayout_2.addWidget(self.frmBotonesTop)
        self.btnAjustes = QtWidgets.QPushButton(self.frmMenuIzq)
        self.btnAjustes.setMinimumSize(QtCore.QSize(140, 0))
        self.btnAjustes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAjustes.setObjectName("btnAjustes")
        self.verticalLayout_2.addWidget(self.btnAjustes)
        self.horizontalLayout.addWidget(self.frmMenuIzq)
        self.frmContenido = QtWidgets.QFrame(self.frmCuerpo)
        self.frmContenido.setStyleSheet("")
        self.frmContenido.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmContenido.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmContenido.setObjectName("frmContenido")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frmContenido)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tablaContenido = QtWidgets.QStackedWidget(self.frmContenido)
        self.tablaContenido.setStyleSheet("")
        self.tablaContenido.setObjectName("tablaContenido")
        self.tabClientes = QtWidgets.QWidget()
        self.tabClientes.setObjectName("tabClientes")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabClientes)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.tabClientes)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.tablaContenido.addWidget(self.tabClientes)
        self.tabInicio = QtWidgets.QWidget()
        self.tabInicio.setStyleSheet("background-color: rgb(85, 170, 80);")
        self.tabInicio.setObjectName("tabInicio")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tabInicio)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.tabInicio)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.tablaContenido.addWidget(self.tabInicio)
        self.tabCuenta = QtWidgets.QWidget()
        self.tabCuenta.setStyleSheet("/* Color de fondo gris*/\n"
"QWidget #tabCuenta\n"
"{\n"
"    background-color: rgb(203, 203, 203);\n"
"}\n"
"\n"
"/* Estilo del cuadro de login */\n"
"QFrame#frmDatosLogin\n"
"{\n"
"    border-radius: 20px;\n"
"    border: 2px solid rgb(198, 160, 30);\n"
"    background-color: rgb(32, 76, 123);\n"
"}\n"
"\n"
"/* Estilo del titulo */\n"
"QLabel#lblTituloLogin\n"
"{\n"
"    color: rgb(198, 160, 30);\n"
"    font: 25 17pt \"Bahnschrift Light\";\n"
"}\n"
"\n"
"/* Estilo de las dos etiquetas */\n"
"QLabel#lblUsuario, #lblPassword\n"
"{\n"
"    color: rgb(225, 225, 225);\n"
"    font: 25 12pt \"Bahnschrift Light\";\n"
"}\n"
"\n"
"/* Estilo de las dos cajas de texto */\n"
"QLineEdit#txtUsuario, #txtPassword\n"
"{\n"
"    border: 1px solid rgb(198, 160, 30);\n"
"    border-radius: 10px;\n"
"    margin-top: 10px;\n"
"    margin-right: 10px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    background-color: rgb(225, 225, 225);\n"
"    color: rgb(77, 77, 77);\n"
"    font: 25 10pt \"Bahnschrift Light\";\n"
"}\n"
"\n"
"/* Estilo de las dos cajas de texto cuando se posicionan en ellas con el ratón */\n"
"QLineEdit#txtUsuario:hover, #txtPassword:hover\n"
"{\n"
"    border: 2px solid rgb(0, 66, 124);\n"
"}\n"
"\n"
"/* Estilo de las dos cajas de texto cuando se tiene el foco en ellas */\n"
"QLineEdit#txtUsuario:focus, #txtPassword:focus\n"
"{\n"
"    border: 2px solid rgb(206, 206, 206);\n"
"    color: rgb(52, 52, 52);\n"
"}\n"
"\n"
"/* Estilo del texto del checkbox */\n"
"QCheckBox#chkSesion\n"
"{\n"
"    color: rgb(225, 225, 225);\n"
"    font: 25 10pt \"Bahnschrift Light\";\n"
"}\n"
"\n"
"/* Estilo de la caja checkbox */\n"
"QCheckBox#chkSesion::indicator\n"
"{\n"
"    border: 1px solid rgb(198, 160, 30);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(225, 225, 225);\n"
"    margin-right: 3px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"/* Estilo de la caja checkbox cuando se posiciona el el check con el ratón */\n"
"QCheckBox#chkSesion::indicator:hover\n"
"{\n"
"    border: 1px solid rgb(0, 66, 124);\n"
"}\n"
"\n"
"/* Estilo de la caja checkbox cuando se marca el check */\n"
"QCheckBox#chkSesion::indicator:checked\n"
"{\n"
"    background: 2px solid rgb(198, 160, 30);\n"
"    background-image: url(:/iconos/iconos/cil-check.png);\n"
"}\n"
"\n"
"/* Estilo del botón de \"Acceder\" */\n"
"QPushButton#btnLogin\n"
"{\n"
"    border: 1px solid rgb(198, 160, 30);\n"
"    border-radius: 10px;\n"
"    padding: 15px;\n"
"    margin-top:10px;\n"
"    margin-right:10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.528, y1:0.858, x2:0.517409, y2:0.159, stop:0 rgba(23, 55, 87, 255), stop:1 rgba(42, 100, 165, 255));\n"
"    color: rgb(225, 225, 225);\n"
"    font: 25 10pt \"Bahnschrift Light\";\n"
"}\n"
"\n"
"/* Color del botón Acceder cuando se posiciona el cursor */\n"
"QPushButton#btnLogin:hover\n"
"{\n"
"      background-color:qlineargradient(spread:pad, x1:0.528409, y1:0.733,                     x2:0.5, y2:0.17, stop:0 #b28d0b, stop:1 #f5cc3d);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Color del botón Acceder cuando se pulsa el botón */\n"
"QPushButton#btnLogin:pressed\n"
"{\n"
"    font-weight: bold;\n"
"    background-color: #b28d0b;\n"
"}\n"
"\n"
"\n"
"")
        self.tabCuenta.setObjectName("tabCuenta")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tabCuenta)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frmLogin = QtWidgets.QFrame(self.tabCuenta)
        self.frmLogin.setStyleSheet("")
        self.frmLogin.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmLogin.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmLogin.setObjectName("frmLogin")
        self.gridLayout = QtWidgets.QGridLayout(self.frmLogin)
        self.gridLayout.setObjectName("gridLayout")
        self.frmDatosLogin = QtWidgets.QFrame(self.frmLogin)
        self.frmDatosLogin.setMinimumSize(QtCore.QSize(380, 350))
        self.frmDatosLogin.setMaximumSize(QtCore.QSize(380, 360))
        self.frmDatosLogin.setStyleSheet("")
        self.frmDatosLogin.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmDatosLogin.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmDatosLogin.setObjectName("frmDatosLogin")
        self.lblUsuario = QtWidgets.QLabel(self.frmDatosLogin)
        self.lblUsuario.setGeometry(QtCore.QRect(59, 90, 70, 40))
        self.lblUsuario.setMinimumSize(QtCore.QSize(70, 40))
        self.lblUsuario.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.lblUsuario.setFont(font)
        self.lblUsuario.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblUsuario.setObjectName("lblUsuario")
        self.txtUsuario = QtWidgets.QLineEdit(self.frmDatosLogin)
        self.txtUsuario.setGeometry(QtCore.QRect(159, 80, 200, 58))
        self.txtUsuario.setMinimumSize(QtCore.QSize(200, 40))
        self.txtUsuario.setMaximumSize(QtCore.QSize(200, 16777215))
        self.txtUsuario.setStyleSheet("")
        self.txtUsuario.setAlignment(QtCore.Qt.AlignCenter)
        self.txtUsuario.setObjectName("txtUsuario")
        self.lblPassword = QtWidgets.QLabel(self.frmDatosLogin)
        self.lblPassword.setGeometry(QtCore.QRect(59, 157, 100, 40))
        self.lblPassword.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.lblPassword.setFont(font)
        self.lblPassword.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblPassword.setObjectName("lblPassword")
        self.txtPassword = QtWidgets.QLineEdit(self.frmDatosLogin)
        self.txtPassword.setGeometry(QtCore.QRect(159, 144, 200, 58))
        self.txtPassword.setMinimumSize(QtCore.QSize(200, 40))
        self.txtPassword.setMaximumSize(QtCore.QSize(200, 16777215))
        self.txtPassword.setStyleSheet("")
        self.txtPassword.setMaxLength(18)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setAlignment(QtCore.Qt.AlignCenter)
        self.txtPassword.setObjectName("txtPassword")
        self.btnLogin = QtWidgets.QPushButton(self.frmDatosLogin)
        self.btnLogin.setGeometry(QtCore.QRect(159, 259, 200, 60))
        self.btnLogin.setMinimumSize(QtCore.QSize(200, 30))
        self.btnLogin.setMaximumSize(QtCore.QSize(200, 60))
        self.btnLogin.setObjectName("btnLogin")
        self.lblTituloLogin = QtWidgets.QLabel(self.frmDatosLogin)
        self.lblTituloLogin.setGeometry(QtCore.QRect(110, 21, 161, 31))
        self.lblTituloLogin.setObjectName("lblTituloLogin")
        self.lblIconoUsuario = QtWidgets.QLabel(self.frmDatosLogin)
        self.lblIconoUsuario.setGeometry(QtCore.QRect(19, 90, 40, 40))
        self.lblIconoUsuario.setMinimumSize(QtCore.QSize(40, 40))
        self.lblIconoUsuario.setText("")
        self.lblIconoUsuario.setPixmap(QtGui.QPixmap(":/iconos/iconos/cil-user.png"))
        self.lblIconoUsuario.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIconoUsuario.setObjectName("lblIconoUsuario")
        self.chkSesion = QtWidgets.QCheckBox(self.frmDatosLogin)
        self.chkSesion.setGeometry(QtCore.QRect(158, 220, 201, 31))
        self.chkSesion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chkSesion.setChecked(False)
        self.chkSesion.setObjectName("chkSesion")
        self.lblIconoPass = QtWidgets.QLabel(self.frmDatosLogin)
        self.lblIconoPass.setGeometry(QtCore.QRect(19, 157, 40, 40))
        self.lblIconoPass.setMinimumSize(QtCore.QSize(40, 40))
        self.lblIconoPass.setText("")
        self.lblIconoPass.setPixmap(QtGui.QPixmap(":/iconos/iconos/cil-https.png"))
        self.lblIconoPass.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIconoPass.setObjectName("lblIconoPass")
        self.gridLayout.addWidget(self.frmDatosLogin, 1, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.frmLogin, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.tablaContenido.addWidget(self.tabCuenta)
        self.tabAjustes = QtWidgets.QWidget()
        self.tabAjustes.setStyleSheet("background-color: rgb(85, 200, 255);")
        self.tabAjustes.setObjectName("tabAjustes")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabAjustes)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.tabAjustes)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.tablaContenido.addWidget(self.tabAjustes)
        self.verticalLayout_4.addWidget(self.tablaContenido)
        self.horizontalLayout.addWidget(self.frmContenido)
        self.verticalLayout.addWidget(self.frmCuerpo)
        self.frmBarraEstado = QtWidgets.QFrame(self.centralwidget)
        self.frmBarraEstado.setMinimumSize(QtCore.QSize(0, 15))
        self.frmBarraEstado.setMaximumSize(QtCore.QSize(16777215, 15))
        self.frmBarraEstado.setStyleSheet("")
        self.frmBarraEstado.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmBarraEstado.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmBarraEstado.setObjectName("frmBarraEstado")
        self.verticalLayout.addWidget(self.frmBarraEstado)
        venPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(venPrincipal)
        self.tablaContenido.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(venPrincipal)
        venPrincipal.setTabOrder(self.txtUsuario, self.txtPassword)
        venPrincipal.setTabOrder(self.txtPassword, self.chkSesion)
        venPrincipal.setTabOrder(self.chkSesion, self.btnLogin)
        venPrincipal.setTabOrder(self.btnLogin, self.btnInicio)
        venPrincipal.setTabOrder(self.btnInicio, self.btnCuenta)
        venPrincipal.setTabOrder(self.btnCuenta, self.btnClientes)
        venPrincipal.setTabOrder(self.btnClientes, self.btnAjustes)
        venPrincipal.setTabOrder(self.btnAjustes, self.btnMenu)
        venPrincipal.setTabOrder(self.btnMenu, self.btnMinimizar)
        venPrincipal.setTabOrder(self.btnMinimizar, self.btnCerrar)
        venPrincipal.setTabOrder(self.btnCerrar, self.btnMaximizar)

    def retranslateUi(self, venPrincipal):
        _translate = QtCore.QCoreApplication.translate
        venPrincipal.setWindowTitle(_translate("venPrincipal", "MainWindow"))
        self.btnMenu.setToolTip(_translate("venPrincipal", "Despliega el Menú"))
        self.lblLogo.setText(_translate("venPrincipal", "Hotel Spa La Tacita de Plata"))
        self.lblBarraUsuario.setText(_translate("venPrincipal", "Usuario: Invitado"))
        self.btnMinimizar.setToolTip(_translate("venPrincipal", "Minimizar"))
        self.btnMaximizar.setToolTip(_translate("venPrincipal", "Maximizar"))
        self.btnCerrar.setToolTip(_translate("venPrincipal", "Cerrar"))
        self.btnInicio.setToolTip(_translate("venPrincipal", "Sección \"Inicio\""))
        self.btnInicio.setText(_translate("venPrincipal", "Inicio"))
        self.btnCuenta.setToolTip(_translate("venPrincipal", "Sección \"Cuenta\""))
        self.btnCuenta.setText(_translate("venPrincipal", "Cuenta"))
        self.btnClientes.setToolTip(_translate("venPrincipal", "Sección \"Clientes\""))
        self.btnClientes.setText(_translate("venPrincipal", "PushButton"))
        self.btnAjustes.setToolTip(_translate("venPrincipal", "Sección \"Ajustes\""))
        self.btnAjustes.setText(_translate("venPrincipal", "Ajustes"))
        self.label.setText(_translate("venPrincipal", "Clientes"))
        self.label_2.setText(_translate("venPrincipal", "INICIO"))
        self.lblUsuario.setText(_translate("venPrincipal", "Usuario:"))
        self.txtUsuario.setPlaceholderText(_translate("venPrincipal", "a@example.com"))
        self.lblPassword.setText(_translate("venPrincipal", "Contraseña:"))
        self.btnLogin.setText(_translate("venPrincipal", "Acceder"))
        self.lblTituloLogin.setText(_translate("venPrincipal", "Inicio de Sesión"))
        self.chkSesion.setText(_translate("venPrincipal", "Mantener la sesión iniciada"))
        self.label_4.setText(_translate("venPrincipal", "AJUSTES"))
