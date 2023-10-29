# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_settings.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFrame, QGridLayout, QLabel,
    QLineEdit, QSizePolicy, QSlider, QSpinBox,
    QTabWidget, QToolButton, QVBoxLayout, QWidget)

class Ui_Settings_Dialog(object):
    def setupUi(self, Settings_Dialog):
        if not Settings_Dialog.objectName():
            Settings_Dialog.setObjectName(u"Settings_Dialog")
        Settings_Dialog.resize(648, 726)
        font = QFont()
        font.setPointSize(11)
        Settings_Dialog.setFont(font)
        self.verticalLayout = QVBoxLayout(Settings_Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.parametersTab = QTabWidget(Settings_Dialog)
        self.parametersTab.setObjectName(u"parametersTab")
        self.sharedParamTab = QWidget()
        self.sharedParamTab.setObjectName(u"sharedParamTab")
        self.sharedParamTab.setAutoFillBackground(True)
        self.gridLayout_2 = QGridLayout(self.sharedParamTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.sharedParamTab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.paramPresets_comboBox = QComboBox(self.sharedParamTab)
        self.paramPresets_comboBox.setObjectName(u"paramPresets_comboBox")
        self.paramPresets_comboBox.setInsertPolicy(QComboBox.InsertAlphabetically)

        self.gridLayout_2.addWidget(self.paramPresets_comboBox, 0, 1, 1, 1)

        self.line_2 = QFrame(self.sharedParamTab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 1, 1, 1, 1)

        self.label_12 = QLabel(self.sharedParamTab)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 1)

        self.ctxsizeSlider = QSlider(self.sharedParamTab)
        self.ctxsizeSlider.setObjectName(u"ctxsizeSlider")
        self.ctxsizeSlider.setMinimum(2048)
        self.ctxsizeSlider.setMaximum(32768)
        self.ctxsizeSlider.setSingleStep(2048)
        self.ctxsizeSlider.setPageStep(2048)
        self.ctxsizeSlider.setValue(4096)
        self.ctxsizeSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.ctxsizeSlider, 2, 1, 1, 1)

        self.ctxsizeSpin = QSpinBox(self.sharedParamTab)
        self.ctxsizeSpin.setObjectName(u"ctxsizeSpin")
        self.ctxsizeSpin.setMinimum(2048)
        self.ctxsizeSpin.setMaximum(32768)
        self.ctxsizeSpin.setSingleStep(2048)
        self.ctxsizeSpin.setStepType(QAbstractSpinBox.DefaultStepType)
        self.ctxsizeSpin.setValue(4096)

        self.gridLayout_2.addWidget(self.ctxsizeSpin, 2, 2, 1, 1)

        self.label_15 = QLabel(self.sharedParamTab)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 3, 0, 1, 1)

        self.temperatureSlider = QSlider(self.sharedParamTab)
        self.temperatureSlider.setObjectName(u"temperatureSlider")
        self.temperatureSlider.setMaximum(199)
        self.temperatureSlider.setValue(70)
        self.temperatureSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.temperatureSlider, 3, 1, 1, 1)

        self.temperatureSpin = QDoubleSpinBox(self.sharedParamTab)
        self.temperatureSpin.setObjectName(u"temperatureSpin")
        self.temperatureSpin.setMaximum(5.000000000000000)
        self.temperatureSpin.setSingleStep(0.010000000000000)
        self.temperatureSpin.setValue(0.700000000000000)

        self.gridLayout_2.addWidget(self.temperatureSpin, 3, 2, 1, 1)

        self.label_5 = QLabel(self.sharedParamTab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)

        self.top_kSlider = QSlider(self.sharedParamTab)
        self.top_kSlider.setObjectName(u"top_kSlider")
        self.top_kSlider.setMaximum(200)
        self.top_kSlider.setValue(20)
        self.top_kSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.top_kSlider, 4, 1, 1, 1)

        self.top_kSpin = QSpinBox(self.sharedParamTab)
        self.top_kSpin.setObjectName(u"top_kSpin")
        self.top_kSpin.setMaximum(200)
        self.top_kSpin.setValue(20)

        self.gridLayout_2.addWidget(self.top_kSpin, 4, 2, 1, 1)

        self.label_17 = QLabel(self.sharedParamTab)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 5, 0, 1, 1)

        self.top_pSlider = QSlider(self.sharedParamTab)
        self.top_pSlider.setObjectName(u"top_pSlider")
        self.top_pSlider.setMaximum(100)
        self.top_pSlider.setValue(90)
        self.top_pSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.top_pSlider, 5, 1, 1, 1)

        self.top_pSpin = QDoubleSpinBox(self.sharedParamTab)
        self.top_pSpin.setObjectName(u"top_pSpin")
        self.top_pSpin.setMaximum(1.000000000000000)
        self.top_pSpin.setSingleStep(0.010000000000000)
        self.top_pSpin.setValue(0.900000000000000)

        self.gridLayout_2.addWidget(self.top_pSpin, 5, 2, 1, 1)

        self.label_11 = QLabel(self.sharedParamTab)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 6, 0, 1, 1)

        self.max_new_tokensSlider = QSlider(self.sharedParamTab)
        self.max_new_tokensSlider.setObjectName(u"max_new_tokensSlider")
        self.max_new_tokensSlider.setMinimum(32)
        self.max_new_tokensSlider.setMaximum(1024)
        self.max_new_tokensSlider.setPageStep(32)
        self.max_new_tokensSlider.setValue(256)
        self.max_new_tokensSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.max_new_tokensSlider, 6, 1, 1, 1)

        self.max_new_tokensSpin = QSpinBox(self.sharedParamTab)
        self.max_new_tokensSpin.setObjectName(u"max_new_tokensSpin")
        self.max_new_tokensSpin.setMinimum(32)
        self.max_new_tokensSpin.setMaximum(2048)
        self.max_new_tokensSpin.setSingleStep(64)
        self.max_new_tokensSpin.setValue(512)

        self.gridLayout_2.addWidget(self.max_new_tokensSpin, 6, 2, 1, 1)

        self.label = QLabel(self.sharedParamTab)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 7, 0, 1, 1)

        self.repetition_penaltySlider = QSlider(self.sharedParamTab)
        self.repetition_penaltySlider.setObjectName(u"repetition_penaltySlider")
        self.repetition_penaltySlider.setMinimum(100)
        self.repetition_penaltySlider.setMaximum(180)
        self.repetition_penaltySlider.setValue(150)
        self.repetition_penaltySlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.repetition_penaltySlider, 7, 1, 1, 1)

        self.repetition_penaltySpin = QDoubleSpinBox(self.sharedParamTab)
        self.repetition_penaltySpin.setObjectName(u"repetition_penaltySpin")
        self.repetition_penaltySpin.setMinimum(1.000000000000000)
        self.repetition_penaltySpin.setMaximum(1.800000000000000)
        self.repetition_penaltySpin.setSingleStep(0.010000000000000)
        self.repetition_penaltySpin.setValue(1.150000000000000)

        self.gridLayout_2.addWidget(self.repetition_penaltySpin, 7, 2, 1, 1)

        self.label_8 = QLabel(self.sharedParamTab)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 8, 0, 1, 1)

        self.typical_pSlider = QSlider(self.sharedParamTab)
        self.typical_pSlider.setObjectName(u"typical_pSlider")
        self.typical_pSlider.setMaximum(100)
        self.typical_pSlider.setValue(25)
        self.typical_pSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.typical_pSlider, 8, 1, 1, 1)

        self.typical_pSpin = QDoubleSpinBox(self.sharedParamTab)
        self.typical_pSpin.setObjectName(u"typical_pSpin")
        self.typical_pSpin.setMaximum(1.000000000000000)
        self.typical_pSpin.setSingleStep(0.010000000000000)
        self.typical_pSpin.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.typical_pSpin, 8, 2, 1, 1)

        self.label_29 = QLabel(self.sharedParamTab)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_2.addWidget(self.label_29, 9, 0, 1, 1)

        self.seedSpin = QSpinBox(self.sharedParamTab)
        self.seedSpin.setObjectName(u"seedSpin")
        self.seedSpin.setMinimum(-1)
        self.seedSpin.setMaximum(10000000)
        self.seedSpin.setValue(-1)

        self.gridLayout_2.addWidget(self.seedSpin, 9, 2, 1, 1)

        self.parametersTab.addTab(self.sharedParamTab, "")
        self.llamacppParamTab = QWidget()
        self.llamacppParamTab.setObjectName(u"llamacppParamTab")
        self.llamacppParamTab.setAutoFillBackground(True)
        self.gridLayout_3 = QGridLayout(self.llamacppParamTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.line = QFrame(self.llamacppParamTab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 10, 2, 1, 1)

        self.label_16 = QLabel(self.llamacppParamTab)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)

        self.gpuAccelCheck = QCheckBox(self.llamacppParamTab)
        self.gpuAccelCheck.setObjectName(u"gpuAccelCheck")
        self.gpuAccelCheck.setChecked(True)

        self.gridLayout_3.addWidget(self.gpuAccelCheck, 9, 0, 1, 3)

        self.label_3 = QLabel(self.llamacppParamTab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 15, 0, 1, 1)

        self.cppThreads = QSpinBox(self.llamacppParamTab)
        self.cppThreads.setObjectName(u"cppThreads")
        self.cppThreads.setMinimum(1)
        self.cppThreads.setMaximum(128)
        self.cppThreads.setValue(6)

        self.gridLayout_3.addWidget(self.cppThreads, 1, 6, 1, 1)

        self.freqPenaltySlider = QSlider(self.llamacppParamTab)
        self.freqPenaltySlider.setObjectName(u"freqPenaltySlider")
        self.freqPenaltySlider.setMinimum(0)
        self.freqPenaltySlider.setMaximum(100)
        self.freqPenaltySlider.setValue(0)
        self.freqPenaltySlider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.freqPenaltySlider, 11, 2, 1, 2)

        self.cppVerboseCheck = QCheckBox(self.llamacppParamTab)
        self.cppVerboseCheck.setObjectName(u"cppVerboseCheck")

        self.gridLayout_3.addWidget(self.cppVerboseCheck, 21, 2, 1, 2)

        self.label_14 = QLabel(self.llamacppParamTab)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 14, 0, 1, 1)

        self.gpuLayersSpin = QSpinBox(self.llamacppParamTab)
        self.gpuLayersSpin.setObjectName(u"gpuLayersSpin")
        self.gpuLayersSpin.setMinimum(1)
        self.gpuLayersSpin.setMaximum(80)
        self.gpuLayersSpin.setValue(18)

        self.gridLayout_3.addWidget(self.gpuLayersSpin, 5, 6, 1, 1)

        self.label_6 = QLabel(self.llamacppParamTab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 4, 0, 1, 1)

        self.presencePenaltySpin = QDoubleSpinBox(self.llamacppParamTab)
        self.presencePenaltySpin.setObjectName(u"presencePenaltySpin")
        self.presencePenaltySpin.setMaximum(1.000000000000000)
        self.presencePenaltySpin.setSingleStep(0.010000000000000)

        self.gridLayout_3.addWidget(self.presencePenaltySpin, 12, 5, 1, 2)

        self.label_7 = QLabel(self.llamacppParamTab)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 12, 0, 1, 1)

        self.horizontalSlider = QSlider(self.llamacppParamTab)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximum(128)
        self.horizontalSlider.setValue(6)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.horizontalSlider, 1, 2, 1, 1)

        self.freqPenaltySpin = QDoubleSpinBox(self.llamacppParamTab)
        self.freqPenaltySpin.setObjectName(u"freqPenaltySpin")
        self.freqPenaltySpin.setMaximum(1.000000000000000)
        self.freqPenaltySpin.setSingleStep(0.010000000000000)

        self.gridLayout_3.addWidget(self.freqPenaltySpin, 11, 5, 1, 2)

        self.cppBatchSizeSpin = QSpinBox(self.llamacppParamTab)
        self.cppBatchSizeSpin.setObjectName(u"cppBatchSizeSpin")
        self.cppBatchSizeSpin.setMinimum(8)
        self.cppBatchSizeSpin.setMaximum(1024)
        self.cppBatchSizeSpin.setSingleStep(8)
        self.cppBatchSizeSpin.setValue(512)

        self.gridLayout_3.addWidget(self.cppBatchSizeSpin, 4, 6, 1, 1)

        self.label_18 = QLabel(self.llamacppParamTab)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 18, 0, 1, 1)

        self.cppBatchSizeSlider = QSlider(self.llamacppParamTab)
        self.cppBatchSizeSlider.setObjectName(u"cppBatchSizeSlider")
        self.cppBatchSizeSlider.setMinimum(8)
        self.cppBatchSizeSlider.setMaximum(1024)
        self.cppBatchSizeSlider.setSingleStep(8)
        self.cppBatchSizeSlider.setPageStep(8)
        self.cppBatchSizeSlider.setValue(512)
        self.cppBatchSizeSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.cppBatchSizeSlider, 4, 2, 1, 1)

        self.cpp_tfszSpin = QDoubleSpinBox(self.llamacppParamTab)
        self.cpp_tfszSpin.setObjectName(u"cpp_tfszSpin")
        self.cpp_tfszSpin.setMinimum(1.000000000000000)
        self.cpp_tfszSpin.setMaximum(5.000000000000000)
        self.cpp_tfszSpin.setSingleStep(0.010000000000000)

        self.gridLayout_3.addWidget(self.cpp_tfszSpin, 13, 5, 1, 2)

        self.cppMmapCheck = QCheckBox(self.llamacppParamTab)
        self.cppMmapCheck.setObjectName(u"cppMmapCheck")
        self.cppMmapCheck.setChecked(True)

        self.gridLayout_3.addWidget(self.cppMmapCheck, 20, 0, 1, 1)

        self.label_10 = QLabel(self.llamacppParamTab)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 5, 0, 1, 1)

        self.label_4 = QLabel(self.llamacppParamTab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 11, 0, 1, 1)

        self.cppLoraLineEdit = QLineEdit(self.llamacppParamTab)
        self.cppLoraLineEdit.setObjectName(u"cppLoraLineEdit")

        self.gridLayout_3.addWidget(self.cppLoraLineEdit, 18, 2, 1, 2)

        self.label_9 = QLabel(self.llamacppParamTab)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 16, 0, 1, 1)

        self.cppMirostatTau = QSpinBox(self.llamacppParamTab)
        self.cppMirostatTau.setObjectName(u"cppMirostatTau")
        self.cppMirostatTau.setMinimum(2)
        self.cppMirostatTau.setMaximum(8)
        self.cppMirostatTau.setValue(5)

        self.gridLayout_3.addWidget(self.cppMirostatTau, 15, 5, 1, 2)

        self.cppMirostatMode = QSpinBox(self.llamacppParamTab)
        self.cppMirostatMode.setObjectName(u"cppMirostatMode")
        self.cppMirostatMode.setMaximum(2)

        self.gridLayout_3.addWidget(self.cppMirostatMode, 14, 5, 1, 2)

        self.cppMlockCheck = QCheckBox(self.llamacppParamTab)
        self.cppMlockCheck.setObjectName(u"cppMlockCheck")

        self.gridLayout_3.addWidget(self.cppMlockCheck, 20, 2, 1, 2)

        self.cppCacheCheck = QCheckBox(self.llamacppParamTab)
        self.cppCacheCheck.setObjectName(u"cppCacheCheck")
        self.cppCacheCheck.setChecked(True)

        self.gridLayout_3.addWidget(self.cppCacheCheck, 21, 0, 1, 1)

        self.label_31 = QLabel(self.llamacppParamTab)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_3.addWidget(self.label_31, 13, 0, 1, 1)

        self.gpuLayersSlider = QSlider(self.llamacppParamTab)
        self.gpuLayersSlider.setObjectName(u"gpuLayersSlider")
        self.gpuLayersSlider.setMinimum(1)
        self.gpuLayersSlider.setMaximum(80)
        self.gpuLayersSlider.setValue(18)
        self.gpuLayersSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.gpuLayersSlider, 5, 2, 1, 1)

        self.cpp_tfszSlider = QSlider(self.llamacppParamTab)
        self.cpp_tfszSlider.setObjectName(u"cpp_tfszSlider")
        self.cpp_tfszSlider.setMinimum(100)
        self.cpp_tfszSlider.setMaximum(500)
        self.cpp_tfszSlider.setValue(100)
        self.cpp_tfszSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.cpp_tfszSlider, 13, 2, 1, 2)

        self.cppLoraSelect = QToolButton(self.llamacppParamTab)
        self.cppLoraSelect.setObjectName(u"cppLoraSelect")

        self.gridLayout_3.addWidget(self.cppLoraSelect, 18, 5, 1, 2)

        self.presencePenaltySlider = QSlider(self.llamacppParamTab)
        self.presencePenaltySlider.setObjectName(u"presencePenaltySlider")
        self.presencePenaltySlider.setMaximum(100)
        self.presencePenaltySlider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.presencePenaltySlider, 12, 2, 1, 2)

        self.cppMirostatEta = QDoubleSpinBox(self.llamacppParamTab)
        self.cppMirostatEta.setObjectName(u"cppMirostatEta")
        self.cppMirostatEta.setMaximum(1.000000000000000)
        self.cppMirostatEta.setSingleStep(0.010000000000000)
        self.cppMirostatEta.setValue(0.100000000000000)

        self.gridLayout_3.addWidget(self.cppMirostatEta, 16, 5, 1, 2)

        self.line_3 = QFrame(self.llamacppParamTab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_3, 17, 2, 1, 1)

        self.parametersTab.addTab(self.llamacppParamTab, "")
        self.exllamaParamTab = QWidget()
        self.exllamaParamTab.setObjectName(u"exllamaParamTab")
        self.exllamaParamTab.setAutoFillBackground(True)
        self.gridLayout = QGridLayout(self.exllamaParamTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.exllamaLoraCheck = QCheckBox(self.exllamaParamTab)
        self.exllamaLoraCheck.setObjectName(u"exllamaLoraCheck")
        self.exllamaLoraCheck.setChecked(False)

        self.gridLayout.addWidget(self.exllamaLoraCheck, 6, 0, 1, 1)

        self.label_19 = QLabel(self.exllamaParamTab)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 0, 0, 1, 1)

        self.beamLengthSlider = QSlider(self.exllamaParamTab)
        self.beamLengthSlider.setObjectName(u"beamLengthSlider")
        self.beamLengthSlider.setMinimum(1)
        self.beamLengthSlider.setMaximum(10)
        self.beamLengthSlider.setPageStep(1)
        self.beamLengthSlider.setValue(1)
        self.beamLengthSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.beamLengthSlider, 3, 1, 1, 1)

        self.beamLengthSpin = QSpinBox(self.exllamaParamTab)
        self.beamLengthSpin.setObjectName(u"beamLengthSpin")
        self.beamLengthSpin.setMinimum(1)
        self.beamLengthSpin.setMaximum(10)

        self.gridLayout.addWidget(self.beamLengthSpin, 3, 2, 1, 1)

        self.token_repetition_penalty_decaySpin = QSpinBox(self.exllamaParamTab)
        self.token_repetition_penalty_decaySpin.setObjectName(u"token_repetition_penalty_decaySpin")
        self.token_repetition_penalty_decaySpin.setMaximum(512)
        self.token_repetition_penalty_decaySpin.setSingleStep(16)
        self.token_repetition_penalty_decaySpin.setValue(256)

        self.gridLayout.addWidget(self.token_repetition_penalty_decaySpin, 1, 2, 1, 1)

        self.numbeamsSpin = QSpinBox(self.exllamaParamTab)
        self.numbeamsSpin.setObjectName(u"numbeamsSpin")
        self.numbeamsSpin.setMinimum(1)
        self.numbeamsSpin.setMaximum(10)

        self.gridLayout.addWidget(self.numbeamsSpin, 2, 2, 1, 1)

        self.minPSpin = QSpinBox(self.exllamaParamTab)
        self.minPSpin.setObjectName(u"minPSpin")
        self.minPSpin.setMaximum(100)

        self.gridLayout.addWidget(self.minPSpin, 0, 2, 1, 1)

        self.exllamaGpuSplitCheck = QCheckBox(self.exllamaParamTab)
        self.exllamaGpuSplitCheck.setObjectName(u"exllamaGpuSplitCheck")

        self.gridLayout.addWidget(self.exllamaGpuSplitCheck, 5, 0, 1, 1)

        self.label25 = QLabel(self.exllamaParamTab)
        self.label25.setObjectName(u"label25")

        self.gridLayout.addWidget(self.label25, 1, 0, 1, 1)

        self.label_22 = QLabel(self.exllamaParamTab)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 2, 0, 1, 1)

        self.exllamaLora = QLineEdit(self.exllamaParamTab)
        self.exllamaLora.setObjectName(u"exllamaLora")

        self.gridLayout.addWidget(self.exllamaLora, 6, 1, 1, 1)

        self.numbeamsSlider = QSlider(self.exllamaParamTab)
        self.numbeamsSlider.setObjectName(u"numbeamsSlider")
        self.numbeamsSlider.setMinimum(1)
        self.numbeamsSlider.setMaximum(10)
        self.numbeamsSlider.setPageStep(1)
        self.numbeamsSlider.setValue(1)
        self.numbeamsSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.numbeamsSlider, 2, 1, 1, 1)

        self.compressPosEmbedSpin = QSpinBox(self.exllamaParamTab)
        self.compressPosEmbedSpin.setObjectName(u"compressPosEmbedSpin")
        self.compressPosEmbedSpin.setMinimum(2)
        self.compressPosEmbedSpin.setMaximum(8)
        self.compressPosEmbedSpin.setSingleStep(2)
        self.compressPosEmbedSpin.setValue(4)

        self.gridLayout.addWidget(self.compressPosEmbedSpin, 7, 1, 1, 1)

        self.label_26 = QLabel(self.exllamaParamTab)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout.addWidget(self.label_26, 3, 0, 1, 1)

        self.token_repetition_penalty_decaySlider = QSlider(self.exllamaParamTab)
        self.token_repetition_penalty_decaySlider.setObjectName(u"token_repetition_penalty_decaySlider")
        self.token_repetition_penalty_decaySlider.setMaximum(512)
        self.token_repetition_penalty_decaySlider.setSingleStep(16)
        self.token_repetition_penalty_decaySlider.setPageStep(16)
        self.token_repetition_penalty_decaySlider.setValue(256)
        self.token_repetition_penalty_decaySlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.token_repetition_penalty_decaySlider, 1, 1, 1, 1)

        self.compressPosEmbedCheck = QCheckBox(self.exllamaParamTab)
        self.compressPosEmbedCheck.setObjectName(u"compressPosEmbedCheck")
        self.compressPosEmbedCheck.setCheckable(True)
        self.compressPosEmbedCheck.setChecked(False)

        self.gridLayout.addWidget(self.compressPosEmbedCheck, 7, 0, 1, 1)

        self.minPSlider = QSlider(self.exllamaParamTab)
        self.minPSlider.setObjectName(u"minPSlider")
        self.minPSlider.setMaximum(100)
        self.minPSlider.setValue(0)
        self.minPSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.minPSlider, 0, 1, 1, 1)

        self.exllamaGpuSplitLine = QLineEdit(self.exllamaParamTab)
        self.exllamaGpuSplitLine.setObjectName(u"exllamaGpuSplitLine")

        self.gridLayout.addWidget(self.exllamaGpuSplitLine, 5, 1, 1, 1)

        self.exllamaLoraSelect = QToolButton(self.exllamaParamTab)
        self.exllamaLoraSelect.setObjectName(u"exllamaLoraSelect")

        self.gridLayout.addWidget(self.exllamaLoraSelect, 6, 2, 1, 1)

        self.line_4 = QFrame(self.exllamaParamTab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 4, 1, 1, 1)

        self.parametersTab.addTab(self.exllamaParamTab, "")

        self.verticalLayout.addWidget(self.parametersTab)


        self.retranslateUi(Settings_Dialog)
        self.ctxsizeSlider.valueChanged.connect(self.ctxsizeSpin.setValue)
        self.ctxsizeSpin.valueChanged.connect(self.ctxsizeSlider.setValue)
        self.top_kSlider.valueChanged.connect(self.top_kSpin.setValue)
        self.top_kSpin.valueChanged.connect(self.top_kSlider.setValue)
        self.max_new_tokensSpin.valueChanged.connect(self.max_new_tokensSlider.setValue)
        self.max_new_tokensSlider.valueChanged.connect(self.max_new_tokensSpin.setValue)
        self.token_repetition_penalty_decaySlider.valueChanged.connect(self.token_repetition_penalty_decaySpin.setValue)
        self.token_repetition_penalty_decaySpin.valueChanged.connect(self.token_repetition_penalty_decaySlider.setValue)
        self.minPSlider.valueChanged.connect(self.minPSpin.setValue)
        self.minPSpin.valueChanged.connect(self.minPSlider.setValue)
        self.numbeamsSpin.valueChanged.connect(self.numbeamsSlider.setValue)
        self.numbeamsSlider.valueChanged.connect(self.numbeamsSpin.setValue)
        self.beamLengthSlider.valueChanged.connect(self.beamLengthSpin.setValue)
        self.beamLengthSpin.valueChanged.connect(self.beamLengthSlider.setValue)
        self.horizontalSlider.valueChanged.connect(self.cppThreads.setValue)
        self.cppThreads.valueChanged.connect(self.horizontalSlider.setValue)
        self.cppBatchSizeSlider.valueChanged.connect(self.cppBatchSizeSpin.setValue)
        self.cppBatchSizeSpin.valueChanged.connect(self.cppBatchSizeSlider.setValue)
        self.gpuLayersSlider.valueChanged.connect(self.gpuLayersSpin.setValue)
        self.gpuLayersSpin.valueChanged.connect(self.gpuLayersSlider.setValue)

        self.parametersTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Settings_Dialog)
    # setupUi

    def retranslateUi(self, Settings_Dialog):
        Settings_Dialog.setWindowTitle(QCoreApplication.translate("Settings_Dialog", u"Parameters", None))
