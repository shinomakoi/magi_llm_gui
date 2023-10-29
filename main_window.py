# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSplitter, QStatusBar, QTabWidget, QTextEdit,
    QToolBox, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1523, 999)
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
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.frame_2 = QFrame(self.splitter)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QSize(340, 16777215))
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.settingsPathSaveButton = QPushButton(self.frame_2)
        self.settingsPathSaveButton.setObjectName(u"settingsPathSaveButton")

        self.gridLayout_2.addWidget(self.settingsPathSaveButton, 1, 0, 1, 1)

        self.mode_tab = QToolBox(self.frame_2)
        self.mode_tab.setObjectName(u"mode_tab")
        self.instructTab = QWidget()
        self.instructTab.setObjectName(u"instructTab")
        self.instructTab.setGeometry(QRect(0, 0, 322, 730))
        self.verticalLayout_2 = QVBoxLayout(self.instructTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.instructTab)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.instructPresetComboBox = QComboBox(self.instructTab)
        self.instructPresetComboBox.setObjectName(u"instructPresetComboBox")

        self.verticalLayout_2.addWidget(self.instructPresetComboBox)

        self.line = QFrame(self.instructTab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.label_41 = QLabel(self.instructTab)
        self.label_41.setObjectName(u"label_41")

        self.verticalLayout_2.addWidget(self.label_41)

        self.yourNameLine = QLineEdit(self.instructTab)
        self.yourNameLine.setObjectName(u"yourNameLine")

        self.verticalLayout_2.addWidget(self.yourNameLine)

        self.label_42 = QLabel(self.instructTab)
        self.label_42.setObjectName(u"label_42")

        self.verticalLayout_2.addWidget(self.label_42)

        self.botNameLine = QLineEdit(self.instructTab)
        self.botNameLine.setObjectName(u"botNameLine")

        self.verticalLayout_2.addWidget(self.botNameLine)

        self.line_2 = QFrame(self.instructTab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.customResponsePrefixCheck = QCheckBox(self.instructTab)
        self.customResponsePrefixCheck.setObjectName(u"customResponsePrefixCheck")

        self.verticalLayout_2.addWidget(self.customResponsePrefixCheck)

        self.customResponsePrefix = QLineEdit(self.instructTab)
        self.customResponsePrefix.setObjectName(u"customResponsePrefix")

        self.verticalLayout_2.addWidget(self.customResponsePrefix)

        self.line_3 = QFrame(self.instructTab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.label_3 = QLabel(self.instructTab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.awesomePresetComboBox = QComboBox(self.instructTab)
        self.awesomePresetComboBox.setObjectName(u"awesomePresetComboBox")

        self.verticalLayout_2.addWidget(self.awesomePresetComboBox)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_11)

        self.mode_tab.addItem(self.instructTab, u"Instruct")
        self.characterTab = QWidget()
        self.characterTab.setObjectName(u"characterTab")
        self.characterTab.setGeometry(QRect(0, 0, 322, 730))
        self.verticalLayout = QVBoxLayout(self.characterTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.characterTab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.characterPresetComboBox = QComboBox(self.characterTab)
        self.characterPresetComboBox.setObjectName(u"characterPresetComboBox")

        self.verticalLayout.addWidget(self.characterPresetComboBox)

        self.label_43 = QLabel(self.characterTab)
        self.label_43.setObjectName(u"label_43")

        self.verticalLayout.addWidget(self.label_43)

        self.yourNameLineChar = QLineEdit(self.characterTab)
        self.yourNameLineChar.setObjectName(u"yourNameLineChar")

        self.verticalLayout.addWidget(self.yourNameLineChar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.mode_tab.addItem(self.characterTab, u"Character")
        self.standardTab = QWidget()
        self.standardTab.setObjectName(u"standardTab")
        self.standardTab.setGeometry(QRect(0, 0, 322, 730))
        self.mode_tab.addItem(self.standardTab, u"Standard")
        self.notebookTab = QWidget()
        self.notebookTab.setObjectName(u"notebookTab")
        self.notebookTab.setGeometry(QRect(0, 0, 322, 730))
        self.mode_tab.addItem(self.notebookTab, u"Notebook")

        self.gridLayout_2.addWidget(self.mode_tab, 0, 0, 1, 1)

        self.splitter.addWidget(self.frame_2)
        self.tabWidget = QTabWidget(self.splitter)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.gridLayout = QGridLayout(self.tabWidgetPage1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stopButton = QPushButton(self.tabWidgetPage1)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setEnabled(False)
        self.stopButton.setMinimumSize(QSize(64, 64))
        self.stopButton.setMaximumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.stopButton, 2, 6, 1, 1)

        self.chatOutputSession = QComboBox(self.tabWidgetPage1)
        self.chatOutputSession.addItem("")
        self.chatOutputSession.setObjectName(u"chatOutputSession")

        self.gridLayout.addWidget(self.chatOutputSession, 1, 1, 1, 6)

        self.generateButton = QPushButton(self.tabWidgetPage1)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setEnabled(False)
        self.generateButton.setMinimumSize(QSize(64, 64))
        self.generateButton.setMaximumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.generateButton, 2, 1, 1, 1)

        self.clearButton = QPushButton(self.tabWidgetPage1)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setEnabled(True)
        self.clearButton.setMinimumSize(QSize(64, 64))
        self.clearButton.setMaximumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.clearButton, 2, 5, 1, 1)

        self.chatInputHistoryCombo = QComboBox(self.tabWidgetPage1)
        self.chatInputHistoryCombo.setObjectName(u"chatInputHistoryCombo")

        self.gridLayout.addWidget(self.chatInputHistoryCombo, 1, 0, 1, 1)

        self.retryButton = QPushButton(self.tabWidgetPage1)
        self.retryButton.setObjectName(u"retryButton")
        self.retryButton.setEnabled(False)
        self.retryButton.setMinimumSize(QSize(64, 64))
        self.retryButton.setMaximumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.retryButton, 2, 2, 1, 1)

        self.inputText = QPlainTextEdit(self.tabWidgetPage1)
        self.inputText.setObjectName(u"inputText")
        self.inputText.setMaximumSize(QSize(16777215, 100))

        self.gridLayout.addWidget(self.inputText, 2, 0, 1, 1)

        self.outputText = QTextEdit(self.tabWidgetPage1)
        self.outputText.setObjectName(u"outputText")
        self.outputText.setReadOnly(True)

        self.gridLayout.addWidget(self.outputText, 0, 0, 1, 7)

        self.rewindButton = QPushButton(self.tabWidgetPage1)
        self.rewindButton.setObjectName(u"rewindButton")
        self.rewindButton.setEnabled(False)
        self.rewindButton.setMinimumSize(QSize(64, 64))
        self.rewindButton.setMaximumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.rewindButton, 2, 3, 1, 1)

        self.continueButton = QPushButton(self.tabWidgetPage1)
        self.continueButton.setObjectName(u"continueButton")
        self.continueButton.setEnabled(False)
        self.continueButton.setMinimumSize(QSize(64, 64))
        self.continueButton.setMaximumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.continueButton, 2, 4, 1, 1)

        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_7 = QGridLayout(self.tab)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.cppCheck = QRadioButton(self.groupBox)
        self.cppCheck.setObjectName(u"cppCheck")
        self.cppCheck.setChecked(True)

        self.gridLayout_4.addWidget(self.cppCheck, 0, 0, 1, 1)

        self.exllamaModelPath = QLineEdit(self.groupBox)
        self.exllamaModelPath.setObjectName(u"exllamaModelPath")

        self.gridLayout_4.addWidget(self.exllamaModelPath, 10, 0, 1, 1)

        self.loadModelButton = QPushButton(self.groupBox)
        self.loadModelButton.setObjectName(u"loadModelButton")

        self.gridLayout_4.addWidget(self.loadModelButton, 3, 0, 1, 1)

        self.streamEnabledCheck = QCheckBox(self.groupBox)
        self.streamEnabledCheck.setObjectName(u"streamEnabledCheck")
        self.streamEnabledCheck.setChecked(True)

        self.gridLayout_4.addWidget(self.streamEnabledCheck, 6, 0, 1, 1)

        self.label_29 = QLabel(self.groupBox)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_4.addWidget(self.label_29, 7, 0, 1, 1)

        self.cppModelPath = QLineEdit(self.groupBox)
        self.cppModelPath.setObjectName(u"cppModelPath")

        self.gridLayout_4.addWidget(self.cppModelPath, 8, 0, 1, 1)

        self.label_40 = QLabel(self.groupBox)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_4.addWidget(self.label_40, 9, 0, 1, 1)

        self.exllamaCheck = QRadioButton(self.groupBox)
        self.exllamaCheck.setObjectName(u"exllamaCheck")

        self.gridLayout_4.addWidget(self.exllamaCheck, 2, 0, 1, 1)

        self.cppModelSelect = QToolButton(self.groupBox)
        self.cppModelSelect.setObjectName(u"cppModelSelect")

        self.gridLayout_4.addWidget(self.cppModelSelect, 8, 1, 1, 1)

        self.cppServerCheck = QRadioButton(self.groupBox)
        self.cppServerCheck.setObjectName(u"cppServerCheck")

        self.gridLayout_4.addWidget(self.cppServerCheck, 1, 0, 1, 1)

        self.exllamaModelSelect = QToolButton(self.groupBox)
        self.exllamaModelSelect.setObjectName(u"exllamaModelSelect")

        self.gridLayout_4.addWidget(self.exllamaModelSelect, 10, 1, 1, 1)

        self.unloadModelButton = QPushButton(self.groupBox)
        self.unloadModelButton.setObjectName(u"unloadModelButton")
        self.unloadModelButton.setEnabled(False)

        self.gridLayout_4.addWidget(self.unloadModelButton, 4, 0, 1, 1)

        self.backendAutoLaunch = QCheckBox(self.groupBox)
        self.backendAutoLaunch.setObjectName(u"backendAutoLaunch")

        self.gridLayout_4.addWidget(self.backendAutoLaunch, 5, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.themeDarkCheck = QRadioButton(self.groupBox_2)
        self.themeDarkCheck.setObjectName(u"themeDarkCheck")
        self.themeDarkCheck.setChecked(True)

        self.gridLayout_5.addWidget(self.themeDarkCheck, 0, 0, 1, 1)

        self.themeLightCheck = QRadioButton(self.groupBox_2)
        self.themeLightCheck.setObjectName(u"themeLightCheck")

        self.gridLayout_5.addWidget(self.themeLightCheck, 1, 0, 1, 1)

        self.themeNativeCheck = QRadioButton(self.groupBox_2)
        self.themeNativeCheck.setObjectName(u"themeNativeCheck")

        self.gridLayout_5.addWidget(self.themeNativeCheck, 2, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.custSystemText = QPlainTextEdit(self.groupBox_3)
        self.custSystemText.setObjectName(u"custSystemText")

        self.gridLayout_3.addWidget(self.custSystemText, 3, 0, 1, 1)

        self.sendStopStringCheck = QCheckBox(self.groupBox_3)
        self.sendStopStringCheck.setObjectName(u"sendStopStringCheck")
        self.sendStopStringCheck.setChecked(True)

        self.gridLayout_3.addWidget(self.sendStopStringCheck, 1, 0, 1, 1)

        self.custSystemCheck = QCheckBox(self.groupBox_3)
        self.custSystemCheck.setObjectName(u"custSystemCheck")

        self.gridLayout_3.addWidget(self.custSystemCheck, 2, 0, 1, 1)

        self.logChatCheck = QCheckBox(self.groupBox_3)
        self.logChatCheck.setObjectName(u"logChatCheck")

        self.gridLayout_3.addWidget(self.logChatCheck, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_3, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.splitter.addWidget(self.tabWidget)

        self.gridLayout_6.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1523, 27))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuSettings.addAction(self.actionPreferences)

        self.retranslateUi(MainWindow)

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
        self.settingsPathSaveButton.setText(QCoreApplication.translate("MainWindow", u"Save settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Instruct preset:", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"User name:", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Bot name:", None))
        self.customResponsePrefixCheck.setText(QCoreApplication.translate("MainWindow", u"Response prefix:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Awesome prompts:", None))
        self.mode_tab.setItemText(self.mode_tab.indexOf(self.instructTab), QCoreApplication.translate("MainWindow", u"Instruct", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Character:", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Your name:", None))
        self.mode_tab.setItemText(self.mode_tab.indexOf(self.characterTab), QCoreApplication.translate("MainWindow", u"Character", None))
        self.mode_tab.setItemText(self.mode_tab.indexOf(self.standardTab), QCoreApplication.translate("MainWindow", u"Standard", None))
        self.mode_tab.setItemText(self.mode_tab.indexOf(self.notebookTab), QCoreApplication.translate("MainWindow", u"Notebook", None))
#if QT_CONFIG(tooltip)
        self.stopButton.setToolTip(QCoreApplication.translate("MainWindow", u"Stop generation", None))
#endif // QT_CONFIG(tooltip)
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"St", None))
        self.chatOutputSession.setItemText(0, QCoreApplication.translate("MainWindow", u"Current", None))

#if QT_CONFIG(tooltip)
        self.chatOutputSession.setToolTip(QCoreApplication.translate("MainWindow", u"Saved chat sessions", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.generateButton.setToolTip(QCoreApplication.translate("MainWindow", u"Send (CTRL+Enter)", None))
#endif // QT_CONFIG(tooltip)
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Gen", None))
#if QT_CONFIG(shortcut)
        self.generateButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.clearButton.setToolTip(QCoreApplication.translate("MainWindow", u"Clear the output history", None))
#endif // QT_CONFIG(tooltip)
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"Clr", None))
#if QT_CONFIG(tooltip)
        self.chatInputHistoryCombo.setToolTip(QCoreApplication.translate("MainWindow", u"Saved chat inputs from session", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.retryButton.setToolTip(QCoreApplication.translate("MainWindow", u"Retry", None))
#endif // QT_CONFIG(tooltip)
        self.retryButton.setText(QCoreApplication.translate("MainWindow", u"Ret", None))
        self.inputText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type something here", None))
        self.outputText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans Display'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.outputText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Output goes here", None))
#if QT_CONFIG(tooltip)
        self.rewindButton.setToolTip(QCoreApplication.translate("MainWindow", u"Continue the last generation", None))
#endif // QT_CONFIG(tooltip)
        self.rewindButton.setText(QCoreApplication.translate("MainWindow", u"Rw", None))
#if QT_CONFIG(tooltip)
        self.continueButton.setToolTip(QCoreApplication.translate("MainWindow", u"Rewinds the chat 1 turn", None))
#endif // QT_CONFIG(tooltip)
        self.continueButton.setText(QCoreApplication.translate("MainWindow", u"Con", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QCoreApplication.translate("MainWindow", u"Main", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Backend", None))
        self.cppCheck.setText(QCoreApplication.translate("MainWindow", u"llama-cpp-python", None))
        self.loadModelButton.setText(QCoreApplication.translate("MainWindow", u"Load backend", None))
        self.streamEnabledCheck.setText(QCoreApplication.translate("MainWindow", u"Stream responses", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"llama.cpp: Model path:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Exllama: Model directory:", None))
        self.exllamaCheck.setText(QCoreApplication.translate("MainWindow", u"Exllama", None))
        self.cppModelSelect.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.cppServerCheck.setText(QCoreApplication.translate("MainWindow", u"llama.cpp server", None))
        self.exllamaModelSelect.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.unloadModelButton.setText(QCoreApplication.translate("MainWindow", u"Unload backend", None))
        self.backendAutoLaunch.setText(QCoreApplication.translate("MainWindow", u"Auto load backend at launch", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Themes", None))
        self.themeDarkCheck.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.themeLightCheck.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.themeNativeCheck.setText(QCoreApplication.translate("MainWindow", u"Native", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Chat", None))
        self.sendStopStringCheck.setText(QCoreApplication.translate("MainWindow", u"Send chat stop string", None))
        self.custSystemCheck.setText(QCoreApplication.translate("MainWindow", u"Custom system prompt:", None))
        self.logChatCheck.setText(QCoreApplication.translate("MainWindow", u"Log chats", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

