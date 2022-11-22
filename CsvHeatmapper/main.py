import sys
from time import sleep
import os
from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler

import matplotlib as mpl
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
    QComboBox,
    QStyledItemDelegate,
    QListView,
    QAbstractItemView,
)
from PySide6 import QtGui, QtMultimedia
from PySide6.QtCore import (
    QRegularExpression,
    QSettings,
    Qt,
    QAbstractAnimation,
    QParallelAnimationGroup,
    QPropertyAnimation,
    QStringListModel,
    QEvent,
)

# from ui.my_widgets import DoubleDragSpinBox, StatusWidget

# from PySide6.QtGui import

# from ui.ui_main_window import UiMainWindow
from ui.ui_generated_main_window import Ui_MainWindow
from ui.ui_generated_ColormapPicker import Ui_Dialog

# from ui.ui_generated_LoadedFilesWidget import Ui_Form

# from ui.ui_generated_setup_dialog import Ui_Dialog

from window_controller import WindowController


APP_NAME = "CsvHeatmapper"
COMPANY = "Yolyne"
setting = QSettings(COMPANY, APP_NAME)
if setting.value("last_dir") == "":
    setting.setValue("last_dir", os.path.expanduser("~/Documents"))


class LoadedFilesWidget(QWidget):
    def __init__(
        self, parent=None, title="", window_controller: WindowController = None
    ):
        # def __init__(self, parent, window_controller: WindowController):
        super().__init__(parent)
        # super().__init__(parent)
        # self.ui = Ui_Form()
        # self.ui.setupUi(self)
        self.controller = window_controller
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setGeometry(
        #     self.screen().availableGeometry().right(),
        #     self.screen().availableGeometry().bottom(),
        #     window_controller.preview_width,
        #     window_controller.preview_height,
        # )
        self.move(18, 46)

        self.toggle_button = QToolButton(
            text=title, checkable=True, checked=False
        )
        # self.toggle_button.setStyleSheet("QToolButton { border: none; }")
        self.toggle_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toggle_button.setArrowType(Qt.RightArrow)
        self.toggle_button.pressed.connect(self.on_pressed)
        self.toggle_button.setFixedSize(164, 24)
        self.toggle_animation = QParallelAnimationGroup(self)

        self.content_area = QScrollArea(maximumHeight=0, minimumHeight=0)
        self.content_area.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Fixed
        )
        # self.content_area.setFixedSize(150, 24)
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

    # @QtCore.pyqtSlot()
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
            animation.setDuration(10)
            animation.setStartValue(collapsed_height)
            animation.setEndValue(collapsed_height + content_height)

        content_animation = self.toggle_animation.animationAt(
            self.toggle_animation.animationCount() - 1
        )
        content_animation.setDuration(10)
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

        self.listView.selectionModel().selectionChanged.connect(
            self._on_file_selection_changed
        )
        # controller.loadedFilesModel.selectionChanged.connect(lambda v: print(v))
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
            # print(property, value)
            widget = self.findChildren(QWidget, pattern)[0]
            if isinstance(widget, QAbstractSpinBox):
                widget.setValue(value)
            elif isinstance(widget, QLineEdit):
                widget.setText(value)
            # elif isinstance(widget, QComboBox):
            #     widget.setItems(value)

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

        loadedFilesWidget = LoadedFilesWidget(self, "Loaded Files", controller)
        loadedFilesWidget.setMinimumSize(164, 0)
        lay = QVBoxLayout()
        lay.setContentsMargins(0, 0, 0, 0)
        self.listView = listView = QListView(loadedFilesWidget)
        listView.setModel(controller.loadedFilesModel)
        listView.setSelectionModel(controller.selectionModel)
        # listView.setDragEnabled(True)
        listView.setSelectionMode(QAbstractItemView.MultiSelection)
        # listView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # listView.setSelectionBehavior(
        #     QAbstractItemView.SelectionBehavior.SelectRows
        # )
        lay.addWidget(listView)
        loadedFilesWidget.setContentLayout(lay)
        loadedFilesWidget.show()

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

    def _on_file_selection_changed(self, selected, deselected):
        # print(selected.indexes(), deselected.indexes())
        # print(self.controller.selectionModel.selectedIndexes())
        # self.controller.selected_file_indexes = (
        #     self.controller.selectionModel.selectedIndexes()
        # )
        # for i in self.controller.selectionModel.selectedIndexes():
        #     if i not in self.controller.selected_file_indexes:
        #         self.controller.selected_file_indexes.append(i)
        [
            self.controller.selected_file_indexes.add(i.row())
            for i in selected.indexes()
        ]
        [
            self.controller.selected_file_indexes.remove(i.row())
            for i in deselected.indexes()
        ]
        print(self.controller.selected_file_indexes)

    def _button_addFile_clicked(self):
        loading_csvs = self._browse_inputfile()
        if loading_csvs:
            self.controller.load_files(loading_csvs)
            width, height = (
                self.controller.figure.get_size_inches()
                * self.controller.figure.dpi
            )
            self.canvas.setFixedSize(width, height)
            self.canvas.draw()

    def _button_sabstractFile_clicked(self):
        # indexes = self.listView.selectedIndexes()
        # print(indexes)
        # if indexes:
        if self.controller.selected_file_indexes:
            # ind = {i.row() for i in self.controller.selected_file_indexes}
            ind = self.controller.selected_file_indexes
            # Clear the selection (as it is no longer valid).
            self.controller.selected_file_indexes = set()
            self.listView.clearSelection()
            print("aaa", ind)
            self.controller.unload_files(ind)
            width, height = (
                self.controller.figure.get_size_inches()
                * self.controller.figure.dpi
            )
            self.canvas.setFixedSize(width, height)

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
        if len(self.controller.figure_handler.datas):
            self.controller.plot()
            self.canvas.draw()

    def _on_button_save_clicked(self):
        if (count := len(self.controller.figure_handler.datas)) == 0:
            return
        elif (count := len(self.controller.figure_handler.datas)) == 1:
            savepath, filetype = QFileDialog.getSaveFileName(
                self,
                "Save as",
                filter="Info (*.csv);;PNG (*.png);;eps (*.eps);;JPEG (*.jpeg);;JPEG (*.jpg);;PDF (*.pdf);;PGF (*.pgf);;PS (*.ps);;RAW (*.raw);;RGBA (*.rgba);;SVG (*.svg);;SVGZ (*.svgz);;Tiff (*.tif);;Tiff (*.tiff)",
                dir=setting.value("last_dir"),
                selectedFilter="PNG",
            )
            if savepath:
                if filetype == "Info (*.csv)":
                    self._save_analyzed_data(savepath)
                else:
                    # plt.savefig(savepath, bbox_inches="tight", transparent=True)
                    self.controller.figure
                setting.setValue("last_dir", os.path.dirname(savepath))
        else:
            now = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
            dir = f"{os.path.expanduser('~/Downloads')}/Heatmap ({now})"
            os.mkdir(dir)
            width, height = self.controller.figure.get_size_inches()
            # print(width, height)
            height = height // count
            for i in range(count - 1, -1, -1):
                self.controller.figure.savefig(
                    f"{dir}/{count-i}.png",
                    transparent=True,
                    bbox_inches=mpl.transforms.Bbox(
                        # This is in "figure fraction" for the bottom half
                        # input in [[xmin, ymin], [xmax, ymax]]
                        [[0, height * i], [width, height * (i + 1)]]
                    ),
                )
            self._save_analyzed_data(f"{dir}/info.csv")

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