#if QT_CONFIG(tooltip)
        Settings_Dialog.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.parametersTab.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Settings_Dialog", u"Preset:", None))
#if QT_CONFIG(tooltip)
        self.paramPresets_comboBox.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Parameter preset", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("Settings_Dialog", u"Context size:", None))
#if QT_CONFIG(tooltip)
        self.ctxsizeSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Maximum length of the prompt and output combined (in tokens)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ctxsizeSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Maximum length of the prompt and output combined (in tokens)", None))
#endif // QT_CONFIG(tooltip)
        self.label_15.setText(QCoreApplication.translate("Settings_Dialog", u"Temperature:", None))
#if QT_CONFIG(tooltip)
        self.temperatureSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Degree of randomness or wildness - how much AI is allowed to sway from the most probable prediction", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.temperatureSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Degree of randomness or wildness - how much AI is allowed to sway from the most probable prediction", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Settings_Dialog", u"Top K:", None))
#if QT_CONFIG(tooltip)
        self.top_kSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Consider only this many most likely tokens - ignore all others", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.top_kSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Consider only this many most likely tokens - ignore all others", None))
#endif // QT_CONFIG(tooltip)
        self.label_17.setText(QCoreApplication.translate("Settings_Dialog", u"Top P:", None))
#if QT_CONFIG(tooltip)
        self.top_pSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Consider only the top tokens whose likelihood together adds up to this number (0-1.0) - ignore all others", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.top_pSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Consider only the top tokens whose likelihood together adds up to this number (0-1.0) - ignore all others", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("Settings_Dialog", u"Max new tokens:", None))
