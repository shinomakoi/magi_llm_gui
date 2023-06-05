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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QSizePolicy,
    QSlider, QSpinBox, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Settings_Dialog(object):
    def setupUi(self, Settings_Dialog):
        if not Settings_Dialog.objectName():
            Settings_Dialog.setObjectName(u"Settings_Dialog")
        Settings_Dialog.resize(632, 690)
        self.verticalLayout = QVBoxLayout(Settings_Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.parametersTab = QTabWidget(Settings_Dialog)
        self.parametersTab.setObjectName(u"parametersTab")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setAutoFillBackground(True)
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.top_kSliderLabel = QLabel(self.groupBox_2)
        self.top_kSliderLabel.setObjectName(u"top_kSliderLabel")

        self.gridLayout_2.addWidget(self.top_kSliderLabel, 3, 2, 1, 1)

        self.seedValue = QSpinBox(self.groupBox_2)
        self.seedValue.setObjectName(u"seedValue")
        self.seedValue.setMinimum(-1)
        self.seedValue.setMaximum(10000000)
        self.seedValue.setValue(-1)

        self.gridLayout_2.addWidget(self.seedValue, 10, 1, 1, 1)

        self.top_kSlider = QSlider(self.groupBox_2)
        self.top_kSlider.setObjectName(u"top_kSlider")
        self.top_kSlider.setMaximum(200)
        self.top_kSlider.setValue(20)
        self.top_kSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.top_kSlider, 3, 1, 1, 1)

        self.reppenaltySliderLabel = QLabel(self.groupBox_2)
        self.reppenaltySliderLabel.setObjectName(u"reppenaltySliderLabel")

        self.gridLayout_2.addWidget(self.reppenaltySliderLabel, 9, 2, 1, 1)

        self.top_pSlider = QSlider(self.groupBox_2)
        self.top_pSlider.setObjectName(u"top_pSlider")
        self.top_pSlider.setMaximum(100)
        self.top_pSlider.setValue(65)
        self.top_pSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.top_pSlider, 5, 1, 1, 1)

        self.label_29 = QLabel(self.groupBox_2)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_2.addWidget(self.label_29, 10, 0, 1, 1)

        self.tempSlider = QSlider(self.groupBox_2)
        self.tempSlider.setObjectName(u"tempSlider")
        self.tempSlider.setMaximum(199)
        self.tempSlider.setValue(95)
        self.tempSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.tempSlider, 2, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 5, 0, 1, 1)

        self.tempSliderLabel = QLabel(self.groupBox_2)
        self.tempSliderLabel.setObjectName(u"tempSliderLabel")

        self.gridLayout_2.addWidget(self.tempSliderLabel, 2, 2, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 7, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 2, 0, 1, 1)

        self.top_pSliderLabel = QLabel(self.groupBox_2)
        self.top_pSliderLabel.setObjectName(u"top_pSliderLabel")

        self.gridLayout_2.addWidget(self.top_pSliderLabel, 5, 2, 1, 1)

        self.reppenaltySlider = QSlider(self.groupBox_2)
        self.reppenaltySlider.setObjectName(u"reppenaltySlider")
        self.reppenaltySlider.setMaximum(150)
        self.reppenaltySlider.setValue(115)
        self.reppenaltySlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.reppenaltySlider, 9, 1, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 9, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.maxnewtokensSlider = QSlider(self.groupBox_2)
        self.maxnewtokensSlider.setObjectName(u"maxnewtokensSlider")
        self.maxnewtokensSlider.setMinimum(32)
        self.maxnewtokensSlider.setMaximum(2048)
        self.maxnewtokensSlider.setValue(256)
        self.maxnewtokensSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.maxnewtokensSlider, 7, 1, 1, 1)

        self.maxnewtokensSliderLabel = QLabel(self.groupBox_2)
        self.maxnewtokensSliderLabel.setObjectName(u"maxnewtokensSliderLabel")

        self.gridLayout_2.addWidget(self.maxnewtokensSliderLabel, 7, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.parametersTab.addTab(self.tab, "")
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
        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 4, 3, 1, 1)

        self.typicalPSliderLabel = QLabel(self.groupBox)
        self.typicalPSliderLabel.setObjectName(u"typicalPSliderLabel")

        self.gridLayout.addWidget(self.typicalPSliderLabel, 0, 4, 1, 1)

        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 0, 1, 1, 1)

        self.token_repetition_penalty_decaySlider = QSlider(self.groupBox)
        self.token_repetition_penalty_decaySlider.setObjectName(u"token_repetition_penalty_decaySlider")
        self.token_repetition_penalty_decaySlider.setMaximum(512)
        self.token_repetition_penalty_decaySlider.setValue(256)
        self.token_repetition_penalty_decaySlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.token_repetition_penalty_decaySlider, 1, 3, 1, 1)

        self.label25 = QLabel(self.groupBox)
        self.label25.setObjectName(u"label25")

        self.gridLayout.addWidget(self.label25, 1, 1, 1, 2)

        self.beamLengthSlider = QSlider(self.groupBox)
        self.beamLengthSlider.setObjectName(u"beamLengthSlider")
        self.beamLengthSlider.setMinimum(1)
        self.beamLengthSlider.setMaximum(10)
        self.beamLengthSlider.setValue(1)
        self.beamLengthSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.beamLengthSlider, 6, 3, 1, 1)

        self.lengthpenaltySliderLabel = QLabel(self.groupBox)
        self.lengthpenaltySliderLabel.setObjectName(u"lengthpenaltySliderLabel")

        self.gridLayout.addWidget(self.lengthpenaltySliderLabel, 6, 4, 1, 1)

        self.label_26 = QLabel(self.groupBox)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout.addWidget(self.label_26, 6, 1, 1, 1)

        self.encoderrepSliderLabel = QLabel(self.groupBox)
        self.encoderrepSliderLabel.setObjectName(u"encoderrepSliderLabel")

        self.gridLayout.addWidget(self.encoderrepSliderLabel, 1, 4, 1, 1)

        self.numbeamsSlider = QSlider(self.groupBox)
        self.numbeamsSlider.setObjectName(u"numbeamsSlider")
        self.numbeamsSlider.setMinimum(1)
        self.numbeamsSlider.setMaximum(10)
        self.numbeamsSlider.setValue(1)
        self.numbeamsSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.numbeamsSlider, 5, 3, 1, 1)

        self.minPSlider = QSlider(self.groupBox)
        self.minPSlider.setObjectName(u"minPSlider")
        self.minPSlider.setMaximum(100)
        self.minPSlider.setValue(0)
        self.minPSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.minPSlider, 0, 3, 1, 1)

        self.numbeamsSliderLabel = QLabel(self.groupBox)
        self.numbeamsSliderLabel.setObjectName(u"numbeamsSliderLabel")

        self.gridLayout.addWidget(self.numbeamsSliderLabel, 5, 4, 1, 1)

        self.label_22 = QLabel(self.groupBox)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 5, 1, 1, 1)


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
        self.label_31 = QLabel(self.groupBox_5)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_4.addWidget(self.label_31, 4, 0, 1, 2)

        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 5, 0, 1, 1)

        self.cppMlockCheck = QCheckBox(self.groupBox_5)
        self.cppMlockCheck.setObjectName(u"cppMlockCheck")

        self.gridLayout_4.addWidget(self.cppMlockCheck, 12, 2, 1, 1)

        self.cppMmapCheck = QCheckBox(self.groupBox_5)
        self.cppMmapCheck.setObjectName(u"cppMmapCheck")
        self.cppMmapCheck.setChecked(True)

        self.gridLayout_4.addWidget(self.cppMmapCheck, 10, 2, 1, 1)

        self.label_14 = QLabel(self.groupBox_5)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 6, 0, 1, 1)

        self.gpuLayersSlider = QSlider(self.groupBox_5)
        self.gpuLayersSlider.setObjectName(u"gpuLayersSlider")
        self.gpuLayersSlider.setMinimum(1)
        self.gpuLayersSlider.setMaximum(80)
        self.gpuLayersSlider.setValue(22)
        self.gpuLayersSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.gpuLayersSlider, 8, 2, 1, 1)

        self.label_16 = QLabel(self.groupBox_5)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 1)

        self.cppThreads = QSpinBox(self.groupBox_5)
        self.cppThreads.setObjectName(u"cppThreads")
        self.cppThreads.setMinimum(1)
        self.cppThreads.setMaximum(64)
        self.cppThreads.setValue(4)

        self.gridLayout_4.addWidget(self.cppThreads, 0, 2, 1, 1)

        self.gpuAccelCheck = QCheckBox(self.groupBox_5)
        self.gpuAccelCheck.setObjectName(u"gpuAccelCheck")
        self.gpuAccelCheck.setChecked(True)

        self.gridLayout_4.addWidget(self.gpuAccelCheck, 13, 2, 1, 1)

        self.CPP_repeat_last_nSliderLabel = QLabel(self.groupBox_5)
        self.CPP_repeat_last_nSliderLabel.setObjectName(u"CPP_repeat_last_nSliderLabel")

        self.gridLayout_4.addWidget(self.CPP_repeat_last_nSliderLabel, 4, 3, 1, 1)

        self.CPP_ctxsize_SliderLabel = QLabel(self.groupBox_5)
        self.CPP_ctxsize_SliderLabel.setObjectName(u"CPP_ctxsize_SliderLabel")

        self.gridLayout_4.addWidget(self.CPP_ctxsize_SliderLabel, 3, 3, 1, 1)

        self.cppBatchSizeSlider_2 = QLabel(self.groupBox_5)
        self.cppBatchSizeSlider_2.setObjectName(u"cppBatchSizeSlider_2")

        self.gridLayout_4.addWidget(self.cppBatchSizeSlider_2, 5, 3, 1, 1)

        self.cppBatchSizeSlider = QSlider(self.groupBox_5)
        self.cppBatchSizeSlider.setObjectName(u"cppBatchSizeSlider")
        self.cppBatchSizeSlider.setMinimum(8)
        self.cppBatchSizeSlider.setMaximum(1024)
        self.cppBatchSizeSlider.setValue(512)
        self.cppBatchSizeSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.cppBatchSizeSlider, 5, 2, 1, 1)

        self.CPP_ctxsize_Slider = QSlider(self.groupBox_5)
        self.CPP_ctxsize_Slider.setObjectName(u"CPP_ctxsize_Slider")
        self.CPP_ctxsize_Slider.setMinimum(64)
        self.CPP_ctxsize_Slider.setMaximum(2048)
        self.CPP_ctxsize_Slider.setValue(2048)
        self.CPP_ctxsize_Slider.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.CPP_ctxsize_Slider, 3, 2, 1, 1)

        self.CPP_repeat_last_nSlider = QSlider(self.groupBox_5)
        self.CPP_repeat_last_nSlider.setObjectName(u"CPP_repeat_last_nSlider")
        self.CPP_repeat_last_nSlider.setMinimum(16)
        self.CPP_repeat_last_nSlider.setMaximum(512)
        self.CPP_repeat_last_nSlider.setValue(64)
        self.CPP_repeat_last_nSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.CPP_repeat_last_nSlider, 4, 2, 1, 1)

        self.label_12 = QLabel(self.groupBox_5)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 3, 0, 1, 2)

        self.cppMirastatMode = QSpinBox(self.groupBox_5)
        self.cppMirastatMode.setObjectName(u"cppMirastatMode")
        self.cppMirastatMode.setMaximum(2)

        self.gridLayout_4.addWidget(self.cppMirastatMode, 6, 2, 1, 1)

        self.line_3 = QFrame(self.groupBox_5)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_3, 1, 2, 1, 1)

        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 8, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_5)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 8, 3, 1, 1)

        self.label_18 = QLabel(self.groupBox_5)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_4.addWidget(self.label_18, 9, 0, 1, 1)

        self.cppLoraLineEdit = QLineEdit(self.groupBox_5)
        self.cppLoraLineEdit.setObjectName(u"cppLoraLineEdit")

        self.gridLayout_4.addWidget(self.cppLoraLineEdit, 9, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_5)

        self.parametersTab.addTab(self.llamacppParamTab, "")

        self.verticalLayout.addWidget(self.parametersTab)


        self.retranslateUi(Settings_Dialog)
        self.CPP_ctxsize_Slider.valueChanged.connect(self.CPP_ctxsize_SliderLabel.setNum)
        self.CPP_repeat_last_nSlider.valueChanged.connect(self.CPP_repeat_last_nSliderLabel.setNum)
        self.cppBatchSizeSlider.valueChanged.connect(self.cppBatchSizeSlider_2.setNum)
        self.numbeamsSlider.valueChanged.connect(self.numbeamsSliderLabel.setNum)
        self.maxnewtokensSlider.valueChanged.connect(self.maxnewtokensSliderLabel.setNum)
        self.top_kSlider.valueChanged.connect(self.top_kSliderLabel.setNum)
        self.gpuLayersSlider.valueChanged.connect(self.label_13.setNum)

        self.parametersTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Settings_Dialog)
    # setupUi

    def retranslateUi(self, Settings_Dialog):
        Settings_Dialog.setWindowTitle(QCoreApplication.translate("Settings_Dialog", u"Parameters", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Settings_Dialog", u"Shared", None))
        self.top_kSliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"20", None))
