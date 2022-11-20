# from dataclasses import dataclass
from time import sleep, perf_counter
import os
import math

# from datetime import datetime
# import json
import logging
from logging.handlers import RotatingFileHandler

from figure import FigureHandler

from PySide6.QtCore import Signal, Slot, QObject, QThread, QMutexLocker, QMutex


# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = RotatingFileHandler("app.log", maxBytes=500_000, backupCount=2)
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter(
    "[%(asctime)s] %(name)s %(threadName)s(%(levelname)s): %(message)s"
)
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)


def determine_interval(length, is_colorbar=False):
    minimum = length / 8
    magnitude = 10 ** math.floor(math.log(minimum, 10))
    residual = minimum / magnitude
    if magnitude < 1 and not is_colorbar:
        # Don't allow x(y)-interval less than 1.
        return 1
    if residual > 5:
        interval = 10 * magnitude
    elif residual > 2:
        interval = 5 * magnitude
    elif residual > 1:
        interval = 2 * magnitude
    else:
        interval = magnitude
    return interval


class WindowController(QObject):
    analyzedvalues_changed = Signal(str)
    data_is_too_big = Signal(bool)
    data_changed = Signal(tuple)
    propertyChanged = Signal(tuple, object)
    valueRangeChanged = Signal(float, float, float, float)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure_handler = FigureHandler()
        self.figure = self.figure_handler.figure
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

    def load_file(self, file):
        self.is_first = True  # regard when csv is read as the first time

        self.figure_handler.load_data(file)
        self._update_analyzedvalues()

        self._display_figure()

    def _update_analyzedvalues(self):
        # self.analyzedvalues =
        analyzedvalues = (
            f"Max: {self.figure_handler.data_max}, "
            f"Min: {self.figure_handler.data_min}, "
            f"Mean: {self.figure_handler.data_mean}, "
            f"Median: {self.figure_handler.data_median}, "
            f"Sample Std: {self.figure_handler.data_std}"
        )
        self.analyzedvalues_changed.emit(analyzedvalues)

        self.data_is_too_big.emit(
            True if self.figure_handler.data_size > 10_000 else False
        )
        self.data_changed.emit(
            (self.figure_handler.data_height, self.figure_handler.data_width)
        )

    def _display_figure(self):
        t_before = perf_counter()
        # if (fig := self.plot()) is None:
        #     return
        self.colorMax = float(math.ceil(self.figure_handler.data_max))
        self.colorMin = float(math.floor(self.figure_handler.data_min))
        self.Xinterval = determine_interval(self.figure_handler.data_width)
        self.Yinterval = determine_interval(self.figure_handler.data_height)
        self.colorinterval = determine_interval(
            self.colorMax - self.colorMin, True
        )
        self.valueRangeChanged.emit(
            self.figure_handler.data_width,
            self.figure_handler.data_height,
            self.colorMin,
            self.colorMax,
        )
        fig = self.figure_handler.plot(
            self.Xinterval,
            self.Yinterval,
            self.colorMax,
            self.colorMin,
            self.colorinterval,
            self.xLabel,
            self.yLabel,
            self.colorLabel,
            self.axisLabelSize,
            self.tickLabelSize,
        )
        # logger.info("ploting time: {} s".format(perf_counter() - t_before))
        # try:
        #     figure_canvas = FigureCanvasTkAgg(fig, master=self.figure_frame)
        #     figure_canvas.draw()
        #     toolbar = MyNavigationToolbar(
        #         figure_canvas, self.canvas_frame, pack_toolbar=False
        #     )
        #     toolbar.update()
        #     # toolbar.pack(
        #     #     side="top",
        #     # )
        #     toolbar.grid(column=0, row=0, sticky=tk.EW)
        #     figure_canvas.get_tk_widget().grid(column=0, row=1, sticky=tk.NSEW)
        # except ValueError:  # Error(Latex) in drawing figure
        #     pass

    @property
    def Xinterval(self):
        return self.__Xinterval

    @Xinterval.setter
    def Xinterval(self, value):
        print(value)
        self.propertyChanged.emit("Xinterval")
        self.__Xinterval = value

    @property
    def Yinterval(self):
        return self.__Yinterval

    @Yinterval.setter
    def Yinterval(self, value):
        self.__Yinterval = value
        self.propertyChanged.emit("Yinterval")

    @property
    def colorMax(self):
        return self.__colorMax

    @colorMax.setter
    def colorMax(self, value):
        self.__colorMax = value
        self.propertyChanged.emit("colorMax")

    @property
    def colorMin(self):
        return self.__colorMin

    @colorMin.setter
    def colorMin(self, value):
        self.__colorMin = value
        self.propertyChanged.emit("colorMin")

    @property
    def colorinterval(self):
        return self.__colorinterval

    @colorinterval.setter
    def colorinterval(self, value):
        self.__colorinterval = value
        self.propertyChanged.emit("colorinterval")

    @property
    def xLabel(self):
        return self.__xLabel

    @xLabel.setter
    def xLabel(self, value):
        self.__xLabel = value
        self.propertyChanged.emit("xLabel")

    @property
    def yLabel(self):
        return self.__yLabel

    @yLabel.setter
    def yLabel(self, value):
        self.__yLabel = value
        self.propertyChanged.emit("yLabel")

    @property
    def colorLabel(self):
        return self.__colorLabel

    @colorLabel.setter
    def colorLabel(self, value):
        self.__colorLabel = value
        self.propertyChanged.emit("colorLabel")

    @property
    def axisLabelSize(self):
        return self.__axisLabelSize

    @axisLabelSize.setter
    def axisLabelSize(self, value):
        self.__axisLabelSize = value
        self.propertyChanged.emit("axisLabelSize")

    @property
    def tickLabelSize(self):
        return self.__tickLabelSize

    @tickLabelSize.setter
    def tickLabelSize(self, value):
        self.__tickLabelSize = value
        self.propertyChanged.emit("tickLabelSize")

    @property
    def colorMap(self):
        return self.__colorMap

    @colorMap.setter
    def colorMap(self, value):
        self.__colorMap = value
        self.propertyChanged.emit("colorMap")

    def set_is_3d(self, state: int):
        self.figure.is_3d = bool(state)