#if QT_CONFIG(tooltip)
        self.max_new_tokensSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Maximum number of tokens the model will output after outputting the prompt - number of tokens to predict", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.max_new_tokensSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Maximum number of tokens the model will output after outputting the prompt - number of tokens to predict", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Settings_Dialog", u"Repetition penalty:", None))
        self.label_8.setText(QCoreApplication.translate("Settings_Dialog", u"Typical P:", None))
#if QT_CONFIG(tooltip)
        self.typical_pSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Locally typical sampling, parameter p (1.0 = disabled)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.typical_pSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Locally typical sampling, parameter p (1.0 = disabled)", None))
#endif // QT_CONFIG(tooltip)
        self.label_29.setText(QCoreApplication.translate("Settings_Dialog", u"Seed:", None))
#if QT_CONFIG(tooltip)
        self.seedSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Seed to use (-1 for random)", None))
#endif // QT_CONFIG(tooltip)
        self.parametersTab.setTabText(self.parametersTab.indexOf(self.sharedParamTab), QCoreApplication.translate("Settings_Dialog", u"Shared", None))
        self.label_16.setText(QCoreApplication.translate("Settings_Dialog", u"Threads:", None))
#if QT_CONFIG(tooltip)
        self.gpuAccelCheck.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Offload model layers to GPU. llama.cpp must be compiled with GPU acceleration", None))
