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
        font = QFont()
        font.setBold(False)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon/imgs/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QLabel[class=\"bold\"] {\n"
"	font-weight: 900;\n"
"}\n"
"QGroupBox\n"
"{\n"
"	font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: content;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"	left: -2px;\n"
"}\n"
"QPushButton {\n"
"	font: 900 12px;\n"
"	max-height:50px;\n"
"    border: 1px solid #8f8f91;\n"
"    border-radius: 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"QPushButton:hover {\n"
"    border-color: #a5f6ff;\n"
"    background-color: #e5fcff;\n"
"}\n"
"QPushButton:pressed {\n"
"	border-color: #aaa;\n"
"	background-color: #ccc;\n"
"}")
        self.action_User_s_manual = QAction(MainWindow)
        self.action_User_s_manual.setObjectName(u"action_User_s_manual")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
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
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
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
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        self.toolButton_addFile.setFont(font1)
        self.toolButton_addFile.setFocusPolicy(Qt.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u":/icon/imgs/plus-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_addFile.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.toolButton_addFile)

        self.toolButton_substractFile = QToolButton(self.frame_2)
        self.toolButton_substractFile.setObjectName(u"toolButton_substractFile")
        sizePolicy2.setHeightForWidth(self.toolButton_substractFile.sizePolicy().hasHeightForWidth())
        self.toolButton_substractFile.setSizePolicy(sizePolicy2)
        self.toolButton_substractFile.setFocusPolicy(Qt.NoFocus)
        icon2 = QIcon()
        icon2.addFile(u":/icon/imgs/minus-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_substractFile.setIcon(icon2)

        self.verticalLayout_4.addWidget(self.toolButton_substractFile)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.groupBox_file)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.frame_3 = QFrame(self.groupBox_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMaximumSize(QSize(16777215, 80))
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(14)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.frame_3)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_5 = QGridLayout(self.widget_2)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, 0, 0, 0)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.doubleSpinBox_Xinterval = QDoubleSpinBox(self.widget_2)
        self.doubleSpinBox_Xinterval.setObjectName(u"doubleSpinBox_Xinterval")

        self.gridLayout_5.addWidget(self.doubleSpinBox_Xinterval, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)

        self.doubleSpinBox_Yinterval = QDoubleSpinBox(self.widget_2)
        self.doubleSpinBox_Yinterval.setObjectName(u"doubleSpinBox_Yinterval")

        self.gridLayout_5.addWidget(self.doubleSpinBox_Yinterval, 1, 1, 1, 1)

        self.checkBox_origin = QCheckBox(self.widget_2)
        self.checkBox_origin.setObjectName(u"checkBox_origin")

        self.gridLayout_5.addWidget(self.checkBox_origin, 2, 0, 1, 2)


        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)

        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.groupBox_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(14)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.frame_4)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_6 = QGridLayout(self.widget_3)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 0, 0, 0)
        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_6.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)

        self.doubleSpinBox_colorMin = QDoubleSpinBox(self.widget_3)
        self.doubleSpinBox_colorMin.setObjectName(u"doubleSpinBox_colorMin")

        self.gridLayout_6.addWidget(self.doubleSpinBox_colorMin, 3, 2, 1, 1)

        self.doubleSpinBox_colorinterval = QDoubleSpinBox(self.widget_3)
        self.doubleSpinBox_colorinterval.setObjectName(u"doubleSpinBox_colorinterval")

        self.gridLayout_6.addWidget(self.doubleSpinBox_colorinterval, 4, 2, 1, 1)

        self.doubleSpinBox_colorMax = QDoubleSpinBox(self.widget_3)
        self.doubleSpinBox_colorMax.setObjectName(u"doubleSpinBox_colorMax")

        self.gridLayout_6.addWidget(self.doubleSpinBox_colorMax, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 3, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.groupBox_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.gridLayout_3 = QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(14)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)

        self.widget_4 = QWidget(self.frame_5)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_10 = QGridLayout(self.widget_4)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(-1, 0, 0, 0)
        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_10.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_10.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_7 = QLabel(self.widget_4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_10.addWidget(self.label_7, 4, 0, 1, 1)

        self.lineEdit_colorLabel = QLineEdit(self.widget_4)
        self.lineEdit_colorLabel.setObjectName(u"lineEdit_colorLabel")
        self.lineEdit_colorLabel.setMaximumSize(QSize(95, 16777215))
        self.lineEdit_colorLabel.setFrame(True)
        self.lineEdit_colorLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_colorLabel.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout_10.addWidget(self.lineEdit_colorLabel, 4, 1, 1, 1)

        self.lineEdit_yLabel = QLineEdit(self.widget_4)
        self.lineEdit_yLabel.setObjectName(u"lineEdit_yLabel")
        self.lineEdit_yLabel.setMaximumSize(QSize(95, 16777215))
        self.lineEdit_yLabel.setFrame(True)
        self.lineEdit_yLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_yLabel.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout_10.addWidget(self.lineEdit_yLabel, 1, 1, 1, 1)

        self.lineEdit_xLabel = QLineEdit(self.widget_4)
        self.lineEdit_xLabel.setObjectName(u"lineEdit_xLabel")
        self.lineEdit_xLabel.setMaximumSize(QSize(95, 16777215))
        self.lineEdit_xLabel.setFrame(True)
        self.lineEdit_xLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_xLabel.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout_10.addWidget(self.lineEdit_xLabel, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.widget_4, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_11 = QFrame(self.groupBox_2)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy1.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy1)
        self.frame_11.setMaximumSize(QSize(16777215, 80))
        self.gridLayout_7 = QGridLayout(self.frame_11)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(14)
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_11)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_7.addWidget(self.label_19, 0, 0, 1, 1)

        self.widget_5 = QWidget(self.frame_11)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_11 = QGridLayout(self.widget_5)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(-1, 0, 0, 0)
        self.label_17 = QLabel(self.widget_5)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_11.addWidget(self.label_17, 3, 0, 1, 1)

        self.label_18 = QLabel(self.widget_5)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_11.addWidget(self.label_18, 0, 0, 1, 1)

        self.spinBox_axisLabelSize = QSpinBox(self.widget_5)
        self.spinBox_axisLabelSize.setObjectName(u"spinBox_axisLabelSize")
        self.spinBox_axisLabelSize.setMinimum(1)
        self.spinBox_axisLabelSize.setMaximum(30)
        self.spinBox_axisLabelSize.setValue(20)

        self.gridLayout_11.addWidget(self.spinBox_axisLabelSize, 0, 1, 1, 1)

        self.spinBox_tickLabelSize = QSpinBox(self.widget_5)
        self.spinBox_tickLabelSize.setObjectName(u"spinBox_tickLabelSize")
        self.spinBox_tickLabelSize.setMinimum(1)
        self.spinBox_tickLabelSize.setMaximum(30)
        self.spinBox_tickLabelSize.setValue(12)

        self.gridLayout_11.addWidget(self.spinBox_tickLabelSize, 3, 1, 1, 1)


        self.gridLayout_7.addWidget(self.widget_5, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.groupBox_2)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy1.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy1)
        self.frame_12.setMaximumSize(QSize(16777215, 80))
        self.gridLayout_8 = QGridLayout(self.frame_12)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(14)
        self.gridLayout_8.setVerticalSpacing(0)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_selectColormap = QPushButton(self.frame_12)
        self.pushButton_selectColormap.setObjectName(u"pushButton_selectColormap")

        self.gridLayout_8.addWidget(self.pushButton_selectColormap, 1, 0, 1, 1)

        self.checkBox_colormapIsReversed = QCheckBox(self.frame_12)
        self.checkBox_colormapIsReversed.setObjectName(u"checkBox_colormapIsReversed")

        self.gridLayout_8.addWidget(self.checkBox_colormapIsReversed, 1, 1, 1, 1)

        self.label_20 = QLabel(self.frame_12)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_8.addWidget(self.label_20, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_12)

        self.frame_31 = QFrame(self.groupBox_2)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_31)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.checkBox_3d = QCheckBox(self.frame_31)
        self.checkBox_3d.setObjectName(u"checkBox_3d")

        self.horizontalLayout.addWidget(self.checkBox_3d)

        self.radioButton = QRadioButton(self.frame_31)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.frame_31)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout.addWidget(self.radioButton_2)


        self.verticalLayout_2.addWidget(self.frame_31)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.frame_41 = QFrame(self.frame)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_plot = QPushButton(self.frame_41)
        self.pushButton_plot.setObjectName(u"pushButton_plot")
        self.pushButton_plot.setMinimumSize(QSize(0, 23))

        self.horizontalLayout_4.addWidget(self.pushButton_plot)

        self.pushButton_save = QPushButton(self.frame_41)
        self.pushButton_save.setObjectName(u"pushButton_save")
        sizePolicy2.setHeightForWidth(self.pushButton_save.sizePolicy().hasHeightForWidth())
        self.pushButton_save.setSizePolicy(sizePolicy2)
        icon3 = QIcon()
        icon3.addFile(u":/icon/imgs/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_save.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.pushButton_save)


        self.verticalLayout.addWidget(self.frame_41)

        self.listWidget = QListWidget(self.frame)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout.addWidget(self.listWidget)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_figure = QFrame(self.widget)
        self.frame_figure.setObjectName(u"frame_figure")
        self.frame_figure.setFrameShape(QFrame.StyledPanel)
        self.frame_figure.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_figure)


        self.verticalLayout_3.addWidget(self.widget)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
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
        QWidget.setTabOrder(self.doubleSpinBox_Xinterval, self.doubleSpinBox_Yinterval)
        QWidget.setTabOrder(self.doubleSpinBox_Yinterval, self.checkBox_origin)
        QWidget.setTabOrder(self.checkBox_origin, self.doubleSpinBox_colorMax)
        QWidget.setTabOrder(self.doubleSpinBox_colorMax, self.doubleSpinBox_colorMin)
        QWidget.setTabOrder(self.doubleSpinBox_colorMin, self.doubleSpinBox_colorinterval)
        QWidget.setTabOrder(self.doubleSpinBox_colorinterval, self.lineEdit_xLabel)
        QWidget.setTabOrder(self.lineEdit_xLabel, self.lineEdit_yLabel)
        QWidget.setTabOrder(self.lineEdit_yLabel, self.lineEdit_colorLabel)
        QWidget.setTabOrder(self.lineEdit_colorLabel, self.spinBox_axisLabelSize)
        QWidget.setTabOrder(self.spinBox_axisLabelSize, self.spinBox_tickLabelSize)
        QWidget.setTabOrder(self.spinBox_tickLabelSize, self.pushButton_selectColormap)
        QWidget.setTabOrder(self.pushButton_selectColormap, self.checkBox_colormapIsReversed)
        QWidget.setTabOrder(self.checkBox_colormapIsReversed, self.checkBox_3d)
        QWidget.setTabOrder(self.checkBox_3d, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.radioButton_2)
        QWidget.setTabOrder(self.radioButton_2, self.pushButton_plot)
        QWidget.setTabOrder(self.pushButton_plot, self.pushButton_save)
        QWidget.setTabOrder(self.pushButton_save, self.listWidget)
        QWidget.setTabOrder(self.listWidget, self.toolButton_substractFile)
        QWidget.setTabOrder(self.toolButton_substractFile, self.toolButton_addFile)

        self.menubar.addAction(self.menu_Help.menuAction())
        self.menu_Help.addAction(self.action_User_s_manual)

        self.retranslateUi(MainWindow)

        self.pushButton_save.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Csv Heatmapper", None))
        self.action_User_s_manual.setText(QCoreApplication.translate("MainWindow", u"&User's manual", None))
        self.groupBox_file.setTitle(QCoreApplication.translate("MainWindow", u"CSV File", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Plot Setting", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"X Interval", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Y Interval", None))
        self.checkBox_origin.setText(QCoreApplication.translate("MainWindow", u"Turn the origin into (0, 0)", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Axis Scale", None))
        self.label_11.setProperty("class", QCoreApplication.translate("MainWindow", u"bold", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Color Scale", None))
        self.label_12.setProperty("class", QCoreApplication.translate("MainWindow", u"bold", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Interval", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.label_13.setProperty("class", QCoreApplication.translate("MainWindow", u"bold", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"X Label", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Y Label", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ColorBar Label", None))
        self.lineEdit_colorLabel.setText(QCoreApplication.translate("MainWindow", u"z ()", None))
        self.lineEdit_yLabel.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.lineEdit_xLabel.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Font Size", None))
        self.label_19.setProperty("class", QCoreApplication.translate("MainWindow", u"bold", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Tick Label", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Axis Label", None))
        self.pushButton_selectColormap.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.checkBox_colormapIsReversed.setText(QCoreApplication.translate("MainWindow", u"Reversed", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Color Map", None))
        self.label_20.setProperty("class", QCoreApplication.translate("MainWindow", u"bold", None))
        self.checkBox_3d.setText(QCoreApplication.translate("MainWindow", u"3D", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Scatter", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Surface", None))
        self.pushButton_plot.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.pushButton_save.setText("")
        self.menu_Help.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
    # retranslateUi

