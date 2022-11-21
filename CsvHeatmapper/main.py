import sys
from time import sleep
import os
import logging
from logging.handlers import RotatingFileHandler

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar,
)


# from stage_controller import StageController

# from stage_controller import StageNo

from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QDialog,
    QMessageBox,
    QLabel,
    QLineEdit,
    QAbstractSpinBox,
    QWidget,
    QFileDialog,
    QVBoxLayout,
    QButtonGroup,
    QRadioButton,
    QToolButton,
    QScrollArea,
    QSizePolicy,
    QFrame,
)
from PySide6 import QtGui, QtMultimedia
from PySide6.QtCore import (
    QRegularExpression,
    QSettings,
    Qt,
    QAbstractAnimation,
    QParallelAnimationGroup,
    QPropertyAnimation,
)

# from ui.my_widgets import DoubleDragSpinBox, StatusWidget

# from PySide6.QtGui import

# from ui.ui_main_window import UiMainWindow
from ui.ui_generated_main_window import Ui_MainWindow
from ui.ui_generated_ColormapPicker import Ui_Dialog

# from ui.ui_generated_setup_dialog import Ui_Dialog

from window_controller import WindowController


APP_NAME = "CsvHeatmapper"
COMPANY = "Yolyne"
setting = QSettings(COMPANY, APP_NAME)
if setting.value("last_dir") == "":
    setting.setValue("last_dir", os.path.expanduser("~/Documents"))


class CollapsibleBox(QWidget):
    def __init__(self, title="", parent=None):
        super(CollapsibleBox, self).__init__(parent)

        self.toggle_button = QToolButton(
            text=title, checkable=True, checked=False
        )
        self.toggle_button.setStyleSheet("QToolButton { border: none; }")
        self.toggle_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toggle_button.setArrowType(Qt.RightArrow)
        self.toggle_button.pressed.connect(self.on_pressed)

        self.toggle_animation = QParallelAnimationGroup(self)

        self.content_area = QScrollArea(maximumHeight=0, minimumHeight=0)
        self.content_area.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Fixed
        )
        self.content_area.setFrameShape(QFrame.NoFrame)

        lay = QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.toggle_button)
        lay.addWidget(self.content_area)

        self.toggle_animation.addAnimation(
            QPropertyAnimation(self, b"minimumHeight")
        )
        self.toggle_animation.addAnimation(
            QPropertyAnimation(self, b"maximumHeight")
        )
        self.toggle_animation.addAnimation(
            QPropertyAnimation(self.content_area, b"maximumHeight")
        )

    # @pyqtSlot()
    def on_pressed(self):
        checked = self.toggle_button.isChecked()
        self.toggle_button.setArrowType(
            Qt.DownArrow if not checked else Qt.RightArrow
        )
        self.toggle_animation.setDirection(
            QAbstractAnimation.Forward
            if not checked
            else QAbstractAnimation.Backward
        )
        self.toggle_animation.start()

    def setContentLayout(self, layout):
        lay = self.content_area.layout()
        del lay
        self.content_area.setLayout(layout)
        collapsed_height = (
            self.sizeHint().height() - self.content_area.maximumHeight()
        )
        content_height = layout.sizeHint().height()
        for i in range(self.toggle_animation.animationCount()):
            animation = self.toggle_animation.animationAt(i)
            animation.setDuration(500)
            animation.setStartValue(collapsed_height)
            animation.setEndValue(collapsed_height + content_height)

        content_animation = self.toggle_animation.animationAt(
            self.toggle_animation.animationCount() - 1
        )
        content_animation.setDuration(500)
        content_animation.setStartValue(0)
        content_animation.setEndValue(content_height)