#endif // QT_CONFIG(tooltip)
        self.gpuAccelCheck.setText(QCoreApplication.translate("Settings_Dialog", u"Use GPU acceleration", None))
        self.label_3.setText(QCoreApplication.translate("Settings_Dialog", u"Mirostat Tau:", None))
#if QT_CONFIG(tooltip)
        self.cppThreads.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Number of threads to use during computation", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.freqPenaltySlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Repeat alpha frequency penalty (0.0 = disabled)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cppVerboseCheck.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Print timings and cache info after prompts", None))
#endif // QT_CONFIG(tooltip)
        self.cppVerboseCheck.setText(QCoreApplication.translate("Settings_Dialog", u"Verbose", None))
        self.label_14.setText(QCoreApplication.translate("Settings_Dialog", u"Mirostat mode:", None))
#if QT_CONFIG(tooltip)
        self.gpuLayersSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Number of GPU layers to use", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("Settings_Dialog", u"Batch size:", None))
#if QT_CONFIG(tooltip)
        self.presencePenaltySpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Repeat alpha presence penalty (0.0 = disabled)", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("Settings_Dialog", u"Presence penalty:", None))
#if QT_CONFIG(tooltip)
        self.freqPenaltySpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Repeat alpha frequency penalty (0.0 = disabled)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cppBatchSizeSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Batch size to use", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("Settings_Dialog", u"LoRA:", None))
