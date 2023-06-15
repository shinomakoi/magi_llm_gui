# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_settings.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSlider,
    QSpinBox, QTabWidget, QVBoxLayout, QWidget)

class Ui_Settings_Dialog(object):
    def setupUi(self, Settings_Dialog):
        if not Settings_Dialog.objectName():
            Settings_Dialog.setObjectName(u"Settings_Dialog")
        Settings_Dialog.resize(632, 690)
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
        self.gridLayout_3 = QGridLayout(self.sharedParamTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_2 = QGroupBox(self.sharedParamTab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.top_pSlider = QSlider(self.groupBox_2)
        self.top_pSlider.setObjectName(u"top_pSlider")
        self.top_pSlider.setMaximum(100)
        self.top_pSlider.setValue(65)
        self.top_pSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.top_pSlider, 5, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.repetition_penaltySpin = QDoubleSpinBox(self.groupBox_2)
        self.repetition_penaltySpin.setObjectName(u"repetition_penaltySpin")
        self.repetition_penaltySpin.setMinimum(1.000000000000000)
        self.repetition_penaltySpin.setMaximum(1.500000000000000)
        self.repetition_penaltySpin.setSingleStep(0.010000000000000)
        self.repetition_penaltySpin.setValue(1.150000000000000)

        self.gridLayout_2.addWidget(self.repetition_penaltySpin, 9, 3, 1, 1)

        self.temperatureSpin = QDoubleSpinBox(self.groupBox_2)
        self.temperatureSpin.setObjectName(u"temperatureSpin")
        self.temperatureSpin.setMaximum(5.000000000000000)
        self.temperatureSpin.setSingleStep(0.010000000000000)
        self.temperatureSpin.setValue(0.950000000000000)

        self.gridLayout_2.addWidget(self.temperatureSpin, 2, 3, 1, 1)

        self.max_new_tokensSlider = QSlider(self.groupBox_2)
        self.max_new_tokensSlider.setObjectName(u"max_new_tokensSlider")
        self.max_new_tokensSlider.setMinimum(32)
        self.max_new_tokensSlider.setMaximum(2048)
        self.max_new_tokensSlider.setPageStep(32)
        self.max_new_tokensSlider.setValue(256)
        self.max_new_tokensSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.max_new_tokensSlider, 7, 1, 1, 1)

        self.temperatureSlider = QSlider(self.groupBox_2)
        self.temperatureSlider.setObjectName(u"temperatureSlider")
        self.temperatureSlider.setMaximum(199)
        self.temperatureSlider.setValue(95)
        self.temperatureSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.temperatureSlider, 2, 1, 1, 1)

        self.repetition_penaltySlider = QSlider(self.groupBox_2)
        self.repetition_penaltySlider.setObjectName(u"repetition_penaltySlider")
        self.repetition_penaltySlider.setMinimum(100)
        self.repetition_penaltySlider.setMaximum(150)
        self.repetition_penaltySlider.setValue(115)
        self.repetition_penaltySlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.repetition_penaltySlider, 9, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 5, 0, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 9, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 2, 0, 1, 1)

        self.top_kSlider = QSlider(self.groupBox_2)
        self.top_kSlider.setObjectName(u"top_kSlider")
        self.top_kSlider.setMaximum(200)
        self.top_kSlider.setValue(20)
        self.top_kSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.top_kSlider, 3, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 7, 0, 1, 1)

        self.top_pSpin = QDoubleSpinBox(self.groupBox_2)
        self.top_pSpin.setObjectName(u"top_pSpin")
        self.top_pSpin.setMaximum(1.000000000000000)
        self.top_pSpin.setSingleStep(0.010000000000000)
        self.top_pSpin.setValue(0.650000000000000)

        self.gridLayout_2.addWidget(self.top_pSpin, 5, 3, 1, 1)

        self.top_kSpin = QSpinBox(self.groupBox_2)
        self.top_kSpin.setObjectName(u"top_kSpin")
        self.top_kSpin.setMaximum(200)
        self.top_kSpin.setValue(20)

        self.gridLayout_2.addWidget(self.top_kSpin, 3, 3, 1, 1)

        self.max_new_tokensSpin = QSpinBox(self.groupBox_2)
        self.max_new_tokensSpin.setObjectName(u"max_new_tokensSpin")
        self.max_new_tokensSpin.setMinimum(32)
        self.max_new_tokensSpin.setMaximum(2048)
        self.max_new_tokensSpin.setSingleStep(32)
        self.max_new_tokensSpin.setValue(256)

        self.gridLayout_2.addWidget(self.max_new_tokensSpin, 7, 3, 1, 1)

        self.seedSpin = QSpinBox(self.groupBox_2)
        self.seedSpin.setObjectName(u"seedSpin")
        self.seedSpin.setMinimum(-1)
        self.seedSpin.setMaximum(10000000)
        self.seedSpin.setValue(-1)

        self.gridLayout_2.addWidget(self.seedSpin, 10, 1, 1, 1)

        self.label_29 = QLabel(self.groupBox_2)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_2.addWidget(self.label_29, 10, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.paramPresets_comboBox = QComboBox(self.groupBox_2)
        self.paramPresets_comboBox.setObjectName(u"paramPresets_comboBox")
        self.paramPresets_comboBox.setInsertPolicy(QComboBox.InsertAlphabetically)

        self.gridLayout_2.addWidget(self.paramPresets_comboBox, 0, 1, 1, 2)

        self.line_2 = QFrame(self.groupBox_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 2, 0, 1, 3)

        self.parametersTab.addTab(self.sharedParamTab, "")
        self.exllamaParamTab = QWidget()
        self.exllamaParamTab.setObjectName(u"exllamaParamTab")
        self.exllamaParamTab.setAutoFillBackground(True)
        self.verticalLayout_2 = QVBoxLayout(self.exllamaParamTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.exllamaParamTab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.beamLengthSlider = QSlider(self.groupBox)
        self.beamLengthSlider.setObjectName(u"beamLengthSlider")
        self.beamLengthSlider.setMinimum(1)
        self.beamLengthSlider.setMaximum(10)
        self.beamLengthSlider.setPageStep(1)
        self.beamLengthSlider.setValue(1)
        self.beamLengthSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.beamLengthSlider, 6, 3, 1, 1)

        self.minPSlider = QSlider(self.groupBox)
        self.minPSlider.setObjectName(u"minPSlider")
        self.minPSlider.setMaximum(100)
        self.minPSlider.setValue(0)
        self.minPSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.minPSlider, 0, 3, 1, 1)

        self.label_22 = QLabel(self.groupBox)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 5, 1, 1, 1)

        self.token_repetition_penalty_decaySpin = QSpinBox(self.groupBox)
        self.token_repetition_penalty_decaySpin.setObjectName(u"token_repetition_penalty_decaySpin")
        self.token_repetition_penalty_decaySpin.setMaximum(512)
        self.token_repetition_penalty_decaySpin.setSingleStep(16)
        self.token_repetition_penalty_decaySpin.setValue(256)

        self.gridLayout.addWidget(self.token_repetition_penalty_decaySpin, 1, 4, 1, 1)

        self.token_repetition_penalty_decaySlider = QSlider(self.groupBox)
        self.token_repetition_penalty_decaySlider.setObjectName(u"token_repetition_penalty_decaySlider")
        self.token_repetition_penalty_decaySlider.setMaximum(512)
        self.token_repetition_penalty_decaySlider.setSingleStep(16)
        self.token_repetition_penalty_decaySlider.setPageStep(16)
        self.token_repetition_penalty_decaySlider.setValue(256)
        self.token_repetition_penalty_decaySlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.token_repetition_penalty_decaySlider, 1, 3, 1, 1)

        self.beamLengthSpin = QSpinBox(self.groupBox)
        self.beamLengthSpin.setObjectName(u"beamLengthSpin")
        self.beamLengthSpin.setMinimum(1)
        self.beamLengthSpin.setMaximum(10)

        self.gridLayout.addWidget(self.beamLengthSpin, 6, 4, 1, 1)

        self.numbeamsSlider = QSlider(self.groupBox)
        self.numbeamsSlider.setObjectName(u"numbeamsSlider")
        self.numbeamsSlider.setMinimum(1)
        self.numbeamsSlider.setMaximum(10)
        self.numbeamsSlider.setPageStep(1)
        self.numbeamsSlider.setValue(1)
        self.numbeamsSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.numbeamsSlider, 5, 3, 1, 1)

        self.numbeamsSpin = QSpinBox(self.groupBox)
        self.numbeamsSpin.setObjectName(u"numbeamsSpin")
        self.numbeamsSpin.setMinimum(1)
        self.numbeamsSpin.setMaximum(10)

        self.gridLayout.addWidget(self.numbeamsSpin, 5, 4, 1, 1)

        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 0, 1, 1, 1)

        self.label25 = QLabel(self.groupBox)
        self.label25.setObjectName(u"label25")

        self.gridLayout.addWidget(self.label25, 1, 1, 1, 2)

        self.label_26 = QLabel(self.groupBox)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout.addWidget(self.label_26, 6, 1, 1, 1)

        self.minPSpin = QSpinBox(self.groupBox)
        self.minPSpin.setObjectName(u"minPSpin")
        self.minPSpin.setMaximum(100)

        self.gridLayout.addWidget(self.minPSpin, 0, 4, 1, 1)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 4, 3, 1, 1)

        self.exllamaGpuSplitCheck = QCheckBox(self.groupBox)
        self.exllamaGpuSplitCheck.setObjectName(u"exllamaGpuSplitCheck")

        self.gridLayout.addWidget(self.exllamaGpuSplitCheck, 7, 1, 1, 1)

        self.exllamaGpuSplitLine = QLineEdit(self.groupBox)
        self.exllamaGpuSplitLine.setObjectName(u"exllamaGpuSplitLine")

        self.gridLayout.addWidget(self.exllamaGpuSplitLine, 7, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.parametersTab.addTab(self.exllamaParamTab, "")
        self.llamacppParamTab = QWidget()
        self.llamacppParamTab.setObjectName(u"llamacppParamTab")
        self.llamacppParamTab.setAutoFillBackground(True)
        self.verticalLayout_4 = QVBoxLayout(self.llamacppParamTab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_5 = QGroupBox(self.llamacppParamTab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_4 = QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_16 = QLabel(self.groupBox_5)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 1)

        self.cppBatchSizeSlider = QSlider(self.groupBox_5)
        self.cppBatchSizeSlider.setObjectName(u"cppBatchSizeSlider")
        self.cppBatchSizeSlider.setMinimum(8)
        self.cppBatchSizeSlider.setMaximum(1024)
        self.cppBatchSizeSlider.setSingleStep(8)
        self.cppBatchSizeSlider.setPageStep(8)
        self.cppBatchSizeSlider.setValue(512)
        self.cppBatchSizeSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.cppBatchSizeSlider, 4, 2, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox_5)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.cppMlockCheck = QCheckBox(self.groupBox_3)
        self.cppMlockCheck.setObjectName(u"cppMlockCheck")

        self.gridLayout_5.addWidget(self.cppMlockCheck, 1, 1, 1, 1)

        self.cppMmapCheck = QCheckBox(self.groupBox_3)
        self.cppMmapCheck.setObjectName(u"cppMmapCheck")
        self.cppMmapCheck.setChecked(True)

        self.gridLayout_5.addWidget(self.cppMmapCheck, 1, 0, 1, 1)

        self.cppCacheCheck = QCheckBox(self.groupBox_3)
        self.cppCacheCheck.setObjectName(u"cppCacheCheck")
        self.cppCacheCheck.setChecked(True)

        self.gridLayout_5.addWidget(self.cppCacheCheck, 3, 0, 1, 1)

        self.cppVerboseCheck = QCheckBox(self.groupBox_3)
        self.cppVerboseCheck.setObjectName(u"cppVerboseCheck")

        self.gridLayout_5.addWidget(self.cppVerboseCheck, 3, 1, 1, 1)

        self.gpuAccelCheck = QCheckBox(self.groupBox_3)
        self.gpuAccelCheck.setObjectName(u"gpuAccelCheck")
        self.gpuAccelCheck.setChecked(True)

        self.gridLayout_5.addWidget(self.gpuAccelCheck, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_3, 12, 0, 1, 4)

        self.gpuLayersSlider = QSlider(self.groupBox_5)
        self.gpuLayersSlider.setObjectName(u"gpuLayersSlider")
        self.gpuLayersSlider.setMinimum(1)
        self.gpuLayersSlider.setMaximum(80)
        self.gpuLayersSlider.setValue(18)
        self.gpuLayersSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.gpuLayersSlider, 10, 2, 1, 1)

        self.CPP_ctxsize_Slider = QSlider(self.groupBox_5)
        self.CPP_ctxsize_Slider.setObjectName(u"CPP_ctxsize_Slider")
        self.CPP_ctxsize_Slider.setMinimum(64)
        self.CPP_ctxsize_Slider.setMaximum(4096)
        self.CPP_ctxsize_Slider.setSingleStep(32)
        self.CPP_ctxsize_Slider.setPageStep(32)
        self.CPP_ctxsize_Slider.setValue(2048)
        self.CPP_ctxsize_Slider.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.CPP_ctxsize_Slider, 2, 2, 1, 1)

        self.label_14 = QLabel(self.groupBox_5)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 5, 0, 1, 1)

        self.cppBatchSizeSpin = QSpinBox(self.groupBox_5)
        self.cppBatchSizeSpin.setObjectName(u"cppBatchSizeSpin")
        self.cppBatchSizeSpin.setMinimum(8)
        self.cppBatchSizeSpin.setMaximum(1024)
        self.cppBatchSizeSpin.setSingleStep(8)
        self.cppBatchSizeSpin.setValue(512)

        self.gridLayout_4.addWidget(self.cppBatchSizeSpin, 4, 3, 1, 1)

        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 4, 0, 1, 1)

        self.gpuLayersSpin = QSpinBox(self.groupBox_5)
        self.gpuLayersSpin.setObjectName(u"gpuLayersSpin")
        self.gpuLayersSpin.setMinimum(1)
        self.gpuLayersSpin.setMaximum(80)
        self.gpuLayersSpin.setValue(18)

        self.gridLayout_4.addWidget(self.gpuLayersSpin, 10, 3, 1, 1)

        self.cppMirastatMode = QSpinBox(self.groupBox_5)
        self.cppMirastatMode.setObjectName(u"cppMirastatMode")
        self.cppMirastatMode.setMaximum(2)

        self.gridLayout_4.addWidget(self.cppMirastatMode, 5, 3, 1, 1)

        self.CPP_ctxsize_Spin = QSpinBox(self.groupBox_5)
        self.CPP_ctxsize_Spin.setObjectName(u"CPP_ctxsize_Spin")
        self.CPP_ctxsize_Spin.setMinimum(64)
        self.CPP_ctxsize_Spin.setMaximum(4096)
        self.CPP_ctxsize_Spin.setSingleStep(32)
        self.CPP_ctxsize_Spin.setValue(2048)

        self.gridLayout_4.addWidget(self.CPP_ctxsize_Spin, 2, 3, 1, 1)

        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 10, 0, 1, 1)

        self.cppLoraLineEdit = QLineEdit(self.groupBox_5)
        self.cppLoraLineEdit.setObjectName(u"cppLoraLineEdit")

        self.gridLayout_4.addWidget(self.cppLoraLineEdit, 11, 2, 1, 1)

        self.label_12 = QLabel(self.groupBox_5)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 2, 0, 1, 2)

        self.label_18 = QLabel(self.groupBox_5)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_4.addWidget(self.label_18, 11, 0, 1, 1)

        self.cppThreads = QSpinBox(self.groupBox_5)
        self.cppThreads.setObjectName(u"cppThreads")
        self.cppThreads.setMinimum(1)
        self.cppThreads.setMaximum(64)
        self.cppThreads.setValue(4)

        self.gridLayout_4.addWidget(self.cppThreads, 0, 3, 1, 1)

        self.label_31 = QLabel(self.groupBox_5)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_4.addWidget(self.label_31, 9, 0, 1, 1)

        self.cpp_tfszSlider = QSlider(self.groupBox_5)
        self.cpp_tfszSlider.setObjectName(u"cpp_tfszSlider")
        self.cpp_tfszSlider.setMinimum(100)
        self.cpp_tfszSlider.setMaximum(500)
        self.cpp_tfszSlider.setValue(100)
        self.cpp_tfszSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.cpp_tfszSlider, 5, 2, 1, 1)

        self.cpp_tfszSpin = QDoubleSpinBox(self.groupBox_5)
        self.cpp_tfszSpin.setObjectName(u"cpp_tfszSpin")
        self.cpp_tfszSpin.setMinimum(1.000000000000000)
        self.cpp_tfszSpin.setMaximum(5.000000000000000)
        self.cpp_tfszSpin.setSingleStep(0.010000000000000)

        self.gridLayout_4.addWidget(self.cpp_tfszSpin, 9, 3, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_5)

        self.parametersTab.addTab(self.llamacppParamTab, "")
        self.tsParamTab = QWidget()
        self.tsParamTab.setObjectName(u"tsParamTab")
        self.tsParamTab.setAutoFillBackground(True)
        self.horizontalLayout = QHBoxLayout(self.tsParamTab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.tsParamTab)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.tsModelLine = QLineEdit(self.tsParamTab)
        self.tsModelLine.setObjectName(u"tsModelLine")

        self.horizontalLayout.addWidget(self.tsModelLine)

        self.parametersTab.addTab(self.tsParamTab, "")

        self.verticalLayout.addWidget(self.parametersTab)


        self.retranslateUi(Settings_Dialog)
        self.minPSlider.valueChanged.connect(self.minPSpin.setValue)
        self.minPSpin.valueChanged.connect(self.minPSlider.setValue)
        self.token_repetition_penalty_decaySlider.valueChanged.connect(self.token_repetition_penalty_decaySpin.setValue)
        self.token_repetition_penalty_decaySpin.valueChanged.connect(self.token_repetition_penalty_decaySlider.setValue)
        self.numbeamsSlider.valueChanged.connect(self.numbeamsSpin.setValue)
        self.numbeamsSpin.valueChanged.connect(self.numbeamsSlider.setValue)
        self.beamLengthSlider.valueChanged.connect(self.beamLengthSpin.setValue)
        self.beamLengthSpin.valueChanged.connect(self.beamLengthSlider.setValue)
        self.CPP_ctxsize_Slider.valueChanged.connect(self.CPP_ctxsize_Spin.setValue)
        self.CPP_ctxsize_Spin.valueChanged.connect(self.CPP_ctxsize_Slider.setValue)
        self.gpuLayersSlider.valueChanged.connect(self.gpuLayersSpin.setValue)
        self.gpuLayersSpin.valueChanged.connect(self.gpuLayersSlider.setValue)
        self.top_kSlider.valueChanged.connect(self.top_kSpin.setValue)
        self.top_kSpin.valueChanged.connect(self.top_kSlider.setValue)
        self.max_new_tokensSlider.valueChanged.connect(self.max_new_tokensSpin.setValue)
        self.max_new_tokensSpin.valueChanged.connect(self.max_new_tokensSlider.setValue)
        self.cppBatchSizeSpin.valueChanged.connect(self.cppBatchSizeSlider.setValue)
        self.cppBatchSizeSlider.valueChanged.connect(self.cppBatchSizeSpin.setValue)

        self.parametersTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Settings_Dialog)
    # setupUi

    def retranslateUi(self, Settings_Dialog):
        Settings_Dialog.setWindowTitle(QCoreApplication.translate("Settings_Dialog", u"Parameters", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Settings_Dialog", u"Shared", None))
#if QT_CONFIG(tooltip)
        self.top_pSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Consider only the top tokens whose likelihood together adds up to this number (0-1.0) - ignore all others", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Settings_Dialog", u"Top K:", None))
