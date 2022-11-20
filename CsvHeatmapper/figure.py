import os
import math
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


class FigureHandler:
    def __init__(self, file=None) -> None:
        self.figure = plt.figure(figsize=(9, 6), dpi=100, tight_layout=True)
        if file:
            self.data = self._file_to_ndarr(file)
            self._analyze_data()

    def load_data(self, file):
        self.data = self._file_to_ndarr(file)
        self._analyze_data()

    def _file_to_ndarr(self, file):
        if os.path.splitext(file)[-1].lower() == ".csv":
            df = pd.read_csv(file, header=None).dropna(axis=1)
        else:
            df_file = pd.ExcelFile(file)
            df = df_file.parse(sheet_name=0, header=None).dropna(axis=1)
        print(df.dtypes)

        return df.to_numpy(dtype=df.dtypes)

    def _analyze_data(self):
        self.data_height, self.data_width = self.data.shape
        self.data_size = self.data.size
        self.data_mean = np.mean(self.data)
        self.data_max = np.amax(self.data)
        self.data_min = np.amin(self.data)
        self.data_median = np.median(self.data)
        self.data_std = np.std(self.data, ddof=1)

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
        colorMap,
        is3d,
        type3d,
    ):
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

        if is3d:
            ax = self.figure.subplots(projection="3d")
            ax.set_box_aspect((1, 1, 0.1))
            if type3d == "surface":
                alpha = 1
                list_x = np.array(
                    [
                        x + (-1) ** n * 0.5
                        for x in range(1, self.indata_width + 1)
                        for n in range(1, 3)
                    ]
                )
                list_y = np.array(
                    [
                        x + (-1) ** n * 0.5
                        for x in range(1, self.indata_height + 1)
                        for n in range(1, 3)
                    ]
                )
                X, Y = np.meshgrid(list_x, list_y)
                arr = np.kron(self.data, np.ones((2, 2)))
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
                list_x = np.arange(1, self.indata_width + 1)
                list_y = np.arange(1, self.indata_height + 1)
                X, Y = np.meshgrid(list_x, list_y)
                ax.scatter(
                    X,
                    Y,
                    self.data,
                    c=self.data,
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
            ax.set_xlim3d(0.5, self.indata_width + 0.5)
            ax.set_ylim3d(self.indata_height + 0.5, 0.5)
            ax.set_zlim3d(math.floor(self.data_min), math.ceil(self.data_max))
            ax.set_box_aspect(
                (
                    self.indata_width,
                    self.indata_height,
                    max(self.indata_width, self.indata_height),
                )
            )
        else:
            ax = self.figure.subplots()
            extent = (
                0.5,
                self.indata_width + 0.5,
                self.indata_height + 0.5,
                0.5,
            )
            ax.matshow(self.data, norm=cbar_norm, cmap=colorMap, extent=extent)
            # # ax.matshow(df, norm=cbar_norm, cmap=colorMap,)
            ax.xaxis.set_label_position("top")
            ax.yaxis.set_ticks_position("both")

            divider = make_axes_locatable(ax)  # axに紐付いたAxesDividerを取得
            cax = divider.append_axes(
                "right", size="3%", pad=0.2
            )  # append_axesで新しいaxesを作成
            cbar = self.figure.colorbar(
                mpl.cm.ScalarMappable(norm=cbar_norm, cmap=colorMap),
                cax=cax,
            )
        cbar.set_label(
            rf"{(self.input_frame.cbarlabel.get())}", fontsize=axisLabelSize
        )
        cbar.ax.set_yticks(
            np.concatenate(
                [
                    [colorMin],
                    _ := np.round(
                        np.arange(
                            colorMin + colorinterval, colorMax, colorinterval
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

        ax.set_xticks(
            list(np.arange(Xinterval, self.indata_width + 1, Xinterval))
            if Xinterval == 1
            else [1]
            + list(np.arange(Xinterval, self.indata_width + 1, Xinterval))
        )
        ax.set_yticks(
            list(np.arange(Yinterval, self.indata_height + 1, Yinterval))
            if Yinterval == 1
            else [1]
            + list(np.arange(Yinterval, self.indata_height + 1, Yinterval))
        )
        cbar.ax.tick_params(axis="y", labelsize=tickLabelSize)
        ax.tick_params(axis="x", labelsize=tickLabelSize)
        ax.tick_params(axis="y", labelsize=tickLabelSize)
        ax.set_xlabel(
            rf"{(self.input_frame.xlabel.get())}", fontsize=axisLabelSize
        )
        ax.set_ylabel(
            rf"{(self.input_frame.ylabel.get())}", fontsize=axisLabelSize
        )
        # cbar.ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        # cbar.ax.ticklabel_format(style="sci",  axis="y",scilimits=(0,0))
        # cbar.ax.yaxis.set_offset_position('left')
        # cbar.ax.text(0, 90, r'$\times$10$^{-1}$', va='bottom', ha='left')

        # _ = (
        #     list(range(1, 10))
        #     + [i for i in range(10, self.indata_width, 5)]
        #     + [self.indata_width]
        #     if self.indata_width > 10
        #     else list(range(1, self.indata_width + 1))
        # )
        # self.input_frame.xaxis_entry["values"] = [
        #     i for i in _ if self.indata_width / i < 21
        # ]
        # _ = (
        #     list(range(1, 10))
        #     + [i for i in range(10, self.indata_height, 5)]
        #     + [self.indata_height]
        #     if self.indata_height > 10
        #     else list(range(1, self.indata_height + 1))
        # )
        # self.input_frame.yaxis_entry["values"] = [
        #     i for i in _ if self.indata_height / i < 21
        # ]

        # self.figure_frame.fig = fig
        # return fig