#if QT_CONFIG(tooltip)
        self.cppBatchSizeSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Batch size to use", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cpp_tfszSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Tail free sampling, parameter z (1.0 = disabled)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cppMmapCheck.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Memory-map model. Disabled = slower load but may reduce pageouts if not using mlock", None))
#endif // QT_CONFIG(tooltip)
        self.cppMmapCheck.setText(QCoreApplication.translate("Settings_Dialog", u"Use MMAP", None))
        self.label_10.setText(QCoreApplication.translate("Settings_Dialog", u"GPU Layers:", None))
        self.label_4.setText(QCoreApplication.translate("Settings_Dialog", u"Frequency penalty:", None))
#if QT_CONFIG(tooltip)
        self.cppLoraLineEdit.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Path to a LoRA .bin file", None))
#endif // QT_CONFIG(tooltip)
        self.cppLoraLineEdit.setPlaceholderText(QCoreApplication.translate("Settings_Dialog", u"ggml-adapter-model.bin", None))
        self.label_9.setText(QCoreApplication.translate("Settings_Dialog", u"Mirostat Eta:", None))
#if QT_CONFIG(tooltip)
        self.cppMirostatMode.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Use Mirostat sampling. Top K, Nucleus, Tail Free and Locally Typical samplers are ignored if used. (0 = disabled, 1 = Mirostat, 2 = Mirostat 2.0)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cppMlockCheck.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Force system to keep model in RAM rather than swapping or compressing", None))
