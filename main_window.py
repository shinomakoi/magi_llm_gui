# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
    QGridLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSplitter,
    QStatusBar, QTextEdit, QToolBox, QToolButton,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1518, 1014)
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
        self.frame_2.setMaximumSize(QSize(290, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.toolBox_2 = QToolBox(self.frame_2)
        self.toolBox_2.setObjectName(u"toolBox_2")
        self.toolBox_2.setAutoFillBackground(False)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.page_13.setGeometry(QRect(0, 0, 270, 743))
        self.gridLayout_5 = QGridLayout(self.page_13)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_9, 9, 0, 1, 2)

        self.unloadModelButton = QPushButton(self.page_13)
        self.unloadModelButton.setObjectName(u"unloadModelButton")

        self.gridLayout_5.addWidget(self.unloadModelButton, 5, 0, 1, 1)

        self.streamEnabledCheck = QCheckBox(self.page_13)
        self.streamEnabledCheck.setObjectName(u"streamEnabledCheck")
        self.streamEnabledCheck.setChecked(True)

        self.gridLayout_5.addWidget(self.streamEnabledCheck, 8, 0, 1, 1)

        self.exllamaCheck = QRadioButton(self.page_13)
        self.exllamaCheck.setObjectName(u"exllamaCheck")

        self.gridLayout_5.addWidget(self.exllamaCheck, 2, 0, 1, 1)

        self.backendAutoLaunch = QCheckBox(self.page_13)
        self.backendAutoLaunch.setObjectName(u"backendAutoLaunch")

        self.gridLayout_5.addWidget(self.backendAutoLaunch, 7, 0, 1, 1)

        self.cppServerCheck = QRadioButton(self.page_13)
        self.cppServerCheck.setObjectName(u"cppServerCheck")

        self.gridLayout_5.addWidget(self.cppServerCheck, 1, 0, 1, 1)

        self.loadModelButton = QPushButton(self.page_13)
        self.loadModelButton.setObjectName(u"loadModelButton")

        self.gridLayout_5.addWidget(self.loadModelButton, 4, 0, 1, 1)

        self.line_5 = QFrame(self.page_13)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_5, 6, 0, 1, 1)

        self.cppCheck = QRadioButton(self.page_13)
        self.cppCheck.setObjectName(u"cppCheck")
        self.cppCheck.setChecked(True)

        self.gridLayout_5.addWidget(self.cppCheck, 0, 0, 1, 1)

        self.line = QFrame(self.page_13)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line, 3, 0, 1, 1)

        self.toolBox_2.addItem(self.page_13, u"Backend")
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.page_14.setGeometry(QRect(0, 0, 270, 743))
        self.gridLayout_44 = QGridLayout(self.page_14)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_44.addItem(self.verticalSpacer_10, 7, 0, 1, 1)

        self.exllamaModelPath = QLineEdit(self.page_14)
        self.exllamaModelPath.setObjectName(u"exllamaModelPath")

        self.gridLayout_44.addWidget(self.exllamaModelPath, 5, 0, 1, 1)

        self.cppModelPath = QLineEdit(self.page_14)
        self.cppModelPath.setObjectName(u"cppModelPath")

        self.gridLayout_44.addWidget(self.cppModelPath, 2, 0, 1, 1)

        self.label_29 = QLabel(self.page_14)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_44.addWidget(self.label_29, 1, 0, 1, 1)

        self.label_40 = QLabel(self.page_14)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_44.addWidget(self.label_40, 4, 0, 1, 1)

        self.cppModelSelect = QToolButton(self.page_14)
        self.cppModelSelect.setObjectName(u"cppModelSelect")

        self.gridLayout_44.addWidget(self.cppModelSelect, 2, 1, 1, 1)

        self.exllamaModelSelect = QToolButton(self.page_14)
        self.exllamaModelSelect.setObjectName(u"exllamaModelSelect")

        self.gridLayout_44.addWidget(self.exllamaModelSelect, 5, 1, 1, 1)

        self.toolBox_2.addItem(self.page_14, u"Paths")
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.page_15.setGeometry(QRect(0, 0, 270, 743))
        self.gridLayout_45 = QGridLayout(self.page_15)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.label_3 = QLabel(self.page_15)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_45.addWidget(self.label_3, 6, 0, 1, 1)

        self.label_41 = QLabel(self.page_15)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_45.addWidget(self.label_41, 13, 0, 1, 1)

        self.charactersRadioButton = QRadioButton(self.page_15)
        self.charactersRadioButton.setObjectName(u"charactersRadioButton")

        self.gridLayout_45.addWidget(self.charactersRadioButton, 4, 0, 1, 1)

        self.customResponsePrefix = QLineEdit(self.page_15)
        self.customResponsePrefix.setObjectName(u"customResponsePrefix")

        self.gridLayout_45.addWidget(self.customResponsePrefix, 19, 0, 1, 1)

        self.logChatCheck = QCheckBox(self.page_15)
        self.logChatCheck.setObjectName(u"logChatCheck")

        self.gridLayout_45.addWidget(self.logChatCheck, 9, 0, 1, 1)

        self.awesomePresetComboBox = QComboBox(self.page_15)
        self.awesomePresetComboBox.setObjectName(u"awesomePresetComboBox")

        self.gridLayout_45.addWidget(self.awesomePresetComboBox, 7, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_45.addItem(self.verticalSpacer_11, 20, 0, 1, 1)

        self.botNameLine = QLineEdit(self.page_15)
        self.botNameLine.setObjectName(u"botNameLine")

        self.gridLayout_45.addWidget(self.botNameLine, 16, 0, 1, 1)

        self.sendStopStringCheck = QCheckBox(self.page_15)
        self.sendStopStringCheck.setObjectName(u"sendStopStringCheck")
        self.sendStopStringCheck.setChecked(True)

        self.gridLayout_45.addWidget(self.sendStopStringCheck, 10, 0, 1, 1)

        self.customResponsePrefixCheck = QCheckBox(self.page_15)
        self.customResponsePrefixCheck.setObjectName(u"customResponsePrefixCheck")

        self.gridLayout_45.addWidget(self.customResponsePrefixCheck, 18, 0, 1, 1)

        self.yourNameLine = QLineEdit(self.page_15)
        self.yourNameLine.setObjectName(u"yourNameLine")

        self.gridLayout_45.addWidget(self.yourNameLine, 14, 0, 1, 1)

        self.instructRadioButton = QRadioButton(self.page_15)
        self.instructRadioButton.setObjectName(u"instructRadioButton")
        self.instructRadioButton.setChecked(True)

        self.gridLayout_45.addWidget(self.instructRadioButton, 0, 0, 1, 1)

        self.line_3 = QFrame(self.page_15)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_45.addWidget(self.line_3, 8, 0, 1, 1)

        self.line_6 = QFrame(self.page_15)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_45.addWidget(self.line_6, 11, 0, 1, 1)

        self.instructPresetComboBox = QComboBox(self.page_15)
        self.instructPresetComboBox.setObjectName(u"instructPresetComboBox")

        self.gridLayout_45.addWidget(self.instructPresetComboBox, 1, 0, 1, 1)

        self.characterPresetComboBox = QComboBox(self.page_15)
        self.characterPresetComboBox.setObjectName(u"characterPresetComboBox")

        self.gridLayout_45.addWidget(self.characterPresetComboBox, 5, 0, 1, 1)

        self.label_42 = QLabel(self.page_15)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_45.addWidget(self.label_42, 15, 0, 1, 1)

        self.line_2 = QFrame(self.page_15)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_45.addWidget(self.line_2, 17, 0, 1, 1)

        self.toolBox_2.addItem(self.page_15, u"Chat")
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.page_16.setGeometry(QRect(0, 0, 270, 743))
        self.gridLayout_46 = QGridLayout(self.page_16)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.verticalSpacer_12 = QSpacerItem(20, 725, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_46.addItem(self.verticalSpacer_12, 3, 0, 1, 1)

        self.themeDarkCheck = QRadioButton(self.page_16)
        self.themeDarkCheck.setObjectName(u"themeDarkCheck")
        self.themeDarkCheck.setChecked(True)

        self.gridLayout_46.addWidget(self.themeDarkCheck, 0, 0, 1, 1)

        self.themeLightCheck = QRadioButton(self.page_16)
        self.themeLightCheck.setObjectName(u"themeLightCheck")

        self.gridLayout_46.addWidget(self.themeLightCheck, 1, 0, 1, 1)

        self.themeNativeCheck = QRadioButton(self.page_16)
        self.themeNativeCheck.setObjectName(u"themeNativeCheck")

        self.gridLayout_46.addWidget(self.themeNativeCheck, 2, 0, 1, 1)

        self.toolBox_2.addItem(self.page_16, u"Themes")

        self.gridLayout_2.addWidget(self.toolBox_2, 0, 0, 1, 1)

        self.settingsPathSaveButton = QPushButton(self.frame_2)
        self.settingsPathSaveButton.setObjectName(u"settingsPathSaveButton")

        self.gridLayout_2.addWidget(self.settingsPathSaveButton, 1, 0, 1, 1)

        self.splitter.addWidget(self.frame_2)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.continueButton = QPushButton(self.frame)
        self.continueButton.setObjectName(u"continueButton")
        self.continueButton.setEnabled(False)
        self.continueButton.setMinimumSize(QSize(64, 64))
        self.continueButton.setMaximumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.continueButton, 2, 2, 1, 1)

        self.stopButton = QPushButton(self.frame)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setEnabled(False)
        self.stopButton.setMinimumSize(QSize(64, 64))
        self.stopButton.setMaximumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.stopButton, 2, 5, 1, 1)

        self.inputText = QPlainTextEdit(self.frame)
        self.inputText.setObjectName(u"inputText")
        self.inputText.setMaximumSize(QSize(16777215, 90))

        self.gridLayout.addWidget(self.inputText, 2, 0, 1, 1)

        self.generateButton = QPushButton(self.frame)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setEnabled(False)
        self.generateButton.setMinimumSize(QSize(64, 64))
        self.generateButton.setMaximumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.generateButton, 2, 1, 1, 1)

        self.outputText = QTextEdit(self.frame)
        self.outputText.setObjectName(u"outputText")
        self.outputText.setReadOnly(True)

        self.gridLayout.addWidget(self.outputText, 0, 0, 1, 6)

        self.rewindButton = QPushButton(self.frame)
        self.rewindButton.setObjectName(u"rewindButton")
        self.rewindButton.setEnabled(False)
        self.rewindButton.setMinimumSize(QSize(64, 64))
        self.rewindButton.setMaximumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.rewindButton, 2, 3, 1, 1)

        self.clearButton = QPushButton(self.frame)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setEnabled(True)
        self.clearButton.setMinimumSize(QSize(64, 64))
        self.clearButton.setMaximumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.clearButton, 2, 4, 1, 1)

        self.chatInputHistoryCombo = QComboBox(self.frame)
        self.chatInputHistoryCombo.setObjectName(u"chatInputHistoryCombo")

        self.gridLayout.addWidget(self.chatInputHistoryCombo, 1, 0, 1, 1)

        self.chatOutputSession = QComboBox(self.frame)
        self.chatOutputSession.addItem("")
        self.chatOutputSession.setObjectName(u"chatOutputSession")

        self.gridLayout.addWidget(self.chatOutputSession, 1, 1, 1, 5)

        self.splitter.addWidget(self.frame)

        self.gridLayout_6.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1518, 27))
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

        self.toolBox_2.setCurrentIndex(0)


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
        self.unloadModelButton.setText(QCoreApplication.translate("MainWindow", u"Unload backend", None))
        self.streamEnabledCheck.setText(QCoreApplication.translate("MainWindow", u"Stream responses", None))
        self.exllamaCheck.setText(QCoreApplication.translate("MainWindow", u"Exllama", None))
        self.backendAutoLaunch.setText(QCoreApplication.translate("MainWindow", u"Auto load backend at launch", None))
        self.cppServerCheck.setText(QCoreApplication.translate("MainWindow", u"llama.cpp server", None))
        self.loadModelButton.setText(QCoreApplication.translate("MainWindow", u"Load backend", None))
        self.cppCheck.setText(QCoreApplication.translate("MainWindow", u"llama-cpp-python", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_13), QCoreApplication.translate("MainWindow", u"Backend", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"llama.cpp: Model path:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Exllama: Model directory:", None))
        self.cppModelSelect.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.exllamaModelSelect.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_14), QCoreApplication.translate("MainWindow", u"Paths", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Awesome prompts:", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"User name:", None))
        self.charactersRadioButton.setText(QCoreApplication.translate("MainWindow", u"Characters:", None))
        self.logChatCheck.setText(QCoreApplication.translate("MainWindow", u"Log chats", None))
        self.sendStopStringCheck.setText(QCoreApplication.translate("MainWindow", u"Send chat stop string", None))
        self.customResponsePrefixCheck.setText(QCoreApplication.translate("MainWindow", u"Response prefix:", None))
        self.instructRadioButton.setText(QCoreApplication.translate("MainWindow", u"Instruct:", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Bot name:", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_15), QCoreApplication.translate("MainWindow", u"Chat", None))
        self.themeDarkCheck.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.themeLightCheck.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.themeNativeCheck.setText(QCoreApplication.translate("MainWindow", u"Native", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_16), QCoreApplication.translate("MainWindow", u"Themes", None))
        self.settingsPathSaveButton.setText(QCoreApplication.translate("MainWindow", u"Save settings", None))
#if QT_CONFIG(tooltip)
        self.continueButton.setToolTip(QCoreApplication.translate("MainWindow", u"Continue the last generation", None))
#endif // QT_CONFIG(tooltip)
        self.continueButton.setText(QCoreApplication.translate("MainWindow", u"Con", None))
#if QT_CONFIG(tooltip)
        self.stopButton.setToolTip(QCoreApplication.translate("MainWindow", u"Stop generation", None))
#endif // QT_CONFIG(tooltip)
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"St", None))
        self.inputText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type something here", None))
#if QT_CONFIG(tooltip)
        self.generateButton.setToolTip(QCoreApplication.translate("MainWindow", u"Send (CTRL+Enter)", None))
#endif // QT_CONFIG(tooltip)
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Gen", None))
#if QT_CONFIG(shortcut)
        self.generateButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
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
        self.rewindButton.setToolTip(QCoreApplication.translate("MainWindow", u"Rewinds the chat 1 turn", None))
#endif // QT_CONFIG(tooltip)
        self.rewindButton.setText(QCoreApplication.translate("MainWindow", u"Rw", None))
#if QT_CONFIG(tooltip)
        self.clearButton.setToolTip(QCoreApplication.translate("MainWindow", u"Clear the output history", None))
#endif // QT_CONFIG(tooltip)
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"Clr", None))
#if QT_CONFIG(tooltip)
        self.chatInputHistoryCombo.setToolTip(QCoreApplication.translate("MainWindow", u"Saved chat inputs from session", None))
#endif // QT_CONFIG(tooltip)
        self.chatOutputSession.setItemText(0, QCoreApplication.translate("MainWindow", u"Current", None))

#if QT_CONFIG(tooltip)
        self.chatOutputSession.setToolTip(QCoreApplication.translate("MainWindow", u"Saved chat sessions", None))
#endif // QT_CONFIG(tooltip)
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuMode.setTitle(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

