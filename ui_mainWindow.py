# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(460, 405)
        MainWindow.setMinimumSize(QSize(460, 405))
        MainWindow.setMaximumSize(QSize(460, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 460, 405))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(460, 405))
        self.widget.setMaximumSize(QSize(460, 405))
        self.labelColorVerde = QLabel(self.widget)
        self.labelColorVerde.setObjectName(u"labelColorVerde")
        self.labelColorVerde.setGeometry(QRect(200, 260, 95, 35))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelColorVerde.setFont(font)
        self.labelColorVerde.setAlignment(Qt.AlignCenter)
        self.spinBoxId = QSpinBox(self.widget)
        self.spinBoxId.setObjectName(u"spinBoxId")
        self.spinBoxId.setGeometry(QRect(120, 50, 90, 30))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        self.spinBoxId.setFont(font1)
        self.spinBoxId.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBoxId.setWrapping(False)
        self.spinBoxId.setMaximum(9999)
        self.labelCOLOR = QLabel(self.widget)
        self.labelCOLOR.setObjectName(u"labelCOLOR")
        self.labelCOLOR.setGeometry(QRect(10, 290, 95, 35))
        self.labelCOLOR.setFont(font)
        self.labelCOLOR.setAlignment(Qt.AlignCenter)
        self.labelColorRojo = QLabel(self.widget)
        self.labelColorRojo.setObjectName(u"labelColorRojo")
        self.labelColorRojo.setGeometry(QRect(100, 260, 95, 35))
        self.labelColorRojo.setFont(font)
        self.labelColorRojo.setAlignment(Qt.AlignCenter)
        self.spinBoxDestinoY = QSpinBox(self.widget)
        self.spinBoxDestinoY.setObjectName(u"spinBoxDestinoY")
        self.spinBoxDestinoY.setGeometry(QRect(240, 210, 90, 30))
        self.spinBoxDestinoY.setFont(font1)
        self.spinBoxDestinoY.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBoxDestinoY.setWrapping(False)
        self.spinBoxDestinoY.setMaximum(500)
        self.spinBoxColorRojo = QSpinBox(self.widget)
        self.spinBoxColorRojo.setObjectName(u"spinBoxColorRojo")
        self.spinBoxColorRojo.setGeometry(QRect(100, 300, 90, 30))
        self.spinBoxColorRojo.setFont(font1)
        self.spinBoxColorRojo.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBoxColorRojo.setWrapping(False)
        self.spinBoxColorRojo.setMaximum(255)
        self.labelVELOCIDAD = QLabel(self.widget)
        self.labelVELOCIDAD.setObjectName(u"labelVELOCIDAD")
        self.labelVELOCIDAD.setGeometry(QRect(240, 10, 95, 35))
        self.labelVELOCIDAD.setFont(font)
        self.labelVELOCIDAD.setAlignment(Qt.AlignCenter)
        self.labelORIGEN_X = QLabel(self.widget)
        self.labelORIGEN_X.setObjectName(u"labelORIGEN_X")
        self.labelORIGEN_X.setGeometry(QRect(120, 90, 95, 35))
        self.labelORIGEN_X.setFont(font)
        self.labelORIGEN_X.setAlignment(Qt.AlignCenter)
        self.spinBoxVelocidad = QSpinBox(self.widget)
        self.spinBoxVelocidad.setObjectName(u"spinBoxVelocidad")
        self.spinBoxVelocidad.setGeometry(QRect(240, 50, 90, 30))
        self.spinBoxVelocidad.setFont(font1)
        self.spinBoxVelocidad.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBoxVelocidad.setWrapping(False)
        self.spinBoxVelocidad.setMaximum(9999)
        self.spinBoxDestinoX = QSpinBox(self.widget)
        self.spinBoxDestinoX.setObjectName(u"spinBoxDestinoX")
        self.spinBoxDestinoX.setGeometry(QRect(240, 130, 90, 30))
        self.spinBoxDestinoX.setFont(font1)
        self.spinBoxDestinoX.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBoxDestinoX.setWrapping(False)
        self.spinBoxDestinoX.setMaximum(500)
        self.labelDESTINO_X = QLabel(self.widget)
        self.labelDESTINO_X.setObjectName(u"labelDESTINO_X")
        self.labelDESTINO_X.setGeometry(QRect(240, 90, 95, 35))
        self.labelDESTINO_X.setFont(font)
        self.labelDESTINO_X.setAlignment(Qt.AlignCenter)
        self.labelID = QLabel(self.widget)
        self.labelID.setObjectName(u"labelID")
        self.labelID.setGeometry(QRect(120, 10, 95, 35))
        self.labelID.setFont(font)
        self.labelID.setAlignment(Qt.AlignCenter)
        self.labelColorAzul = QLabel(self.widget)
        self.labelColorAzul.setObjectName(u"labelColorAzul")
        self.labelColorAzul.setGeometry(QRect(300, 260, 95, 35))
        self.labelColorAzul.setFont(font)
        self.labelColorAzul.setAlignment(Qt.AlignCenter)
        self.labelDESTINO_Y = QLabel(self.widget)
        self.labelDESTINO_Y.setObjectName(u"labelDESTINO_Y")
        self.labelDESTINO_Y.setGeometry(QRect(240, 170, 95, 35))
        self.labelDESTINO_Y.setFont(font)
        self.labelDESTINO_Y.setAlignment(Qt.AlignCenter)
        self.spinBoxColorVerde = QSpinBox(self.widget)
        self.spinBoxColorVerde.setObjectName(u"spinBoxColorVerde")
        self.spinBoxColorVerde.setGeometry(QRect(200, 300, 90, 30))
        self.spinBoxColorVerde.setFont(font1)
        self.spinBoxColorVerde.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBoxColorVerde.setWrapping(False)
        self.spinBoxColorVerde.setMaximum(255)
        self.spinOrigenY = QSpinBox(self.widget)
        self.spinOrigenY.setObjectName(u"spinOrigenY")
        self.spinOrigenY.setGeometry(QRect(120, 210, 90, 30))
        self.spinOrigenY.setFont(font1)
        self.spinOrigenY.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinOrigenY.setWrapping(False)
        self.spinOrigenY.setMaximum(500)
        self.spinBoxColorAzul = QSpinBox(self.widget)
        self.spinBoxColorAzul.setObjectName(u"spinBoxColorAzul")
        self.spinBoxColorAzul.setGeometry(QRect(300, 300, 90, 30))
        self.spinBoxColorAzul.setFont(font1)
        self.spinBoxColorAzul.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBoxColorAzul.setWrapping(False)
        self.spinBoxColorAzul.setMaximum(255)
        self.spinBoxOrigenX = QSpinBox(self.widget)
        self.spinBoxOrigenX.setObjectName(u"spinBoxOrigenX")
        self.spinBoxOrigenX.setGeometry(QRect(120, 130, 90, 30))
        self.spinBoxOrigenX.setFont(font1)
        self.spinBoxOrigenX.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBoxOrigenX.setWrapping(False)
        self.spinBoxOrigenX.setMaximum(500)
        self.labelORIGEN_Y = QLabel(self.widget)
        self.labelORIGEN_Y.setObjectName(u"labelORIGEN_Y")
        self.labelORIGEN_Y.setGeometry(QRect(120, 170, 95, 35))
        self.labelORIGEN_Y.setFont(font)
        self.labelORIGEN_Y.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 360, 170, 40))
        self.pushButton.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelColorVerde.setText(QCoreApplication.translate("MainWindow", u"VERDE:", None))
        self.labelCOLOR.setText(QCoreApplication.translate("MainWindow", u"COLOR:", None))
        self.labelColorRojo.setText(QCoreApplication.translate("MainWindow", u"ROJO:", None))
        self.labelVELOCIDAD.setText(QCoreApplication.translate("MainWindow", u"VEL.:", None))
        self.labelORIGEN_X.setText(QCoreApplication.translate("MainWindow", u"ORIGEN: X", None))
        self.labelDESTINO_X.setText(QCoreApplication.translate("MainWindow", u"DESTINO: X", None))
        self.labelID.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.labelColorAzul.setText(QCoreApplication.translate("MainWindow", u"AZUL:", None))
        self.labelDESTINO_Y.setText(QCoreApplication.translate("MainWindow", u"DESTINO: Y", None))
        self.labelORIGEN_Y.setText(QCoreApplication.translate("MainWindow", u"ORIGEN: Y", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PRESIONAME", None))
    # retranslateUi