#endif // QT_CONFIG(tooltip)
        self.cppMlockCheck.setText(QCoreApplication.translate("Settings_Dialog", u"Use MLOCK", None))
#if QT_CONFIG(tooltip)
        self.cppCacheCheck.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Saves context cache to RAM for faster prompt processing", None))
#endif // QT_CONFIG(tooltip)
        self.cppCacheCheck.setText(QCoreApplication.translate("Settings_Dialog", u"Use cache", None))
        self.label_31.setText(QCoreApplication.translate("Settings_Dialog", u"Tail Free Sampling:", None))
#if QT_CONFIG(tooltip)
        self.gpuLayersSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Number of GPU layers to use", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cpp_tfszSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Tail free sampling, parameter z (1.0 = disabled)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cppLoraSelect.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Select LoRA file", None))
#endif // QT_CONFIG(tooltip)
        self.cppLoraSelect.setText(QCoreApplication.translate("Settings_Dialog", u"...", None))
#if QT_CONFIG(tooltip)
        self.presencePenaltySlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Repeat alpha presence penalty (0.0 = disabled)", None))
#endif // QT_CONFIG(tooltip)
        self.parametersTab.setTabText(self.parametersTab.indexOf(self.llamacppParamTab), QCoreApplication.translate("Settings_Dialog", u"llama.cpp", None))
        self.exllamaLoraCheck.setText(QCoreApplication.translate("Settings_Dialog", u"LoRA:", None))
        self.label_19.setText(QCoreApplication.translate("Settings_Dialog", u"Min P:", None))
