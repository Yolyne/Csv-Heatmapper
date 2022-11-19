import sys
from time import sleep
import os
import logging
from logging.handlers import RotatingFileHandler

# from stage_controller import StageController

# from stage_controller import StageNo

from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QDialog,
    QMessageBox,
    QLabel,
    QWidget,
    QFileDialog,
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
        self.ui.pushButton_browse.clicked.connect(self._button_browse_clicked)

        # self.ui.doubleSpinBox.valueChanged.connect(self.controller.set_leftarm)
        # self.ui.doubleSpinBox_2.valueChanged.connect(
        #     self.controller.set_rightarm
        # )
        # self.ui.doubleSpinBox_3.valueChanged.connect(
        #     self.controller.set_polarizer
        # )
        # self.ui.doubleSpinBox_4.valueChanged.connect(
        #     self.controller.set_compensator
        # )
        # self.ui.doubleSpinBox_5.valueChanged.connect(
        #     self.controller.set_analyzer
        # )
        # self.ui.doubleSpinBox_6.valueChanged.connect(
        #     self.controller.set_detector
        # )

        # self.ui.button_rotate.clicked.connect(self._on_rotate_button_clicked)
        # self.controller.ready_rotate.connect(self._on_ready_rotate)

        # self.controller.current_angles_changed.connect(
        #     self._update_current_angles
        # )

        # self.ui.button_preview.clicked.connect(self._show_preview)
        # self.controller.preview_stopped.connect(self._on_preview_stopped)

        # self.controller.exposure_time_changed.connect(
        #     self.ui.doubleSpinBox_exposure.setValue
        # )
        # self.ui.doubleSpinBox_exposure.valueChanged.connect(
        #     self.controller.set_exposure_time
        # )
        # self.ui.pushButton_exposure_auto.clicked.connect(
        #     self._on_exposure_auto
        # )
        # self.controller.exposure_auto_completed.connect(
        #     self._on_exposure_auto_completed
        # )
        # self.ui.spinBox_gain.valueChanged.connect(self.controller.set_gain)

        # self.ui.comboBox_s3_interval.currentIndexChanged.connect(
        #     self.controller.set_s3_interval_index
        # )
        # self.ui.comboBox_shot.currentIndexChanged.connect(
        #     self.controller.set_shot_count_index
        # )

        # self.ui.comboBox_smoothing_sizes.currentIndexChanged.connect(
        #     self.controller.set_smoothing_sizes_index
        # )
        # self.ui.spinBox_ver_skip.valueChanged.connect(
        #     self.controller.set_ver_skip
        # )
        # self.ui.spinBox_hor_skip.valueChanged.connect(
        #     self.controller.set_hor_skip
        # )

        # self.ui.comboBox_filter.currentIndexChanged.connect(
        #     self.controller.set_filters_index
        # )
        # self.ui.checkBox_delta_range.stateChanged.connect(
        #     self.controller.set_delta_restriction
        # )

        # self.ui.button_measure.clicked.connect(self._on_button_measure_clicked)
        # self.controller.measurement_stopped.connect(
        #     self._on_measurement_stopped
        # )
        # self.controller.measurement_process_changed.connect(
        #     self._on_measurement_process_changed
        # )
        pass

    def _get_ui_properties(self):
        # self.controller.exposure_time_decimals = (
        #     self.ui.doubleSpinBox_exposure.decimals()
        # )
        pass

    def _add_ui_properties(self):

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
        if csv_path and csv_path != self.input_frame.filepath.get():
            self.is_first = True  # regard when csv is read as the first time

            self.input_frame.filepath.set(csv_path)
            self._create_df(csv_path)
            self._analyze_indata()
            self._update_analyzedvalues()
            if self.df.size > 10_000:
                self.input_frame.is_3d.set(False)
                self.input_frame.threeD_check["state"] = "disabled"
            else:
                self.input_frame.threeD_check["state"] = "normal"
            self._update_sbox_max()

            self.display_figure()

    def _browse_inputfile(self):
        return QFileDialog.getOpenFileName(
            self,
            "Select",
        )

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
