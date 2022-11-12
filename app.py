"""
app.py

Copyright (c) 2022 Yolyne

This software is released under the MIT license.
See https://opensource.org/licenses/MIT

"""

import logging
from logging.handlers import RotatingFileHandler
from time import perf_counter

import tkinter as tk
from tkinter import BooleanVar, StringVar, ttk
from tkinter import filedialog
import pandas as pd
import sys
import os
import math
import numpy as np
import matplotlib as mpl
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import webbrowser

# from matplotlib.ticker import ScalarFormatter
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk,
)

# from matplotlib.backend_bases import key_press_handler

# plt.switch_backend("tkagg")


# APP_NAME = "Ellipso Microscope Commander"
# COMPANY = "Yolyne"
# setting = QSettings(COMPANY, APP_NAME)
# if setting.value("last_dir") == "":
#     setting.setValue("last_dir", os.path.expanduser("~/Documents"))


# create logger with 'spam_application'
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


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


# mpl.use("pgf") #set drawing driver (latexを使える
# # 文字に latex を利用するための設定
# config = {
#     "text.usetex": True,
#     "text.latex.preamble": "\n".join([r"\usepackage{siunitx}"]),
#     "pgf.preamble": "\n".join([r"\usepackage{siunitx}"])  # plots will use this preamble
#     #     'font.sans-serif':['DejaVu Serif', 'Bitstream Vera Serif', 'Computer Modern Roman', 'New Century Schoolbook', 'Century Schoolbook L', 'Utopia', 'ITC Bookman', 'Bookman', 'Nimbus Roman No9 L', 'Times New Roman', 'Times', 'Palatino', 'Charter', 'serif']
# }
# plt.rcParams.update(config)


class MyNavigationToolbar(NavigationToolbar2Tk):
    toolitems = [t for t in NavigationToolbar2Tk.toolitems[:-2]]

    def __init__(self, canvas, window, *, pack_toolbar=True):
        super().__init__(canvas, window, pack_toolbar=pack_toolbar)
        self.config(background="#E6E6FA")
        self._message_label.config(background="#E6E6FA")
        # self.update()