#if QT_CONFIG(tooltip)
        self.beamLengthSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Beam length value", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.beamLengthSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Beam length value", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.token_repetition_penalty_decaySpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Token repetition penalty sustain", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.numbeamsSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Number of beams. Slower, more VRAm", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.minPSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Minimum P value", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.exllamaGpuSplitCheck.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Split memory across multiple GPUs", None))
#endif // QT_CONFIG(tooltip)
        self.exllamaGpuSplitCheck.setText(QCoreApplication.translate("Settings_Dialog", u"Multi-GPU split:", None))
        self.label25.setText(QCoreApplication.translate("Settings_Dialog", u"Token repetition penalty sustain:", None))
        self.label_22.setText(QCoreApplication.translate("Settings_Dialog", u"Num beams:", None))
#if QT_CONFIG(tooltip)
        self.exllamaLora.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Path to LoRA folder, containing 'adapter_config.json' and 'adapter_model.bin'", None))
#endif // QT_CONFIG(tooltip)
        self.exllamaLora.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.numbeamsSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Number of beams. Slower, more VRAM", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.compressPosEmbedSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"For longer context models. For 4k context set to 2, for 8k context set to 4, etc.", None))
#endif // QT_CONFIG(tooltip)
        self.label_26.setText(QCoreApplication.translate("Settings_Dialog", u"Beam length:", None))