#if QT_CONFIG(tooltip)
        self.repetition_penaltySpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u" Sets the amount the model will be penalized for attempting to use one of those tokens in repeat window", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.temperatureSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Degree of randomness or wildness - how much AI is allowed to sway from the most probable prediction", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.max_new_tokensSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Maximum number of tokens the model will output after outputting the prompt - number of tokens to predict", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.temperatureSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Degree of randomness or wildness - how much AI is allowed to sway from the most probable prediction", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.repetition_penaltySlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u" Sets the amount the model will be penalized for attempting to use one of those tokens in repeat window", None))
#endif // QT_CONFIG(tooltip)
        self.label_17.setText(QCoreApplication.translate("Settings_Dialog", u"Top P:", None))
        self.label.setText(QCoreApplication.translate("Settings_Dialog", u"Repetition penalty:", None))
        self.label_15.setText(QCoreApplication.translate("Settings_Dialog", u"Temperature:", None))
#if QT_CONFIG(tooltip)
        self.top_kSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Consider only this many most likely tokens - ignore all others", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("Settings_Dialog", u"Max new tokens:", None))
#if QT_CONFIG(tooltip)
        self.top_pSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Consider only the top tokens whose likelihood together adds up to this number (0-1.0) - ignore all others", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.top_kSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Consider only this many most likely tokens - ignore all others", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.max_new_tokensSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Maximum number of tokens the model will output after outputting the prompt - number of tokens to predict", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.seedSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Seed to use", None))
