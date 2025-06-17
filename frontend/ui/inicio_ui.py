# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inicio.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 981)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #F8F9FA;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QVBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(20)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(30, 30, 30, 30)
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setStyleSheet(u"font-size: 32px; \n"
"font-weight: bold; \n"
"color: #212529; \n"
"margin: 20px 0px;")

        self.mainLayout.addWidget(self.titleLabel)

        self.statsLayout = QHBoxLayout()
        self.statsLayout.setSpacing(20)
        self.statsLayout.setObjectName(u"statsLayout")
        self.studentsFrame = QFrame(self.centralwidget)
        self.studentsFrame.setObjectName(u"studentsFrame")
        self.studentsFrame.setStyleSheet(u"QFrame {\n"
"    background-color: #F0F4F8;\n"
"    border: 1px solid #F0F4F8;\n"
"    border-radius: 8px;\n"
"    padding: 15px;\n"
"}")
        self.studentsFrame.setFrameShape(QFrame.Shape.Box)
        self.studentsLayout = QVBoxLayout(self.studentsFrame)
        self.studentsLayout.setObjectName(u"studentsLayout")
        self.studentsHeaderLayout = QHBoxLayout()
        self.studentsHeaderLayout.setObjectName(u"studentsHeaderLayout")
        self.studentsIcon = QLabel(self.studentsFrame)
        self.studentsIcon.setObjectName(u"studentsIcon")
        self.studentsIcon.setStyleSheet(u"font-size: 20px; color: #6C757D; border:none;")

        self.studentsHeaderLayout.addWidget(self.studentsIcon)

        self.studentsTitle = QLabel(self.studentsFrame)
        self.studentsTitle.setObjectName(u"studentsTitle")
        self.studentsTitle.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.studentsTitle.setStyleSheet(u"font-size: 14px; color: black; font-weight: bold; border:none; padding: 0 10px;")

        self.studentsHeaderLayout.addWidget(self.studentsTitle)

        self.studentsHeaderSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.studentsHeaderLayout.addItem(self.studentsHeaderSpacer)


        self.studentsLayout.addLayout(self.studentsHeaderLayout)

        self.studentsValue = QLabel(self.studentsFrame)
        self.studentsValue.setObjectName(u"studentsValue")
        self.studentsValue.setStyleSheet(u"font-size: 36px; color: #2567B3; font-weight: bold; margin-left: -80px;")
        self.studentsValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.studentsLayout.addWidget(self.studentsValue)


        self.statsLayout.addWidget(self.studentsFrame)

        self.labsFrame = QFrame(self.centralwidget)
        self.labsFrame.setObjectName(u"labsFrame")
        self.labsFrame.setStyleSheet(u"QFrame {\n"
"    background-color: #F0F4F8;\n"
"    border: 1px solid #F0F4F8;\n"
"    border-radius: 8px;\n"
"    padding: 15px;\n"
"}")
        self.labsFrame.setFrameShape(QFrame.Shape.Box)
        self.labsLayout = QVBoxLayout(self.labsFrame)
        self.labsLayout.setObjectName(u"labsLayout")
        self.labsHeaderLayout = QHBoxLayout()
        self.labsHeaderLayout.setObjectName(u"labsHeaderLayout")
        self.labsIcon = QLabel(self.labsFrame)
        self.labsIcon.setObjectName(u"labsIcon")
        self.labsIcon.setStyleSheet(u"font-size: 20px; color: #6C757D; border:none;")

        self.labsHeaderLayout.addWidget(self.labsIcon)

        self.labsTitle = QLabel(self.labsFrame)
        self.labsTitle.setObjectName(u"labsTitle")
        self.labsTitle.setStyleSheet(u"font-size: 14px; color: black; font-weight: bold; border:none; padding: 0 10px;")

        self.labsHeaderLayout.addWidget(self.labsTitle)

        self.labsHeaderSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.labsHeaderLayout.addItem(self.labsHeaderSpacer)


        self.labsLayout.addLayout(self.labsHeaderLayout)

        self.labsValue = QLabel(self.labsFrame)
        self.labsValue.setObjectName(u"labsValue")
        font = QFont()
        font.setBold(True)
        font.setKerning(True)
        self.labsValue.setFont(font)
        self.labsValue.setStyleSheet(u"font-size: 36px; color: #2567B3; font-weight: bold; margin-left: -100px;")
        self.labsValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labsValue.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.labsLayout.addWidget(self.labsValue)


        self.statsLayout.addWidget(self.labsFrame)

        self.conflictsFrame = QFrame(self.centralwidget)
        self.conflictsFrame.setObjectName(u"conflictsFrame")
        self.conflictsFrame.setStyleSheet(u"QFrame {\n"
"    background-color: #F0F4F8;\n"
"    border: 1px solid #F0F4F8;\n"
"    border-radius: 8px;\n"
"    padding: 15px;\n"
"}")
        self.conflictsFrame.setFrameShape(QFrame.Shape.Box)
        self.conflictsLayout = QVBoxLayout(self.conflictsFrame)
        self.conflictsLayout.setObjectName(u"conflictsLayout")
        self.conflictsHeaderLayout = QHBoxLayout()
        self.conflictsHeaderLayout.setObjectName(u"conflictsHeaderLayout")
        self.conflictsIcon = QLabel(self.conflictsFrame)
        self.conflictsIcon.setObjectName(u"conflictsIcon")
        self.conflictsIcon.setStyleSheet(u"font-size: 20px; color: #6C757D; border:none;")

        self.conflictsHeaderLayout.addWidget(self.conflictsIcon)

        self.conflictsTitle = QLabel(self.conflictsFrame)
        self.conflictsTitle.setObjectName(u"conflictsTitle")
        self.conflictsTitle.setStyleSheet(u"font-size: 14px; color: black; font-weight: bold; border:none; padding: 0 10px;")

        self.conflictsHeaderLayout.addWidget(self.conflictsTitle)

        self.conflictsHeaderSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.conflictsHeaderLayout.addItem(self.conflictsHeaderSpacer)


        self.conflictsLayout.addLayout(self.conflictsHeaderLayout)

        self.conflictsValue = QLabel(self.conflictsFrame)
        self.conflictsValue.setObjectName(u"conflictsValue")
        self.conflictsValue.setStyleSheet(u"font-size: 36px; color: #2567B3; font-weight: bold; margin-left: -140px;")
        self.conflictsValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.conflictsLayout.addWidget(self.conflictsValue)


        self.statsLayout.addWidget(self.conflictsFrame)


        self.mainLayout.addLayout(self.statsLayout)

        self.middleSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.middleSpacer)

        self.actionsLayout = QGridLayout()
        self.actionsLayout.setSpacing(20)
        self.actionsLayout.setObjectName(u"actionsLayout")
        self.groupsFrame = QFrame(self.centralwidget)
        self.groupsFrame.setObjectName(u"groupsFrame")
        self.groupsFrame.setStyleSheet(u"QFrame {\n"
"    background-color: white;\n"
"    border: 2px solid #2567B3;\n"
"    border-radius: 12px;\n"
"    padding: 20px;\n"
"}")
        self.groupsFrame.setFrameShape(QFrame.Shape.Box)
        self.groupsLayout = QVBoxLayout(self.groupsFrame)
        self.groupsLayout.setObjectName(u"groupsLayout")
        self.groupsHeaderLayout = QHBoxLayout()
        self.groupsHeaderLayout.setObjectName(u"groupsHeaderLayout")
        self.groupsHeaderLayout.setContentsMargins(0, 0, 0, 0)
        self.groupsIcon = QLabel(self.groupsFrame)
        self.groupsIcon.setObjectName(u"groupsIcon")
        self.groupsIcon.setStyleSheet(u"font-size: 20px; color: #6C757D; border:none;")

        self.groupsHeaderLayout.addWidget(self.groupsIcon)

        self.groupsCardTitle = QLabel(self.groupsFrame)
        self.groupsCardTitle.setObjectName(u"groupsCardTitle")
        self.groupsCardTitle.setStyleSheet(u"font-size: 14px; color: black; font-weight: bold; border:none; padding: 0 10px;")

        self.groupsHeaderLayout.addWidget(self.groupsCardTitle)

        self.groupsCardHeaderSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.groupsHeaderLayout.addItem(self.groupsCardHeaderSpacer)


        self.groupsLayout.addLayout(self.groupsHeaderLayout)

        self.groupsSubtitle = QLabel(self.groupsFrame)
        self.groupsSubtitle.setObjectName(u"groupsSubtitle")
        self.groupsSubtitle.setStyleSheet(u"font-size: 14px; color: black; margin: 3px 40px; border:none; font-weight:bold;")
        self.groupsSubtitle.setMargin(0)

        self.groupsLayout.addWidget(self.groupsSubtitle)

        self.assignLabsButton = QPushButton(self.groupsFrame)
        self.assignLabsButton.setObjectName(u"assignLabsButton")
        self.assignLabsButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #2567B3;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #357ABD;\n"
