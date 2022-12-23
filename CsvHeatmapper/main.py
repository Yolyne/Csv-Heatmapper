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
from matplotlib.transforms import Bbox


# from stage_controller import StageController

# from stage_controller import StageNo

from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QDialog,
    QLabel,
    QLineEdit,
    QAbstractSpinBox,
    QDoubleSpinBox,
    QWidget,
    QFileDialog,
    QVBoxLayout,
    QButtonGroup,
    QRadioButton,
    QToolButton,
    QScrollArea,
    QSizePolicy,
    QFrame,
    QListView,
    QAbstractItemView,
    QPushButton,
    QListWidgetItem,
    QCheckBox,
)
from PySide6 import QtCore, QtGui
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

# from ui.ui_generated_LoadedFilesWidget import Ui_Form

# from ui.ui_generated_setup_dialog import Ui_Dialog

from window_controller import WindowController


APP_NAME = "CsvHeatmapper"
COMPANY = "Yolyne"
setting = QSettings(COMPANY, APP_NAME)
if not setting.value("last_dir"):
    setting.setValue("last_dir", os.path.expanduser("~/Documents"))


class LoadedFilesWidget(QWidget):
    def __init__(
        self,
        parent: QWidget = None,
        title="",
        window_controller: WindowController = None,
    ):
        super().__init__(parent)
        self.controller = window_controller
        self.setMinimumSize(164, 0)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setGeometry(
        #     self.screen().availableGeometry().right(),
        #     self.screen().availableGeometry().bottom(),
        #     window_controller.preview_width,
        #     window_controller.preview_height,
        # )
        self.move(22, 55)

        self.toggle_button = QToolButton(
            text=title, checkable=True, checked=False
        )
        self.toggle_button.setObjectName("toggle_button")
        self.toggle_button.setStyleSheet(
            """QToolButton {border:1px solid #8f8f91;}
QToolButton:hover {
    border-color: #a5f6ff;
    background-color: #e5fcff;
}
QToolButton:pressed {
    border-color: #aaa;
    background-color: #ccc;
}"""
        )
        self.toggle_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toggle_button.setArrowType(Qt.RightArrow)
        self.toggle_button.pressed.connect(self.on_pressed)
        self.toggle_button.setFixedSize(164, 24)
        self.toggle_animation = QParallelAnimationGroup(self)

        self.back = back = QPushButton(parent)
        back.setGeometry(0, 0, 0, 0)
        back.setStyleSheet("background:rgba(0, 0, 0, 128)")
        back.stackUnder(self)
        back.clicked.connect(self.toggle_button.click)

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
        # checked = self.toggle_button.setChecked()
        checked = self.toggle_button.isChecked()
        if checked:
            self.back.setGeometry(0, 0, 0, 0)
        else:
            self.back.setGeometry(0, 22, 2000, 1500)
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
        ui.action_User_s_manual.triggered.connect(controller.show_manual)

        self.listView.selectionModel().selectionChanged.connect(
            self._on_file_selection_changed
        )
        # controller.loadedFilesModel.selectionChanged.connect(lambda v: print(v))
        ui.toolButton_addFile.clicked.connect(self._button_addFile_clicked)
        ui.toolButton_substractFile.clicked.connect(
            self._button_sabstractFile_clicked
        )

        ui.checkBox_origin.stateChanged.connect(
            self._on_checkBox_origin_checked
        )

        # def _set_attr(obj, name, value):
        #     print(name, value)
        #     setattr(obj, name, value)

        def _on_textChanged(value, lineEdit: QWidget, property_name):
            # print(value)
            _pos = lineEdit.cursorPosition()
            setattr(controller, property_name, value)
            lineEdit.setCursorPosition(_pos)
            # print(getattr(controller, property_name))

        def _axis_scale_max_changed(value, property_name):
            if property_name == "xMax":
                ui.doubleSpinBox_Xinterval.setMaximum(value)
            else:  # "yMax"
                ui.doubleSpinBox_Yinterval.setMaximum(value)
            setattr(controller, property_name, value)

        widget: QWidget
        for widget in self.findChildren(QWidget):
            if widget_name := widget.objectName():
                controller_property_name = widget_name.split("_")[-1]
                # print(controller_property_name)
                if widget_name in {"doubleSpinBox_xMax", "doubleSpinBox_yMax"}:
                    widget.valueChanged.connect(
                        lambda v, property_name=controller_property_name: _axis_scale_max_changed(
                            v, property_name
                        )
                    )
                elif hasattr(widget, "valueChanged"):
                    widget.valueChanged.connect(
                        lambda v, property_name=controller_property_name: setattr(
                            controller, property_name, v
                        )
                    )
                    # widget.valueChanged.connect(
                    #     lambda v, property_name=controller_property_name: _set_attr(
                    #         controller, property_name, v
                    #     )
                    # )
                elif hasattr(widget, "textChanged"):
                    if isinstance(widget, QLineEdit):
                        widget: QLineEdit
                        lineEdit = widget
                    elif isinstance(widget, QAbstractSpinBox):
                        widget: QAbstractSpinBox
                        lineEdit = widget.lineEdit()
                    widget.textChanged.connect(
                        lambda v, widget=lineEdit, property_name=controller_property_name: _on_textChanged(
                            v, widget, property_name
                        )
                    )

                    lineEdit.returnPressed.connect(
                        self._on_button_plot_clicked
                    )
                elif hasattr(widget, "stateChanged"):
                    widget.stateChanged.connect(
                        lambda v, property_name=controller_property_name: setattr(
                            controller, property_name, v
                        )
                    )

        def _on_propertyChanged(property_name, value):
            pattern = QRegularExpression(property_name)
            # print(property_name, value)
            widget = self.findChildren(QWidget, pattern)[0]
            if isinstance(widget, QAbstractSpinBox):
                widget.setValue(value)
            elif isinstance(widget, QLineEdit):
                widget.setText(value)
            # elif isinstance(widget, QComboBox):
            #     widget.setItems(value)

        controller.propertyChanged.connect(_on_propertyChanged)
        controller.valueRangeChanged.connect(self._on_valueRangeChanged)

        controller.max_larger_min.connect(self._on_max_larger_min)

        ui.pushButton_selectColormap.clicked.connect(self._open_colorpicker)

        ui.spinBox_decimalPlaces.valueChanged.connect(
            self._on_decimalPlaces_changed
        )

        ui.checkBox_3d.stateChanged.connect(controller.set_is_3d)
        controller.data_is_too_big.connect(self._change_checkBox_3d_state)
        # controller.data_changed.connect(self._updata_spinbox_max)

        controller.analyzedvalues_changed.connect(ui.statusbar.showMessage)

        ui.pushButton_plot.clicked.connect(self._on_button_plot_clicked)
        ui.pushButton_save.clicked.connect(self._on_button_save_clicked)

    def _on_valueRangeChanged(self, width, height, min, max):
        # self.ui.doubleSpinBox_Xinterval.setMaximum(width)
        # self.ui.doubleSpinBox_Yinterval.setMaximum(height)
        self.ui.doubleSpinBox_Xinterval.setRange(width / 40, width)
        self.ui.doubleSpinBox_Yinterval.setRange(height / 40, height)
        self.ui.doubleSpinBox_colorMax.setRange(min, max)
        self.ui.doubleSpinBox_colorMin.setRange(min, max)
        # self.ui.doubleSpinBox_colorinterval.setMaximum(max - min)
        self.ui.doubleSpinBox_colorinterval.setRange(
            (max - min) / 40, max - min
        )

    def _get_ui_properties(self):
        # self.controller.exposure_time_decimals = (
        #     self.ui.doubleSpinBox_exposure.decimals()
        # )
        pass

    def _add_ui_properties(self):
        ui = self.ui
        controller = self.controller

        ui.doubleSpinBox_Xinterval.setValue(controller.Xinterval)
        ui.doubleSpinBox_Yinterval.setValue(controller.Yinterval)
        ui.doubleSpinBox_xMax.setValue(controller.xMax)
        ui.doubleSpinBox_yMax.setValue(controller.yMax)
        ui.doubleSpinBox_colorMax.setValue(controller.colorMax)
        ui.doubleSpinBox_colorMin.setValue(controller.colorMin)
        ui.doubleSpinBox_colorinterval.setValue(controller.colorinterval)
        ui.lineEdit_xLabel.setText(controller.xLabel)
        ui.lineEdit_yLabel.setText(controller.yLabel)
        ui.lineEdit_colorLabel.setText(controller.colorLabel)
        ui.spinBox_axisLabelSize.setValue(controller.axisLabelSize)
        ui.spinBox_tickLabelSize.setValue(controller.tickLabelSize)

        def _textFromValue(value, self):
            return str(round(value, self.decimals())).rstrip("0").rstrip(".")
            # return str(value).rstrip()

        sb: QDoubleSpinBox
        for sb in self.findChildren(QWidget):
            if isinstance(sb, QDoubleSpinBox):
                sb.textFromValue = lambda v, sb=sb: _textFromValue(v, sb)

        groupBox_file_dummy = QWidget(self.ui.frame)
        groupBox_file_dummy.setMinimumSize(0, 60)
        self.ui.verticalLayout.insertWidget(0, groupBox_file_dummy)
        gb = ui.groupBox_file
        gb.setParent(self)
        gb.setGeometry(10, 32, 220, 60)
        loadedFilesWidget = LoadedFilesWidget(self, "Loaded Files", controller)
        ui.groupBox_file.stackUnder(loadedFilesWidget)
        lay = QVBoxLayout()
        lay.setContentsMargins(0, 0, 0, 0)
        self.listView = listView = QListView(loadedFilesWidget)
        listView.setModel(controller.loadedFilesModel)
        listView.setSelectionModel(controller.selectionModel)
        listView.setSelectionMode(QAbstractItemView.MultiSelection)

        def _listView_keyPressEvent(event):
            if event.key() == Qt.Key_Delete:
                self._button_sabstractFile_clicked()

        listView.keyPressEvent = _listView_keyPressEvent
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
        dir_open = (
            setting.value("last_dir")
            if os.path.exists(setting.value("last_dir"))
            else os.path.expanduser("~/Documents")
        )
        files = QFileDialog.getOpenFileNames(
            self,
            "Select",
            filter="CSV-like files (*.csv *.xlsx)",
            dir=dir_open,
        )[0]

        if files:
            setting.setValue("last_dir", os.path.dirname(files[-1]))
        return files

    def _on_checkBox_origin_checked(self, checked: int):
        setattr(
            self.controller,
            self.ui.checkBox_origin.objectName().split()[-1],
            bool(checked),
        )
        if checked:
            self.ui.frame_axisMax.setEnabled(True)
            self.ui.doubleSpinBox_Xinterval.setRange(
                self.ui.doubleSpinBox_xMax.value() / 40,
                self.ui.doubleSpinBox_xMax.value(),
            )
            self.ui.doubleSpinBox_Yinterval.setRange(
                self.ui.doubleSpinBox_yMax.value() / 40,
                self.ui.doubleSpinBox_yMax.value(),
            )
            # self.ui.doubleSpinBox_Xinterval.setMaximum(
            #     self.ui.doubleSpinBox_xMax.value()
            # )
            # self.ui.doubleSpinBox_Yinterval.setMaximum(
            #     self.ui.doubleSpinBox_yMax.value()
            # )
        else:
            self.ui.frame_axisMax.setEnabled(False)
            self.ui.doubleSpinBox_Xinterval.setRange(
                self.controller.figure_handler.datas_width / 40,
                self.controller.figure_handler.datas_width,
            )
            self.ui.doubleSpinBox_Yinterval.setRange(
                self.controller.figure_handler.datas_height / 40,
                self.controller.figure_handler.datas_height,
            )
            # self.ui.doubleSpinBox_Xinterval.setMaximum(
            #     self.controller.figure_handler.datas_width
            # )
            # self.ui.doubleSpinBox_Yinterval.setMaximum(
            #     self.controller.figure_handler.datas_height
            # )

    def _on_max_larger_min(self, max_larger_min):
        self.ui.pushButton_plot.setEnabled(max_larger_min)
        if max_larger_min:
            self.ui.listWidget.takeItem(0)
        else:
            if self.ui.listWidget.count() == 1:
                return
            item = QListWidgetItem()
            self.ui.listWidget.addItem(item)
            label = QLabel(
                '<font color="red">Error</font>: Max must be larger than Min in Color Scale.'
            )
            item.setSizeHint(label.sizeHint())
            self.ui.listWidget.setItemWidget(item, label)

    def _open_colorpicker(self):
        if self.colordialog is None:
            self.colordialog = ColormapPickerDialog(
                self, window_controller=self.controller
            )
        self.colordialog.show()

    def _on_decimalPlaces_changed(self, value):
        sb: QDoubleSpinBox
        for sb in self.findChildren(QWidget):
            if isinstance(sb, QDoubleSpinBox):
                sb.setDecimals(value)
                # sb.setMinimum(float("0." + "0" * (value - 1) + "1"))

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
            file = self.controller.loadedFilesModel.files[0]
            name = os.path.splitext(os.path.basename(file))[0]
            savepath, filetype = QFileDialog.getSaveFileName(
                self,
                "Save as",
                filter="Info (*.csv);;PNG (*.png);;eps (*.eps);;JPEG (*.jpeg);;JPEG (*.jpg);;PDF (*.pdf);;PGF (*.pgf);;PS (*.ps);;RAW (*.raw);;RGBA (*.rgba);;SVG (*.svg);;SVGZ (*.svgz);;Tiff (*.tif);;Tiff (*.tiff)",
                dir=setting.value("last_dir") + f"/heatmap-{name}.png",
                selectedFilter="PNG",
            )
            if savepath:
                if filetype == "Info (*.csv)":
                    self._save_analyzed_data(savepath)
                else:
                    self.controller.figure.savefig(
                        savepath, bbox_inches="tight", transparent=True
                    )
                    # self.controller.figure
                setting.setValue("last_dir", os.path.dirname(savepath))
        else:
            now = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
            dir = f"{os.path.expanduser('~/Downloads')}/Heatmap ({now})"
            os.mkdir(dir)
            width, height = self.controller.figure.get_size_inches()
            # print(
            #     [
            #         axis.get_window_extent().transformed(
            #             self.controller.figure.dpi_scale_trans.inverted()
            #         )
            #         for axis in self.controller.figure.axes
            #     ]
            # )
            # bboxes = [
            #     axis.get_window_extent().transformed(
            #         self.controller.figure.dpi_scale_trans.inverted()
            #     )
            #     for axis in self.controller.figure.axes
            # ]
            # [ for plot, cbar in zip(bboxes[:count], bboxes[count:])]
            def full_extent(ax, cbar, pad=0.0) -> Bbox:
                """Get the full extent of an axes, including axes labels, tick labels, and
                titles."""
                # For text objects, we need to draw the figure first, otherwise the extents
                # are undefined.
                # ax.figure.canvas.draw()
                # items = ax.get_xticklabels() + ax.get_yticklabels()
                items = [
                    ax,
                    ax.title,
                    ax.xaxis.label,
                    ax.yaxis.label,
                    cbar.yaxis.label,
                ]
                # items += [ax, ax.title]
                bbox = Bbox.union([item.get_window_extent() for item in items])

                return bbox.expanded(1.0 + pad, 1.0 + 0.05)

            # print(width, height)
            height = height // count
            # for i, file in enumerate(self.controller.loadedFilesModel.files):
            #     name = os.path.splitext(os.path.basename(file))[0]
            #     self.controller.figure.savefig(
            #         f"{dir}/heatmap-{name}.png",
            #         transparent=True,
            #         bbox_inches=mpl.transforms.Bbox(
            #             # This is in "figure fraction" for the bottom half
            #             # input in [[xmin, ymin], [xmax, ymax]]
            #             [
            #                 [0, height * (count - i - 1)],
            #                 [width, height * (count - i)],
            #             ]
            #         ),
            #     )
            print(
                self.controller.figure.axes[:count],
                self.controller.figure.axes[count:],
            )
            i = 1
            for plot, cbar, file in zip(
                self.controller.figure.axes[:count],
                self.controller.figure.axes[count:],
                self.controller.loadedFilesModel.files,
            ):
                # now = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
                name = os.path.splitext(os.path.basename(file))[0]
                extent = full_extent(plot, cbar).transformed(
                    self.controller.figure.dpi_scale_trans.inverted()
                )
                self.controller.figure.savefig(
                    f"{dir}/heatmap-{name}-{i}.png",
                    transparent=True,
                    bbox_inches=extent,
                )
                i += 1
            # self._save_analyzed_data(f"{dir}/info.csv")

    def _save_analyzed_data(self, savepath):
        # header = ",".join(
        header = [
            "name",
            "height",
            "width",
            "size",
            "max",
            "min",
            "mean",
            "median",
            "std",
        ]
        import numpy
        import pandas as pd

        # arr = pd.DataFrame(
        #     (

        #             [
        #                 [file]
        #                 for file in self.controller.loadedFilesModel.files
        #             ],
        #             dtype=str,
        #         ),
        #         self.controller.figure_handler.datas_analyzed,
        #     ),
        # )
        # arr = pd.concat()
        df = pd.DataFrame(self.controller.figure_handler.datas_analyzed)
        df = pd.concat(
            (pd.Series(self.controller.loadedFilesModel.files), df), axis=1
        )
        df.columns = header
        # df.set_index(pd.Series(self.controller.loadedFilesModel.files))
        # print(df)
        # numpy.savetxt(
        #     savepath,
        #     arr,
        #     fmt=["%s"] + ["%d"] * 3 + ["%f"] * 5,
        #     delimiter=",",
        #     header=header,
        # )
        df.to_csv(savepath, index=False)


def main():
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
