# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ver_horarios.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(self.centralwidget)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(Qt.AlignmentFlag.AlignLeading)

        self.verticalLayout.addWidget(self.lblTitle)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabCalendario = QWidget()
        self.tabCalendario.setObjectName(u"tabCalendario")
        self.verticalLayout_2 = QVBoxLayout(self.tabCalendario)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableCalendario = QTableWidget(self.tabCalendario)
        if (self.tableCalendario.columnCount() < 6):
            self.tableCalendario.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableCalendario.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableCalendario.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableCalendario.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableCalendario.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableCalendario.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableCalendario.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableCalendario.rowCount() < 5):
            self.tableCalendario.setRowCount(5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableCalendario.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableCalendario.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableCalendario.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableCalendario.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableCalendario.setVerticalHeaderItem(4, __qtablewidgetitem10)
        self.tableCalendario.setObjectName(u"tableCalendario")
        self.tableCalendario.setAlternatingRowColors(True)
        self.tableCalendario.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableCalendario.setCornerButtonEnabled(False)
        self.tableCalendario.horizontalHeader().setDefaultSectionSize(100)
        self.tableCalendario.horizontalHeader().setStretchLastSection(True)
        self.tableCalendario.verticalHeader().setDefaultSectionSize(40)

        self.verticalLayout_2.addWidget(self.tableCalendario)

        self.tabWidget.addTab(self.tabCalendario, "")
        self.tabMapaCalor = QWidget()
        self.tabMapaCalor.setObjectName(u"tabMapaCalor")
        self.verticalLayout_3 = QVBoxLayout(self.tabMapaCalor)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labelMapaCalor = QLabel(self.tabMapaCalor)
        self.labelMapaCalor.setObjectName(u"labelMapaCalor")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.labelMapaCalor.setFont(font1)

        self.verticalLayout_3.addWidget(self.labelMapaCalor)

        self.tableMapaCalor = QTableWidget(self.tabMapaCalor)
        if (self.tableMapaCalor.columnCount() < 6):
            self.tableMapaCalor.setColumnCount(6)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableMapaCalor.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableMapaCalor.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableMapaCalor.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableMapaCalor.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableMapaCalor.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableMapaCalor.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        if (self.tableMapaCalor.rowCount() < 5):
            self.tableMapaCalor.setRowCount(5)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableMapaCalor.setVerticalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableMapaCalor.setVerticalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableMapaCalor.setVerticalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableMapaCalor.setVerticalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableMapaCalor.setVerticalHeaderItem(4, __qtablewidgetitem21)
        self.tableMapaCalor.setObjectName(u"tableMapaCalor")
        self.tableMapaCalor.setAlternatingRowColors(True)
        self.tableMapaCalor.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableMapaCalor.setCornerButtonEnabled(False)
        self.tableMapaCalor.horizontalHeader().setDefaultSectionSize(100)
        self.tableMapaCalor.horizontalHeader().setStretchLastSection(True)
        self.tableMapaCalor.verticalHeader().setDefaultSectionSize(40)

        self.verticalLayout_3.addWidget(self.tableMapaCalor)

        self.tabWidget.addTab(self.tabMapaCalor, "")
        self.tabDetalle = QWidget()
        self.tabDetalle.setObjectName(u"tabDetalle")
        self.verticalLayout_4 = QVBoxLayout(self.tabDetalle)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelDetalle = QLabel(self.tabDetalle)
        self.labelDetalle.setObjectName(u"labelDetalle")
        self.labelDetalle.setFont(font1)
        self.labelDetalle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.labelDetalle)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnSearch = QPushButton(self.tabDetalle)
        self.btnSearch.setObjectName(u"btnSearch")
        self.btnSearch.setMinimumSize(QSize(200, 30))

        self.horizontalLayout.addWidget(self.btnSearch)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.lblProfilePicture = QLabel(self.tabDetalle)
        self.lblProfilePicture.setObjectName(u"lblProfilePicture")
        self.lblProfilePicture.setMinimumSize(QSize(150, 150))
        self.lblProfilePicture.setMaximumSize(QSize(150, 150))
        self.lblProfilePicture.setFrameShape(QFrame.Shape.Box)
        self.lblProfilePicture.setPixmap(QPixmap(u":/icons/profile_placeholder.png"))
        self.lblProfilePicture.setScaledContents(True)
        self.lblProfilePicture.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lblProfilePicture)

        self.textStudentInfo = QTextEdit(self.tabDetalle)
        self.textStudentInfo.setObjectName(u"textStudentInfo")
        self.textStudentInfo.setMinimumSize(QSize(200, 150))
        self.textStudentInfo.setMaximumSize(QSize(300, 150))
        self.textStudentInfo.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.textStudentInfo)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(self.tabDetalle)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.comboSigla = QComboBox(self.groupBox)
        self.comboSigla.addItem("")
        self.comboSigla.setObjectName(u"comboSigla")

        self.verticalLayout_5.addWidget(self.comboSigla)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tabDetalle)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.comboGrupo = QComboBox(self.groupBox_2)
        self.comboGrupo.addItem("")
        self.comboGrupo.addItem("")
        self.comboGrupo.setObjectName(u"comboGrupo")

        self.verticalLayout_6.addWidget(self.comboGrupo)


        self.horizontalLayout_3.addWidget(self.groupBox_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.groupBoxProfesores = QGroupBox(self.tabDetalle)
        self.groupBoxProfesores.setObjectName(u"groupBoxProfesores")
        self.verticalLayout_7 = QVBoxLayout(self.groupBoxProfesores)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.listProfesores = QListWidget(self.groupBoxProfesores)
        QListWidgetItem(self.listProfesores)
        QListWidgetItem(self.listProfesores)
        QListWidgetItem(self.listProfesores)
        self.listProfesores.setObjectName(u"listProfesores")

        self.verticalLayout_7.addWidget(self.listProfesores)


        self.verticalLayout_4.addWidget(self.groupBoxProfesores)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnRegresar = QPushButton(self.tabDetalle)
        self.btnRegresar.setObjectName(u"btnRegresar")

        self.horizontalLayout_4.addWidget(self.btnRegresar)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.tabDetalle, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ver Horarios", None))
        self.lblTitle.setText(QCoreApplication.translate("MainWindow", u"VER HORARIOS", None))
        ___qtablewidgetitem = self.tableCalendario.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Horas/dias", None));
        ___qtablewidgetitem1 = self.tableCalendario.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Lunes", None));
        ___qtablewidgetitem2 = self.tableCalendario.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Martes", None));
        ___qtablewidgetitem3 = self.tableCalendario.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Mi\u00e9rcoles", None));
        ___qtablewidgetitem4 = self.tableCalendario.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Jueves", None));
        ___qtablewidgetitem5 = self.tableCalendario.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Viernes", None));
        ___qtablewidgetitem6 = self.tableCalendario.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"08:30-10:00", None));
        ___qtablewidgetitem7 = self.tableCalendario.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"10:30-12:00", None));
        ___qtablewidgetitem8 = self.tableCalendario.verticalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"12:00-14:00", None));
        ___qtablewidgetitem9 = self.tableCalendario.verticalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"14:30-16:00", None));
        ___qtablewidgetitem10 = self.tableCalendario.verticalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"16:30-18:00", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCalendario), QCoreApplication.translate("MainWindow", u"Ver Calendario", None))
        self.labelMapaCalor.setText(QCoreApplication.translate("MainWindow", u"Mapa de calor", None))
        ___qtablewidgetitem11 = self.tableMapaCalor.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Horas/dias", None));
        ___qtablewidgetitem12 = self.tableMapaCalor.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Lunes", None));
        ___qtablewidgetitem13 = self.tableMapaCalor.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Martes", None));
        ___qtablewidgetitem14 = self.tableMapaCalor.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Mi\u00e9rcoles", None));
        ___qtablewidgetitem15 = self.tableMapaCalor.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Jueves", None));
        ___qtablewidgetitem16 = self.tableMapaCalor.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Viernes", None));
        ___qtablewidgetitem17 = self.tableMapaCalor.verticalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"08:30-10:00", None));
        ___qtablewidgetitem18 = self.tableMapaCalor.verticalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"10:30-12:00", None));
        ___qtablewidgetitem19 = self.tableMapaCalor.verticalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"12:00-14:00", None));
        ___qtablewidgetitem20 = self.tableMapaCalor.verticalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"14:30-16:00", None));
        ___qtablewidgetitem21 = self.tableMapaCalor.verticalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"16:30-18:00", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMapaCalor), QCoreApplication.translate("MainWindow", u"Mapa de Calor", None))
        self.labelDetalle.setText(QCoreApplication.translate("MainWindow", u"Detalle por Estudiante O Laboratorio", None))
        self.btnSearch.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udd0d search", None))
        self.lblProfilePicture.setText("")
        self.textStudentInfo.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt;\">Nombre: saul</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt;\">CI: 55554444</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inden"
                        "t:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt;\">MATERIA SIS2210</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt;\">Grupo 2</span></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Sigla", None))
        self.comboSigla.setItemText(0, QCoreApplication.translate("MainWindow", u"SIS2210", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Grupo", None))
        self.comboGrupo.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboGrupo.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))

        self.groupBoxProfesores.setTitle("")

        __sortingEnabled = self.listProfesores.isSortingEnabled()
        self.listProfesores.setSortingEnabled(False)
        ___qlistwidgetitem = self.listProfesores.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Marco P\u00e9rez", None));
        ___qlistwidgetitem1 = self.listProfesores.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Selmen Urica", None));
        ___qlistwidgetitem2 = self.listProfesores.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Ruben Salazar", None));
        self.listProfesores.setSortingEnabled(__sortingEnabled)

        self.btnRegresar.setText(QCoreApplication.translate("MainWindow", u"\u25c0 REGRESAR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDetalle), QCoreApplication.translate("MainWindow", u"Detalle por Estudiante o por Laboratorio", None))
    # retranslateUi

