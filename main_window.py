# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QTabWidget,
    QTextEdit, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1198, 957)
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        MainWindow.setFont(font)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionChat = QAction(MainWindow)
        self.actionChat.setObjectName(u"actionChat")
        self.actionStandard = QAction(MainWindow)
        self.actionStandard.setObjectName(u"actionStandard")
        self.actionNotebook = QAction(MainWindow)
        self.actionNotebook.setObjectName(u"actionNotebook")
        self.actionParameters = QAction(MainWindow)
        self.actionParameters.setObjectName(u"actionParameters")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainTabWidget = QTabWidget(self.centralwidget)
        self.mainTabWidget.setObjectName(u"mainTabWidget")
        self.textgenTab = QWidget()
        self.textgenTab.setObjectName(u"textgenTab")
        self.textgenTab.setAutoFillBackground(True)
        self.gridLayout_2 = QGridLayout(self.textgenTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.outputText = QTextEdit(self.textgenTab)
        self.outputText.setObjectName(u"outputText")
        self.outputText.setReadOnly(True)

        self.gridLayout_2.addWidget(self.outputText, 0, 0, 1, 6)

        self.chatInputHistoryCombo = QComboBox(self.textgenTab)
        self.chatInputHistoryCombo.setObjectName(u"chatInputHistoryCombo")

        self.gridLayout_2.addWidget(self.chatInputHistoryCombo, 1, 0, 1, 1)

        self.chatOutputSession = QComboBox(self.textgenTab)
        self.chatOutputSession.addItem("")
        self.chatOutputSession.setObjectName(u"chatOutputSession")

        self.gridLayout_2.addWidget(self.chatOutputSession, 1, 1, 1, 5)

        self.inputText = QPlainTextEdit(self.textgenTab)
        self.inputText.setObjectName(u"inputText")
        self.inputText.setMaximumSize(QSize(16777215, 90))

        self.gridLayout_2.addWidget(self.inputText, 2, 0, 1, 1)

        self.generateButton = QPushButton(self.textgenTab)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setEnabled(False)
        self.generateButton.setMinimumSize(QSize(64, 64))
        self.generateButton.setMaximumSize(QSize(64, 64))

        self.gridLayout_2.addWidget(self.generateButton, 2, 1, 1, 1)

        self.continueButton = QPushButton(self.textgenTab)
        self.continueButton.setObjectName(u"continueButton")
        self.continueButton.setEnabled(False)
        self.continueButton.setMinimumSize(QSize(64, 64))
        self.continueButton.setMaximumSize(QSize(64, 64))

        self.gridLayout_2.addWidget(self.continueButton, 2, 2, 1, 1)

        self.rewindButton = QPushButton(self.textgenTab)
        self.rewindButton.setObjectName(u"rewindButton")
        self.rewindButton.setEnabled(False)
        self.rewindButton.setMinimumSize(QSize(64, 64))
        self.rewindButton.setMaximumSize(QSize(64, 64))

        self.gridLayout_2.addWidget(self.rewindButton, 2, 3, 1, 1)

        self.clearButton = QPushButton(self.textgenTab)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setEnabled(True)
        self.clearButton.setMinimumSize(QSize(64, 64))
        self.clearButton.setMaximumSize(QSize(64, 64))

        self.gridLayout_2.addWidget(self.clearButton, 2, 4, 1, 1)

        self.stopButton = QPushButton(self.textgenTab)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setEnabled(False)
        self.stopButton.setMinimumSize(QSize(64, 64))
        self.stopButton.setMaximumSize(QSize(64, 64))

        self.gridLayout_2.addWidget(self.stopButton, 2, 5, 1, 1)

        self.mainTabWidget.addTab(self.textgenTab, "")
        self.preferencesTab = QWidget()
        self.preferencesTab.setObjectName(u"preferencesTab")
        self.preferencesTab.setAutoFillBackground(True)
        self.gridLayout_3 = QGridLayout(self.preferencesTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.preferencesTab)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setAutoFillBackground(True)
        self.gridLayout_6 = QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.backendGroup = QGroupBox(self.tab_2)
        self.backendGroup.setObjectName(u"backendGroup")
        self.gridLayout_10 = QGridLayout(self.backendGroup)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.streamEnabledCheck = QCheckBox(self.backendGroup)
        self.streamEnabledCheck.setObjectName(u"streamEnabledCheck")
        self.streamEnabledCheck.setChecked(True)

        self.gridLayout_10.addWidget(self.streamEnabledCheck, 9, 0, 1, 1)

        self.unloadModelButton = QPushButton(self.backendGroup)
        self.unloadModelButton.setObjectName(u"unloadModelButton")
        self.unloadModelButton.setEnabled(False)

        self.gridLayout_10.addWidget(self.unloadModelButton, 7, 1, 1, 1)

        self.backendAutoLaunch = QCheckBox(self.backendGroup)
        self.backendAutoLaunch.setObjectName(u"backendAutoLaunch")
        self.backendAutoLaunch.setChecked(True)

        self.gridLayout_10.addWidget(self.backendAutoLaunch, 8, 0, 1, 1)

        self.cppCheck = QRadioButton(self.backendGroup)
        self.cppCheck.setObjectName(u"cppCheck")
        self.cppCheck.setChecked(True)

        self.gridLayout_10.addWidget(self.cppCheck, 0, 0, 1, 1)

        self.cppServerCheck = QRadioButton(self.backendGroup)
        self.cppServerCheck.setObjectName(u"cppServerCheck")

        self.gridLayout_10.addWidget(self.cppServerCheck, 1, 0, 1, 1)

        self.exllamaCheck = QRadioButton(self.backendGroup)
        self.exllamaCheck.setObjectName(u"exllamaCheck")
        self.exllamaCheck.setChecked(False)

        self.gridLayout_10.addWidget(self.exllamaCheck, 2, 0, 1, 1)

        self.loadModelButton = QPushButton(self.backendGroup)
        self.loadModelButton.setObjectName(u"loadModelButton")

        self.gridLayout_10.addWidget(self.loadModelButton, 7, 0, 1, 1)


        self.gridLayout_6.addWidget(self.backendGroup, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.cppModelPath = QLineEdit(self.groupBox_2)
        self.cppModelPath.setObjectName(u"cppModelPath")

        self.gridLayout_5.addWidget(self.cppModelPath, 3, 1, 1, 1)

        self.rwkvCppModelPath = QLineEdit(self.groupBox_2)
        self.rwkvCppModelPath.setObjectName(u"rwkvCppModelPath")

        self.gridLayout_5.addWidget(self.rwkvCppModelPath, 5, 1, 1, 1)

        self.RWKVcppModelSelect = QToolButton(self.groupBox_2)
        self.RWKVcppModelSelect.setObjectName(u"RWKVcppModelSelect")

        self.gridLayout_5.addWidget(self.RWKVcppModelSelect, 5, 2, 1, 1)

        self.exllamaModelSelect = QToolButton(self.groupBox_2)
        self.exllamaModelSelect.setObjectName(u"exllamaModelSelect")

        self.gridLayout_5.addWidget(self.exllamaModelSelect, 4, 2, 1, 1)

        self.cppModelSelect = QToolButton(self.groupBox_2)
        self.cppModelSelect.setObjectName(u"cppModelSelect")
        self.cppModelSelect.setArrowType(Qt.NoArrow)

        self.gridLayout_5.addWidget(self.cppModelSelect, 3, 2, 1, 1)

        self.label_28 = QLabel(self.groupBox_2)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_5.addWidget(self.label_28, 3, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 4, 0, 1, 1)

        self.exllamaModelPath = QLineEdit(self.groupBox_2)
        self.exllamaModelPath.setObjectName(u"exllamaModelPath")

        self.gridLayout_5.addWidget(self.exllamaModelPath, 4, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 5, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setAutoFillBackground(True)
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_7.addWidget(self.label_4, 1, 0, 1, 1)

        self.customResponsePrefix = QLineEdit(self.groupBox)
        self.customResponsePrefix.setObjectName(u"customResponsePrefix")

        self.gridLayout_7.addWidget(self.customResponsePrefix, 3, 2, 1, 1)

        self.botNameLine = QLineEdit(self.groupBox)
        self.botNameLine.setObjectName(u"botNameLine")

        self.gridLayout_7.addWidget(self.botNameLine, 2, 2, 1, 1)

        self.yourNameLine = QLineEdit(self.groupBox)
        self.yourNameLine.setObjectName(u"yourNameLine")

        self.gridLayout_7.addWidget(self.yourNameLine, 1, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_7.addWidget(self.label_5, 2, 0, 1, 1)

        self.customResponsePrefixCheck = QCheckBox(self.groupBox)
        self.customResponsePrefixCheck.setObjectName(u"customResponsePrefixCheck")

        self.gridLayout_7.addWidget(self.customResponsePrefixCheck, 3, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_8 = QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.awesomePresetComboBox = QComboBox(self.groupBox_4)
        self.awesomePresetComboBox.setObjectName(u"awesomePresetComboBox")

        self.gridLayout_8.addWidget(self.awesomePresetComboBox, 2, 1, 1, 1)

        self.instructPresetComboBox = QComboBox(self.groupBox_4)
        self.instructPresetComboBox.setObjectName(u"instructPresetComboBox")

        self.gridLayout_8.addWidget(self.instructPresetComboBox, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.gridLayout_8.addWidget(self.label, 2, 0, 1, 1)

        self.instructRadioButton = QRadioButton(self.groupBox_4)
        self.instructRadioButton.setObjectName(u"instructRadioButton")
        self.instructRadioButton.setChecked(True)

        self.gridLayout_8.addWidget(self.instructRadioButton, 0, 0, 1, 1)

        self.charactersRadioButton = QRadioButton(self.groupBox_4)
        self.charactersRadioButton.setObjectName(u"charactersRadioButton")

        self.gridLayout_8.addWidget(self.charactersRadioButton, 1, 0, 1, 1)

        self.characterPresetComboBox = QComboBox(self.groupBox_4)
        self.characterPresetComboBox.setObjectName(u"characterPresetComboBox")

        self.gridLayout_8.addWidget(self.characterPresetComboBox, 1, 1, 1, 1)

        self.logChatCheck = QCheckBox(self.groupBox_4)
        self.logChatCheck.setObjectName(u"logChatCheck")
        self.logChatCheck.setChecked(False)

        self.gridLayout_8.addWidget(self.logChatCheck, 3, 0, 1, 1)

        self.sendStopStringCheck = QCheckBox(self.groupBox_4)
        self.sendStopStringCheck.setObjectName(u"sendStopStringCheck")
        self.sendStopStringCheck.setChecked(True)

        self.gridLayout_8.addWidget(self.sendStopStringCheck, 3, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setAutoFillBackground(True)
        self.gridLayout_9 = QGridLayout(self.tab_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.groupBox_3 = QGroupBox(self.tab_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.themeDarkCheck = QRadioButton(self.groupBox_3)
        self.themeDarkCheck.setObjectName(u"themeDarkCheck")
        self.themeDarkCheck.setChecked(False)

        self.verticalLayout_2.addWidget(self.themeDarkCheck)

        self.themeLightCheck = QRadioButton(self.groupBox_3)
        self.themeLightCheck.setObjectName(u"themeLightCheck")

        self.verticalLayout_2.addWidget(self.themeLightCheck)

        self.themeNativeCheck = QRadioButton(self.groupBox_3)
        self.themeNativeCheck.setObjectName(u"themeNativeCheck")
        self.themeNativeCheck.setChecked(True)

        self.verticalLayout_2.addWidget(self.themeNativeCheck)


        self.gridLayout_9.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.settingsPathSaveButton = QPushButton(self.preferencesTab)
        self.settingsPathSaveButton.setObjectName(u"settingsPathSaveButton")
        self.settingsPathSaveButton.setFont(font)

        self.gridLayout_3.addWidget(self.settingsPathSaveButton, 1, 0, 1, 1, Qt.AlignRight)

        self.mainTabWidget.addTab(self.preferencesTab, "")

        self.gridLayout.addWidget(self.mainTabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1198, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuMode = QMenu(self.menubar)
        self.menuMode.setObjectName(u"menuMode")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuMode.addAction(self.actionChat)
        self.menuMode.addAction(self.actionStandard)
        self.menuMode.addAction(self.actionNotebook)
        self.menuSettings.addAction(self.actionPreferences)

        self.retranslateUi(MainWindow)

        self.mainTabWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Magi LLM", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionChat.setText(QCoreApplication.translate("MainWindow", u"Chat", None))
        self.actionStandard.setText(QCoreApplication.translate("MainWindow", u"Standard", None))
        self.actionNotebook.setText(QCoreApplication.translate("MainWindow", u"Notebook", None))
        self.actionParameters.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.outputText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans Display';\"><br /></p></body></html>", None))
        self.outputText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Output goes here", None))
#if QT_CONFIG(tooltip)
        self.chatInputHistoryCombo.setToolTip(QCoreApplication.translate("MainWindow", u"Saved chat inputs from session", None))
#endif // QT_CONFIG(tooltip)
        self.chatOutputSession.setItemText(0, QCoreApplication.translate("MainWindow", u"Current", None))

#if QT_CONFIG(tooltip)
        self.chatOutputSession.setToolTip(QCoreApplication.translate("MainWindow", u"Saved chat sessions", None))
#endif // QT_CONFIG(tooltip)
        self.inputText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type something here", None))
#if QT_CONFIG(tooltip)
        self.generateButton.setToolTip(QCoreApplication.translate("MainWindow", u"Send (CTRL+Enter)", None))
#endif // QT_CONFIG(tooltip)
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Gen", None))
#if QT_CONFIG(shortcut)
        self.generateButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.continueButton.setToolTip(QCoreApplication.translate("MainWindow", u"Continue the last generation", None))
#endif // QT_CONFIG(tooltip)
        self.continueButton.setText(QCoreApplication.translate("MainWindow", u"Con", None))
#if QT_CONFIG(tooltip)
        self.rewindButton.setToolTip(QCoreApplication.translate("MainWindow", u"Rewinds the chat 1 turn", None))
#endif // QT_CONFIG(tooltip)
        self.rewindButton.setText(QCoreApplication.translate("MainWindow", u"Rw", None))
#if QT_CONFIG(tooltip)
        self.clearButton.setToolTip(QCoreApplication.translate("MainWindow", u"Clear the output history", None))
#endif // QT_CONFIG(tooltip)
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"Clr", None))
#if QT_CONFIG(tooltip)
        self.stopButton.setToolTip(QCoreApplication.translate("MainWindow", u"Stop generation", None))
#endif // QT_CONFIG(tooltip)
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"St", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.textgenTab), QCoreApplication.translate("MainWindow", u"Chat", None))
        self.backendGroup.setTitle(QCoreApplication.translate("MainWindow", u"Backend", None))
#if QT_CONFIG(tooltip)
        self.streamEnabledCheck.setToolTip(QCoreApplication.translate("MainWindow", u"Stream responses", None))
#endif // QT_CONFIG(tooltip)
        self.streamEnabledCheck.setText(QCoreApplication.translate("MainWindow", u"Stream responses", None))
#if QT_CONFIG(tooltip)
        self.unloadModelButton.setToolTip(QCoreApplication.translate("MainWindow", u"Unload the selected backend and model", None))
#endif // QT_CONFIG(tooltip)
        self.unloadModelButton.setText(QCoreApplication.translate("MainWindow", u"Unload backend", None))
        self.backendAutoLaunch.setText(QCoreApplication.translate("MainWindow", u"Auto load backend at launch", None))
#if QT_CONFIG(tooltip)
        self.cppCheck.setToolTip(QCoreApplication.translate("MainWindow", u"Use llama.cpp backend", None))
#endif // QT_CONFIG(tooltip)
        self.cppCheck.setText(QCoreApplication.translate("MainWindow", u"llama-cpp-python", None))
#if QT_CONFIG(tooltip)
        self.cppServerCheck.setToolTip(QCoreApplication.translate("MainWindow", u"Connects to a launched llama.cpp server instead of llama-cpp-python", None))
#endif // QT_CONFIG(tooltip)
        self.cppServerCheck.setText(QCoreApplication.translate("MainWindow", u"llama.cpp server", None))
#if QT_CONFIG(tooltip)
        self.exllamaCheck.setToolTip(QCoreApplication.translate("MainWindow", u"Use Exllama backend", None))
#endif // QT_CONFIG(tooltip)
        self.exllamaCheck.setText(QCoreApplication.translate("MainWindow", u"Exllama", None))
#if QT_CONFIG(tooltip)
        self.loadModelButton.setToolTip(QCoreApplication.translate("MainWindow", u"Load the selected backend and model", None))
#endif // QT_CONFIG(tooltip)
        self.loadModelButton.setText(QCoreApplication.translate("MainWindow", u"Load backend", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Paths", None))
#if QT_CONFIG(tooltip)
        self.cppModelPath.setToolTip(QCoreApplication.translate("MainWindow", u"Path to GGML model for llama.cpp", None))
#endif // QT_CONFIG(tooltip)
        self.cppModelPath.setText("")
#if QT_CONFIG(tooltip)
        self.rwkvCppModelPath.setToolTip(QCoreApplication.translate("MainWindow", u"Path to GGML model for rwkv.cpp", None))
#endif // QT_CONFIG(tooltip)
        self.RWKVcppModelSelect.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.exllamaModelSelect.setToolTip(QCoreApplication.translate("MainWindow", u"Select Exllama model folder", None))
#endif // QT_CONFIG(tooltip)
        self.exllamaModelSelect.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.cppModelSelect.setToolTip(QCoreApplication.translate("MainWindow", u"Select GGML model", None))
#endif // QT_CONFIG(tooltip)
        self.cppModelSelect.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"llama.cpp: Model path:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Exllama: Model directory:", None))
#if QT_CONFIG(tooltip)
        self.exllamaModelPath.setToolTip(QCoreApplication.translate("MainWindow", u"Path to Exllama GPTQ model folder (mode file, tokenizer.json, config.json)", None))
#endif // QT_CONFIG(tooltip)
        self.exllamaModelPath.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"RWKV.cpp model path:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Models", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Chat prefixes", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"User name:", None))
#if QT_CONFIG(tooltip)
        self.customResponsePrefix.setToolTip(QCoreApplication.translate("MainWindow", u"Prefix to apply to prompts", None))
#endif // QT_CONFIG(tooltip)
        self.customResponsePrefix.setText(QCoreApplication.translate("MainWindow", u"Sure! ", None))
#if QT_CONFIG(tooltip)
        self.botNameLine.setToolTip(QCoreApplication.translate("MainWindow", u"Bot name to be used in chat", None))
#endif // QT_CONFIG(tooltip)
        self.botNameLine.setText(QCoreApplication.translate("MainWindow", u"Assistant", None))
#if QT_CONFIG(tooltip)
        self.yourNameLine.setToolTip(QCoreApplication.translate("MainWindow", u"User name to be used in chat", None))
#endif // QT_CONFIG(tooltip)
        self.yourNameLine.setText(QCoreApplication.translate("MainWindow", u"User", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Bot name:", None))
#if QT_CONFIG(tooltip)
        self.customResponsePrefixCheck.setToolTip(QCoreApplication.translate("MainWindow", u"Apply custom prefix to prompts", None))
#endif // QT_CONFIG(tooltip)
        self.customResponsePrefixCheck.setText(QCoreApplication.translate("MainWindow", u"Response prefix:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Chat", None))
#if QT_CONFIG(tooltip)
        self.awesomePresetComboBox.setToolTip(QCoreApplication.translate("MainWindow", u"Select a preset prompt", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.instructPresetComboBox.setToolTip(QCoreApplication.translate("MainWindow", u"Select instruct format", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Awesome prompts:", None))
#if QT_CONFIG(tooltip)
        self.instructRadioButton.setToolTip(QCoreApplication.translate("MainWindow", u"Use instruct mode (from presets/instruct folder)", None))
#endif // QT_CONFIG(tooltip)
        self.instructRadioButton.setText(QCoreApplication.translate("MainWindow", u"Instruct:", None))
#if QT_CONFIG(tooltip)
        self.charactersRadioButton.setToolTip(QCoreApplication.translate("MainWindow", u"Use character/chat mode (from presets/characters folder)", None))
#endif // QT_CONFIG(tooltip)
        self.charactersRadioButton.setText(QCoreApplication.translate("MainWindow", u"Characters:", None))
#if QT_CONFIG(tooltip)
        self.characterPresetComboBox.setToolTip(QCoreApplication.translate("MainWindow", u"Select a character", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.logChatCheck.setToolTip(QCoreApplication.translate("MainWindow", u"Write chat logs to file", None))
#endif // QT_CONFIG(tooltip)
        self.logChatCheck.setText(QCoreApplication.translate("MainWindow", u"Log chats", None))
#if QT_CONFIG(tooltip)
        self.sendStopStringCheck.setToolTip(QCoreApplication.translate("MainWindow", u"Send chat user stop string when generating", None))
#endif // QT_CONFIG(tooltip)
        self.sendStopStringCheck.setText(QCoreApplication.translate("MainWindow", u"Send chat stop string", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Chat", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Themes", None))
#if QT_CONFIG(tooltip)
        self.themeDarkCheck.setToolTip(QCoreApplication.translate("MainWindow", u"Use a dark theme", None))
#endif // QT_CONFIG(tooltip)
        self.themeDarkCheck.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
#if QT_CONFIG(tooltip)
        self.themeLightCheck.setToolTip(QCoreApplication.translate("MainWindow", u"Use a light theme", None))
#endif // QT_CONFIG(tooltip)
        self.themeLightCheck.setText(QCoreApplication.translate("MainWindow", u"Light", None))
#if QT_CONFIG(tooltip)
        self.themeNativeCheck.setToolTip(QCoreApplication.translate("MainWindow", u"Use OS native theme", None))
#endif // QT_CONFIG(tooltip)
        self.themeNativeCheck.setText(QCoreApplication.translate("MainWindow", u"Native", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Misc", None))
#if QT_CONFIG(tooltip)
        self.settingsPathSaveButton.setToolTip(QCoreApplication.translate("MainWindow", u"Save settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsPathSaveButton.setText(QCoreApplication.translate("MainWindow", u"Save settings", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.preferencesTab), QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuMode.setTitle(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

