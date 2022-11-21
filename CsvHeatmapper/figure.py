import os
import math
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


class FigureHandler:
    def __init__(self, files=None) -> None:
        # self.figure = plt.figure(figsize=(9, 6), dpi=100)
        # self.figure.subplots_adjust(
        #     left=0.05, right=0.95, bottom=0.1, top=0.95
        # )
        self.figure = plt.figure(figsize=(9, 6), dpi=100, tight_layout=True)
        # if files:
        #     self.datas = self._file_to_ndarr(files)
        #     self._analyze_data()

    def load_data(self, files):
        self.datas = [self._file_to_ndarr(file) for file in files]
        # print(self.data)
        # self.figure.set_dpi(100 * len(files))
        self.figure.set_size_inches(9, 6 * len(self.datas))
        self._analyze_data()

    def remove_data(self, index):
        del self.datas[index]
        self.figure.set_size_inches(9, 6 * len(self.datas))
        self._analyze_data()

    def _file_to_ndarr(self, file):
        # print(file)
        if os.path.splitext(file)[-1].lower() == ".csv":
            df = pd.read_csv(file, header=None).dropna(axis=1)
        else:
            df_file = pd.ExcelFile(file)
            df = df_file.parse(sheet_name=0, header=None).dropna(axis=1)
        # print(df.dtypes)

        return df.to_numpy()
        # return df.to_numpy(dtype=df.dtypes)

    def _analyze_data(self):
        datas_analyzed = []
        for data in self.datas:
            data_height, data_width = data.shape
            data_size = data.size
            data_max = np.amax(data)
            data_min = np.amin(data)
            data_mean = np.mean(data)
            data_median = np.median(data)
            data_std = np.std(data, ddof=1)
            datas_analyzed.append(
                [
                    data_height,
                    data_width,
                    data_size,
                    data_max,
                    data_min,
                    data_mean,
                    data_median,
                    data_std,
                ]
            )
        self.datas_analyzed = np.array(datas_analyzed)
        match (len(self.datas_analyzed)):
            case 0:
                self.datas_height = None
                self.datas_width = None
                self.datas_size = 0
                self.datas_max = None
                self.datas_min = None
                self.datas_mean = None
                self.datas_median = None
            case 1:
                self.datas_height = np.amax(self.datas_analyzed[0, 0])
                self.datas_width = np.amax(self.datas_analyzed[0, 1])
                self.datas_size = np.amax(self.datas_analyzed[0, 2])
                self.datas_max = np.amax(self.datas_analyzed[0, 3])
                self.datas_min = np.amin(self.datas_analyzed[0, 4])
                self.datas_mean = np.mean(self.datas_analyzed[0, 5])
                self.datas_median = np.median(self.datas_analyzed[0, 6])
            case _:
                self.datas_height = np.amax(self.datas_analyzed[:, 0])
                self.datas_width = np.amax(self.datas_analyzed[:, 1])
                self.datas_size = np.amax(self.datas_analyzed[:, 2])
                self.datas_max = np.amax(self.datas_analyzed[:, 3])
                self.datas_min = np.amin(self.datas_analyzed[:, 4])
                self.datas_mean = np.mean(self.datas_analyzed[:, 5])
                self.datas_median = np.median(self.datas_analyzed[:, 6])

    def plot(
        self,
        Xinterval,
        Yinterval,
        colorMax,
        colorMin,
        colorinterval,
        xLabel,
        yLabel,
        colorLabel,
        axisLabelSize,
        tickLabelSize,
        colorMap="jet",
        is3d=False,
        type3d="scatter",
    ):
        if hasattr(self, "figure"):
            # print("tes")
            self.figure.clear()  # Clear the canvas.
        # if hasattr(self, "ax"):
        #     self.ax.cla()

        # if self.is_first:  # set initial values
        #     self.is_first = False
        #     self.input_frame.msg_dict = {}
        #     self.input_frame.msg.set("")
        #     self.input_frame.calculate_button["state"] = "normal"
        #     # self.input_frame.change_intervalslist()
        # else:
        #     # self.input_frame.change_intervalslist()

        cbar_norm = mpl.colors.Normalize(colorMin, colorMax)
        # ///if self.input_frame.cm_reversed.get():
        #     cmap = cmap + "_r"

        if len(self.datas) == 1:
            self.list_ax = [self.figure.subplots(len(self.datas), 1)]
        else:
            self.list_ax = self.figure.subplots(len(self.datas), 1)
        for ax, data in zip(self.list_ax, self.datas):
            if is3d:
                # ax = self.figure.subplots(projection="3d")
                self.ax = ax = self.figure.add_subplot(111, projection="3d")
                ax.set_box_aspect((1, 1, 0.1))
                if type3d == "surface":
                    alpha = 1
                    list_x = np.array(
                        [
                            x + (-1) ** n * 0.5
                            for x in range(1, self.datas_width + 1)
                            for n in range(1, 3)
                        ]
                    )
                    list_y = np.array(
                        [
                            x + (-1) ** n * 0.5
                            for x in range(1, self.datas_height + 1)
                            for n in range(1, 3)
                        ]
                    )
                    X, Y = np.meshgrid(list_x, list_y)
                    arr = np.kron(self.datas, np.ones((2, 2)))
                    ax.plot_surface(
                        X,
                        Y,
                        arr,
                        cmap=colorMap,
                        norm=cbar_norm,
                        linewidth=0.1,
                        edgecolor="black",
                        rstride=1,
                        cstride=1,
                    )
                    # ax.plot_surface(
                    #     X,
                    #     Y,
                    #     df,
                    #     cmap=cmap,
                    #     norm=cbar_norm,
                    #     linewidth=0.1,
                    #     edgecolor="black",
                    #     rstride=1,
                    #     cstride=1,
                    # )
                elif type3d == "scatter":
                    alpha = 0.3
                    list_x = np.arange(1, self.datas_width + 1)
                    list_y = np.arange(1, self.datas_height + 1)
                    X, Y = np.meshgrid(list_x, list_y)
                    ax.scatter(
                        X,
                        Y,
                        self.datas,
                        c=self.datas,
                        marker="o",
                        cmap=colorMap,
                        norm=cbar_norm,
                        alpha=alpha,
                    )
                    alpha *= 2
                cbar = self.figure.colorbar(
                    mpl.cm.ScalarMappable(norm=cbar_norm, cmap=colorMap),
                    ax=ax,
                    alpha=alpha if alpha <= 1 else 1,
                )
                ax.tick_params(axis="z", labelsize=tickLabelSize, pad=10)
                ax.set_xlim3d(0.5, self.datas_width + 0.5)
                ax.set_ylim3d(self.datas_height + 0.5, 0.5)
                ax.set_zlim3d(
                    math.floor(self.datas_min), math.ceil(self.datas_max)
                )
                ax.set_box_aspect(
                    (
                        self.datas_width,
                        self.datas_height,
                        max(self.datas_width, self.datas_height),
                    )
                )
            else:
                # self.ax = ax = self.figure.add_subplot(111)
                # self.list_ax = self.figure.subplots(len(self.datas), 1)
                extent = (
                    0.5,
                    self.datas_width + 0.5,
                    self.datas_height + 0.5,
                    0.5,
                )
                # for ax, data in zip(self.list_ax, self.datas):
                ax.matshow(data, norm=cbar_norm, cmap=colorMap, extent=extent)
                ax.xaxis.set_label_position("top")
                ax.yaxis.set_ticks_position("both")

                ax.set_xticks(
                    list(np.arange(Xinterval, self.datas_width + 1, Xinterval))
                    if Xinterval == 1
                    else [1]
                    + list(
                        np.arange(Xinterval, self.datas_width + 1, Xinterval)
                    )
                )
                ax.set_yticks(
                    list(
                        np.arange(Yinterval, self.datas_height + 1, Yinterval)
                    )
                    if Yinterval == 1
                    else [1]
                    + list(
                        np.arange(Yinterval, self.datas_height + 1, Yinterval)
                    )
                )
                ax.tick_params(axis="x", labelsize=tickLabelSize)
                ax.tick_params(axis="y", labelsize=tickLabelSize)
                ax.set_xlabel(rf"{xLabel}", fontsize=axisLabelSize)
                ax.set_ylabel(rf"{yLabel}", fontsize=axisLabelSize)

                divider = make_axes_locatable(ax)  # axに紐付いたAxesDividerを取得
                cbar_ax = divider.append_axes(
                    "right", size="3%", pad=0.2
                )  # append_axesで新しいaxesを作成
                # cbar_ax = self.figure.add_axes([0.85, 0.15, 0.05, 0.7])
                cbar = self.figure.colorbar(
                    mpl.cm.ScalarMappable(norm=cbar_norm, cmap=colorMap),
                    cax=cbar_ax,
                )

            cbar.set_label(rf"{colorLabel}", fontsize=axisLabelSize)
            cbar.ax.set_yticks(
                np.concatenate(
                    [
                        [colorMin],
                        _ := np.round(
                            np.arange(
                                colorMin + colorinterval,
                                colorMax,
                                colorinterval,
                            ),
                            len(str(colorinterval).split(".")[-1]),
                        ),
                        [colorMax],
                    ]
                )
            )
            cbar.ax.set_yticklabels(
                # [rf"$\leq {float(cmin)}$"]
                # + [f"${i}$" for i in _]
                # + [rf"$\geq {float(colorMax)}$"]
                [r"$\leq %s$" % str(colorMin).rstrip("0").rstrip(".")]
                + [r"$%s$" % str(i).rstrip("0").rstrip(".") for i in _]
                + [r"$\geq %s$" % str(colorMax).rstrip("0").rstrip(".")]
            )
            cbar.ax.tick_params(axis="y", labelsize=tickLabelSize)
        # plt.rcParams["figure.constrained_layout.use"] = True

        #     ax.matshow(
        #         self.datas, norm=cbar_norm, cmap=colorMap, extent=extent
        #     )
        #     # ax[0].matshow(self.data, norm=cbar_norm, cmap=colorMap, extent=extent)
        #     # # ax.matshow(df, norm=cbar_norm, cmap=colorMap,)
        #     ax.xaxis.set_label_position("top")
        #     ax.yaxis.set_ticks_position("both")

        #     divider = make_axes_locatable(ax)  # axに紐付いたAxesDividerを取得
        #     cax = divider.append_axes(
        #         "right", size="3%", pad=0.2
        #     )  # append_axesで新しいaxesを作成
        #     cbar = self.figure.colorbar(
        #         mpl.cm.ScalarMappable(norm=cbar_norm, cmap=colorMap),
        #         cax=cax,
        #     )
        # cbar.set_label(rf"{colorLabel}", fontsize=axisLabelSize)
        # cbar.ax.set_yticks(
        #     np.concatenate(
        #         [
        #             [colorMin],
        #             _ := np.round(
        #                 np.arange(
        #                     colorMin + colorinterval, colorMax, colorinterval
        #                 ),
        #                 len(str(colorinterval).split(".")[-1]),
        #             ),
        #             [colorMax],
        #         ]
        #     )
        # )
        # cbar.ax.set_yticklabels(
        #     # [rf"$\leq {float(cmin)}$"]
        #     # + [f"${i}$" for i in _]
        #     # + [rf"$\geq {float(colorMax)}$"]
        #     [r"$\leq %s$" % str(colorMin).rstrip("0").rstrip(".")]
        #     + [r"$%s$" % str(i).rstrip("0").rstrip(".") for i in _]
        #     + [r"$\geq %s$" % str(colorMax).rstrip("0").rstrip(".")]
        # )

        # ax.set_xticks(
        #     list(np.arange(Xinterval, self.data_width + 1, Xinterval))
        #     if Xinterval == 1
        #     else [1]
        #     + list(np.arange(Xinterval, self.data_width + 1, Xinterval))
        # )
        # ax.set_yticks(
        #     list(np.arange(Yinterval, self.data_height + 1, Yinterval))
        #     if Yinterval == 1
        #     else [1]
        #     + list(np.arange(Yinterval, self.data_height + 1, Yinterval))
        # )
        # cbar.ax.tick_params(axis="y", labelsize=tickLabelSize)
        # ax.tick_params(axis="x", labelsize=tickLabelSize)
        # ax.tick_params(axis="y", labelsize=tickLabelSize)
        # ax.set_xlabel(rf"{xLabel}", fontsize=axisLabelSize)
        # ax.set_ylabel(rf"{yLabel}", fontsize=axisLabelSize)
