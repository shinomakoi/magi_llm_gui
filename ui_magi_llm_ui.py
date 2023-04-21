# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'magi_llm_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QTabWidget, QToolButton, QVBoxLayout,
    QWidget)

class Ui_magi_llm_window(object):
    def setupUi(self, magi_llm_window):
        if not magi_llm_window.objectName():
            magi_llm_window.setObjectName(u"magi_llm_window")
        magi_llm_window.resize(819, 987)
        self.actionSettings = QAction(magi_llm_window)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionExit = QAction(magi_llm_window)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(magi_llm_window)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionStop = QAction(magi_llm_window)
        self.actionStop.setObjectName(u"actionStop")
        self.centralwidget = QWidget(magi_llm_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setEnabled(False)

        self.gridLayout.addWidget(self.stopButton, 2, 0, 1, 1)

        self.textgenTab = QTabWidget(self.centralwidget)
        self.textgenTab.setObjectName(u"textgenTab")
        self.textgenTab.setAutoFillBackground(False)
        self.default_textgenTab = QWidget()
        self.default_textgenTab.setObjectName(u"default_textgenTab")
        self.default_textgenTab.setAutoFillBackground(True)
        self.gridLayout_6 = QGridLayout(self.default_textgenTab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.defaultTextHistory = QPlainTextEdit(self.default_textgenTab)
        self.defaultTextHistory.setObjectName(u"defaultTextHistory")
        font = QFont()
        font.setFamilies([u"Lato"])
        font.setPointSize(12)
        self.defaultTextHistory.setFont(font)
        self.defaultTextHistory.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.defaultTextHistory.setAcceptDrops(False)
        self.defaultTextHistory.setStyleSheet(u"")
        self.defaultTextHistory.setReadOnly(True)

        self.gridLayout_6.addWidget(self.defaultTextHistory, 0, 0, 1, 3)

        self.defaultClearButton = QPushButton(self.default_textgenTab)
        self.defaultClearButton.setObjectName(u"defaultClearButton")

        self.gridLayout_6.addWidget(self.defaultClearButton, 2, 2, 1, 1)

        self.defaultGenerateButton = QPushButton(self.default_textgenTab)
        self.defaultGenerateButton.setObjectName(u"defaultGenerateButton")
        font1 = QFont()
        font1.setBold(True)
        self.defaultGenerateButton.setFont(font1)

        self.gridLayout_6.addWidget(self.defaultGenerateButton, 2, 0, 1, 1)

        self.defaultContinueButton = QPushButton(self.default_textgenTab)
        self.defaultContinueButton.setObjectName(u"defaultContinueButton")

        self.gridLayout_6.addWidget(self.defaultContinueButton, 2, 1, 1, 1)

        self.defaultTextInput = QPlainTextEdit(self.default_textgenTab)
        self.defaultTextInput.setObjectName(u"defaultTextInput")
        self.defaultTextInput.setFont(font)
        self.defaultTextInput.setStyleSheet(u"")
        self.defaultTextInput.setReadOnly(False)

        self.gridLayout_6.addWidget(self.defaultTextInput, 1, 0, 1, 3)

        self.textgenTab.addTab(self.default_textgenTab, "")
        self.notebook_textgenTab = QWidget()
        self.notebook_textgenTab.setObjectName(u"notebook_textgenTab")
        self.notebook_textgenTab.setAutoFillBackground(True)
        self.gridLayout_2 = QGridLayout(self.notebook_textgenTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.notebookHistory = QPlainTextEdit(self.notebook_textgenTab)
        self.notebookHistory.setObjectName(u"notebookHistory")
        self.notebookHistory.setFont(font)
        self.notebookHistory.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.notebookHistory, 0, 0, 1, 3)

        self.notebookGenerateButton = QPushButton(self.notebook_textgenTab)
        self.notebookGenerateButton.setObjectName(u"notebookGenerateButton")
        self.notebookGenerateButton.setFont(font1)

        self.gridLayout_2.addWidget(self.notebookGenerateButton, 1, 0, 1, 1)

        self.notebookContinueButton = QPushButton(self.notebook_textgenTab)
        self.notebookContinueButton.setObjectName(u"notebookContinueButton")

        self.gridLayout_2.addWidget(self.notebookContinueButton, 1, 1, 1, 1)

        self.notebookClearButton = QPushButton(self.notebook_textgenTab)
        self.notebookClearButton.setObjectName(u"notebookClearButton")

        self.gridLayout_2.addWidget(self.notebookClearButton, 1, 2, 1, 1)

        self.textgenTab.addTab(self.notebook_textgenTab, "")
        self.chat_textgenTab = QWidget()
        self.chat_textgenTab.setObjectName(u"chat_textgenTab")
        self.chat_textgenTab.setAutoFillBackground(True)
        self.gridLayout_3 = QGridLayout(self.chat_textgenTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.chatHistory = QPlainTextEdit(self.chat_textgenTab)
        self.chatHistory.setObjectName(u"chatHistory")
        self.chatHistory.setFont(font)

        self.gridLayout_3.addWidget(self.chatHistory, 2, 0, 1, 3)

        self.chatInput = QPlainTextEdit(self.chat_textgenTab)
        self.chatInput.setObjectName(u"chatInput")
        self.chatInput.setFont(font)
        self.chatInput.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.chatInput, 5, 0, 1, 3, Qt.AlignBottom)

        self.chatContinueButton = QPushButton(self.chat_textgenTab)
        self.chatContinueButton.setObjectName(u"chatContinueButton")

        self.gridLayout_3.addWidget(self.chatContinueButton, 6, 1, 1, 1)

        self.chatClearButton = QPushButton(self.chat_textgenTab)
        self.chatClearButton.setObjectName(u"chatClearButton")

        self.gridLayout_3.addWidget(self.chatClearButton, 6, 2, 1, 1)

        self.chatPresetComboBox = QComboBox(self.chat_textgenTab)
        self.chatPresetComboBox.setObjectName(u"chatPresetComboBox")

        self.gridLayout_3.addWidget(self.chatPresetComboBox, 1, 0, 1, 3)

        self.chatGenerateButton = QPushButton(self.chat_textgenTab)
        self.chatGenerateButton.setObjectName(u"chatGenerateButton")
        self.chatGenerateButton.setFont(font1)

        self.gridLayout_3.addWidget(self.chatGenerateButton, 6, 0, 1, 1)

        self.label = QLabel(self.chat_textgenTab)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.chat_textgenTab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.toolButton_2 = QToolButton(self.groupBox_3)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setArrowType(Qt.UpArrow)

        self.horizontalLayout.addWidget(self.toolButton_2)

        self.toolButton = QToolButton(self.groupBox_3)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setArrowType(Qt.DownArrow)

        self.horizontalLayout.addWidget(self.toolButton)


        self.gridLayout_3.addWidget(self.groupBox_3, 0, 2, 1, 1, Qt.AlignRight)

        self.textgenTab.addTab(self.chat_textgenTab, "")
        self.settingsTab = QWidget()
        self.settingsTab.setObjectName(u"settingsTab")
        self.settingsTab.setAutoFillBackground(True)
        self.gridLayout_4 = QGridLayout(self.settingsTab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.settingsTab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.customResponsePrefixCheck = QCheckBox(self.groupBox)
        self.customResponsePrefixCheck.setObjectName(u"customResponsePrefixCheck")

        self.gridLayout_7.addWidget(self.customResponsePrefixCheck, 0, 0, 1, 1)

        self.customResponsePrefix = QLineEdit(self.groupBox)
        self.customResponsePrefix.setObjectName(u"customResponsePrefix")

        self.gridLayout_7.addWidget(self.customResponsePrefix, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 2, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.settingsTab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.oobaCheck = QRadioButton(self.groupBox_5)
        self.oobaCheck.setObjectName(u"oobaCheck")
        self.oobaCheck.setChecked(True)

        self.verticalLayout_3.addWidget(self.oobaCheck)

        self.cppCheck = QRadioButton(self.groupBox_5)
        self.cppCheck.setObjectName(u"cppCheck")
        self.cppCheck.setChecked(False)

        self.verticalLayout_3.addWidget(self.cppCheck)


        self.gridLayout_4.addWidget(self.groupBox_5, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.settingsTab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.line = QFrame(self.groupBox_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line, 1, 0, 1, 2)

        self.cppModelPath = QLineEdit(self.groupBox_2)
        self.cppModelPath.setObjectName(u"cppModelPath")

        self.gridLayout_5.addWidget(self.cppModelPath, 2, 1, 1, 1)

        self.label_28 = QLabel(self.groupBox_2)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_5.addWidget(self.label_28, 2, 0, 1, 1)

        self.settingsPathSaveButton = QPushButton(self.groupBox_2)
        self.settingsPathSaveButton.setObjectName(u"settingsPathSaveButton")

        self.gridLayout_5.addWidget(self.settingsPathSaveButton, 3, 0, 1, 1)

        self.streamEnabledCheck = QCheckBox(self.groupBox_2)
        self.streamEnabledCheck.setObjectName(u"streamEnabledCheck")
        self.streamEnabledCheck.setChecked(True)

        self.gridLayout_5.addWidget(self.streamEnabledCheck, 0, 0, 1, 1)

        self.cppModelSelect = QToolButton(self.groupBox_2)
        self.cppModelSelect.setObjectName(u"cppModelSelect")
        self.cppModelSelect.setArrowType(Qt.NoArrow)

        self.gridLayout_5.addWidget(self.cppModelSelect, 2, 2, 1, 1)

        self.logChatCheck = QCheckBox(self.groupBox_2)
        self.logChatCheck.setObjectName(u"logChatCheck")
        self.logChatCheck.setChecked(False)

        self.gridLayout_5.addWidget(self.logChatCheck, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.textgenTab.addTab(self.settingsTab, "")

        self.gridLayout.addWidget(self.textgenTab, 1, 0, 1, 1)

        magi_llm_window.setCentralWidget(self.centralwidget)
        self.llm_menubar = QMenuBar(magi_llm_window)
        self.llm_menubar.setObjectName(u"llm_menubar")
        self.llm_menubar.setGeometry(QRect(0, 0, 819, 23))
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
        self.toolButton_2.clicked.connect(self.chatHistory.zoomIn)
        self.toolButton.clicked.connect(self.chatHistory.zoomOut)

        self.textgenTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(magi_llm_window)
    # setupUi

    def retranslateUi(self, magi_llm_window):
        magi_llm_window.setWindowTitle(QCoreApplication.translate("magi_llm_window", u"Magi LLM", None))
        self.actionSettings.setText(QCoreApplication.translate("magi_llm_window", u"Parameters", None))
        self.actionExit.setText(QCoreApplication.translate("magi_llm_window", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("magi_llm_window", u"About", None))
        self.actionStop.setText(QCoreApplication.translate("magi_llm_window", u"Stop", None))
        self.stopButton.setText(QCoreApplication.translate("magi_llm_window", u"Stop", None))
        self.defaultTextHistory.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Output appears here", None))
        self.defaultClearButton.setText(QCoreApplication.translate("magi_llm_window", u"Clear", None))
        self.defaultGenerateButton.setText(QCoreApplication.translate("magi_llm_window", u"Generate", None))
#if QT_CONFIG(shortcut)
        self.defaultGenerateButton.setShortcut(QCoreApplication.translate("magi_llm_window", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.defaultContinueButton.setText(QCoreApplication.translate("magi_llm_window", u"Continue", None))
        self.defaultTextInput.setPlainText("")
        self.defaultTextInput.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Type something here", None))
        self.textgenTab.setTabText(self.textgenTab.indexOf(self.default_textgenTab), QCoreApplication.translate("magi_llm_window", u"Default", None))
        self.notebookHistory.setPlainText("")
        self.notebookHistory.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Type something here", None))
        self.notebookGenerateButton.setText(QCoreApplication.translate("magi_llm_window", u"Generate", None))
        self.notebookContinueButton.setText(QCoreApplication.translate("magi_llm_window", u"Continue", None))
        self.notebookClearButton.setText(QCoreApplication.translate("magi_llm_window", u"Clear", None))
        self.textgenTab.setTabText(self.textgenTab.indexOf(self.notebook_textgenTab), QCoreApplication.translate("magi_llm_window", u"Notebook", None))
        self.chatHistory.setPlainText(QCoreApplication.translate("magi_llm_window", u"Below is an instruction that describes a task. Write a response that appropriately completes the request.", None))
        self.chatInput.setPlainText("")
        self.chatInput.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Enter some text here", None))
        self.chatContinueButton.setText(QCoreApplication.translate("magi_llm_window", u"Continue", None))
        self.chatClearButton.setText(QCoreApplication.translate("magi_llm_window", u"Clear", None))
        self.chatGenerateButton.setText(QCoreApplication.translate("magi_llm_window", u"Generate", None))
        self.label.setText(QCoreApplication.translate("magi_llm_window", u"Presets:", None))
        self.groupBox_3.setTitle("")
        self.label_2.setText(QCoreApplication.translate("magi_llm_window", u"Font size:", None))
        self.toolButton_2.setText(QCoreApplication.translate("magi_llm_window", u"...", None))
        self.toolButton.setText(QCoreApplication.translate("magi_llm_window", u"...", None))
        self.textgenTab.setTabText(self.textgenTab.indexOf(self.chat_textgenTab), QCoreApplication.translate("magi_llm_window", u"Chat", None))
        self.groupBox.setTitle(QCoreApplication.translate("magi_llm_window", u"Custom chat prefixes:", None))
        self.customResponsePrefixCheck.setText(QCoreApplication.translate("magi_llm_window", u"Response prefix:", None))
        self.customResponsePrefix.setText(QCoreApplication.translate("magi_llm_window", u"Sure!", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("magi_llm_window", u"Backend:", None))
        self.oobaCheck.setText(QCoreApplication.translate("magi_llm_window", u"Oobabooga WebUI", None))
        self.cppCheck.setText(QCoreApplication.translate("magi_llm_window", u"llama.cpp", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("magi_llm_window", u"Settings:", None))
#if QT_CONFIG(tooltip)
        self.cppModelPath.setToolTip(QCoreApplication.translate("magi_llm_window", u"Path to GGML model for llama.cpp", None))
#endif // QT_CONFIG(tooltip)
        self.cppModelPath.setText("")
        self.label_28.setText(QCoreApplication.translate("magi_llm_window", u"llama.cpp: Model path:", None))
        self.settingsPathSaveButton.setText(QCoreApplication.translate("magi_llm_window", u"Save", None))
#if QT_CONFIG(tooltip)
        self.streamEnabledCheck.setToolTip(QCoreApplication.translate("magi_llm_window", u"Stream responses (WebUI option only)", None))
#endif // QT_CONFIG(tooltip)
        self.streamEnabledCheck.setText(QCoreApplication.translate("magi_llm_window", u"Stream responses", None))
        self.cppModelSelect.setText(QCoreApplication.translate("magi_llm_window", u"...", None))
        self.logChatCheck.setText(QCoreApplication.translate("magi_llm_window", u"Log chats", None))
        self.textgenTab.setTabText(self.textgenTab.indexOf(self.settingsTab), QCoreApplication.translate("magi_llm_window", u"Settings", None))
        self.menuFile.setTitle(QCoreApplication.translate("magi_llm_window", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("magi_llm_window", u"Help", None))
    # retranslateUi