#endif // QT_CONFIG(tooltip)
        self.label_29.setText(QCoreApplication.translate("Settings_Dialog", u"Seed:", None))
        self.label_2.setText(QCoreApplication.translate("Settings_Dialog", u"Preset:", None))
#if QT_CONFIG(tooltip)
        self.paramPresets_comboBox.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Parameter preset", None))
#endif // QT_CONFIG(tooltip)
        self.parametersTab.setTabText(self.parametersTab.indexOf(self.sharedParamTab), QCoreApplication.translate("Settings_Dialog", u"Shared", None))
        self.groupBox.setTitle(QCoreApplication.translate("Settings_Dialog", u"Exllama", None))
#if QT_CONFIG(tooltip)
        self.beamLengthSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Beam length value", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.minPSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"If not set to 1, select only tokens that are at least this much more likely to appear than random tokens, given the prior text.", None))
#endif // QT_CONFIG(tooltip)
        self.label_22.setText(QCoreApplication.translate("Settings_Dialog", u"Num beams:", None))
#if QT_CONFIG(tooltip)
        self.token_repetition_penalty_decaySpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Token repetition penalty sustain", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.token_repetition_penalty_decaySlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Token repetition penalty sustain", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.beamLengthSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Beam length value", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.numbeamsSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Number of beams. Slower, more VRAM", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.numbeamsSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Number of beams. Slower, more VRAm", None))