"}")

        self.groupsLayout.addWidget(self.assignLabsButton)


        self.actionsLayout.addWidget(self.groupsFrame, 0, 0, 1, 1)

        self.scheduleFrame = QFrame(self.centralwidget)
        self.scheduleFrame.setObjectName(u"scheduleFrame")
        self.scheduleFrame.setStyleSheet(u"QFrame {\n"
"    background-color: white;\n"
"    border: 2px solid #2567B3;\n"
"    border-radius: 12px;\n"
"    padding: 20px;\n"
"}")
        self.scheduleFrame.setFrameShape(QFrame.Shape.Box)
        self.scheduleLayout = QVBoxLayout(self.scheduleFrame)
        self.scheduleLayout.setObjectName(u"scheduleLayout")
        self.scheduleHeaderLayout = QHBoxLayout()
        self.scheduleHeaderLayout.setObjectName(u"scheduleHeaderLayout")
        self.scheduleIcon = QLabel(self.scheduleFrame)
        self.scheduleIcon.setObjectName(u"scheduleIcon")
        self.scheduleIcon.setStyleSheet(u"font-size: 20px; color: #6C757D; border:none;")

        self.scheduleHeaderLayout.addWidget(self.scheduleIcon)

        self.scheduleCardTitle = QLabel(self.scheduleFrame)
        self.scheduleCardTitle.setObjectName(u"scheduleCardTitle")
        self.scheduleCardTitle.setStyleSheet(u"font-size: 14px; color: black; font-weight: bold; border:none; padding: 0 10px;")

        self.scheduleHeaderLayout.addWidget(self.scheduleCardTitle)

        self.scheduleCardHeaderSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.scheduleHeaderLayout.addItem(self.scheduleCardHeaderSpacer)


        self.scheduleLayout.addLayout(self.scheduleHeaderLayout)

        self.scheduleSubtitle = QLabel(self.scheduleFrame)
        self.scheduleSubtitle.setObjectName(u"scheduleSubtitle")
        font1 = QFont()
        font1.setBold(True)
        self.scheduleSubtitle.setFont(font1)
        self.scheduleSubtitle.setStyleSheet(u"font-size: 14px; color: black; margin: 3px 0px; border:none; font-weight:bold;")

        self.scheduleLayout.addWidget(self.scheduleSubtitle)

        self.viewScheduleButton = QPushButton(self.scheduleFrame)
        self.viewScheduleButton.setObjectName(u"viewScheduleButton")
        self.viewScheduleButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #2567B3;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #357ABD;\n"
