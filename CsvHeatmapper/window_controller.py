# from dataclasses import dataclass
from time import sleep, perf_counter
import os
import math
import matplotlib as mpl

# from datetime import datetime
# import json
import logging
from logging.handlers import RotatingFileHandler

from figure import FigureHandler

from PySide6.QtCore import (
    Signal,
    Slot,
    QObject,
    QThread,
    QMutexLocker,
    QMutex,
    QStringListModel,
    Qt,
    QItemSelectionModel,
)


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


class LoadedFilesModel(QStringListModel):
    def __init__(self, *args, files=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.files = files or []
        # self.setHeaderData(0, Qt.Horizontal, "Loaded Files")

    def data(self, index, role):
        if role == Qt.DisplayRole:
            text = self.files[index.row()]
            return text

    def rowCount(self, index):
        return len(self.files)

    # def headerData(self, section: int, orientation: PySide6.QtCore.Qt.Orientation, role: int = ...) -> Any:
    #     return super().headerData(section, orientation, role)


class WindowController(QObject):
    analyzedvalues_changed = Signal(str)
    data_is_too_big = Signal(bool)
    # data_changed = Signal(tuple)
    propertyChanged = Signal(str, object)
    valueRangeChanged = Signal(float, float, float, float)
    is_first_plot = True

    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure_handler = FigureHandler()
        self.figure = self.figure_handler.figure
        # self.__loadedFiles = []
        self.loadedFilesModel = LoadedFilesModel(parent=self)
        self.selectionModel = QItemSelectionModel(self.loadedFilesModel, self)
        self.selected_file_indexes = set()
        # self.__loadedFiles.append = self.my_append
        self.__Xinterval = None
        self.__Yinterval = None
        self.__colorMax = None
        self.__colorMin = None
        self.__colorinterval = None
        self.__xLabel = "x"
        self.__yLabel = "y"
        self.__colorLabel = "z ()"
        self.__axisLabelSize = 20
        self.__tickLabelSize = 12
        self.__colorMap = None

        self.colormaps = list(mpl.cm._colormaps._cmaps.keys())

    def load_files(self, files):
        for file in files:
            if file not in self.loadedFilesModel.files:
                self.loadedFilesModel.files.append(file)
        self.loadedFilesModel.layoutChanged.emit()

        # print(self.loadedFilesModel.files)
        self.figure_handler.load_data(self.loadedFilesModel.files)
        self._update_analyzedvalues()
        self._update_properties()

        self.plot()

    def unload_files(self, indexes: set):
        indexes = sorted(list(indexes), reverse=True)
        # print(indexes)
        for index in indexes:
            self.figure_handler.remove_data(index)
            # Remove the item and refresh.
            del self.loadedFilesModel.files[index]
            # self.figure_handler.remove_data(index.row())
            # # Remove the item and refresh.
            # del self.loadedFilesModel.files[index.row()]
        self.loadedFilesModel.layoutChanged.emit()
        # self.save()
        self._update_analyzedvalues()

    def _update_properties(self):
        int_min = float(math.floor(self.figure_handler.datas_min))
        int_max = float(math.ceil(self.figure_handler.datas_max))
        self.valueRangeChanged.emit(
            self.figure_handler.datas_width,
            self.figure_handler.datas_height,
            int_min,
            int_max,
        )
        self.colorMax = int_max
        self.colorMin = int_min
        self.Xinterval = determine_interval(self.figure_handler.datas_width)
        self.Yinterval = determine_interval(self.figure_handler.datas_height)
        if self.is_first_plot:
            self.colorinterval = determine_interval(
                self.colorMax - self.colorMin, True
            )
            self.is_first_plot = False

    def _update_analyzedvalues(self):
        # print(self.figure_handler.datas)
        # if self.figure_handler.datas
        analyzedvalues = (
            f"Max: {self.figure_handler.datas_max}, "
            f"Min: {self.figure_handler.datas_min}, "
            f"Mean: {self.figure_handler.datas_mean}, "
            f"Median: {self.figure_handler.datas_median}, "
            f"Sample Std: {self.figure_handler.datas_std}"
        )
        self.analyzedvalues_changed.emit(analyzedvalues)

        self.data_is_too_big.emit(
            True if self.figure_handler.datas_size > 10_000 else False
        )
        # self.data_changed.emit(
        #     (self.figure_handler.data_height, self.figure_handler.data_width)
        # )

    def plot(self):
        t_before = perf_counter()
        # if (fig := self.plot()) is None:
        #     return
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
            self.colorMap,
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

    # @property
    # def loadedFiles(self):
    #     return self.__loadedFiles

    # @loadedFiles.setter
    # def loadedFiles(self, values):
    #     self.__loadedFiles = values
    #     self.propertyChanged.emit("loadedFiles", self.__loadedFiles)

    # def my_append(self, value):
    #     self.__loadedFiles.append(value)
    #     self.propertyChanged.emit("loadedFiles", self.__loadedFiles)

    @property
    def Xinterval(self):
        return self.__Xinterval

    @Xinterval.setter
    def Xinterval(self, value):
        # print(value)
        self.propertyChanged.emit("Xinterval", value)
        self.__Xinterval = value

    @property
    def Yinterval(self):
        return self.__Yinterval

    @Yinterval.setter
    def Yinterval(self, value):
        self.__Yinterval = value
        self.propertyChanged.emit("Yinterval", value)

    @property
    def colorMax(self):
        return self.__colorMax

    @colorMax.setter
    def colorMax(self, value):
        self.__colorMax = value
        self.propertyChanged.emit("colorMax", value)

    @property
    def colorMin(self):
        return self.__colorMin

    @colorMin.setter
    def colorMin(self, value):
        self.__colorMin = value
        self.propertyChanged.emit("colorMin", value)

    @property
    def colorinterval(self):
        return self.__colorinterval

    @colorinterval.setter
    def colorinterval(self, value):
        self.__colorinterval = value
        self.propertyChanged.emit("colorinterval", value)

    @property
    def xLabel(self):
        return self.__xLabel

    @xLabel.setter
    def xLabel(self, value):
        self.__xLabel = value
        self.propertyChanged.emit("xLabel", value)

    @property
    def yLabel(self):
        return self.__yLabel

    @yLabel.setter
    def yLabel(self, value):
        self.__yLabel = value
        self.propertyChanged.emit("yLabel", value)

    @property
    def colorLabel(self):
        return self.__colorLabel

    @colorLabel.setter
    def colorLabel(self, value):
        self.__colorLabel = value
        self.propertyChanged.emit("colorLabel", value)

    @property
    def axisLabelSize(self):
        return self.__axisLabelSize

    @axisLabelSize.setter
    def axisLabelSize(self, value):
        self.__axisLabelSize = value
        self.propertyChanged.emit("axisLabelSize", value)

    @property
    def tickLabelSize(self):
        return self.__tickLabelSize

    @tickLabelSize.setter
    def tickLabelSize(self, value):
        self.__tickLabelSize = value
        self.propertyChanged.emit("tickLabelSize", value)

    @property
    def colorMap(self):
        return self.__colorMap

    @colorMap.setter
    def colorMap(self, i):
        self.__colorMap = self.colormaps[i]
        # self.propertyChanged.emit("colorMap", value)

    def set_is_3d(self, state: int):
        self.figure.is_3d = bool(state)
