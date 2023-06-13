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
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTabWidget, QTextEdit, QToolButton, QVBoxLayout,
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

        self.gridLayout_6.addWidget(self.defaultTextInput, 1, 0, 1, 2)

        self.default_modeTextHistory = QPlainTextEdit(self.default_textgenTab)
        self.default_modeTextHistory.setObjectName(u"default_modeTextHistory")
        self.default_modeTextHistory.setFont(font)
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
        self.chat_modeTextHistory = QTextEdit(self.chat_textgenTab)
        self.chat_modeTextHistory.setObjectName(u"chat_modeTextHistory")
        self.chat_modeTextHistory.setFont(font)
        self.chat_modeTextHistory.setReadOnly(True)

        self.gridLayout_3.addWidget(self.chat_modeTextHistory, 2, 0, 1, 2)

        self.chatInputSessionCombo = QComboBox(self.chat_textgenTab)
        self.chatInputSessionCombo.setObjectName(u"chatInputSessionCombo")
        self.chatInputSessionCombo.setMaxCount(128)

        self.gridLayout_3.addWidget(self.chatInputSessionCombo, 3, 0, 1, 2)

        self.groupBox_4 = QGroupBox(self.chat_textgenTab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_10 = QGridLayout(self.groupBox_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.instructPresetComboBox = QComboBox(self.groupBox_4)
        self.instructPresetComboBox.setObjectName(u"instructPresetComboBox")

        self.gridLayout_10.addWidget(self.instructPresetComboBox, 0, 2, 1, 1)

        self.charactersRadioButton = QRadioButton(self.groupBox_4)
        self.charactersRadioButton.setObjectName(u"charactersRadioButton")

        self.gridLayout_10.addWidget(self.charactersRadioButton, 0, 3, 1, 1, Qt.AlignRight)

        self.awesomePresetComboBox = QComboBox(self.groupBox_4)
        self.awesomePresetComboBox.setObjectName(u"awesomePresetComboBox")

        self.gridLayout_10.addWidget(self.awesomePresetComboBox, 1, 2, 1, 1)

        self.instructRadioButton = QRadioButton(self.groupBox_4)
        self.instructRadioButton.setObjectName(u"instructRadioButton")
        self.instructRadioButton.setChecked(True)

        self.gridLayout_10.addWidget(self.instructRadioButton, 0, 1, 1, 1)

        self.characterPresetComboBox = QComboBox(self.groupBox_4)
        self.characterPresetComboBox.setObjectName(u"characterPresetComboBox")

        self.gridLayout_10.addWidget(self.characterPresetComboBox, 0, 4, 1, 1)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.gridLayout_10.addWidget(self.label, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_4, 0, 0, 1, 2)

        self.frame_6 = QFrame(self.chat_textgenTab)
        self.frame_6.setObjectName(u"frame_6")
        self.gridLayout_11 = QGridLayout(self.frame_6)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.chatStopButton = QPushButton(self.frame_6)
        self.chatStopButton.setObjectName(u"chatStopButton")
        self.chatStopButton.setEnabled(False)

        self.gridLayout_11.addWidget(self.chatStopButton, 0, 2, 1, 1)

        self.chatClearButton = QPushButton(self.frame_6)
        self.chatClearButton.setObjectName(u"chatClearButton")

        self.gridLayout_11.addWidget(self.chatClearButton, 0, 1, 1, 1)

        self.chatContinueButton = QPushButton(self.frame_6)
        self.chatContinueButton.setObjectName(u"chatContinueButton")

        self.gridLayout_11.addWidget(self.chatContinueButton, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_6, 6, 1, 1, 1)

        self.chat_modeTextInput = QPlainTextEdit(self.chat_textgenTab)
        self.chat_modeTextInput.setObjectName(u"chat_modeTextInput")
        self.chat_modeTextInput.setFont(font)

        self.gridLayout_3.addWidget(self.chat_modeTextInput, 4, 0, 1, 2, Qt.AlignBottom)

        self.chatGenerateButton = QPushButton(self.chat_textgenTab)
        self.chatGenerateButton.setObjectName(u"chatGenerateButton")
        self.chatGenerateButton.setFont(font1)

        self.gridLayout_3.addWidget(self.chatGenerateButton, 6, 0, 1, 1)

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
        self.cppCheck = QRadioButton(self.groupBox_5)
        self.cppCheck.setObjectName(u"cppCheck")
        self.cppCheck.setChecked(True)

        self.verticalLayout_3.addWidget(self.cppCheck)

        self.exllamaCheck = QRadioButton(self.groupBox_5)
        self.exllamaCheck.setObjectName(u"exllamaCheck")
        self.exllamaCheck.setChecked(False)

        self.verticalLayout_3.addWidget(self.exllamaCheck)

        self.tsServerCheck = QRadioButton(self.groupBox_5)
        self.tsServerCheck.setObjectName(u"tsServerCheck")
        self.tsServerCheck.setChecked(False)

        self.verticalLayout_3.addWidget(self.tsServerCheck)

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
        self.customResponsePrefixCheck = QCheckBox(self.groupBox)
        self.customResponsePrefixCheck.setObjectName(u"customResponsePrefixCheck")

        self.gridLayout_7.addWidget(self.customResponsePrefixCheck, 3, 0, 1, 1)

        self.yourNameLine = QLineEdit(self.groupBox)
        self.yourNameLine.setObjectName(u"yourNameLine")

        self.gridLayout_7.addWidget(self.yourNameLine, 1, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_7.addWidget(self.label_5, 1, 3, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_7.addWidget(self.label_4, 1, 0, 1, 1)

        self.customResponsePrefix = QLineEdit(self.groupBox)
        self.customResponsePrefix.setObjectName(u"customResponsePrefix")

        self.gridLayout_7.addWidget(self.customResponsePrefix, 3, 2, 1, 1)

        self.botNameLine = QLineEdit(self.groupBox)
        self.botNameLine.setObjectName(u"botNameLine")

        self.gridLayout_7.addWidget(self.botNameLine, 1, 4, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.settingsPathSaveButton = QPushButton(self.settingsTab)
        self.settingsPathSaveButton.setObjectName(u"settingsPathSaveButton")

        self.verticalLayout.addWidget(self.settingsPathSaveButton)

        self.textgenTab.addTab(self.settingsTab, "")

        self.gridLayout.addWidget(self.textgenTab, 0, 0, 1, 1)

        magi_llm_window.setCentralWidget(self.centralwidget)
        self.llm_menubar = QMenuBar(magi_llm_window)
        self.llm_menubar.setObjectName(u"llm_menubar")
        self.llm_menubar.setGeometry(QRect(0, 0, 819, 27))
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
        self.defaultClearButton.clicked.connect(self.default_modeTextHistory.clear)
        self.notebookClearButton.clicked.connect(self.notebook_modeTextHistory.clear)

        self.textgenTab.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(magi_llm_window)
    # setupUi

    def retranslateUi(self, magi_llm_window):
        magi_llm_window.setWindowTitle(QCoreApplication.translate("magi_llm_window", u"Magi LLM", None))
        self.actionSettings.setText(QCoreApplication.translate("magi_llm_window", u"Parameters", None))
        self.actionExit.setText(QCoreApplication.translate("magi_llm_window", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("magi_llm_window", u"About", None))
        self.actionStop.setText(QCoreApplication.translate("magi_llm_window", u"Stop", None))
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
        self.notebook_modeTextHistory.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Type something here", None))
        self.notebookGenerateButton.setText(QCoreApplication.translate("magi_llm_window", u"Generate", None))
#if QT_CONFIG(shortcut)
        self.notebookGenerateButton.setShortcut(QCoreApplication.translate("magi_llm_window", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        self.notebookClearButton.setText(QCoreApplication.translate("magi_llm_window", u"Clear", None))
        self.notebookContinueButton.setText(QCoreApplication.translate("magi_llm_window", u"Continue", None))
        self.notebookStopButton.setText(QCoreApplication.translate("magi_llm_window", u"Stop", None))
        self.textgenTab.setTabText(self.textgenTab.indexOf(self.notebook_textgenTab), QCoreApplication.translate("magi_llm_window", u"Notebook", None))
        self.chat_modeTextHistory.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Output goes here", None))
        self.chatInputSessionCombo.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Chat input history", None))
        self.groupBox_4.setTitle("")
#if QT_CONFIG(tooltip)
        self.instructPresetComboBox.setToolTip(QCoreApplication.translate("magi_llm_window", u"Select instruct format", None))
#endif // QT_CONFIG(tooltip)
        self.charactersRadioButton.setText(QCoreApplication.translate("magi_llm_window", u"Characters:", None))
        self.instructRadioButton.setText(QCoreApplication.translate("magi_llm_window", u"Instruct:", None))
#if QT_CONFIG(tooltip)
        self.characterPresetComboBox.setToolTip(QCoreApplication.translate("magi_llm_window", u"Select a character", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("magi_llm_window", u"Awesome prompts:", None))
        self.chatStopButton.setText(QCoreApplication.translate("magi_llm_window", u"Stop", None))
        self.chatClearButton.setText(QCoreApplication.translate("magi_llm_window", u"Clear", None))
        self.chatContinueButton.setText(QCoreApplication.translate("magi_llm_window", u"Continue", None))
        self.chat_modeTextInput.setPlainText("")
        self.chat_modeTextInput.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Type something here", None))
        self.chatGenerateButton.setText(QCoreApplication.translate("magi_llm_window", u"Generate", None))
#if QT_CONFIG(shortcut)
        self.chatGenerateButton.setShortcut(QCoreApplication.translate("magi_llm_window", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        self.textgenTab.setTabText(self.textgenTab.indexOf(self.chat_textgenTab), QCoreApplication.translate("magi_llm_window", u"Chat", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("magi_llm_window", u"Backend:", None))
#if QT_CONFIG(tooltip)
        self.cppCheck.setToolTip(QCoreApplication.translate("magi_llm_window", u"Use llama.cpp backend", None))
#endif // QT_CONFIG(tooltip)
        self.cppCheck.setText(QCoreApplication.translate("magi_llm_window", u"llama.cpp", None))
#if QT_CONFIG(tooltip)
        self.exllamaCheck.setToolTip(QCoreApplication.translate("magi_llm_window", u"Use Exllama backend", None))
#endif // QT_CONFIG(tooltip)
        self.exllamaCheck.setText(QCoreApplication.translate("magi_llm_window", u"Exllama", None))
        self.tsServerCheck.setText(QCoreApplication.translate("magi_llm_window", u"TextSynth", None))
#if QT_CONFIG(tooltip)
        self.paramWinShowButton.setToolTip(QCoreApplication.translate("magi_llm_window", u"Open parameter window", None))
#endif // QT_CONFIG(tooltip)
        self.paramWinShowButton.setText(QCoreApplication.translate("magi_llm_window", u"Parameters", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("magi_llm_window", u"Settings:", None))
        self.label_28.setText(QCoreApplication.translate("magi_llm_window", u"llama.cpp: Model path:", None))
#if QT_CONFIG(tooltip)
        self.logChatCheck.setToolTip(QCoreApplication.translate("magi_llm_window", u"Write chat logs to file", None))
#endif // QT_CONFIG(tooltip)
        self.logChatCheck.setText(QCoreApplication.translate("magi_llm_window", u"Log chats", None))
#if QT_CONFIG(tooltip)
        self.streamEnabledCheck.setToolTip(QCoreApplication.translate("magi_llm_window", u"Stream responses", None))
#endif // QT_CONFIG(tooltip)
        self.streamEnabledCheck.setText(QCoreApplication.translate("magi_llm_window", u"Stream responses", None))
#if QT_CONFIG(tooltip)
        self.cppModelSelect.setToolTip(QCoreApplication.translate("magi_llm_window", u"Select GGML model", None))
#endif // QT_CONFIG(tooltip)
        self.cppModelSelect.setText(QCoreApplication.translate("magi_llm_window", u"...", None))
#if QT_CONFIG(tooltip)
        self.cppModelPath.setToolTip(QCoreApplication.translate("magi_llm_window", u"Path to GGML model for llama.cpp", None))
#endif // QT_CONFIG(tooltip)
        self.cppModelPath.setText("")
        self.label_3.setText(QCoreApplication.translate("magi_llm_window", u"Exllama: Model directory:", None))
#if QT_CONFIG(tooltip)
        self.exllamaModelPath.setToolTip(QCoreApplication.translate("magi_llm_window", u"Path to Exllama GPTQ model folder (mode file, tokenizer.json, config.json)", None))
#endif // QT_CONFIG(tooltip)
        self.exllamaModelPath.setText("")
#if QT_CONFIG(tooltip)
        self.exllamaModelSelect.setToolTip(QCoreApplication.translate("magi_llm_window", u"Select Exllama model folder", None))
#endif // QT_CONFIG(tooltip)
        self.exllamaModelSelect.setText(QCoreApplication.translate("magi_llm_window", u"...", None))
        self.groupBox.setTitle(QCoreApplication.translate("magi_llm_window", u"Custom chat prefixes:", None))
        self.customResponsePrefixCheck.setText(QCoreApplication.translate("magi_llm_window", u"Response prefix:", None))
#if QT_CONFIG(tooltip)
        self.yourNameLine.setToolTip(QCoreApplication.translate("magi_llm_window", u"User name to be used in Character mode", None))
#endif // QT_CONFIG(tooltip)
        self.yourNameLine.setText(QCoreApplication.translate("magi_llm_window", u"User", None))
        self.label_5.setText(QCoreApplication.translate("magi_llm_window", u"Bot name:", None))
        self.label_4.setText(QCoreApplication.translate("magi_llm_window", u"User name:", None))
#if QT_CONFIG(tooltip)
        self.customResponsePrefix.setToolTip(QCoreApplication.translate("magi_llm_window", u"Prefix to apply to prompts", None))
#endif // QT_CONFIG(tooltip)
        self.customResponsePrefix.setText(QCoreApplication.translate("magi_llm_window", u"Sure!", None))
        self.botNameLine.setText(QCoreApplication.translate("magi_llm_window", u"Assistant", None))
#if QT_CONFIG(tooltip)
        self.settingsPathSaveButton.setToolTip(QCoreApplication.translate("magi_llm_window", u"Save model paths", None))
#endif // QT_CONFIG(tooltip)
        self.settingsPathSaveButton.setText(QCoreApplication.translate("magi_llm_window", u"Save settings", None))
        self.textgenTab.setTabText(self.textgenTab.indexOf(self.settingsTab), QCoreApplication.translate("magi_llm_window", u"Settings", None))
        self.menuFile.setTitle(QCoreApplication.translate("magi_llm_window", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("magi_llm_window", u"Help", None))
    # retranslateUi

