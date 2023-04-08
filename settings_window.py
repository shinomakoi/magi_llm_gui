# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_settings.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QSizePolicy,
    QSlider, QSpinBox, QVBoxLayout, QWidget)

class Ui_Settings_Dialog(object):
    def setupUi(self, Settings_Dialog):
        if not Settings_Dialog.objectName():
            Settings_Dialog.setObjectName(u"Settings_Dialog")
        Settings_Dialog.resize(645, 765)
        icon = QIcon()
        icon.addFile(u"icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Settings_Dialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Settings_Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(Settings_Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 5, 0, 1, 1)

        self.typicalPSlider = QSlider(self.groupBox_2)
        self.typicalPSlider.setObjectName(u"typicalPSlider")
        self.typicalPSlider.setMaximum(100)
        self.typicalPSlider.setValue(100)
        self.typicalPSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.typicalPSlider, 6, 1, 1, 1)

        self.maxnewtokensSlider = QSlider(self.groupBox_2)
        self.maxnewtokensSlider.setObjectName(u"maxnewtokensSlider")
        self.maxnewtokensSlider.setMinimum(128)
        self.maxnewtokensSlider.setMaximum(1024)
        self.maxnewtokensSlider.setValue(200)
        self.maxnewtokensSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.maxnewtokensSlider, 2, 1, 1, 1)

        self.oobaServerAddress = QLineEdit(self.groupBox_2)
        self.oobaServerAddress.setObjectName(u"oobaServerAddress")

        self.gridLayout_2.addWidget(self.oobaServerAddress, 1, 1, 1, 1)

        self.top_pSliderLabel = QLabel(self.groupBox_2)
        self.top_pSliderLabel.setObjectName(u"top_pSliderLabel")

        self.gridLayout_2.addWidget(self.top_pSliderLabel, 5, 2, 1, 1)

        self.maxnewtokensSliderLabel = QLabel(self.groupBox_2)
        self.maxnewtokensSliderLabel.setObjectName(u"maxnewtokensSliderLabel")

        self.gridLayout_2.addWidget(self.maxnewtokensSliderLabel, 2, 2, 1, 1)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 4, 0, 1, 1)

        self.tempSliderLabel = QLabel(self.groupBox_2)
        self.tempSliderLabel.setObjectName(u"tempSliderLabel")

        self.gridLayout_2.addWidget(self.tempSliderLabel, 4, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_2.addWidget(self.label_19, 6, 0, 1, 1)

        self.dosampleCheck = QCheckBox(self.groupBox_2)
        self.dosampleCheck.setObjectName(u"dosampleCheck")
        self.dosampleCheck.setChecked(True)

        self.gridLayout_2.addWidget(self.dosampleCheck, 3, 1, 1, 1)

        self.top_pSlider = QSlider(self.groupBox_2)
        self.top_pSlider.setObjectName(u"top_pSlider")
        self.top_pSlider.setMaximum(100)
        self.top_pSlider.setValue(73)
        self.top_pSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.top_pSlider, 5, 1, 1, 1)

        self.typicalPSliderLabel = QLabel(self.groupBox_2)
        self.typicalPSliderLabel.setObjectName(u"typicalPSliderLabel")

        self.gridLayout_2.addWidget(self.typicalPSliderLabel, 6, 2, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)

        self.tempSlider = QSlider(self.groupBox_2)
        self.tempSlider.setObjectName(u"tempSlider")
        self.tempSlider.setMaximum(199)
        self.tempSlider.setValue(72)
        self.tempSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.tempSlider, 4, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.paramsPresetsComboBox = QComboBox(self.groupBox_2)
        self.paramsPresetsComboBox.setObjectName(u"paramsPresetsComboBox")

        self.gridLayout_2.addWidget(self.paramsPresetsComboBox, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(Settings_Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.norepeatngramSlider = QSlider(self.groupBox)
        self.norepeatngramSlider.setObjectName(u"norepeatngramSlider")
        self.norepeatngramSlider.setMaximum(20)
        self.norepeatngramSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.norepeatngramSlider, 4, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.reppenaltySliderLabel = QLabel(self.groupBox)
        self.reppenaltySliderLabel.setObjectName(u"reppenaltySliderLabel")

        self.gridLayout.addWidget(self.reppenaltySliderLabel, 0, 2, 1, 1)

        self.minlengthSlider = QSlider(self.groupBox)
        self.minlengthSlider.setObjectName(u"minlengthSlider")
        self.minlengthSlider.setMaximum(1024)
        self.minlengthSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.minlengthSlider, 3, 1, 1, 1)

        self.encoderrepSlider = QSlider(self.groupBox)
        self.encoderrepSlider.setObjectName(u"encoderrepSlider")
        self.encoderrepSlider.setMaximum(150)
        self.encoderrepSlider.setValue(100)
        self.encoderrepSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.encoderrepSlider, 1, 1, 1, 1)

        self.norepeatngramSliderLabel = QLabel(self.groupBox)
        self.norepeatngramSliderLabel.setObjectName(u"norepeatngramSliderLabel")

        self.gridLayout.addWidget(self.norepeatngramSliderLabel, 4, 2, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)

        self.minlengthSliderLabel = QLabel(self.groupBox)
        self.minlengthSliderLabel.setObjectName(u"minlengthSliderLabel")

        self.gridLayout.addWidget(self.minlengthSliderLabel, 3, 2, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.reppenaltySlider = QSlider(self.groupBox)
        self.reppenaltySlider.setObjectName(u"reppenaltySlider")
        self.reppenaltySlider.setMaximum(150)
        self.reppenaltySlider.setValue(110)
        self.reppenaltySlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.reppenaltySlider, 0, 1, 1, 1)

        self.top_kSlider = QSlider(self.groupBox)
        self.top_kSlider.setObjectName(u"top_kSlider")
        self.top_kSlider.setMaximum(200)
        self.top_kSlider.setValue(40)
        self.top_kSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.top_kSlider, 2, 1, 1, 1)

        self.encoderrepSliderLabel = QLabel(self.groupBox)
        self.encoderrepSliderLabel.setObjectName(u"encoderrepSliderLabel")

        self.gridLayout.addWidget(self.encoderrepSliderLabel, 1, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.top_kSliderLabel = QLabel(self.groupBox)
        self.top_kSliderLabel.setObjectName(u"top_kSliderLabel")

        self.gridLayout.addWidget(self.top_kSliderLabel, 2, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(Settings_Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.penaltyAlphaSlider = QSlider(self.groupBox_3)
        self.penaltyAlphaSlider.setObjectName(u"penaltyAlphaSlider")
        self.penaltyAlphaSlider.setMaximum(500)
        self.penaltyAlphaSlider.setValue(0)
        self.penaltyAlphaSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.penaltyAlphaSlider, 1, 1, 1, 1)

        self.label_26 = QLabel(self.groupBox_3)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_3.addWidget(self.label_26, 2, 0, 1, 1)

        self.earlyStoppingCheck = QCheckBox(self.groupBox_3)
        self.earlyStoppingCheck.setObjectName(u"earlyStoppingCheck")

        self.gridLayout_3.addWidget(self.earlyStoppingCheck, 3, 1, 1, 1)

        self.numbeamsSliderLabel = QLabel(self.groupBox_3)
        self.numbeamsSliderLabel.setObjectName(u"numbeamsSliderLabel")

        self.gridLayout_3.addWidget(self.numbeamsSliderLabel, 0, 2, 1, 1)

        self.numbeamsSlider = QSlider(self.groupBox_3)
        self.numbeamsSlider.setObjectName(u"numbeamsSlider")
        self.numbeamsSlider.setMaximum(5)
        self.numbeamsSlider.setValue(1)
        self.numbeamsSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.numbeamsSlider, 0, 1, 1, 1)

        self.label_21 = QLabel(self.groupBox_3)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_3.addWidget(self.label_21, 1, 0, 1, 1)

        self.penaltyAlphaSliderLabel = QLabel(self.groupBox_3)
        self.penaltyAlphaSliderLabel.setObjectName(u"penaltyAlphaSliderLabel")

        self.gridLayout_3.addWidget(self.penaltyAlphaSliderLabel, 1, 2, 1, 1)

        self.lengthpenaltySliderLabel = QLabel(self.groupBox_3)
        self.lengthpenaltySliderLabel.setObjectName(u"lengthpenaltySliderLabel")

        self.gridLayout_3.addWidget(self.lengthpenaltySliderLabel, 2, 2, 1, 1)

        self.lengthpenaltySlider = QSlider(self.groupBox_3)
        self.lengthpenaltySlider.setObjectName(u"lengthpenaltySlider")
        self.lengthpenaltySlider.setMaximum(50)
        self.lengthpenaltySlider.setValue(10)
        self.lengthpenaltySlider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.lengthpenaltySlider, 2, 1, 1, 1)

        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_3.addWidget(self.label_22, 0, 0, 1, 1)

        self.label_29 = QLabel(self.groupBox_3)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_3.addWidget(self.label_29, 4, 0, 1, 1)

        self.seedValue = QSpinBox(self.groupBox_3)
        self.seedValue.setObjectName(u"seedValue")
        self.seedValue.setMinimum(-1)
        self.seedValue.setMaximum(10000000)
        self.seedValue.setValue(42)

        self.gridLayout_3.addWidget(self.seedValue, 4, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_3)


        self.retranslateUi(Settings_Dialog)
        self.maxnewtokensSlider.actionTriggered.connect(self.maxnewtokensSliderLabel.setNum)
        self.maxnewtokensSlider.valueChanged.connect(self.maxnewtokensSliderLabel.setNum)
        self.numbeamsSlider.valueChanged.connect(self.numbeamsSliderLabel.setNum)
        self.minlengthSlider.valueChanged.connect(self.minlengthSliderLabel.setNum)
        self.norepeatngramSlider.valueChanged.connect(self.norepeatngramSliderLabel.setNum)
        self.top_kSlider.valueChanged.connect(self.top_kSliderLabel.setNum)

        QMetaObject.connectSlotsByName(Settings_Dialog)
    # setupUi

    def retranslateUi(self, Settings_Dialog):
        Settings_Dialog.setWindowTitle(QCoreApplication.translate("Settings_Dialog", u"Parameters", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Settings_Dialog", u"Group 1", None))
        self.label_17.setText(QCoreApplication.translate("Settings_Dialog", u"top_p", None))
        self.oobaServerAddress.setText(QCoreApplication.translate("Settings_Dialog", u"127.0.0.1", None))
        self.top_pSliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"0.73", None))
        self.maxnewtokensSliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"200", None))
        self.label_15.setText(QCoreApplication.translate("Settings_Dialog", u"temperature", None))
        self.tempSliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"0.72", None))
        self.label_2.setText(QCoreApplication.translate("Settings_Dialog", u"Server IP", None))
        self.label_19.setText(QCoreApplication.translate("Settings_Dialog", u"typical_p", None))
        self.dosampleCheck.setText(QCoreApplication.translate("Settings_Dialog", u"do_sample", None))
        self.typicalPSliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"1.0", None))
        self.label_11.setText(QCoreApplication.translate("Settings_Dialog", u"max_new_tokens", None))
        self.label_4.setText(QCoreApplication.translate("Settings_Dialog", u"Preset", None))
        self.groupBox.setTitle(QCoreApplication.translate("Settings_Dialog", u"Group 2", None))
        self.label_3.setText(QCoreApplication.translate("Settings_Dialog", u"encoder_repetition_penalty", None))
        self.reppenaltySliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"1.1", None))
        self.norepeatngramSliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"0", None))
        self.label_9.setText(QCoreApplication.translate("Settings_Dialog", u"no_repeat_ngram_size", None))
        self.minlengthSliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"0", None))
        self.label.setText(QCoreApplication.translate("Settings_Dialog", u"repetition_penalty", None))
        self.label_7.setText(QCoreApplication.translate("Settings_Dialog", u"min_length", None))
        self.encoderrepSliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"1.0", None))
        self.label_5.setText(QCoreApplication.translate("Settings_Dialog", u"top_k", None))
        self.top_kSliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"40", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Settings_Dialog", u"Group 3", None))
        self.label_26.setText(QCoreApplication.translate("Settings_Dialog", u"length_penalty", None))
        self.earlyStoppingCheck.setText(QCoreApplication.translate("Settings_Dialog", u"early_stopping", None))
        self.numbeamsSliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"1", None))
        self.label_21.setText(QCoreApplication.translate("Settings_Dialog", u"penalty_alpha", None))
        self.penaltyAlphaSliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"0", None))
        self.lengthpenaltySliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"1", None))
        self.label_22.setText(QCoreApplication.translate("Settings_Dialog", u"num_beams", None))
        self.label_29.setText(QCoreApplication.translate("Settings_Dialog", u"seed", None))
    # retranslateUi