"}")

        self.scheduleLayout.addWidget(self.viewScheduleButton)


        self.actionsLayout.addWidget(self.scheduleFrame, 0, 1, 1, 1)

        self.lastAssignmentFrame = QFrame(self.centralwidget)
        self.lastAssignmentFrame.setObjectName(u"lastAssignmentFrame")
        self.lastAssignmentFrame.setStyleSheet(u"QFrame {\n"
"    background-color: #F0F4F8;\n"
"    border: 2px solid #F0F4F8;\n"
"    border-radius: 12px;\n"
"    padding: 20px;\n"
"}")
        self.lastAssignmentFrame.setFrameShape(QFrame.Shape.Box)
        self.lastAssignmentLayout = QVBoxLayout(self.lastAssignmentFrame)
        self.lastAssignmentLayout.setObjectName(u"lastAssignmentLayout")
        self.lastAssignmentHeaderLayout = QHBoxLayout()
        self.lastAssignmentHeaderLayout.setObjectName(u"lastAssignmentHeaderLayout")
        self.lastAssignmentIcon = QLabel(self.lastAssignmentFrame)
        self.lastAssignmentIcon.setObjectName(u"lastAssignmentIcon")
        self.lastAssignmentIcon.setStyleSheet(u"font-size: 20px; color: #6C757D; border:none;")

        self.lastAssignmentHeaderLayout.addWidget(self.lastAssignmentIcon)

        self.lastAssignmentTitle = QLabel(self.lastAssignmentFrame)
        self.lastAssignmentTitle.setObjectName(u"lastAssignmentTitle")
        self.lastAssignmentTitle.setStyleSheet(u"font-size: 14px; color: black; font-weight: bold; border:none; padding: 0 10px;")

        self.lastAssignmentHeaderLayout.addWidget(self.lastAssignmentTitle)

        self.lastAssignmentHeaderSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lastAssignmentHeaderLayout.addItem(self.lastAssignmentHeaderSpacer)


        self.lastAssignmentLayout.addLayout(self.lastAssignmentHeaderLayout)

        self.lastAssignmentInfo = QLabel(self.lastAssignmentFrame)
        self.lastAssignmentInfo.setObjectName(u"lastAssignmentInfo")
        self.lastAssignmentInfo.setStyleSheet(u"font-size: 14px; color: black; margin: 3px 0px; border:none; font-weight:bold;")
        self.lastAssignmentInfo.setWordWrap(True)

        self.lastAssignmentLayout.addWidget(self.lastAssignmentInfo)


        self.actionsLayout.addWidget(self.lastAssignmentFrame, 0, 2, 1, 1)

        self.importFrame = QFrame(self.centralwidget)
        self.importFrame.setObjectName(u"importFrame")
        self.importFrame.setStyleSheet(u"QFrame {\n"
"    background-color: white;\n"
"    border: 2px solid #2567B3;\n"
"    border-radius: 12px;\n"
"    padding: 20px;\n"
"}")
        self.importFrame.setFrameShape(QFrame.Shape.Box)
        self.importLayout = QVBoxLayout(self.importFrame)
        self.importLayout.setObjectName(u"importLayout")
        self.importHeaderLayout = QHBoxLayout()
        self.importHeaderLayout.setObjectName(u"importHeaderLayout")
        self.importIcon = QLabel(self.importFrame)
        self.importIcon.setObjectName(u"importIcon")
        self.importIcon.setStyleSheet(u"font-size: 20px; color: #6C757D; border:none;")

        self.importHeaderLayout.addWidget(self.importIcon)

        self.importTitle = QLabel(self.importFrame)
        self.importTitle.setObjectName(u"importTitle")
        self.importTitle.setFont(font1)
        self.importTitle.setStyleSheet(u"font-size: 14px; color: black; font-weight: bold; border:none; padding: 0 10px;")

        self.importHeaderLayout.addWidget(self.importTitle)

        self.importHeaderSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.importHeaderLayout.addItem(self.importHeaderSpacer)


        self.importLayout.addLayout(self.importHeaderLayout)

        self.importSubtitle = QLabel(self.importFrame)
        self.importSubtitle.setObjectName(u"importSubtitle")
        self.importSubtitle.setStyleSheet(u"font-size: 14px; color: black; margin: 3px 0px; border:none; font-weight:bold;")

        self.importLayout.addWidget(self.importSubtitle)

        self.loadFilesButton = QPushButton(self.importFrame)
        self.loadFilesButton.setObjectName(u"loadFilesButton")
        self.loadFilesButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #2567B3;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #357ABD;\n"
