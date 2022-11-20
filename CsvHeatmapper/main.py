import sys
from time import sleep
import os
import logging
from logging.handlers import RotatingFileHandler

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import (
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
)
from PySide6 import QtGui, QtMultimedia
from PySide6.QtCore import QRegularExpression, QSettings

# from ui.my_widgets import DoubleDragSpinBox, StatusWidget

# from PySide6.QtGui import

# from ui.ui_main_window import UiMainWindow
from ui.ui_generated_main_window import Ui_MainWindow

# from ui.ui_generated_setup_dialog import Ui_Dialog

from window_controller import WindowController


class MainWindow(QMainWindow):
    def __init__(self):
        self.controller = WindowController()
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

        ui.pushButton_browse.clicked.connect(self._button_browse_clicked)

        # def _set_attr(obj, name, value):
        #     print(name, value)
        #     setattr(obj, name, value)

        widget: QWidget
        for widget in self.findChildren(QWidget):
            if hasattr(widget, "valueChanged"):
                if widget_name := widget.objectName():
                    controller_property = widget_name.split("_")[-1]
                    print(controller_property)
                    widget.valueChanged.connect(
                        lambda v: setattr(controller, controller_property, v)
                    )
                    # widget.valueChanged.connect(
                    #     lambda v: _set_attr(controller, controller_property, v)
                    # )

        def _on_propertyChanged(property, value):
            # pattern = QRegularExpression(property)
            widget = self.findChildren(QWidget, property)[0]
            if isinstance(widget, QAbstractSpinBox):
                widget.setValue(value)
            elif isinstance(widget, QLineEdit):
                widget.setText(value)

        controller.propertyChanged.connect(_on_propertyChanged)

        def _on_valueRangeChanged(width, height, min, max):
            ui.doubleSpinBox_Xinterval.setMaximum(width)
            ui.doubleSpinBox_Yinterval.setMaximum(height)
            ui.doubleSpinBox_colorMax.setRange(min, max)
            ui.doubleSpinBox_colorMin.setRange(min, max)
            ui.doubleSpinBox_colorinterval.setMaximum(max - min)

        controller.valueRangeChanged.connect(_on_valueRangeChanged)
        # ui.doubleSpinBox_Xinterval.valueChanged.connect(
        #     controller.set_Xinterval
        # )
        # ui.doubleSpinBox_Xinterval.valueChanged.connect(
        #     controller.set_Yinterval
        # )
        # ui.doubleSpinBox_colorMax.valueChanged.connect(lambda _: setattr(controller, "", _))
        # ui.doubleSpinBox_colorMin.valueChanged.connect(controller.set_colorMin)
        # ui.doubleSpinBox_colorinterval.valueChanged.connect(
        #     controller.set_colorinterval
        # )
        # ui.lineEdit_xLabel.textChanged.connect(controller.set_xLabel)
        # ui.lineEdit_yLabel.textChanged.connect(controller.set_yLabel)
        # ui.lineEdit_colorLabel.textChanged.connect(controller.set_colorLabel)
        # ui.spinBox_axisLabelSize.valueChanged.connect(
        #     controller.set_axisLabelSize
        # )
        # ui.spinBox_tickLabelSize.valueChanged.connect(
        #     controller.set_tickLabelSize
        # )

        ui.checkBox_3d.stateChanged.connect(controller.set_is_3d)
        controller.data_is_too_big.connect(self._change_checkBox_3d_state)
        controller.data_changed.connect(self._updata_spinbox_max)

        controller.analyzedvalues_changed.connect(ui.statusbar.showMessage)

    def _get_ui_properties(self):
        # self.controller.exposure_time_decimals = (
        #     self.ui.doubleSpinBox_exposure.decimals()
        # )
        pass

    def _add_ui_properties(self):
        ui = self.ui
        controller = self.controller

        vlayout = QVBoxLayout(ui.frame_figure)
        self.canvas = canvas = FigureCanvas(controller.figure)
        vlayout.addWidget(canvas)
        vlayout.addWidget(
            NavigationToolbar(
                canvas,
                self,
            )
        )
        #     self.status_widget = StatusWidget()
        #     self.status_widget.progressBar.setVisible(False)
        #     self.ui.statusBar.addWidget(self.status_widget, 1)

        #     self.ui.tabWidget.setCurrentIndex(1)
        #     self.ui.tabWidget.removeTab(0)
        #     self.ui.tabWidget.removeTab(2)

        #     # self.setWindowFlags(Qt.FramelessWindowHint)
        #     # self.ui.button_stop.setEnabled(False)
        #     self.doubledragspinboxes: list[DoubleDragSpinBox] = sorted(
        #         [dsb for dsb in self.findChildren(DoubleDragSpinBox)],
        #         key=lambda _: _.objectName(),
        #     )
        #     self.doubledragspinboxes[2].setEnabled(False)
        #     self.doubledragspinboxes[4].setEnabled(False)
        #     self.current_angle_labels: list[QLabel] = sorted(
        #         [
        #             lbl
        #             for lbl in self.findChildren(
        #                 QLabel, QRegularExpression("current_angle")
        #             )
        #         ],
        #         key=lambda _: _.objectName(),
        #     )

        #     self.ui.doubleSpinBox.setMaximum(90)
        #     self.ui.doubleSpinBox_2.setMaximum(90)
        #     self.ui.doubleSpinBox_3.setMaximum(360)
        #     self.ui.doubleSpinBox_4.setMaximum(360)
        #     self.ui.doubleSpinBox_5.setMaximum(360)
        #     self.ui.doubleSpinBox_6.setMaximum(65)
        #     [
        #         dsb.setValue(stage.target_angle)
        #         for dsb, stage in zip(
        #             self.doubledragspinboxes, self.controller.stages
        #         )
        #     ]

        #     self.ui.doubleSpinBox_exposure.setRange(
        #         0.01, self.controller.exposure_range[1]
        #     )
        #     self.ui.doubleSpinBox_exposure.setValue(self.controller.exposure_time)
        #     self.ui.doubleSpinBox_exposure.divisor = 10
        #     self.ui.spinBox_gain.setRange(*self.controller.gain_range)
        #     self.ui.spinBox_gain.setValue(self.controller.gain)

        #     self.ui.comboBox_s3_interval.addItems(
        #         [f"{_}°" for _ in self.controller.s3_intervals]
        #     )
        #     self.ui.comboBox_s3_interval.setCurrentIndex(
        #         self.controller.s3_interval_index
        #     )

        #     self.ui.comboBox_shot.setEnabled(False)
        #     self.ui.comboBox_shot.addItems(self.controller.shot_counts)
        #     self.ui.comboBox_shot.setCurrentIndex(self.controller.shot_count_index)

        #     self.ui.comboBox_smoothing_sizes.addItems(
        #         self.controller.smoothing_sizes_text
        #     )

        #     self.ui.spinBox_ver_skip.setValue(self.controller.ver_skip)
        #     self.ui.spinBox_hor_skip.setValue(self.controller.hor_skip)

        #     self.ui.comboBox_filter.addItems(self.controller.filter_wavelens)
        #     self.ui.comboBox_filter.setCurrentIndex(self.controller.filters_index)
        pass

    def _button_browse_clicked(self):
        csv_path = self._browse_inputfile()
        if csv_path and csv_path != self.ui.label_file.text():
            self.ui.label_file.setText(csv_path)
            self.controller.load_file(csv_path)
            self.controller.display_figure()
            self.canvas.draw()

    def _browse_inputfile(self):
        return QFileDialog.getOpenFileName(
            self, "Select", filter="CSV-like files (*.csv *.xlsx)"
        )[0]

    def _change_checkBox_3d_state(self, data_is_big):
        if data_is_big:
            self.ui.checkBox_3d.setChecked(False)
            self.ui.checkBox_3d.setEnabled(False)
        else:
            self.ui.checkBox_3d.setEnabled(True)

    def _updata_spinbox_max(self, data_info):
        self.ui.doubleSpinBox_Xinterval = data_info[1]
        self.ui.doubleSpinBox_Yinterval = data_info[0]

    # def _show_preview(self):
    #     self.ui.button_preview.setEnabled(False)

    #     logger.info("preview button clicked")
    #     # if self.controller.camera_controller.previewThread:
    #     #     print(self.controller.camera_controller.previewThread.is_alive())
    #     des_pos = self.screen().availableGeometry().topLeft()
    #     self.move(des_pos)
    #     # sleep(0.1)

    #     # print("creating preview")
    #     if self.preview_window is None:
    #         self.preview_window = PreviewWindow(
    #             window_controller=self.controller
    #         )

    #     logger.info("showing preview")
    #     self.preview_window.show()

    # def _export_csv(self):
    #     dir_bin = QFileDialog.getExistingDirectory(
    #         self,
    #         "Select a folder contains binary files",
    #         self.controller.working_dir,
    #     )
    #     if dir_bin:
    #         self.controller.create_csv(dir_bin)

    # def _show_progressbar(self):
    #     self.status_widget.progressBar.setVisible(True)
    #     self.status_widget.progressBar.setRange(0, 0)

    # def _hide_progressbar(self):
    #     self.status_widget.progressBar.setVisible(False)
    #     self.status_widget.progressBar.setRange(0, 1)

    # def _fill_progressbar(self):
    #     self.status_widget.progressBar.setRange(0, 1)
    #     self.status_widget.progressBar.setValue(1)

    # def closeEvent(self, event):
    #     arm_stages_are_origin = all(
    #         angle == 0 for angle in self.controller.current_angles[:2]
    #     )

    #     if not arm_stages_are_origin:
    #         ret = self._popup_closing_message()
    #         if ret != QMessageBox.Ok:
    #             event.ignore()
    #             return

    #     # self.controller.app_closing = True
    #     for window in QApplication.topLevelWidgets():
    #         if not isinstance(window, QMainWindow):
    #             window.close()
    #     self.controller.on_close()
    #     return super().closeEvent(event)

    # def _popup_closing_message(self):
    #     message = QMessageBox(self)
    #     # message.setStyleSheet(".QLabel{min-width: 700px;}")
    #     message.setIcon(QMessageBox.Icon.Information)
    #     message.setWindowTitle("Confirmation")
    #     message.setText("<b>The stages will be returned to its origin.</b>")
    #     message.setInformativeText(
    #         '<nobr><font color="red">Set the sample table to the lowest position! (until the orange light under the table goes out)</font></nobr><br/>Press <b>"OK"</b> when you have lowered the table.</span>'
    #     )
    #     message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    #     return message.exec()


def main():
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