#if QT_CONFIG(tooltip)
        self.seedValue.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Seed to use", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.top_kSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Consider only this many most likely tokens - ignore all others", None))
#endif // QT_CONFIG(tooltip)
        self.reppenaltySliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"1.15", None))
#if QT_CONFIG(tooltip)
        self.top_pSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Consider only the top tokens whose likelihood together adds up to this number (0-1.0) - ignore all others", None))
#endif // QT_CONFIG(tooltip)
        self.label_29.setText(QCoreApplication.translate("Settings_Dialog", u"Seed", None))
#if QT_CONFIG(tooltip)
        self.tempSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Degree of randomness or wildness - how much AI is allowed to sway from the most probable prediction", None))
#endif // QT_CONFIG(tooltip)
        self.label_17.setText(QCoreApplication.translate("Settings_Dialog", u"Top P:", None))
        self.tempSliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"0.95", None))
        self.label_11.setText(QCoreApplication.translate("Settings_Dialog", u"Max new tokens:", None))
        self.label_15.setText(QCoreApplication.translate("Settings_Dialog", u"Temperature:", None))
        self.top_pSliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"0.65", None))
#if QT_CONFIG(tooltip)
        self.reppenaltySlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u" Sets the amount the model will be penalized for attempting to use one of those tokens in repeat window", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Settings_Dialog", u"Repetition penalty:", None))
        self.label_5.setText(QCoreApplication.translate("Settings_Dialog", u"Top K:", None))