"}")

        self.importLayout.addWidget(self.loadFilesButton)


        self.actionsLayout.addWidget(self.importFrame, 1, 0, 1, 1)

        self.studentsManagementFrame = QFrame(self.centralwidget)
        self.studentsManagementFrame.setObjectName(u"studentsManagementFrame")
        self.studentsManagementFrame.setStyleSheet(u"QFrame {\n"
"    background-color: white;\n"
"    border: 2px solid #2567B3;\n"
"    border-radius: 12px;\n"
"    padding: 20px;\n"
"}")
        self.studentsManagementFrame.setFrameShape(QFrame.Shape.Box)
        self.studentsManagementLayout = QVBoxLayout(self.studentsManagementFrame)
        self.studentsManagementLayout.setObjectName(u"studentsManagementLayout")
        self.studentsManagementHeaderLayout = QHBoxLayout()
        self.studentsManagementHeaderLayout.setObjectName(u"studentsManagementHeaderLayout")
        self.studentsManagementIcon = QLabel(self.studentsManagementFrame)
        self.studentsManagementIcon.setObjectName(u"studentsManagementIcon")
        self.studentsManagementIcon.setStyleSheet(u"font-size: 20px; color: #6C757D; border:none;")

        self.studentsManagementHeaderLayout.addWidget(self.studentsManagementIcon)

        self.studentsManagementTitle = QLabel(self.studentsManagementFrame)
        self.studentsManagementTitle.setObjectName(u"studentsManagementTitle")
        self.studentsManagementTitle.setFont(font1)
        self.studentsManagementTitle.setStyleSheet(u"font-size: 14px; color: black; font-weight: bold; border:none; padding: 0 10px;")

        self.studentsManagementHeaderLayout.addWidget(self.studentsManagementTitle)

        self.studentsManagementHeaderSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.studentsManagementHeaderLayout.addItem(self.studentsManagementHeaderSpacer)


        self.studentsManagementLayout.addLayout(self.studentsManagementHeaderLayout)

        self.studentsManagementSubtitle = QLabel(self.studentsManagementFrame)
        self.studentsManagementSubtitle.setObjectName(u"studentsManagementSubtitle")
        self.studentsManagementSubtitle.setStyleSheet(u"font-size: 14px; color: black; margin: 3px 0px; border:none; font-weight:bold;")

        self.studentsManagementLayout.addWidget(self.studentsManagementSubtitle)

        self.viewStudentsButton = QPushButton(self.studentsManagementFrame)
        self.viewStudentsButton.setObjectName(u"viewStudentsButton")
        self.viewStudentsButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #2567B3;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #357ABD;\n"