class ColormapsWindow(tk.Toplevel):
    def __init__(self, container):
        super().__init__(container, width=1, height=1)
        # self.attributes("-alpha", 0.0)
        self.resizable(width=False, height=False)
        root_x = container.winfo_x()
        root_y = container.winfo_y()
        # root_width = container.winfo_width()
        # root_height = container.winfo_height()
        # x = root_x + root_width - size[0]/2
        # y = root_y + root_height - size[1]/2
        self.geometry("+%d+%d" % (root_x - 30, root_y))
        icon = tk.PhotoImage(file=resource_path("imgs/icon.png"))
        self.tk.call("wm", "iconphoto", self._w, icon)

        cmap_list = list(mpl.cm._colormaps._cmaps.keys())
        cm_num = int(len(cmap_list) / 2)
        self.ncols = int(cm_num // 3 + 1)
        self.background = tk.PhotoImage(file=resource_path("imgs/cm.png"))
        bg = tk.Label(self, image=self.background)
        bg.grid(column=0, row=0, sticky=tk.NSEW)
        self.cm_rbtns = [
            tk.Radiobutton(
                self,
                variable=app.input_frame.which_cm,
                value=cm,
                background="white",
            )
            for cm in cmap_list[:cm_num]
        ]
        [
            self.cm_rbtns[i].place(
                x=22 + 30 * (i % self.ncols),
                y=26 + 200 * (i // self.ncols),
                anchor=tk.CENTER,
            )
            for i in range(cm_num)
        ]
        # self.attributes("-alpha", 1.0)


# class FigureFrame(ttk.Frame):
#     def __init__(self, container):
#         super().__init__(container)  # Generate canvas instance, Embedding fig in root
#         # self.df


class InputFrame(tk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)
        tcl_validate_input = container.register(
            self.validate_input
        )  # Register validate func to app.
        self.container = container
        # setup the grid layout manager
        self.columnconfigure(
            [
                0,
            ],
            weight=1,
        )
        self.rowconfigure(
            [
                4,
            ],
            weight=1,
        )
        # # self.columns_span = 4

        # browse frame
        self.browse_frame = tk.LabelFrame(self, text="CSV File")
        # self.browse_frame = tk.LabelFrame(self, )
        self.browse_frame.grid(column=0, row=0, ipadx=5, ipady=3, sticky=tk.EW)
        self.browse_frame.columnconfigure(
            [
                0,
            ],
            weight=1,
        )
        # filepath entry
        self.filepath = tk.StringVar()
        self.filepath_label = ttk.Label(
            self.browse_frame, textvariable=self.filepath, wraplength=155
        )
        self.filepath_label.grid(
            column=0,
            row=0,
            sticky=tk.EW,
            padx=5,
        )
        self.filepath_label.focus()
        # self.filepath_delta_entry = ttk.Entry(self.browse_frame, textvariable=self.filepath_delta)
        # self.filepath_delta_entry.grid(column=1, row=1, sticky=tk.EW)
        ## browse button
        self.img_mglass = tk.PhotoImage(file=resource_path("imgs/mglass.png"))
        self.load_button = ttk.Button(
            self.browse_frame,
            image=self.img_mglass,
            command=self.master.load_button_clicked,
        )
        self.load_button.grid(
            column=1,
            row=0,
            sticky=tk.E,
            padx=(0, 5),
        )

        # setting frame
        self.setting_frame = tk.LabelFrame(self, text="Plot Setting")
        self.setting_frame.grid(
            column=0, row=1, ipadx=5, ipady=3, sticky=tk.EW
        )
        # ticks frame
        self.axes_frame = ttk.LabelFrame(self.setting_frame, text="Axis Scale")
        self.axes_frame.grid(column=0, row=0, ipadx=5, ipady=3, sticky=tk.EW)
        self.axes_frame.columnconfigure(
            [
                1,
            ],
            weight=1,
        )
        self.xaxis_interval = tk.DoubleVar()
        self.yaxis_interval = tk.DoubleVar()
        self.xaxis_label = ttk.Label(self.axes_frame, text="x-Interval")
        self.xaxis_label.grid(column=0, row=0, sticky=tk.W)
        self.yaxis_label = ttk.Label(self.axes_frame, text="y-Interval")
        self.yaxis_label.grid(column=0, row=1, sticky=tk.W)
        self.xaxis_entry = ttk.Entry(
            self.axes_frame,
            textvariable=self.xaxis_interval,
            validate="key",
            validatecommand=(tcl_validate_input, "%P", "x-Interval"),
        )
        # self.xaxis_cbox = ttk.Combobox(
        #     self.axes_frame, state="readonly",
        #     textvariable=self.xaxis_interval
        # )
        self.xaxis_entry.grid(column=1, row=0, sticky=tk.E)
        self.yaxis_entry = ttk.Entry(
            self.axes_frame,
            textvariable=self.yaxis_interval,
            validate="key",
            validatecommand=(tcl_validate_input, "%P", "y-Interval"),
        )
        # self.yaxis_cbox = ttk.Combobox(
        #     self.axes_frame, state="readonly",
        #     textvariable=self.yaxis_interval
        # )
        self.yaxis_entry.grid(column=1, row=1, sticky=tk.E)
        # colorscale_frame
        self.colorscale_frame = ttk.LabelFrame(
            self.setting_frame, text="Color Scale"
        )
        self.colorscale_frame.grid(
            column=0, row=1, ipadx=5, ipady=3, sticky=tk.EW
        )
        self.colorscale_frame.columnconfigure(
            [
                1,
            ],
            weight=1,
        )
        self.scalemax_label = ttk.Label(self.colorscale_frame, text="Max")
        self.scalemax_label.grid(column=0, row=0, sticky=tk.W)
        self.scalemin_label = ttk.Label(self.colorscale_frame, text="Min")
        self.scalemin_label.grid(column=0, row=1, sticky=tk.W)
        self.scaleintervals_label = ttk.Label(
            self.colorscale_frame, text="Interval"
        )
        self.scaleintervals_label.grid(column=0, row=2, sticky=tk.W)
        self.scalemax = tk.DoubleVar(value=None)
        self.scalemin = tk.DoubleVar(value=None)
        self.scalemax_entry = ttk.Entry(
            self.colorscale_frame,
            textvariable=self.scalemax,
            validate="key",
            validatecommand=(tcl_validate_input, "%P", "Color Scale-Max"),
        )
        self.scalemax_entry.grid(column=1, row=0, sticky=tk.E)
        self.scalemin_entry = ttk.Entry(
            self.colorscale_frame,
            textvariable=self.scalemin,
            validate="key",
            validatecommand=(tcl_validate_input, "%P", "Color Scale-Min"),
        )
        self.scalemin_entry.grid(column=1, row=1, sticky=tk.E)
        self.scaleinterval = tk.DoubleVar()
        self.scaleinterval_entry = ttk.Entry(
            self.colorscale_frame,
            textvariable=self.scaleinterval,
            validate="key",
            validatecommand=(tcl_validate_input, "%P", "Color Scale-Interval"),
        )
        # self.scaleintervals_cbox = ttk.Combobox(
        #     self.colorscale_frame,
        #     postcommand=self.change_intervalslist,
        #     textvariable=self.scaleinterval,
        # )
        self.scaleinterval_entry.grid(column=1, row=2, sticky=tk.E)
        # axes labal frame
        self.label_frame = ttk.LabelFrame(self.setting_frame, text="Label")
        self.label_frame.grid(column=0, row=2, ipadx=5, ipady=3, sticky=tk.EW)
        self.label_frame.columnconfigure(
            [
                1,
            ],
            weight=1,
        )
        self.xlabel_label = ttk.Label(self.label_frame, text="X Label")
        self.xlabel_label.grid(column=0, row=0, sticky=tk.W)
        self.xlabel = tk.StringVar(value="x")
        self.xlabel_entry = ttk.Entry(
            self.label_frame, textvariable=self.xlabel
        )
        self.xlabel_entry.grid(column=1, row=0, sticky=tk.E)
        self.ylabel_label = ttk.Label(self.label_frame, text="Y Label")
        self.ylabel_label.grid(column=0, row=1, sticky=tk.W)
        self.ylabel = tk.StringVar(value="y")
        self.ylabel_entry = ttk.Entry(
            self.label_frame, textvariable=self.ylabel
        )
        self.ylabel_entry.grid(column=1, row=1, sticky=tk.E)
        self.cbarlabel_label = ttk.Label(self.label_frame, text="Z Label")
        self.cbarlabel_label.grid(column=0, row=2, sticky=tk.W)
        self.cbarlabel = tk.StringVar(value="z ()")
        self.cbarlabel_entry = ttk.Entry(
            self.label_frame, textvariable=self.cbarlabel
        )
        self.cbarlabel_entry.grid(column=1, row=2, sticky=tk.E)
        # fontsize
        self.font_frame = ttk.LabelFrame(self.setting_frame, text="Fontsize")
        self.font_frame.grid(column=0, row=3, ipadx=5, ipady=3, sticky=tk.EW)
        self.font_frame.columnconfigure(
            [
                1,
            ],
            weight=1,
        )
        self.labelsize_label = ttk.Label(self.font_frame, text="Axis Label")
        self.labelsize_label.grid(column=0, row=0, sticky=tk.W)
        self.labelsize = tk.IntVar(value=20)
        self.labelsize_sbox = ttk.Spinbox(
            self.font_frame,
            state="readonly",
            textvariable=self.labelsize,
            from_=1,
            to=30,
        )
        self.labelsize_sbox.grid(column=1, row=0, sticky=tk.E)
        self.tickslabelsize_label = ttk.Label(
            self.font_frame, text="Ticks Label"
        )
        self.tickslabelsize_label.grid(column=0, row=1, sticky=tk.W)
        self.tickslabelsize = tk.IntVar(value=12)
        self.tickslabelsize_sbox = ttk.Spinbox(
            self.font_frame,
            state="readonly",
            textvariable=self.tickslabelsize,
            from_=1,
            to=30,
        )
        self.tickslabelsize_sbox.grid(column=1, row=1, sticky=tk.E)
        # colormap
        self.which_cm = StringVar(value="magma")
        self.cm_frame = ttk.LabelFrame(self.setting_frame, text="Colormap")
        self.cm_frame.grid(column=0, row=4, ipadx=5, ipady=3, sticky=tk.EW)
        self.cm_button = ttk.Button(self.cm_frame, text="Select Colormap")
        self.cm_button["command"] = self.select_cm
        self.cm_button.grid(column=0, row=0)
        self.cm_reversed = BooleanVar()
        self.cm_check = ttk.Checkbutton(
            self.cm_frame,
            text="reversed",
            onvalue=True,
            offvalue=False,
            variable=self.cm_reversed,
        )
        self.cm_check.grid(column=1, row=0)
        # 3d
        self.is_3d = BooleanVar()
        self.threeD_check = ttk.Checkbutton(
            self.setting_frame,
            text="3D",
            onvalue=True,
            offvalue=False,
            variable=self.is_3d,
        )
        self.threeD_check.grid(column=0, row=5, sticky=tk.W)
        # shared option
        for child in self.setting_frame.winfo_children():
            child.grid_configure(padx=3, pady=3)
        # for child in self.winfo_children():
        #     child.configure(bg='white')

        # button frame
        self.button_frame = ttk.Frame(self)
        self.button_frame.grid(column=0, row=3, sticky=tk.EW)
        self.button_frame.columnconfigure(
            [
                0,
            ],
            weight=1,
        )
        # plot button
        self.calculate_button = ttk.Button(
            self.button_frame, text="Plot", state="key"
        )
        self.calculate_button["command"] = self.master.display_figure
        self.calculate_button.grid(column=0, row=0, sticky=tk.NSEW)
        # save button
        self.img_save = tk.PhotoImage(file=resource_path("imgs/save.png"))
        self.save_button = ttk.Button(
            self.button_frame, image=self.img_save, command=self.save_image
        )
        self.save_button.grid(column=1, row=0, padx=(5, 0))

        # result frame
        self.msg_frame = tk.Frame(self, bg="white")
        self.msg_frame.grid(column=0, row=4, sticky=tk.NSEW)
        # result text
        self.msg = tk.StringVar()
        self.msg_dict = {}
        self.msg_box = tk.Message(
            self.msg_frame,
            textvariable=self.msg,
            fg="red",
            bg="white",
            width=190,
            anchor="w",
        )
        self.msg_box.grid(column=0, row=0, sticky=tk.NSEW)

        # shared option
        for child in self.winfo_children():
            child.grid_configure(pady=(0, 3))
            child.columnconfigure(
                [
                    0,
                ],
                weight=1,
            )
        for frame in self.setting_frame.winfo_children():
            for child in frame.winfo_children():
                if isinstance(child, (ttk.Entry, ttk.Spinbox, ttk.Combobox)):
                    child["width"] = 10
                    child.grid_configure(sticky=tk.EW)
                if isinstance(child, (ttk.Label)):
                    child["width"] = 15

    def validate_input(self, input, name):
        try:
            input = float(input)  # Check if half-width digits
            self.calculate_button["state"] = "normal"
            self.msg_dict.pop(name, None)
        except ValueError:  # When "input" is not half-width digits.
            # print(e.__class__)
            if name in ("Color Scale-Max", "Color Scale-Min"):
                self.msg_dict.pop("Color Scale", None)
            self.calculate_button["state"] = "disabled"
            self.msg_dict[name] = (
                f"＊ {name}\n" "       :Enter half-width digits!\n"
            )
            # return False
        else:  # When "input" is half-width digits.
            try:
                if name == "Color Scale-Max":
                    # Also check if half-width digits
                    if input > self.scalemin.get():
                        self.calculate_button["state"] = "normal"
                        self.msg_dict.pop("Color Scale", None)
                    else:
                        self.calculate_button["state"] = "disabled"
                        self.msg_dict["Color Scale"] = (
                            "＊ Color Scale\n"
                            "       :Min is equal to or greater than\n"
                            "        Max!\n"
                        )
                elif name == "Color Scale-Min":
                    if self.scalemax.get() > input:
                        self.calculate_button["state"] = "normal"
                        self.msg_dict.pop("Color Scale", None)
                    else:
                        self.calculate_button["state"] = "disabled"
                        self.msg_dict["Color Scale"] = (
                            "＊ Color Scale\n"
                            "       :Min is equal to or greater than\n"
                            "        Max!\n"
                        )
                elif name == "Color Scale-Interval":
                    if input <= self.scalemax.get() - self.scalemin.get():
                        self.msg_dict.pop("Color Scale", None)
                    else:
                        self.msg_dict[name] = (
                            f"＊ {name}\n"
                            "       :Interval is greater than distance\n"
                            "        between Max & Min!\n"
                        )
            except ValueError:
                # When Max or Min is not half-width digits.
                # print(e, "inner")
                pass
        self.msg.set("".join(self.msg_dict.values()))
        return True

    # def show_warning(self):
    #     if
    #         self.calculate_button["state"] = "disabled"

    def select_cm(self):
        """モーダルダイアログボックスの作成"""
        dlg_modal = ColormapsWindow(app)
        dlg_modal.title("Select Colormap")  # ウィンドウタイトル

        # モーダルにする設定
        # dlg_modal.grab_set()  # モーダルにする
        dlg_modal.focus_set()  # フォーカスを新しいウィンドウへ移す
        # dlg_modal.transient(app)   # タスクバーに表示しない

        # ダイアログが閉じられるまで待つ
        # app.wait_window(dlg_modal)

    def save_image(self):
        savepath = filedialog.asksaveasfilename(
            filetypes=[
                ("PNG", ".png"),
                ("eps", ".eps"),
                ("JPEG", ".jpeg"),
                ("JPEG", ".jpg"),
                ("PDF", ".pdf"),
                ("PGF", ".pgf"),
                ("PS", ".ps"),
                ("RAW", ".raw"),
                ("RGBA", ".rgba"),
                ("SVG", ".svg"),
                ("SVGZ", ".svgz"),
                ("Tiff", ".tif"),
                ("Tiff", ".tiff"),
            ],
            # title="",
            defaultextension="png",
            initialdir=os.path.expanduser("~/Documents"),
        )
        self.container.figure_frame.fig.savefig(savepath, transparent=True)

    def change_intervalslist(self):
        if "" in (self.scalemax.get(), self.scalemin.get()):
            return
        mm_range = self.scalemax.get() - self.scalemin.get()
        _ = self.make_divisors(mm_range)
        self.scaleinterval_entry["values"] = [
            i for i in _ if mm_range / i < 21
        ]

    @staticmethod
    def make_divisors(n):
        multiplier = 10 ** (len(str(n).split(".")[-1]) + 1)
        n_bymultiplier = n * multiplier
        lower_divisors, upper_divisors = [], []
        i = 1
        while i * i <= n_bymultiplier:
            if n_bymultiplier % i == 0:
                lower_divisors.append(i)
                if i != n_bymultiplier // i:
                    upper_divisors.append(n_bymultiplier // i)
            i += 1
        return [i / multiplier for i in lower_divisors + upper_divisors[::-1]]

    # def view(self):
    #     df=pd.read_csv(self.filepath,header=None)
    #     # df_=file.parse(sheet_name=0,header=None)
    #     # df_.drop(df_k1_refbehind.index[[0]])
    #     df = df.dropna(axis=1)
    #     print(df)


#     # def preview_csv(self):
#     #     de


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Csv Heatmapper")
        self.attributes("-alpha", 0.0)
        # self.resizable(width=False, height=False)
        self.minsize(width=400, height=720)
        icon = tk.PhotoImage(file=resource_path("imgs/icon.png"))
        self.tk.call("wm", "iconphoto", self._w, icon)

        menubar = tk.Menu(self)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Document", command=self.display_doc)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.config(menu=menubar)

        # layout on the root window
        self.columnconfigure([1], weight=1)
        self.rowconfigure([0], weight=1)
        # create the input frame
        self.input_frame = InputFrame(
            self,
            width=200,
        )
        self.input_frame.grid(
            column=0, row=0, sticky=tk.NSEW, padx=10, pady=10
        )
        self.input_frame.grid_propagate(False)

        # self.figure_frame = tk.Frame(
        #     self, width=900, height=720, background="#E6E6FA"
        # )
        # self.figure_frame.grid(
        #     column=1, row=0, sticky=tk.NSEW, padx=(0, 10), pady=10
        # )
        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.grid(
            column=1, row=0, sticky=tk.NSEW, padx=(0, 10), pady=10
        )
        # self.canvas_frame.grid_propagate(False)
        self.canvas_frame.columnconfigure([0], weight=1)
        self.canvas_frame.rowconfigure([1], weight=1)
        self.frame_canvas = tk.Canvas(
            self.canvas_frame, width=900, height=720, background="#E6E6FA"
        )
        self.frame_canvas.grid(column=0, row=1, sticky=tk.NSEW)
        # self.frame_canvas.propagate(False)
        v_scrollbar = tk.Scrollbar(self.canvas_frame, orient=tk.VERTICAL)
        v_scrollbar.grid(row=0, column=1, sticky="news", rowspan=2)
        v_scrollbar.configure(command=self.frame_canvas.yview)
        h_scrollbar = tk.Scrollbar(self.canvas_frame, orient=tk.HORIZONTAL)
        h_scrollbar.grid(row=2, column=0, sticky="news")
        h_scrollbar.configure(command=self.frame_canvas.xview)
        self.frame_canvas.configure(
            xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set
        )
        self.figure_frame: pd.DataFrame = tk.Frame(master=self.frame_canvas)
        self.figure_frame.bind(
            "<Configure>",
            # lambda e: self.frame_canvas.configure(
            #     scrollregion=self.frame_canvas.bbox("all")
            # ),
            self.on_resize,
        )
        self.frame_canvas.create_window(
            (0, 0), window=self.figure_frame, anchor="nw"
        )  # フレームをキャンバスへ描画
        # self.figure_frame.columnconfigure([0], weight=1)

        self.analyzedvalues = tk.StringVar(value="Load a csv-like file.")
        self.statusbar = tk.Label(
            self,
            textvariable=self.analyzedvalues,
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
        )
        self.statusbar.grid(column=0, row=1, columnspan=2, sticky=tk.EW)

        self.df: pd.DataFrame = None
        self.df_mean = 0.0
        self.df_max = 0.0
        self.df_min = 0.0
        self.is_first = True

    @staticmethod
    def display_doc():
        webbrowser.open(resource_path("docs/index.html"))

    def on_resize(self, event):
        self.frame_canvas.configure(scrollregion=self.frame_canvas.bbox("all"))
        # print(self.frame_canvas.bbox("all"))

    def load_button_clicked(self):
        csv_path = self._browse_inputfile()
        if csv_path and csv_path != self.input_frame.filepath.get():
            self.is_first = True  # regard when csv is read as the first time
            self.input_frame.filepath.set(csv_path)
            self._create_df(csv_path)
            self._update_analyzedvalues()
            if self.df.size > 10_000:
                self.input_frame.is_3d.set(False)
                self.input_frame.threeD_check["state"] = "disabled"
            else:
                self.input_frame.threeD_check["state"] = "normal"

            self.display_figure()

    def _browse_inputfile(self):
        return filedialog.askopenfilename(
            filetypes=[
                ("CSV-like files", "*.csv"),
                ("CSV-like files", "*.xlsx"),
            ],
            title="load",
            initialdir=os.path.expanduser("~/Documents"),
        )

    def _create_df(self, csv_path):
        if os.path.splitext(csv_path)[-1].lower() == ".csv":
            self.df = pd.read_csv(csv_path, header=None).dropna(axis=1)
        else:
            df_file = pd.ExcelFile(csv_path)
            self.df = df_file.parse(sheet_name=0, header=None).dropna(axis=1)

    def _update_analyzedvalues(self):
        self.df_mean = self.df.mean().mean()
        self.df_max = self.df.max().max()
        self.df_min = self.df.min().min()
        self.analyzedvalues.set(
            (
                f"Max: {self.df_max}, "
                f"Min: {self.df_min}, "
                f"Mean: {self.df_mean}"
            )
        )

    def display_figure(self):
        t_before = perf_counter()
        if (fig := self.plot()) is None:
            return
        logger.info("ploting time: {} s".format(perf_counter() - t_before))
        try:
            figure_canvas = FigureCanvasTkAgg(fig, master=self.figure_frame)
            figure_canvas.draw()
            toolbar = MyNavigationToolbar(
                figure_canvas, self.canvas_frame, pack_toolbar=False
            )
            toolbar.update()
            # toolbar.pack(
            #     side="top",
            # )
            toolbar.grid(column=0, row=0, sticky=tk.EW)
            figure_canvas.get_tk_widget().grid(column=0, row=1, sticky=tk.NSEW)
        except ValueError:  # Error(Latex) in drawing figure
            pass
            # print(traceback.format_exception(*sys.exc_info()))
            # figure_canvas = FigureCanvasTkAgg(fig, master=self.figure_frame)

    def plot(self):
        if self.input_frame.filepath.get() == "":
            return None
        plt.close("all")

        df = self.df
        fig = plt.figure(figsize=(9, 6), dpi=100, tight_layout=True)

        df_width = len(df.columns)
        df_height = len(df)
        labelsize = self.input_frame.labelsize.get()
        tickslabelsize = self.input_frame.tickslabelsize.get()

        if self.is_first:  # set initial values
            self.is_first = False
            cmax = float(math.ceil(self.df_max))
            cmin = float(math.floor(self.df_min))
            cinterval = self.determine_interval(cmax - cmin, True)
            x_interval = self.determine_interval(df_width)
            y_interval = self.determine_interval(df_height)
            self.input_frame.scalemax.set(cmax)
            self.input_frame.scalemin.set(cmin)
            self.input_frame.scaleinterval.set(cinterval)
            self.input_frame.xaxis_interval.set(x_interval)
            self.input_frame.yaxis_interval.set(y_interval)
            self.input_frame.msg_dict = {}
            self.input_frame.msg.set("")
            self.input_frame.calculate_button["state"] = "normal"
            # self.input_frame.change_intervalslist()
        else:
            cmax = self.input_frame.scalemax.get()
            cmin = self.input_frame.scalemin.get()
            # self.input_frame.change_intervalslist()
            cinterval = self.input_frame.scaleinterval.get()
            x_interval = self.input_frame.xaxis_interval.get()
            y_interval = self.input_frame.yaxis_interval.get()

        cbar_norm = mpl.colors.Normalize(cmin, cmax)
        cmap = self.input_frame.which_cm.get()
        if self.input_frame.cm_reversed.get():
            cmap = cmap + "_r"

        if self.input_frame.is_3d.get():
            ax = fig.add_subplot(111, projection="3d")
            ax.set_box_aspect((1, 1, 0.1))
            list_x = np.array(
                [
                    x + (-1) ** n * 0.5
                    for x in range(1, df_width + 1)
                    for n in range(1, 3)
                ]
            )
            list_y = np.array(
                [
                    x + (-1) ** n * 0.5
                    for x in range(1, df_height + 1)
                    for n in range(1, 3)
                ]
            )
            X, Y = np.meshgrid(list_x, list_y)
            arr = np.kron(df, np.ones((2, 2)))
            ax.plot_surface(
                X,
                Y,
                arr,
                cmap=cmap,
                norm=cbar_norm,
                linewidth=0.1,
                edgecolor="black",
                rstride=1,
                cstride=1,
            )
            # ax.plot_surface(
            #     X,
            #     Y,
            #     arr,
            #     linewidth=0.4,
            #     facecolors=cm.get_cmap(cmap)(cbar_norm(arr)),
            #     rstride=1,
            #     cstride=1,
            # )

            # list_x = np.arange(1, df_width + 1)
            # list_y = np.arange(1, df_height + 1)
            # x, y = np.meshgrid(list_x, list_y)
            # ax.plot_surface(
            #     x,
            #     y,
            #     df,
            #     facecolors=cm.get_cmap(cmap)(cbar_norm(df)),
            #     rstride=1,
            #     cstride=1,
            #     shade=False,
            # )

            # ax.plot_trisurf(
            #     x.ravel(),
            #     y.ravel(),
            #     df.to_numpy().ravel(),
            #     cmap=cmap,
            #     shade=False,
            # )

            Xs_2d, Ys_2d = np.meshgrid(
                np.arange(1, df_width + 1), np.arange(1, df_height + 1)
            )
            Xs = Xs_2d.ravel()
            Ys = Ys_2d.ravel()
            Zs = df.to_numpy().ravel()
            data = np.stack((Xs, Ys, Zs), axis=-1)
            ind = np.argsort(data[:, -1])
            data_sorted = data[ind]
            # print(data_sorted)
            tops = Zs - self.df_min
            cmap_instance = cm.get_cmap(cmap)
            # for x, y, z in data_sorted:
            #     ax.bar3d(
            #         x=x - 0.5,
            #         y=y - 0.5,
            #         z=self.df_min,
            #         dx=1,
            #         dy=1,
            #         dz=z - self.df_min,
            #         shade=True,
            #         alpha=1,
            #         color=cmap_instance(cbar_norm(z)),
            #         rasterized=True,
            #     )
            # i = 2
            # for x, y, z in zip(Xs, Ys, Zs):
            #     print(f"({x},{y},{z})")
            #     ax.bar3d(
            #         x=x - 0.5,
            #         y=y - 0.5,
            #         z=self.df_min,
            #         dx=1,
            #         dy=1,
            #         dz=z - self.df_min,
            #         shade=True,
            #         alpha=1,
            #         color=cmap_instance(cbar_norm(z)),
            #         rasterized=True,
            #         zorder=i,
            #     )
            #     i += 1
            # ax.bar3d(
            #     x=Xs - 0.5,
            #     y=Ys - 0.5,
            #     z=self.df_min,
            #     dx=1,
            #     dy=1,
            #     dz=tops,
            #     shade=True,
            #     alpha=1,
            #     color=cmap_instance(cbar_norm(Zs)),
            #     rasterized=True,
            # )
            cbar = fig.colorbar(
                mpl.cm.ScalarMappable(norm=cbar_norm, cmap=cmap),
                ax=ax,
            )
            ax.tick_params(axis="z", labelsize=tickslabelsize, pad=10)
            ax.set_xlim3d(0.5, df_width + 0.5)
            ax.set_ylim3d(df_height + 0.5, 0.5)
            ax.set_zlim3d(math.floor(self.df_min), math.ceil(self.df_max))
            # ax.set_zlabel(
            #     rf"{(self.input_frame.cbarlabel.get())}",
            #     fontsize=labelsize,
            #     labelpad=15,
            # )
            ax.set_box_aspect((df_width, df_height, max(df_height, df_width)))
        else:
            ax = fig.add_subplot(111)
            extent = 0.5, df_width + 0.5, df_height + 0.5, 0.5
            ax.matshow(df, norm=cbar_norm, cmap=cmap, extent=extent)
            # # ax.matshow(df, norm=cbar_norm, cmap=cmap,)
            ax.xaxis.set_label_position("top")
            ax.yaxis.set_ticks_position("both")

            divider = make_axes_locatable(ax)  # axに紐付いたAxesDividerを取得
            cax = divider.append_axes(
                "right", size="3%", pad=0.2
            )  # append_axesで新しいaxesを作成
            cbar = fig.colorbar(
                mpl.cm.ScalarMappable(norm=cbar_norm, cmap=cmap),
                cax=cax,
            )
        cbar.set_label(
            rf"{(self.input_frame.cbarlabel.get())}", fontsize=labelsize
        )
        cbar.ax.set_yticks(
            # [cmin]
            # + (
            #     _ := [
            #         tick
            #         for i in range(cbar_step)
            #         if (tick := round(cmin + (i + 1) * cinterval, 3)) != cmax
            #     ]
            # )
            # + [cmax]
            np.concatenate(
                [
                    [cmin],
                    _ := np.round(
                        np.arange(cmin + cinterval, cmax, cinterval),
                        len(str(cinterval).split(".")[-1]),
                    ),
                    [cmax],
                ]
            )
        )
        cbar.ax.set_yticklabels(
            # [rf"$\leq {float(cmin)}$"]
            # + [f"${i}$" for i in _]
            # + [rf"$\geq {float(cmax)}$"]
            [r"$\leq %s$" % str(cmin).rstrip("0").rstrip(".")]
            + [r"$%s$" % str(i).rstrip("0").rstrip(".") for i in _]
            + [r"$\geq %s$" % str(cmax).rstrip("0").rstrip(".")]
        )

        ax.set_xticks(
            list(np.arange(x_interval, df_width + 1, x_interval))
            if x_interval == 1
            else [1]
            #     + [
            #         i
            #         for i in range(int(x_interval), df_width + 1, int(x_interval))
            #     ]
            + list(np.arange(x_interval, df_width + 1, x_interval))
        )
        ax.set_yticks(
            list(np.arange(y_interval, df_height + 1, y_interval))
            if y_interval == 1
            else [1]
            # + [
            #     i
            #     for i in range(int(y_interval), df_height + 1, int(y_interval))
            # ]
            + list(np.arange(y_interval, df_height + 1, y_interval))
        )
        cbar.ax.tick_params(axis="y", labelsize=tickslabelsize)
        ax.tick_params(axis="x", labelsize=tickslabelsize)
        ax.tick_params(axis="y", labelsize=tickslabelsize)
        ax.set_xlabel(
            rf"{(self.input_frame.xlabel.get())}", fontsize=labelsize
        )
        ax.set_ylabel(
            rf"{(self.input_frame.ylabel.get())}", fontsize=labelsize
        )
        # cbar.ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        # cbar.ax.ticklabel_format(style="sci",  axis="y",scilimits=(0,0))
        # cbar.ax.yaxis.set_offset_position('left')
        # cbar.ax.text(0, 90, r'$\times$10$^{-1}$', va='bottom', ha='left')

        # _ = (
        #     list(range(1, 10))
        #     + [i for i in range(10, df_width, 5)]
        #     + [df_width]
        #     if df_width > 10
        #     else list(range(1, df_width + 1))
        # )
        # self.input_frame.xaxis_entry["values"] = [
        #     i for i in _ if df_width / i < 21
        # ]
        # _ = (
        #     list(range(1, 10))
        #     + [i for i in range(10, df_height, 5)]
        #     + [df_height]
        #     if df_height > 10
        #     else list(range(1, df_height + 1))
        # )
        # self.input_frame.yaxis_entry["values"] = [
        #     i for i in _ if df_height / i < 21
        # ]

        self.figure_frame.fig = fig
        return fig

    @staticmethod
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


def center(win):
    screen_width = win.winfo_screenwidth()  # モニター横幅取得
    screen_height = win.winfo_screenheight()  # モニター縦幅取得
    # w = int((w - float(re.split("[+]", win.geometry())[1]))/2)  # メイン画面横幅分調整
    # h = int((h - float(re.split("[+]", win.geometry())[2]))/2)  # メイン画面縦幅分調整
    # win.geometry("+" + str(w // 2 - 572) + "+" + str(h // 2 - 310))  # 位置設定
    size = tuple(int(_) for _ in win.geometry().split("+")[0].split("x"))
    print(screen_width, screen_height, size, sep="\n")
    x = screen_width / 2 - size[0] / 2
    y = screen_height / 2 - size[1] / 2
    win.geometry("+%d+%d" % (x, y))


def on_closing():
    app.quit()
    app.destroy()


if __name__ == "__main__":
    # df = pd.DataFrame()
    app = App()
    # center(app)
    app.eval("tk::PlaceWindow . center")

    app.attributes("-alpha", 1.0)
    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()