#if QT_CONFIG(tooltip)
        self.maxnewtokensSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Maximum number of tokens the model will output after outputting the prompt - number of tokens to predict", None))
#endif // QT_CONFIG(tooltip)
        self.maxnewtokensSliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"256", None))
        self.parametersTab.setTabText(self.parametersTab.indexOf(self.tab), QCoreApplication.translate("Settings_Dialog", u"Shared", None))
        self.groupBox.setTitle(QCoreApplication.translate("Settings_Dialog", u"Exllama", None))
        self.typicalPSliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"0", None))
        self.label_19.setText(QCoreApplication.translate("Settings_Dialog", u"Min P:", None))
#if QT_CONFIG(tooltip)
        self.token_repetition_penalty_decaySlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Also known as the \"Hallucinations filter\". Used to penalize tokens that are *not* in the prior text. Higher value = more likely to stay in context, lower value = more likely to diverge", None))
#endif // QT_CONFIG(tooltip)
        self.label25.setText(QCoreApplication.translate("Settings_Dialog", u"Token repetition penalty sustain:", None))
#if QT_CONFIG(tooltip)
        self.beamLengthSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Beam search length penalty", None))
#endif // QT_CONFIG(tooltip)
        self.lengthpenaltySliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"1", None))
        self.label_26.setText(QCoreApplication.translate("Settings_Dialog", u"Beam length:", None))
        self.encoderrepSliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"256", None))