"}")

        self.studentsManagementLayout.addWidget(self.viewStudentsButton)


        self.actionsLayout.addWidget(self.studentsManagementFrame, 1, 1, 1, 1)

        self.alertsFrame = QFrame(self.centralwidget)
        self.alertsFrame.setObjectName(u"alertsFrame")
        self.alertsFrame.setStyleSheet(u"QFrame {\n"
"    background-color: white;\n"
"    border: 2px solid #CF2A27;\n"
"    border-radius: 12px;\n"
"    padding: 20px;\n"
"}")
        self.alertsFrame.setFrameShape(QFrame.Shape.Box)
        self.alertsLayout = QVBoxLayout(self.alertsFrame)
        self.alertsLayout.setObjectName(u"alertsLayout")
        self.alertsHeaderLayout = QHBoxLayout()
        self.alertsHeaderLayout.setObjectName(u"alertsHeaderLayout")
        self.alertsIcon = QLabel(self.alertsFrame)
        self.alertsIcon.setObjectName(u"alertsIcon")
        self.alertsIcon.setStyleSheet(u"font-size: 20px; color: #6C757D; border:none;")

        self.alertsHeaderLayout.addWidget(self.alertsIcon)

        self.alertsTitle = QLabel(self.alertsFrame)
        self.alertsTitle.setObjectName(u"alertsTitle")
        self.alertsTitle.setFont(font1)
        self.alertsTitle.setStyleSheet(u"font-size: 14px; color: black; font-weight: bold; border:none; padding: 0 10px;")

        self.alertsHeaderLayout.addWidget(self.alertsTitle)

        self.alertsHeaderSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.alertsHeaderLayout.addItem(self.alertsHeaderSpacer)


        self.alertsLayout.addLayout(self.alertsHeaderLayout)

        self.warningLayout = QHBoxLayout()
        self.warningLayout.setObjectName(u"warningLayout")
        self.warningIcon = QLabel(self.alertsFrame)
        self.warningIcon.setObjectName(u"warningIcon")
        self.warningIcon.setStyleSheet(u"font-size: 14px; color: #6C757D; margin: 5px 0px; border:none;")

        self.warningLayout.addWidget(self.warningIcon)

        self.warningText = QLabel(self.alertsFrame)
        self.warningText.setObjectName(u"warningText")
        self.warningText.setStyleSheet(u"font-size: 14px; color: #CF2A27; margin: 5px 0px; border:none; font-weight:bold;\n"
"")

        self.warningLayout.addWidget(self.warningText)

        self.warningTextSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.warningLayout.addItem(self.warningTextSpacer)


        self.alertsLayout.addLayout(self.warningLayout)

        self.viewAlertsButton = QPushButton(self.alertsFrame)
        self.viewAlertsButton.setObjectName(u"viewAlertsButton")
        self.viewAlertsButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #DC3545;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #CF2A27;\n"
