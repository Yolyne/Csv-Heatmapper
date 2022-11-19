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
from ui.my_widgets import DoubleDragSpinBox, StatusWidget

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

        self.preview_window: QWidget = None

    def _setup_app(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self._get_ui_properties()
        self._add_ui_properties()

    def _connect_signal_slot(self):
        pass

    #     self.ui.doubleSpinBox.valueChanged.connect(self.controller.set_leftarm)
    #     self.ui.doubleSpinBox_2.valueChanged.connect(
    #         self.controller.set_rightarm
    #     )
    #     self.ui.doubleSpinBox_3.valueChanged.connect(
    #         self.controller.set_polarizer
    #     )
    #     self.ui.doubleSpinBox_4.valueChanged.connect(
    #         self.controller.set_compensator
    #     )
    #     self.ui.doubleSpinBox_5.valueChanged.connect(
    #         self.controller.set_analyzer
    #     )
    #     self.ui.doubleSpinBox_6.valueChanged.connect(
    #         self.controller.set_detector
    #     )

    #     self.ui.button_rotate.clicked.connect(self._on_rotate_button_clicked)
    #     self.controller.ready_rotate.connect(self._on_ready_rotate)

    #     self.controller.current_angles_changed.connect(
    #         self._update_current_angles
    #     )

    #     self.ui.button_preview.clicked.connect(self._show_preview)
    #     self.controller.preview_stopped.connect(self._on_preview_stopped)

    #     self.controller.exposure_time_changed.connect(
    #         self.ui.doubleSpinBox_exposure.setValue
    #     )
    #     self.ui.doubleSpinBox_exposure.valueChanged.connect(
    #         self.controller.set_exposure_time
    #     )
    #     self.ui.pushButton_exposure_auto.clicked.connect(
    #         self._on_exposure_auto
    #     )
    #     self.controller.exposure_auto_completed.connect(
    #         self._on_exposure_auto_completed
    #     )
    #     self.ui.spinBox_gain.valueChanged.connect(self.controller.set_gain)

    #     self.ui.comboBox_s3_interval.currentIndexChanged.connect(
    #         self.controller.set_s3_interval_index
    #     )
    #     self.ui.comboBox_shot.currentIndexChanged.connect(
    #         self.controller.set_shot_count_index
    #     )

    #     self.ui.comboBox_smoothing_sizes.currentIndexChanged.connect(
    #         self.controller.set_smoothing_sizes_index
    #     )
    #     self.ui.spinBox_ver_skip.valueChanged.connect(
    #         self.controller.set_ver_skip
    #     )
    #     self.ui.spinBox_hor_skip.valueChanged.connect(
    #         self.controller.set_hor_skip
    #     )

    #     self.ui.comboBox_filter.currentIndexChanged.connect(
    #         self.controller.set_filters_index
    #     )
    #     self.ui.checkBox_delta_range.stateChanged.connect(
    #         self.controller.set_delta_restriction
    #     )

    #     self.ui.button_measure.clicked.connect(self._on_button_measure_clicked)
    #     self.controller.measurement_stopped.connect(
    #         self._on_measurement_stopped
    #     )
    #     self.controller.measurement_process_changed.connect(
    #         self._on_measurement_process_changed
    #     )

    # def _get_ui_properties(self):
    #     self.controller.exposure_time_decimals = (
    #         self.ui.doubleSpinBox_exposure.decimals()
    #     )

    def _add_ui_properties(self):
        pass

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

    # def _on_rotate_button_clicked(self):
    #     if self.controller.is_rotating:
    #         self._on_rotation_interrupted()
    #     else:
    #         self._before_rotate_stages()
    #         self.controller.rotate_stages()

    # def _before_rotate_stages(self):
    #     self.ui.button_measure.setEnabled(False)
    #     self.status_widget.label_status.setText("Rotating stages...")
    #     self.ui.button_rotate.setText("Stop")

    # def _on_rotation_interrupted(self):
    #     self.ui.button_rotate.setEnabled(False)
    #     self.status_widget.label_status.setText("Stage rotation interrupted.")
    #     self.controller.stop_stages()

    # def _on_ready_rotate(self, ready):
    #     self.ui.button_rotate.setText("Rotate to Destination")
    #     # self.ui.button_rotate.setEnabled(ready)
    #     # self.ui.button_measure.setEnabled(ready)
    #     if self.controller.rotation_interrupting:
    #         self.status_widget.label_status.setText(
    #             "Stage rotation interrupted."
    #         )
    #         self.controller.rotation_interrupting = False
    #     else:
    #         self.status_widget.label_status.setText(ready)
    #     if ready == "Sum of arm angles must be <= 120.":
    #         self.ui.button_measure.setEnabled(False)
    #         self.ui.button_rotate.setEnabled(False)
    #     else:
    #         self.ui.button_measure.setEnabled(True)
    #         self.ui.button_rotate.setEnabled(True)

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

    # def _on_preview_stopped(self):
    #     self.ui.button_preview.setEnabled(True)

    # # def _enable_button_stop(self, can_stop: bool):
    # #     self.ui.button_stop.setEnabled(can_stop)
    # #     self.ui.button_stop.setFocus()

    # def _update_current_angles(self):
    #     for label, angle in zip(
    #         self.current_angle_labels, self.controller.current_angles
    #     ):
    #         label.setText(str(angle))

    # def _on_exposure_auto(self):
    #     self.status_widget.label_status.setText("Changing expossure time ...")
    #     self.ui.doubleSpinBox_exposure.setEnabled(False)
    #     self.ui.pushButton_exposure_auto.setEnabled(False)
    #     self.ui.button_measure.setEnabled(False)
    #     self._show_progressbar()
    #     self.controller.exposure_auto()

    # def _on_exposure_auto_completed(self):
    #     self.status_widget.label_status.setText("Done!")
    #     self.ui.doubleSpinBox_exposure.setEnabled(True)
    #     self.ui.pushButton_exposure_auto.setEnabled(True)
    #     self.ui.button_measure.setEnabled(True)
    #     self._hide_progressbar()

    # def _on_button_measure_clicked(self):
    #     if self.controller.is_measuring:
    #         self._on_interrupting_measurement()
    #     else:
    #         working_dir_parent = QFileDialog.getExistingDirectory(
    #             self,
    #             "Select a folder to save the working folder",
    #             dir=setting.value("last_dir"),
    #         )

    #         if working_dir_parent:
    #             setting.setValue("last_dir", working_dir_parent)

    #             self._before_measure()
    #             self.controller.measure(working_dir_parent)

    # def _before_measure(self):
    #     self.ui.doubleSpinBox_exposure.setEnabled(False)
    #     self.ui.spinBox_gain.setEnabled(False)
    #     self.ui.comboBox_s3_interval.setEnabled(False)
    #     self.ui.comboBox_smoothing_sizes.setEnabled(False)
    #     self.ui.spinBox_ver_skip.setEnabled(False)
    #     self.ui.spinBox_hor_skip.setEnabled(False)
    #     self.ui.comboBox_filter.setEnabled(False)

    #     self.ui.button_rotate.setEnabled(False)
    #     self.ui.pushButton_exposure_auto.setEnabled(False)

    #     # if self.preview_window and self.preview_window.isVisible():
    #     #     self.preview_window.close()

    #     self._show_progressbar()
    #     self.status_widget.label_status.setText("Starting measurement...")
    #     self.ui.button_measure.setText("Stop")

    # def _on_measurement_stopped(self, state):
    #     self.ui.doubleSpinBox_exposure.setEnabled(True)
    #     self.ui.spinBox_gain.setEnabled(True)
    #     self.ui.comboBox_s3_interval.setEnabled(True)
    #     self.ui.comboBox_smoothing_sizes.setEnabled(True)
    #     self.ui.spinBox_ver_skip.setEnabled(True)
    #     self.ui.spinBox_hor_skip.setEnabled(True)
    #     self.ui.comboBox_filter.setEnabled(True)

    #     self.ui.button_rotate.setEnabled(True)
    #     self.ui.pushButton_exposure_auto.setEnabled(True)
    #     if state == "completed":
    #         self.status_widget.label_status.setText("Done!")
    #         # effect = QtMultimedia.QSoundEffect()
    #         # effect.setSource("engine.wav")
    #         # effect.setLoopCount(QtMultimedia.QSoundEffect.)
    #         # effect.setVolume(0.25f)
    #         # effect.play()
    #     elif state == "interrupted":
    #         self.status_widget.label_status.setText("Measurement interrupted.")

    #     self._hide_progressbar()
    #     self.ui.button_measure.setText("Measure")

    # def _on_interrupting_measurement(self):
    #     self.controller.stop_measure()
    #     # self._hide_progressbar()
    #     # self.status_widget.label_status.setText("Measurement interrupted.")
    #     # self.ui.button_measure.setText("Measure")

    # def _on_measurement_process_changed(self, value):
    #     if value == 0:
    #         self.status_widget.label_status.setText("Collecting images...")
    #     if value == 1:
    #         self.status_widget.label_status.setText(
    #             "Coverting images to CSVs..."
    #         )
    #     if value == 2:
    #         self.status_widget.label_status.setText(
    #             "Calcurating Delta & Psi..."
    #         )

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
