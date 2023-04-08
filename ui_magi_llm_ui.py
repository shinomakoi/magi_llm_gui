# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'magi_llm_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
    QSizePolicy, QStatusBar, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_magi_llm_window(object):
    def setupUi(self, magi_llm_window):
        if not magi_llm_window.objectName():
            magi_llm_window.setObjectName(u"magi_llm_window")
        magi_llm_window.resize(892, 955)
        self.actionSettings = QAction(magi_llm_window)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionExit = QAction(magi_llm_window)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(magi_llm_window)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(magi_llm_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textgenTab = QTabWidget(self.centralwidget)
        self.textgenTab.setObjectName(u"textgenTab")
        self.textgenTab.setAutoFillBackground(False)
        self.default_textgenTab = QWidget()
        self.default_textgenTab.setObjectName(u"default_textgenTab")
        self.default_textgenTab.setAutoFillBackground(True)
        self.gridLayout_6 = QGridLayout(self.default_textgenTab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.defaultClearButton = QPushButton(self.default_textgenTab)
        self.defaultClearButton.setObjectName(u"defaultClearButton")

        self.gridLayout_6.addWidget(self.defaultClearButton, 2, 1, 1, 1)

        self.defaultTextHistory = QPlainTextEdit(self.default_textgenTab)
        self.defaultTextHistory.setObjectName(u"defaultTextHistory")
        self.defaultTextHistory.setStyleSheet(u"")
        self.defaultTextHistory.setReadOnly(True)

        self.gridLayout_6.addWidget(self.defaultTextHistory, 0, 0, 1, 2)

        self.defaultGenerateButton = QPushButton(self.default_textgenTab)
        self.defaultGenerateButton.setObjectName(u"defaultGenerateButton")

        self.gridLayout_6.addWidget(self.defaultGenerateButton, 2, 0, 1, 1)

        self.defaultTextInput = QPlainTextEdit(self.default_textgenTab)
        self.defaultTextInput.setObjectName(u"defaultTextInput")
        self.defaultTextInput.setStyleSheet(u"")
        self.defaultTextInput.setReadOnly(False)

        self.gridLayout_6.addWidget(self.defaultTextInput, 1, 0, 1, 2)

        self.textgenTab.addTab(self.default_textgenTab, "")
        self.notebook_textgenTab = QWidget()
        self.notebook_textgenTab.setObjectName(u"notebook_textgenTab")
        self.notebook_textgenTab.setAutoFillBackground(True)
        self.gridLayout_2 = QGridLayout(self.notebook_textgenTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.notebookGenerateButton = QPushButton(self.notebook_textgenTab)
        self.notebookGenerateButton.setObjectName(u"notebookGenerateButton")

        self.gridLayout_2.addWidget(self.notebookGenerateButton, 1, 0, 1, 1)

        self.notebookClearButton = QPushButton(self.notebook_textgenTab)
        self.notebookClearButton.setObjectName(u"notebookClearButton")

        self.gridLayout_2.addWidget(self.notebookClearButton, 1, 1, 1, 1)

        self.notebookHistory = QPlainTextEdit(self.notebook_textgenTab)
        self.notebookHistory.setObjectName(u"notebookHistory")
        self.notebookHistory.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.notebookHistory, 0, 0, 1, 2)

        self.textgenTab.addTab(self.notebook_textgenTab, "")
        self.chat_textgenTab = QWidget()
        self.chat_textgenTab.setObjectName(u"chat_textgenTab")
        self.chat_textgenTab.setAutoFillBackground(True)
        self.gridLayout_3 = QGridLayout(self.chat_textgenTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.chat_textgenTab)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.chatHistory = QTextEdit(self.chat_textgenTab)
        self.chatHistory.setObjectName(u"chatHistory")
        self.chatHistory.setStyleSheet(u"")
        self.chatHistory.setReadOnly(False)

        self.gridLayout_3.addWidget(self.chatHistory, 2, 0, 1, 2)

        self.chatInput = QPlainTextEdit(self.chat_textgenTab)
        self.chatInput.setObjectName(u"chatInput")
        self.chatInput.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.chatInput, 3, 0, 1, 2)

        self.chatGenerateButton = QPushButton(self.chat_textgenTab)
        self.chatGenerateButton.setObjectName(u"chatGenerateButton")

        self.gridLayout_3.addWidget(self.chatGenerateButton, 4, 0, 1, 1)

        self.chatClearButton = QPushButton(self.chat_textgenTab)
        self.chatClearButton.setObjectName(u"chatClearButton")

        self.gridLayout_3.addWidget(self.chatClearButton, 4, 1, 1, 1)

        self.chatPresetComboBox = QComboBox(self.chat_textgenTab)
        self.chatPresetComboBox.addItem("")
        self.chatPresetComboBox.addItem("")
        self.chatPresetComboBox.addItem("")
        self.chatPresetComboBox.addItem("")
        self.chatPresetComboBox.addItem("")
        self.chatPresetComboBox.setObjectName(u"chatPresetComboBox")

        self.gridLayout_3.addWidget(self.chatPresetComboBox, 1, 0, 1, 2)

        self.textgenTab.addTab(self.chat_textgenTab, "")
        self.settingsTab = QWidget()
        self.settingsTab.setObjectName(u"settingsTab")
        self.gridLayout_4 = QGridLayout(self.settingsTab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.settingsTab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.customChatBotPrefix = QLineEdit(self.groupBox)
        self.customChatBotPrefix.setObjectName(u"customChatBotPrefix")

        self.verticalLayout_2.addWidget(self.customChatBotPrefix)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.customChatUserPrefix = QLineEdit(self.groupBox)
        self.customChatUserPrefix.setObjectName(u"customChatUserPrefix")

        self.verticalLayout_2.addWidget(self.customChatUserPrefix)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.settingsTab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.streamEnabledCheck = QCheckBox(self.groupBox_2)
        self.streamEnabledCheck.setObjectName(u"streamEnabledCheck")
        self.streamEnabledCheck.setChecked(False)

        self.gridLayout_5.addWidget(self.streamEnabledCheck, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.textgenTab.addTab(self.settingsTab, "")

        self.gridLayout.addWidget(self.textgenTab, 0, 0, 1, 2)

        magi_llm_window.setCentralWidget(self.centralwidget)
        self.llm_menubar = QMenuBar(magi_llm_window)
        self.llm_menubar.setObjectName(u"llm_menubar")
        self.llm_menubar.setGeometry(QRect(0, 0, 892, 35))
        self.menuFile = QMenu(self.llm_menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.llm_menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        magi_llm_window.setMenuBar(self.llm_menubar)
        self.statusbar = QStatusBar(magi_llm_window)
        self.statusbar.setObjectName(u"statusbar")
        magi_llm_window.setStatusBar(self.statusbar)

        self.llm_menubar.addAction(self.menuFile.menuAction())
        self.llm_menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(magi_llm_window)
        self.defaultClearButton.clicked.connect(self.defaultTextHistory.clear)
        self.notebookClearButton.clicked.connect(self.notebookHistory.clear)
        self.chatClearButton.clicked["bool"].connect(self.chatHistory.clear)

        self.textgenTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(magi_llm_window)
    # setupUi

    def retranslateUi(self, magi_llm_window):
        magi_llm_window.setWindowTitle(QCoreApplication.translate("magi_llm_window", u"Magi LLM", None))
        self.actionSettings.setText(QCoreApplication.translate("magi_llm_window", u"Parameters", None))
        self.actionExit.setText(QCoreApplication.translate("magi_llm_window", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("magi_llm_window", u"About", None))
        self.defaultClearButton.setText(QCoreApplication.translate("magi_llm_window", u"Clear", None))
        self.defaultTextHistory.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Output appears here", None))
        self.defaultGenerateButton.setText(QCoreApplication.translate("magi_llm_window", u"Generate", None))
        self.defaultTextInput.setPlainText(QCoreApplication.translate("magi_llm_window", u"Wouldn't it be nice if", None))
        self.defaultTextInput.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Type something here", None))
        self.textgenTab.setTabText(self.textgenTab.indexOf(self.default_textgenTab), QCoreApplication.translate("magi_llm_window", u"Default", None))
        self.notebookGenerateButton.setText(QCoreApplication.translate("magi_llm_window", u"Generate", None))
        self.notebookClearButton.setText(QCoreApplication.translate("magi_llm_window", u"Clear", None))
        self.notebookHistory.setPlainText(QCoreApplication.translate("magi_llm_window", u"I would like to travel to Rome because of the rich history", None))
        self.notebookHistory.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Type something here", None))
        self.textgenTab.setTabText(self.textgenTab.indexOf(self.notebook_textgenTab), QCoreApplication.translate("magi_llm_window", u"Notebook", None))
        self.label.setText(QCoreApplication.translate("magi_llm_window", u"Presets:", None))
        self.chatHistory.setHtml(QCoreApplication.translate("magi_llm_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans Display'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Assistant is a digital personal assistant to Dave. It is always helpful, honest, patient, nuanced, scientific, introspective, verbose, and writes responses to all inquiries thoroughly and in great detail.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.chatHistory.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Chat history appears here", None))
        self.chatInput.setPlainText(QCoreApplication.translate("magi_llm_window", u"how to make tea?", None))
        self.chatInput.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Enter some text here", None))
        self.chatGenerateButton.setText(QCoreApplication.translate("magi_llm_window", u"Generate", None))
        self.chatClearButton.setText(QCoreApplication.translate("magi_llm_window", u"Clear", None))
        self.chatPresetComboBox.setItemText(0, QCoreApplication.translate("magi_llm_window", u"Default", None))
        self.chatPresetComboBox.setItemText(1, QCoreApplication.translate("magi_llm_window", u"Vicuna", None))
        self.chatPresetComboBox.setItemText(2, QCoreApplication.translate("magi_llm_window", u"Alpaca", None))
        self.chatPresetComboBox.setItemText(3, QCoreApplication.translate("magi_llm_window", u"Open Assistant", None))
        self.chatPresetComboBox.setItemText(4, QCoreApplication.translate("magi_llm_window", u"Custom", None))

        self.textgenTab.setTabText(self.textgenTab.indexOf(self.chat_textgenTab), QCoreApplication.translate("magi_llm_window", u"Chat", None))
        self.groupBox.setTitle(QCoreApplication.translate("magi_llm_window", u"Chat: Custom preset", None))
        self.label_3.setText(QCoreApplication.translate("magi_llm_window", u"Bot prefix", None))
        self.customChatBotPrefix.setText(QCoreApplication.translate("magi_llm_window", u"Bob", None))
        self.label_2.setText(QCoreApplication.translate("magi_llm_window", u"User prefix", None))
        self.customChatUserPrefix.setText(QCoreApplication.translate("magi_llm_window", u"User", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("magi_llm_window", u"More stuff", None))
        self.streamEnabledCheck.setText(QCoreApplication.translate("magi_llm_window", u"Streaming enabled", None))
        self.textgenTab.setTabText(self.textgenTab.indexOf(self.settingsTab), QCoreApplication.translate("magi_llm_window", u"Settings", None))
        self.menuFile.setTitle(QCoreApplication.translate("magi_llm_window", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("magi_llm_window", u"Help", None))
    # retranslateUi