#if QT_CONFIG(tooltip)
        self.numbeamsSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Beam search", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.minPSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"If not set to 1, select only tokens that are at least this much more likely to appear than random tokens, given the prior text.", None))
#endif // QT_CONFIG(tooltip)
        self.numbeamsSliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"1", None))
        self.label_22.setText(QCoreApplication.translate("Settings_Dialog", u"Num beams:", None))
        self.parametersTab.setTabText(self.parametersTab.indexOf(self.exllamaParamTab), QCoreApplication.translate("Settings_Dialog", u"Exllama", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Settings_Dialog", u"llama.cpp", None))
        self.label_31.setText(QCoreApplication.translate("Settings_Dialog", u"Repeat last N:", None))
        self.label_6.setText(QCoreApplication.translate("Settings_Dialog", u"Batch size:", None))
#if QT_CONFIG(tooltip)
        self.cppMlockCheck.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Force the system to keep the model in RAM", None))
#endif // QT_CONFIG(tooltip)
        self.cppMlockCheck.setText(QCoreApplication.translate("Settings_Dialog", u"Use MLOCK", None))
#if QT_CONFIG(tooltip)
        self.cppMmapCheck.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Use mmap if possible", None))
#endif // QT_CONFIG(tooltip)
        self.cppMmapCheck.setText(QCoreApplication.translate("Settings_Dialog", u"Use MMAP", None))
        self.label_14.setText(QCoreApplication.translate("Settings_Dialog", u"Mirostat mode:", None))
        self.label_16.setText(QCoreApplication.translate("Settings_Dialog", u"Threads:", None))
#if QT_CONFIG(tooltip)
        self.cppThreads.setToolTip(QCoreApplication.translate("Settings_Dialog", u"CPU threads to use", None))
#endif // QT_CONFIG(tooltip)
        self.gpuAccelCheck.setText(QCoreApplication.translate("Settings_Dialog", u"Use GPU acceleration", None))
        self.CPP_repeat_last_nSliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"64", None))
        self.CPP_ctxsize_SliderLabel.setText(QCoreApplication.translate("Settings_Dialog", u"2048", None))
        self.cppBatchSizeSlider_2.setText(QCoreApplication.translate("Settings_Dialog", u"512", None))
#if QT_CONFIG(tooltip)
        self.cppBatchSizeSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Batch size to use", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.CPP_ctxsize_Slider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Maximum length of the prompt and output combined (in tokens)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.CPP_repeat_last_nSlider.setToolTip(QCoreApplication.translate("Settings_Dialog", u"Last n tokens to consider for penalize - size of window of tokens that the model will be penalized for repeating", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("Settings_Dialog", u"Context size:", None))
        self.label_10.setText(QCoreApplication.translate("Settings_Dialog", u"GPU Layers:", None))
        self.label_13.setText(QCoreApplication.translate("Settings_Dialog", u"22", None))
        self.label_18.setText(QCoreApplication.translate("Settings_Dialog", u"LoRA path:", None))
        self.parametersTab.setTabText(self.parametersTab.indexOf(self.llamacppParamTab), QCoreApplication.translate("Settings_Dialog", u"llama.cpp", None))
    # retranslateUi

