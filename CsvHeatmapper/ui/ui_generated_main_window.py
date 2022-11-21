# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QToolButton, QVBoxLayout, QWidget)
from  . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(798, 730)
        MainWindow.setMinimumSize(QSize(0, 730))
        icon = QIcon()
        icon.addFile(u":/icon/imgs/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.action_User_s_manual = QAction(MainWindow)
        self.action_User_s_manual.setObjectName(u"action_User_s_manual")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(240, 16777215))
        self.frame.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.groupBox_file = QGroupBox(self.frame)
        self.groupBox_file.setObjectName(u"groupBox_file")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_file.sizePolicy().hasHeightForWidth())
        self.groupBox_file.setSizePolicy(sizePolicy1)
        self.groupBox_file.setMinimumSize(QSize(0, 60))
        self.groupBox_file.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_file)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 2)
        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.frame_2 = QFrame(self.groupBox_file)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toolButton_addFile = QToolButton(self.frame_2)
        self.toolButton_addFile.setObjectName(u"toolButton_addFile")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toolButton_addFile.sizePolicy().hasHeightForWidth())
        self.toolButton_addFile.setSizePolicy(sizePolicy2)
        self.toolButton_addFile.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_4.addWidget(self.toolButton_addFile)

        self.toolButton_substractFile = QToolButton(self.frame_2)
        self.toolButton_substractFile.setObjectName(u"toolButton_substractFile")
        sizePolicy2.setHeightForWidth(self.toolButton_substractFile.sizePolicy().hasHeightForWidth())
        self.toolButton_substractFile.setSizePolicy(sizePolicy2)
        self.toolButton_substractFile.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_4.addWidget(self.toolButton_substractFile)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.groupBox_file)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.groupBox_3.setMaximumSize(QSize(16777215, 80))
        self.groupBox_3.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(-1, 0, -1, 4)
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.doubleSpinBox_Yinterval = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_Yinterval.setObjectName(u"doubleSpinBox_Yinterval")
        self.doubleSpinBox_Yinterval.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout.addWidget(self.doubleSpinBox_Yinterval, 1, 1, 1, 1)

        self.doubleSpinBox_Xinterval = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_Xinterval.setObjectName(u"doubleSpinBox_Xinterval")
        self.doubleSpinBox_Xinterval.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout.addWidget(self.doubleSpinBox_Xinterval, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.groupBox_4.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.gridLayout_2 = QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(-1, 0, -1, 4)
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.doubleSpinBox_colorinterval = QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_colorinterval.setObjectName(u"doubleSpinBox_colorinterval")
        self.doubleSpinBox_colorinterval.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_2.addWidget(self.doubleSpinBox_colorinterval, 2, 1, 1, 1)

        self.doubleSpinBox_colorMin = QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_colorMin.setObjectName(u"doubleSpinBox_colorMin")
        self.doubleSpinBox_colorMin.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_2.addWidget(self.doubleSpinBox_colorMin, 1, 1, 1, 1)

        self.doubleSpinBox_colorMax = QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_colorMax.setObjectName(u"doubleSpinBox_colorMax")
        self.doubleSpinBox_colorMax.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_2.addWidget(self.doubleSpinBox_colorMax, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy1.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy1)
        self.groupBox_5.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.gridLayout_3 = QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(-1, 0, -1, 4)
        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_3.addWidget(self.label_7, 3, 0, 1, 1)

        self.lineEdit_xLabel = QLineEdit(self.groupBox_5)
        self.lineEdit_xLabel.setObjectName(u"lineEdit_xLabel")
        self.lineEdit_xLabel.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.lineEdit_xLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.lineEdit_xLabel, 0, 1, 1, 1)

        self.lineEdit_yLabel = QLineEdit(self.groupBox_5)
        self.lineEdit_yLabel.setObjectName(u"lineEdit_yLabel")
        self.lineEdit_yLabel.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.lineEdit_yLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.lineEdit_yLabel, 2, 1, 1, 1)

        self.lineEdit_colorLabel = QLineEdit(self.groupBox_5)
        self.lineEdit_colorLabel.setObjectName(u"lineEdit_colorLabel")
        self.lineEdit_colorLabel.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.lineEdit_colorLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.lineEdit_colorLabel, 3, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_5)

        self.groupBox_11 = QGroupBox(self.groupBox_2)
        self.groupBox_11.setObjectName(u"groupBox_11")
        sizePolicy1.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy1)
        self.groupBox_11.setMaximumSize(QSize(16777215, 80))
        self.groupBox_11.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.gridLayout_7 = QGridLayout(self.groupBox_11)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setContentsMargins(-1, 0, -1, 4)
        self.spinBox_axisLabelSize = QSpinBox(self.groupBox_11)
        self.spinBox_axisLabelSize.setObjectName(u"spinBox_axisLabelSize")
        self.spinBox_axisLabelSize.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.spinBox_axisLabelSize.setMinimum(1)
        self.spinBox_axisLabelSize.setMaximum(30)
        self.spinBox_axisLabelSize.setValue(20)

        self.gridLayout_7.addWidget(self.spinBox_axisLabelSize, 0, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_7.addWidget(self.label_17, 1, 0, 1, 1)

        self.label_18 = QLabel(self.groupBox_11)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_7.addWidget(self.label_18, 0, 0, 1, 1)

        self.spinBox_tickLabelSize = QSpinBox(self.groupBox_11)
        self.spinBox_tickLabelSize.setObjectName(u"spinBox_tickLabelSize")
        self.spinBox_tickLabelSize.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.spinBox_tickLabelSize.setMinimum(1)
        self.spinBox_tickLabelSize.setMaximum(30)
        self.spinBox_tickLabelSize.setValue(12)

        self.gridLayout_7.addWidget(self.spinBox_tickLabelSize, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_11)

        self.groupBox_12 = QGroupBox(self.groupBox_2)
        self.groupBox_12.setObjectName(u"groupBox_12")
        sizePolicy1.setHeightForWidth(self.groupBox_12.sizePolicy().hasHeightForWidth())
        self.groupBox_12.setSizePolicy(sizePolicy1)
        self.groupBox_12.setMaximumSize(QSize(16777215, 80))
        self.groupBox_12.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.gridLayout_8 = QGridLayout(self.groupBox_12)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.pushButton_selectColormap = QPushButton(self.groupBox_12)
        self.pushButton_selectColormap.setObjectName(u"pushButton_selectColormap")
        self.pushButton_selectColormap.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_8.addWidget(self.pushButton_selectColormap, 0, 0, 1, 1)

        self.checkBox_colormapIsReversed = QCheckBox(self.groupBox_12)
        self.checkBox_colormapIsReversed.setObjectName(u"checkBox_colormapIsReversed")
        self.checkBox_colormapIsReversed.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_8.addWidget(self.checkBox_colormapIsReversed, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_12)

        self.frame_3 = QFrame(self.groupBox_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.checkBox_3d = QCheckBox(self.frame_3)
        self.checkBox_3d.setObjectName(u"checkBox_3d")
        self.checkBox_3d.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout.addWidget(self.checkBox_3d)

        self.radioButton = QRadioButton(self.frame_3)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.radioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.frame_3)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout.addWidget(self.radioButton_2)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_plot = QPushButton(self.frame_4)
        self.pushButton_plot.setObjectName(u"pushButton_plot")
        self.pushButton_plot.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_4.addWidget(self.pushButton_plot)

        self.pushButton_save = QPushButton(self.frame_4)
        self.pushButton_save.setObjectName(u"pushButton_save")
        sizePolicy2.setHeightForWidth(self.pushButton_save.sizePolicy().hasHeightForWidth())
        self.pushButton_save.setSizePolicy(sizePolicy2)
        self.pushButton_save.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon1 = QIcon()
        icon1.addFile(u":/icon/imgs/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_save.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.pushButton_save)


        self.verticalLayout.addWidget(self.frame_4)

        self.listWidget = QListWidget(self.frame)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout.addWidget(self.listWidget)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_figure = QFrame(self.widget)
        self.frame_figure.setObjectName(u"frame_figure")
        self.frame_figure.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frame_figure.setFrameShape(QFrame.StyledPanel)
        self.frame_figure.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_figure)


        self.verticalLayout_3.addWidget(self.widget)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 798, 22))
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName(u"menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_Help.menuAction())
        self.menu_Help.addAction(self.action_User_s_manual)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Csv Heatmapper", None))
        self.action_User_s_manual.setText(QCoreApplication.translate("MainWindow", u"&User's manual", None))
        self.groupBox_file.setTitle(QCoreApplication.translate("MainWindow", u"CSV File", None))
        self.toolButton_addFile.setText(QCoreApplication.translate("MainWindow", u"\u2795", None))
        self.toolButton_substractFile.setText(QCoreApplication.translate("MainWindow", u"\u2796", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Plot Setting", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Axis Scale", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Y Interval", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"X Interval", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Color Scale", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Interval", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Label", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"X Label", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Y Label", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ColorBar Label", None))
        self.lineEdit_xLabel.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.lineEdit_yLabel.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.lineEdit_colorLabel.setText(QCoreApplication.translate("MainWindow", u"z ()", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Font Size", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Tick Label", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Axis Label", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Color Map", None))
        self.pushButton_selectColormap.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.checkBox_colormapIsReversed.setText(QCoreApplication.translate("MainWindow", u"Reversed", None))
        self.checkBox_3d.setText(QCoreApplication.translate("MainWindow", u"3D", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Scatter", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Surface", None))
        self.pushButton_plot.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.pushButton_save.setText("")
        self.menu_Help.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
    # retranslateUi