"}")

        self.alertsLayout.addWidget(self.viewAlertsButton)


        self.actionsLayout.addWidget(self.alertsFrame, 1, 2, 1, 1)


        self.mainLayout.addLayout(self.actionsLayout)

        self.bottomSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.bottomSpacer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dashboard INICIO", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"INICIO", None))
        self.studentsIcon.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udc65", None))
        self.studentsTitle.setText(QCoreApplication.translate("MainWindow", u"Estudiantes Registrados", None))
        self.studentsValue.setText(QCoreApplication.translate("MainWindow", u"850", None))
        self.labsIcon.setText(QCoreApplication.translate("MainWindow", u"\ud83c\udfdb\ufe0f", None))
        self.labsTitle.setText(QCoreApplication.translate("MainWindow", u"Laboratorios Disponibles", None))
        self.labsValue.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.conflictsIcon.setText(QCoreApplication.translate("MainWindow", u"\u26a0\ufe0f", None))
        self.conflictsTitle.setText(QCoreApplication.translate("MainWindow", u"Estudiantes con Conflictos", None))
        self.conflictsValue.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.groupsIcon.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udc65", None))
        self.groupsCardTitle.setText(QCoreApplication.translate("MainWindow", u"Grupos Asignados", None))
        self.groupsSubtitle.setText(QCoreApplication.translate("MainWindow", u"12 Grupos Asignados", None))
        self.assignLabsButton.setText(QCoreApplication.translate("MainWindow", u"ASIGNAR LABORATORIOS", None))
        self.scheduleIcon.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udcc5", None))
        self.scheduleCardTitle.setText(QCoreApplication.translate("MainWindow", u"Horarios Asignados", None))
        self.scheduleSubtitle.setText(QCoreApplication.translate("MainWindow", u"Estudiantes con Horarios\n"
"840 Estudiantes", None))
        self.viewScheduleButton.setText(QCoreApplication.translate("MainWindow", u"VER HORARIOS", None))
        self.lastAssignmentIcon.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udd50", None))
        self.lastAssignmentTitle.setText(QCoreApplication.translate("MainWindow", u"\u00daltima Asignaci\u00f3n", None))
        self.lastAssignmentInfo.setText(QCoreApplication.translate("MainWindow", u"22 de marzo del 2025\n"
"Total 765 estudiantes", None))
        self.importIcon.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udce4", None))
        self.importTitle.setText(QCoreApplication.translate("MainWindow", u"Importar Datos", None))
        self.importSubtitle.setText(QCoreApplication.translate("MainWindow", u"Importar CSV", None))
        self.loadFilesButton.setText(QCoreApplication.translate("MainWindow", u"CARGAR ARCHIVOS", None))
        self.studentsManagementIcon.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udc64", None))
        self.studentsManagementTitle.setText(QCoreApplication.translate("MainWindow", u"Estudiantes", None))
        self.studentsManagementSubtitle.setText(QCoreApplication.translate("MainWindow", u"Buscar y gestionar estudiantes", None))
        self.viewStudentsButton.setText(QCoreApplication.translate("MainWindow", u"VER ESTUDIANTES", None))
        self.alertsIcon.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udd14", None))
        self.alertsTitle.setText(QCoreApplication.translate("MainWindow", u"Notificaciones y reportes", None))
        self.warningIcon.setText(QCoreApplication.translate("MainWindow", u"\u26a0\ufe0f", None))
        self.warningText.setText(QCoreApplication.translate("MainWindow", u"5 conflictos detectados", None))
        self.viewAlertsButton.setText(QCoreApplication.translate("MainWindow", u"VER ALERTAS", None))
    # retranslateUi

