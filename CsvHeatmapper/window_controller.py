# from dataclasses import dataclass
# from time import sleep, perf_counter
# import os
# from datetime import datetime
# import json
# import logging

from figure import Figure

from PySide6.QtCore import Signal, Slot, QObject, QThread, QMutexLocker, QMutex


class WindowController(QObject):
    # ready_rotate = Signal(str)
    # current_angles_changed = Signal()
    # preview_stopped = Signal()
    # measurement_stopped = Signal(str)
    # measurement_process_changed = Signal(int)
    # exposure_time_changed = Signal(float)
    # exposure_auto_completed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure = Figure()
        # leftarm = Stage(StageNo.s0, 40, 0)
        # rightarm = Stage(StageNo.s1, 40, 0)
        # polarizer = Stage(StageNo.s2, 0, 0)
        # compensator = Stage(StageNo.s3, 0, 0)
        # analyzer = Stage(StageNo.s5, 136, 0)
        # detector = Stage(StageNo.s6, 50, 0)
        # self.stages = [
        #     leftarm,
        #     rightarm,
        #     polarizer,
        #     compensator,
        #     analyzer,
        #     detector,
        # ]

        # self.working_dir = ""
        # self.dir_bin = ""
        # self.dir_csv = ""

        # self.exposure_time_decimals = 0

        # self.__s3_intervals = [1, 2, 5, 10, 20]
        # self.s3_interval_index = 2
        # self.__shot_counts = [1, 10, 20]
        # self.shot_count_index = 0

        # self.smoothing_sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # self.smoothing_sizes_text = [
        #     "1x1 (No smoothing)",
        #     "2x2",
        #     "3x3",
        #     "4x4",
        #     "5x5",
        #     "6x6",
        #     "7x7",
        #     "8x8",
        #     "9x9",
        #     "10x10",
        # ]
        # self.smoothing_sizes_index = 0
        # self.ver_skip = 24
        # self.hor_skip = 24

        # self.filters = [1, 2, 3, 4, 5, 7, 8]
        # self.filter_wavelens = [
        #     "1 (530nm)",
        #     "2 (590nm)",
        #     "3 (650nm)",
        #     "4 (720nm)",
        #     "5 (780nm)",
        #     "7 (405nm)",
        #     "8 (470nm)",
        # ]
        # self.filters_index = 1
        # self.delta_restriction = False

        # self.is_rotating = False
        # self.is_measuring = False
        # self.rotation_interrupting = False

        # self.__ports = self.stage_controller.list_ports()
        # if self.__ports:
        #     self.stages_port = self.__ports[0]

        # # self.app_closing = False

        # self.worker_threads = {}
        # self.workers = {}
        # self.qthread_id = 0