#endif // QT_CONFIG(tooltip)
        self.label_19.setText(QCoreApplication.translate("Settings_Dialog", u"Min P:", None))
        self.label25.setText(QCoreApplication.translate("Settings_Dialog", u"Token repetition penalty sustain:", None))
        self.label_26.setText(QCoreApplication.translate("Settings_Dialog", u"Beam length:", None))
#if QT_CONFIG(tooltip)
        self.minPSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Minimum P value", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.exllamaGpuSplitCheck.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Split memory across multiple GPUs", None))
#endif // QT_CONFIG(tooltip)
        self.exllamaGpuSplitCheck.setText(QCoreApplication.translate("Settings_Dialog", u"Multi-GPU split", None))
#if QT_CONFIG(tooltip)
        self.exllamaGpuSplitLine.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Comma-separated list of VRAM (in GB) to use per GPU device for model layers, e.g: - 8,6,4", None))
#endif // QT_CONFIG(tooltip)
        self.exllamaGpuSplitLine.setText("")
        self.exllamaGpuSplitLine.setPlaceholderText(QCoreApplication.translate("Settings_Dialog", u"8,6", None))
        self.parametersTab.setTabText(self.parametersTab.indexOf(self.exllamaParamTab), QCoreApplication.translate("Settings_Dialog", u"Exllama", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Settings_Dialog", u"llama.cpp", None))
        self.label_16.setText(QCoreApplication.translate("Settings_Dialog", u"Threads:", None))
#if QT_CONFIG(tooltip)
        self.cppBatchSizeSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Batch size to use", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_3.setTitle("")
#if QT_CONFIG(tooltip)
        self.cppMlockCheck.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Force the system to keep the model in RAM", None))
#endif // QT_CONFIG(tooltip)
        self.cppMlockCheck.setText(QCoreApplication.translate("Settings_Dialog", u"Use MLOCK", None))
#if QT_CONFIG(tooltip)
        self.cppMmapCheck.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Use mmap if possible", None))
#endif // QT_CONFIG(tooltip)
        self.cppMmapCheck.setText(QCoreApplication.translate("Settings_Dialog", u"Use MMAP", None))
        self.cppCacheCheck.setText(QCoreApplication.translate("Settings_Dialog", u"Use cache", None))
        self.cppVerboseCheck.setText(QCoreApplication.translate("Settings_Dialog", u"Verbose", None))
        self.gpuAccelCheck.setText(QCoreApplication.translate("Settings_Dialog", u"Use GPU acceleration", None))
#if QT_CONFIG(tooltip)
        self.gpuLayersSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Number of GPU layers to use", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.CPP_ctxsize_Slider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Maximum length of the prompt and output combined (in tokens)", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("Settings_Dialog", u"Mirostat mode:", None))
#if QT_CONFIG(tooltip)
        self.cppBatchSizeSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Batch size to use", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("Settings_Dialog", u"Batch size:", None))
#if QT_CONFIG(tooltip)
        self.gpuLayersSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Number of GPU layers to use", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cppMirastatMode.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Mirostat algorithim mode", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.CPP_ctxsize_Spin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Maximum length of the prompt and output combined (in tokens)", None))
#endif // QT_CONFIG(tooltip)
        self.CPP_ctxsize_Spin.setSuffix("")
        self.label_10.setText(QCoreApplication.translate("Settings_Dialog", u"GPU Layers:", None))
        self.label_12.setText(QCoreApplication.translate("Settings_Dialog", u"Context size:", None))
        self.label_18.setText(QCoreApplication.translate("Settings_Dialog", u"LoRA path:", None))
#if QT_CONFIG(tooltip)
        self.cppThreads.setToolTip(QCoreApplication.translate("Settings_Dialog", u"CPU threads to use", None))
#endif // QT_CONFIG(tooltip)
        self.label_31.setText(QCoreApplication.translate("Settings_Dialog", u"Tail Free Sampling:", None))
#if QT_CONFIG(tooltip)
        self.cpp_tfszSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Higher value of  will further suppress less likely tokens from the tail of the distribution, while a value of 1.0 disables the effect of TFS", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cpp_tfszSpin.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Higher value of  will further suppress less likely tokens from the tail of the distribution, while a value of 1.0 disables the effect of TFS", None))
#endif // QT_CONFIG(tooltip)
        self.parametersTab.setTabText(self.parametersTab.indexOf(self.llamacppParamTab), QCoreApplication.translate("Settings_Dialog", u"llama.cpp", None))
        self.label_3.setText(QCoreApplication.translate("Settings_Dialog", u"Model:", None))
        self.tsModelLine.setPlaceholderText(QCoreApplication.translate("Settings_Dialog", u"pythia_deduped_1.4B", None))
        self.parametersTab.setTabText(self.parametersTab.indexOf(self.tsParamTab), QCoreApplication.translate("Settings_Dialog", u"TextSynth", None))
    # retranslateUi