#if QT_CONFIG(tooltip)
        self.token_repetition_penalty_decaySlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Token repetition penalty sustain", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.compressPosEmbedCheck.setToolTip(QCoreApplication.translate("Settings_Dialog", u"For longer context models. For 4k context set to 2, for 8k context set to 4, etc.", None))
#endif // QT_CONFIG(tooltip)
        self.compressPosEmbedCheck.setText(QCoreApplication.translate("Settings_Dialog", u"Compress pos embeddings:", None))
#if QT_CONFIG(tooltip)
        self.minPSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"If not set to 1, select only tokens that are at least this much more likely to appear than random tokens, given the prior text.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.exllamaGpuSplitLine.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Comma-separated list of VRAM (in GB) to use per GPU device for model layers, e.g: - 8,6,4", None))
#endif // QT_CONFIG(tooltip)
        self.exllamaGpuSplitLine.setText("")
        self.exllamaGpuSplitLine.setPlaceholderText(QCoreApplication.translate("Settings_Dialog", u"8,6", None))
#if QT_CONFIG(tooltip)
        self.exllamaLoraSelect.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Select LoRA folder", None))
#endif // QT_CONFIG(tooltip)
        self.exllamaLoraSelect.setText(QCoreApplication.translate("Settings_Dialog", u"...", None))
        self.parametersTab.setTabText(self.parametersTab.indexOf(self.exllamaParamTab), QCoreApplication.translate("Settings_Dialog", u"Exllama", None))
    # retranslateUi