class ColormapPickerDialog(QDialog):
    def __init__(self, parent, window_controller: WindowController):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.controller = window_controller

        self._arrange_radiobuttons()

    def _arrange_radiobuttons(self):
        cm_num = len(self.controller.colormaps) // 2
        ncols = cm_num // 3 + 1
        radioGroup = QButtonGroup(self)
        cm_rbtns = [
            QRadioButton(self.ui.frame_colormaps)
            for cm in self.controller.colormaps[:cm_num]
        ]
        for i, rbtn in enumerate(cm_rbtns):
            radioGroup.addButton(rbtn, i)
            rbtn.move(12 + 30 * (i % ncols), 24 + 200 * (i // ncols))
        radioGroup.idClicked.connect(
            lambda i: setattr(self.controller, "colorMap", i)
        )
        # ラジオボタンオブジェクトのグループ登録
        # self.radioGroup.addButton(radioButton1, 1)
        # self.radioGroup.addButton(radioButton2, 2)
        # self.radioGroup.addButton(radioButton3, 3)

        # # ラジオボタンの配置設定
        # radioButton1.move(10, 0)


class MainWindow(QMainWindow):
    def __init__(self):
        self.controller = WindowController()
        self.colordialog = None
        self._setup_app()
        self._connect_signal_slot()

        # self.preview_window: QWidget = None

    def _setup_app(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self._get_ui_properties()
        self._add_ui_properties()

    def _connect_signal_slot(self):
        ui = self.ui
        controller = self.controller

        ui.toolButton_addFile.clicked.connect(self._button_addFile_clicked)
        ui.toolButton_substractFile.clicked.connect(
            self._button_sabstractFile_clicked
        )

        # def _set_attr(obj, name, value):
        #     print(name, value)
        #     setattr(obj, name, value)

        widget: QWidget
        for widget in self.findChildren(QWidget):
            if widget_name := widget.objectName():
                controller_property = widget_name.split("_")[-1]
                # print(controller_property)
                if hasattr(widget, "valueChanged"):
                    widget.valueChanged.connect(
                        lambda v, property=controller_property: setattr(
                            controller, property, v
                        )
                    )
                    # widget.valueChanged.connect(
                    #     lambda v: _set_attr(controller, controller_property, v)
                    # )
                elif hasattr(widget, "textChanged"):
                    widget.textChanged.connect(
                        lambda v, property=controller_property: setattr(
                            controller, property, v
                        )
                    )

        def _on_propertyChanged(property, value):
            pattern = QRegularExpression(property)
            print(property, value)
            widget = self.findChildren(QWidget, pattern)[0]
            if isinstance(widget, QAbstractSpinBox):
                widget.setValue(value)
            elif isinstance(widget, QLineEdit):
                widget.setText(value)

        controller.propertyChanged.connect(_on_propertyChanged)
        controller.valueRangeChanged.connect(self._on_valueRangeChanged)

        ui.pushButton_selectColormap.clicked.connect(self._open_colorpicker)

        ui.checkBox_3d.stateChanged.connect(controller.set_is_3d)
        controller.data_is_too_big.connect(self._change_checkBox_3d_state)
        # controller.data_changed.connect(self._updata_spinbox_max)

        controller.analyzedvalues_changed.connect(ui.statusbar.showMessage)

        ui.pushButton_plot.clicked.connect(self._on_button_plot_clicked)
        ui.pushButton_save.clicked.connect(self._on_button_save_clicked)

    def _on_valueRangeChanged(self, width, height, min, max):
        self.ui.doubleSpinBox_Xinterval.setMaximum(width)
        self.ui.doubleSpinBox_Yinterval.setMaximum(height)
        self.ui.doubleSpinBox_colorMax.setRange(min, max)
        self.ui.doubleSpinBox_colorMin.setRange(min, max)
        self.ui.doubleSpinBox_colorinterval.setMaximum(max - min)

    def _get_ui_properties(self):
        # self.controller.exposure_time_decimals = (
        #     self.ui.doubleSpinBox_exposure.decimals()
        # )
        pass

    def _add_ui_properties(self):
        ui = self.ui
        controller = self.controller

        # collapsiblebox = CollapsibleBox("Files")
        # ui.groupBox_file.layout().insertWidget(0, collapsiblebox)
        # self.vlay = QVBoxLayout()
        # collapsiblebox.setContentLayout(self.vlay)

        vlayout = QVBoxLayout(ui.frame_figure)
        # vlayout = QVBoxLayout(ui.scrollArea_figure)
        self.canvas = canvas = FigureCanvas(controller.figure)
        vlayout.addWidget(
            NavigationToolbar(
                canvas,
                self,
            )
        )
        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setWidget(canvas)
        # scrollArea.setMaximumHeight(270)
        scrollArea.setMinimumWidth(900)
        vlayout.addWidget(scrollArea)

        def scrolling(event):
            current = scrollArea.verticalScrollBar().value()
            if event.button == "down":
                scrollArea.verticalScrollBar().setValue(current + 100)
            else:
                scrollArea.verticalScrollBar().setValue(current - 100)

        self.canvas.mpl_connect("scroll_event", scrolling)

        # canvas.setFixedSize(canvas.size())
        # canvas.setMinimumSize(canvas.size())

    def _button_addFile_clicked(self):
        csv_paths = self._browse_inputfile()
        if csv_paths:
            # if csv_paths and csv_paths != self.ui.label_file.text():
            # self.ui.label_file.setText(csv_paths)
            # for csv_path in csv_paths:
            # label = QLabel(f"{csv_path}")
            # color = QtGui.QColor(*[random.randint(0, 255) for _ in range(3)])
            # label.setStyleSheet(
            #     "background-color: {}; color : white;".format(color.name())
            # )
            # label.setAlignment(Qt.AlignCenter)
            # self.vlay.addWidget(label)
            self.ui.comboBox_files.addItems(csv_paths)
            self.controller.load_files(
                [
                    self.ui.comboBox_files.itemText(i)
                    for i in range(self.ui.comboBox_files.count())
                ]
            )
            # self.controller.display_figure()
            width, height = (
                self.controller.figure.get_size_inches()
                * self.controller.figure.dpi
            )
            self.canvas.setFixedSize(width, height)
            self.canvas.draw()

    def _button_sabstractFile_clicked(self):
        pass

    def _browse_inputfile(self):
        files = QFileDialog.getOpenFileNames(
            self,
            "Select",
            filter="CSV-like files (*.csv *.xlsx)",
            dir=setting.value("last_dir"),
        )[0]

        if files:
            setting.setValue("last_dir", os.path.dirname(files[-1]))
        return files

    def _open_colorpicker(self):
        if self.colordialog is None:
            self.colordialog = ColormapPickerDialog(
                self, window_controller=self.controller
            )
        self.colordialog.show()

    def _change_checkBox_3d_state(self, data_is_big):
        if data_is_big:
            self.ui.checkBox_3d.setChecked(False)
            self.ui.checkBox_3d.setEnabled(False)
        else:
            self.ui.checkBox_3d.setEnabled(True)

    def _on_button_plot_clicked(self):
        self.controller.plot()
        self.canvas.draw()

    def _on_button_save_clicked(self):
        savepath, filetype = QFileDialog.getSaveFileName(
            self,
            "Save as",
            filter="Info (*.csv);;PNG (*.png);;eps (*.eps);;JPEG (*.jpeg);;JPEG (*.jpg);;PDF (*.pdf);;PGF (*.pgf);;PS (*.ps);;RAW (*.raw);;RGBA (*.rgba);;SVG (*.svg);;SVGZ (*.svgz);;Tiff (*.tif);;Tiff (*.tiff)",
            dir=setting.value("last_dir"),
            selectedFilter="PNG",
        )
        if filetype == "Info (*.csv)":
            self._save_analyzed_data(savepath)
        else:
            plt.savefig(savepath, bbox_inches="tight", transparent=True)

    def _save_analyzed_data(self, savepath):
        header = ",".join(
            [
                "height",
                "width",
                "size",
                "max",
                "min",
                "mean",
                "median",
                "std",
            ]
        )
        import numpy

        numpy.savetxt(
            savepath,
            self.controller.figure_handler.datas_analyzed,
            fmt="%.5f",
            delimiter=",",
            header=header,
        )


def main():
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
