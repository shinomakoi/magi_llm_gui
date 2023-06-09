# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'magi_llm_ui.ui'
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
        self.textgenTab = QTabWidget(self.centralwidget)
        self.textgenTab.setObjectName(u"textgenTab")
        self.textgenTab.setAutoFillBackground(False)
        self.default_textgenTab = QWidget()
        self.default_textgenTab.setObjectName(u"default_textgenTab")
        self.default_textgenTab.setAutoFillBackground(True)
        self.gridLayout_6 = QGridLayout(self.default_textgenTab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.defaultTextInput = QPlainTextEdit(self.default_textgenTab)
        self.defaultTextInput.setObjectName(u"defaultTextInput")
        font = QFont()
        font.setFamilies([u"Lato"])
        font.setPointSize(12)
        self.defaultTextInput.setFont(font)
        self.defaultTextInput.setStyleSheet(u"")
        self.defaultTextInput.setReadOnly(False)

        self.gridLayout_6.addWidget(self.defaultTextInput, 1, 0, 1, 2)

        self.default_modeTextHistory = QPlainTextEdit(self.default_textgenTab)
        self.default_modeTextHistory.setObjectName(u"default_modeTextHistory")
        self.default_modeTextHistory.setFont(font)
        self.default_modeTextHistory.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.default_modeTextHistory.setAcceptDrops(False)
        self.default_modeTextHistory.setStyleSheet(u"")
        self.default_modeTextHistory.setReadOnly(True)

        self.gridLayout_6.addWidget(self.default_modeTextHistory, 0, 0, 1, 2)

        self.defaultGenerateButton = QPushButton(self.default_textgenTab)
        self.defaultGenerateButton.setObjectName(u"defaultGenerateButton")
        font1 = QFont()
        font1.setBold(True)
        self.defaultGenerateButton.setFont(font1)

        self.gridLayout_6.addWidget(self.defaultGenerateButton, 2, 0, 1, 1)

        self.frame_7 = QFrame(self.default_textgenTab)
        self.frame_7.setObjectName(u"frame_7")
        self.gridLayout_12 = QGridLayout(self.frame_7)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.defaultContinueButton = QPushButton(self.frame_7)
        self.defaultContinueButton.setObjectName(u"defaultContinueButton")

        self.gridLayout_12.addWidget(self.defaultContinueButton, 0, 0, 1, 1)

        self.defaultClearButton = QPushButton(self.frame_7)
        self.defaultClearButton.setObjectName(u"defaultClearButton")

        self.gridLayout_12.addWidget(self.defaultClearButton, 0, 1, 1, 1)

        self.defaultStopButton = QPushButton(self.frame_7)
        self.defaultStopButton.setObjectName(u"defaultStopButton")
        self.defaultStopButton.setEnabled(False)

        self.gridLayout_12.addWidget(self.defaultStopButton, 0, 2, 1, 1)


        self.gridLayout_6.addWidget(self.frame_7, 2, 1, 1, 1)

        self.textgenTab.addTab(self.default_textgenTab, "")
        self.notebook_textgenTab = QWidget()
        self.notebook_textgenTab.setObjectName(u"notebook_textgenTab")
        self.notebook_textgenTab.setAutoFillBackground(True)
        self.gridLayout_2 = QGridLayout(self.notebook_textgenTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.notebook_modeTextHistory = QPlainTextEdit(self.notebook_textgenTab)
        self.notebook_modeTextHistory.setObjectName(u"notebook_modeTextHistory")
        self.notebook_modeTextHistory.setFont(font)
        self.notebook_modeTextHistory.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.notebook_modeTextHistory, 0, 0, 1, 2)

        self.notebookGenerateButton = QPushButton(self.notebook_textgenTab)
        self.notebookGenerateButton.setObjectName(u"notebookGenerateButton")
        self.notebookGenerateButton.setFont(font1)

        self.gridLayout_2.addWidget(self.notebookGenerateButton, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.notebook_textgenTab)
        self.frame_4.setObjectName(u"frame_4")
        self.gridLayout_9 = QGridLayout(self.frame_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.notebookClearButton = QPushButton(self.frame_4)
        self.notebookClearButton.setObjectName(u"notebookClearButton")

        self.gridLayout_9.addWidget(self.notebookClearButton, 0, 1, 1, 1)

        self.notebookContinueButton = QPushButton(self.frame_4)
        self.notebookContinueButton.setObjectName(u"notebookContinueButton")

        self.gridLayout_9.addWidget(self.notebookContinueButton, 0, 0, 1, 1)

        self.notebookStopButton = QPushButton(self.frame_4)
        self.notebookStopButton.setObjectName(u"notebookStopButton")
        self.notebookStopButton.setEnabled(False)

        self.gridLayout_9.addWidget(self.notebookStopButton, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame_4, 1, 1, 1, 1)

        self.textgenTab.addTab(self.notebook_textgenTab, "")
        self.chat_textgenTab = QWidget()
        self.chat_textgenTab.setObjectName(u"chat_textgenTab")
        self.chat_textgenTab.setAutoFillBackground(True)
        self.gridLayout_3 = QGridLayout(self.chat_textgenTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.chat_modeTextHistory = QPlainTextEdit(self.chat_textgenTab)
        self.chat_modeTextHistory.setObjectName(u"chat_modeTextHistory")
        self.chat_modeTextHistory.setFont(font)
        self.chat_modeTextHistory.setReadOnly(False)

        self.gridLayout_3.addWidget(self.chat_modeTextHistory, 3, 0, 1, 2)

        self.chat_modeTextInput = QPlainTextEdit(self.chat_textgenTab)
        self.chat_modeTextInput.setObjectName(u"chat_modeTextInput")
        self.chat_modeTextInput.setFont(font)
        self.chat_modeTextInput.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.chat_modeTextInput, 4, 0, 1, 2, Qt.AlignBottom)

        self.chatGenerateButton = QPushButton(self.chat_textgenTab)
        self.chatGenerateButton.setObjectName(u"chatGenerateButton")
        self.chatGenerateButton.setFont(font1)

        self.gridLayout_3.addWidget(self.chatGenerateButton, 5, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.chat_textgenTab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_10 = QGridLayout(self.groupBox_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.instructPresetComboBox = QComboBox(self.groupBox_4)
        self.instructPresetComboBox.setObjectName(u"instructPresetComboBox")
        self.instructPresetComboBox.setInsertPolicy(QComboBox.InsertAlphabetically)

        self.gridLayout_10.addWidget(self.instructPresetComboBox, 0, 2, 1, 1)

        self.charactersRadioButton = QRadioButton(self.groupBox_4)
        self.charactersRadioButton.setObjectName(u"charactersRadioButton")

        self.gridLayout_10.addWidget(self.charactersRadioButton, 0, 3, 1, 1, Qt.AlignRight)

        self.awesomePresetComboBox = QComboBox(self.groupBox_4)
        self.awesomePresetComboBox.setObjectName(u"awesomePresetComboBox")
        self.awesomePresetComboBox.setInsertPolicy(QComboBox.InsertAlphabetically)

        self.gridLayout_10.addWidget(self.awesomePresetComboBox, 1, 2, 1, 1)

        self.instructRadioButton = QRadioButton(self.groupBox_4)
        self.instructRadioButton.setObjectName(u"instructRadioButton")
        self.instructRadioButton.setChecked(True)

        self.gridLayout_10.addWidget(self.instructRadioButton, 0, 1, 1, 1)

        self.characterPresetComboBox = QComboBox(self.groupBox_4)
        self.characterPresetComboBox.setObjectName(u"characterPresetComboBox")
        self.characterPresetComboBox.setInsertPolicy(QComboBox.InsertAlphabetically)

        self.gridLayout_10.addWidget(self.characterPresetComboBox, 0, 4, 1, 1)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.gridLayout_10.addWidget(self.label, 1, 1, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox_4)
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


        self.gridLayout_10.addWidget(self.groupBox_3, 1, 4, 1, 1, Qt.AlignRight)


        self.gridLayout_3.addWidget(self.groupBox_4, 0, 0, 1, 2)

        self.frame_6 = QFrame(self.chat_textgenTab)
        self.frame_6.setObjectName(u"frame_6")
        self.gridLayout_11 = QGridLayout(self.frame_6)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.chatClearButton = QPushButton(self.frame_6)
        self.chatClearButton.setObjectName(u"chatClearButton")

        self.gridLayout_11.addWidget(self.chatClearButton, 0, 1, 1, 1)

        self.chatContinueButton = QPushButton(self.frame_6)
        self.chatContinueButton.setObjectName(u"chatContinueButton")

        self.gridLayout_11.addWidget(self.chatContinueButton, 0, 0, 1, 1)

        self.chatStopButton = QPushButton(self.frame_6)
        self.chatStopButton.setObjectName(u"chatStopButton")
        self.chatStopButton.setEnabled(False)

        self.gridLayout_11.addWidget(self.chatStopButton, 0, 2, 1, 1)


        self.gridLayout_3.addWidget(self.frame_6, 5, 1, 1, 1)

        self.textgenTab.addTab(self.chat_textgenTab, "")
        self.settingsTab = QWidget()
        self.settingsTab.setObjectName(u"settingsTab")
        self.settingsTab.setAutoFillBackground(True)
        self.verticalLayout = QVBoxLayout(self.settingsTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_5 = QGroupBox(self.settingsTab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.exllamaCheck = QRadioButton(self.groupBox_5)
        self.exllamaCheck.setObjectName(u"exllamaCheck")
        self.exllamaCheck.setChecked(False)

        self.verticalLayout_3.addWidget(self.exllamaCheck)

        self.cppCheck = QRadioButton(self.groupBox_5)
        self.cppCheck.setObjectName(u"cppCheck")
        self.cppCheck.setChecked(True)

        self.verticalLayout_3.addWidget(self.cppCheck)

        self.paramWinShowButton = QPushButton(self.groupBox_5)
        self.paramWinShowButton.setObjectName(u"paramWinShowButton")

        self.verticalLayout_3.addWidget(self.paramWinShowButton, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.groupBox_5)

        self.groupBox_2 = QGroupBox(self.settingsTab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_28 = QLabel(self.groupBox_2)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_5.addWidget(self.label_28, 2, 0, 1, 1)

        self.logChatCheck = QCheckBox(self.groupBox_2)
        self.logChatCheck.setObjectName(u"logChatCheck")
        self.logChatCheck.setChecked(False)

        self.gridLayout_5.addWidget(self.logChatCheck, 0, 1, 1, 1)

        self.settingsPathSaveButton = QPushButton(self.groupBox_2)
        self.settingsPathSaveButton.setObjectName(u"settingsPathSaveButton")

        self.gridLayout_5.addWidget(self.settingsPathSaveButton, 4, 0, 1, 1)

        self.line = QFrame(self.groupBox_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line, 1, 0, 1, 2)

        self.streamEnabledCheck = QCheckBox(self.groupBox_2)
        self.streamEnabledCheck.setObjectName(u"streamEnabledCheck")
        self.streamEnabledCheck.setChecked(True)

        self.gridLayout_5.addWidget(self.streamEnabledCheck, 0, 0, 1, 1)

        self.cppModelSelect = QToolButton(self.groupBox_2)
        self.cppModelSelect.setObjectName(u"cppModelSelect")
        self.cppModelSelect.setArrowType(Qt.NoArrow)

        self.gridLayout_5.addWidget(self.cppModelSelect, 2, 2, 1, 1)

        self.cppModelPath = QLineEdit(self.groupBox_2)
        self.cppModelPath.setObjectName(u"cppModelPath")

        self.gridLayout_5.addWidget(self.cppModelPath, 2, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 3, 0, 1, 1)

        self.exllamaModelPath = QLineEdit(self.groupBox_2)
        self.exllamaModelPath.setObjectName(u"exllamaModelPath")

        self.gridLayout_5.addWidget(self.exllamaModelPath, 3, 1, 1, 1)

        self.exllamaModelSelect = QToolButton(self.groupBox_2)
        self.exllamaModelSelect.setObjectName(u"exllamaModelSelect")

        self.gridLayout_5.addWidget(self.exllamaModelSelect, 3, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.settingsTab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.customResponsePrefix = QLineEdit(self.groupBox)
        self.customResponsePrefix.setObjectName(u"customResponsePrefix")

        self.gridLayout_7.addWidget(self.customResponsePrefix, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_7.addWidget(self.label_4, 1, 0, 1, 1)

        self.customResponsePrefixCheck = QCheckBox(self.groupBox)
        self.customResponsePrefixCheck.setObjectName(u"customResponsePrefixCheck")

        self.gridLayout_7.addWidget(self.customResponsePrefixCheck, 0, 0, 1, 1)

        self.yourNameLine = QLineEdit(self.groupBox)
        self.yourNameLine.setObjectName(u"yourNameLine")

        self.gridLayout_7.addWidget(self.yourNameLine, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.textgenTab.addTab(self.settingsTab, "")

        self.gridLayout.addWidget(self.textgenTab, 1, 0, 1, 1)

        magi_llm_window.setCentralWidget(self.centralwidget)
        self.llm_menubar = QMenuBar(magi_llm_window)
        self.llm_menubar.setObjectName(u"llm_menubar")
        self.llm_menubar.setGeometry(QRect(0, 0, 819, 35))
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
        self.toolButton.clicked.connect(self.chat_modeTextHistory.zoomOut)
        self.toolButton_2.clicked.connect(self.chat_modeTextHistory.zoomIn)

        self.textgenTab.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(magi_llm_window)
    # setupUi

    def retranslateUi(self, magi_llm_window):
        magi_llm_window.setWindowTitle(QCoreApplication.translate("magi_llm_window", u"Magi LLM", None))
        self.actionSettings.setText(QCoreApplication.translate("magi_llm_window", u"Parameters", None))
        self.actionExit.setText(QCoreApplication.translate("magi_llm_window", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("magi_llm_window", u"About", None))
        self.actionStop.setText(QCoreApplication.translate("magi_llm_window", u"Stop", None))
        self.defaultTextInput.setPlainText("")
        self.defaultTextInput.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Type something here", None))
        self.default_modeTextHistory.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Output appears here", None))
        self.defaultGenerateButton.setText(QCoreApplication.translate("magi_llm_window", u"Generate", None))
#if QT_CONFIG(shortcut)
        self.defaultGenerateButton.setShortcut(QCoreApplication.translate("magi_llm_window", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        self.defaultContinueButton.setText(QCoreApplication.translate("magi_llm_window", u"Continue", None))
        self.defaultClearButton.setText(QCoreApplication.translate("magi_llm_window", u"Clear", None))
        self.defaultStopButton.setText(QCoreApplication.translate("magi_llm_window", u"Stop", None))
        self.textgenTab.setTabText(self.textgenTab.indexOf(self.default_textgenTab), QCoreApplication.translate("magi_llm_window", u"Default", None))
        self.notebook_modeTextHistory.setPlainText("")
        self.notebook_modeTextHistory.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Type something here", None))
        self.notebookGenerateButton.setText(QCoreApplication.translate("magi_llm_window", u"Generate", None))
#if QT_CONFIG(shortcut)
        self.notebookGenerateButton.setShortcut(QCoreApplication.translate("magi_llm_window", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        self.notebookClearButton.setText(QCoreApplication.translate("magi_llm_window", u"Clear", None))
        self.notebookContinueButton.setText(QCoreApplication.translate("magi_llm_window", u"Continue", None))
        self.notebookStopButton.setText(QCoreApplication.translate("magi_llm_window", u"Stop", None))
        self.textgenTab.setTabText(self.textgenTab.indexOf(self.notebook_textgenTab), QCoreApplication.translate("magi_llm_window", u"Notebook", None))
        self.chat_modeTextHistory.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Output appears here", None))
        self.chat_modeTextInput.setPlainText(QCoreApplication.translate("magi_llm_window", u"what are pigeons?", None))
        self.chat_modeTextInput.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Enter some text here", None))
        self.chatGenerateButton.setText(QCoreApplication.translate("magi_llm_window", u"Generate", None))
#if QT_CONFIG(shortcut)
        self.chatGenerateButton.setShortcut(QCoreApplication.translate("magi_llm_window", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox_4.setTitle("")
        self.charactersRadioButton.setText(QCoreApplication.translate("magi_llm_window", u"Characters:", None))
        self.instructRadioButton.setText(QCoreApplication.translate("magi_llm_window", u"Instruct:", None))
        self.label.setText(QCoreApplication.translate("magi_llm_window", u"Awesome prompts:", None))
        self.groupBox_3.setTitle("")
        self.label_2.setText(QCoreApplication.translate("magi_llm_window", u"Font size:", None))
        self.toolButton_2.setText(QCoreApplication.translate("magi_llm_window", u"...", None))
        self.toolButton.setText(QCoreApplication.translate("magi_llm_window", u"...", None))
        self.chatClearButton.setText(QCoreApplication.translate("magi_llm_window", u"Clear", None))
        self.chatContinueButton.setText(QCoreApplication.translate("magi_llm_window", u"Continue", None))
        self.chatStopButton.setText(QCoreApplication.translate("magi_llm_window", u"Stop", None))
        self.textgenTab.setTabText(self.textgenTab.indexOf(self.chat_textgenTab), QCoreApplication.translate("magi_llm_window", u"Chat", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("magi_llm_window", u"Backend:", None))
        self.exllamaCheck.setText(QCoreApplication.translate("magi_llm_window", u"Exllama", None))
        self.cppCheck.setText(QCoreApplication.translate("magi_llm_window", u"llama.cpp", None))
        self.paramWinShowButton.setText(QCoreApplication.translate("magi_llm_window", u"Parameters", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("magi_llm_window", u"Settings:", None))
        self.label_28.setText(QCoreApplication.translate("magi_llm_window", u"llama.cpp: Model path:", None))
        self.logChatCheck.setText(QCoreApplication.translate("magi_llm_window", u"Log chats", None))
        self.settingsPathSaveButton.setText(QCoreApplication.translate("magi_llm_window", u"Save", None))
#if QT_CONFIG(tooltip)
        self.streamEnabledCheck.setToolTip(QCoreApplication.translate("magi_llm_window", u"Stream responses (WebUI option only)", None))
#endif // QT_CONFIG(tooltip)
        self.streamEnabledCheck.setText(QCoreApplication.translate("magi_llm_window", u"Stream responses", None))
        self.cppModelSelect.setText(QCoreApplication.translate("magi_llm_window", u"...", None))
#if QT_CONFIG(tooltip)
        self.cppModelPath.setToolTip(QCoreApplication.translate("magi_llm_window", u"Path to GGML model for llama.cpp", None))
#endif // QT_CONFIG(tooltip)
        self.cppModelPath.setText("")
        self.label_3.setText(QCoreApplication.translate("magi_llm_window", u"Exllama: Model directory:", None))
        self.exllamaModelPath.setText("")
        self.exllamaModelSelect.setText(QCoreApplication.translate("magi_llm_window", u"...", None))
        self.groupBox.setTitle(QCoreApplication.translate("magi_llm_window", u"Custom chat prefixes:", None))
        self.customResponsePrefix.setText(QCoreApplication.translate("magi_llm_window", u"Sure!", None))
        self.label_4.setText(QCoreApplication.translate("magi_llm_window", u"Your name:", None))
        self.customResponsePrefixCheck.setText(QCoreApplication.translate("magi_llm_window", u"Response prefix:", None))
        self.yourNameLine.setText(QCoreApplication.translate("magi_llm_window", u"Bob", None))
        self.textgenTab.setTabText(self.textgenTab.indexOf(self.settingsTab), QCoreApplication.translate("magi_llm_window", u"Settings", None))
        self.menuFile.setTitle(QCoreApplication.translate("magi_llm_window", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("magi_llm_window", u"Help", None))
    # retranslateUi

