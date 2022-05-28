# python setup.py bdist_msi
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
# # importして使っているライブラリを記載（こちらの方が軽くなるという噂）
includes = [
    "sys",
    "os",
    "tkinter",
    "pandas",
    "math",
    "matplotlib",]

# excludesでは、パッケージ化しないライブラリやモジュールを指定する。
"""
numpy,pandas,lxmlは非常に重いので使わないなら、除く。（合計で80MBほど）
他にも、PIL(5MB)など。
"""
excludes = [
    "lxml",
    "PyQt4",
    "PyQt5",
    "pip"
]
build_options = {'includes': includes, 'packages': [], 'excludes': excludes, "include_files": "images",}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable(
        'app.py',
        base=base,
        icon="images/icon.ico",
        target_name = 'Csv Heatmapper',
        shortcut_name="Csv Heatmapper",
        shortcut_dir="ProgramMenuFolder",
    )
]

shortcut_table = [
    (
        "DesktopShortcut",  # Shortcut
        "DesktopFolder",  # Directory_
        "Csv Heatmapper",  # Name
        "TARGETDIR",  # Component_
        "[TARGETDIR]Csv Heatmapper",  # Target
        None,  # Arguments
        None,  # Description
        None,  # Hotkey
        None,  # Icon
        None,  # IconIndex
        None,  # ShowCmd
        "TARGETDIR",  # WkDir
    )
]

msi_data = {"Shortcut": shortcut_table}

upgrade_code = "{59745BEA-C550-4066-A77D-88B494F22C82}"

bdist_msi_options = {
    "upgrade_code": upgrade_code,
    "data": msi_data,
    "initial_target_dir": f"[ProgramFiles64Folder]Csv Heatmapper",
}

setup(
    name='Csv Heatmapper',
    version = '1.1',
    author="yoririn",
    description = 'convert 2-dimention csv to Heatmap',
    options = {
        'build_exe': build_options,
        "bdist_msi": bdist_msi_options,
    },
    executables = executables
)
