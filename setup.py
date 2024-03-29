# python setup.py bdist_msi
from cx_Freeze import setup, Executable
import sys
import os

app_name = "CsvHeatmapper"
version = "3.0.3"
# Dependencies are automatically detected, but it might need
# fine tuning.
# # importして使っているライブラリを記載（こちらの方が軽くなるという噂）
includes = [
    "sys",
    "os",
    "tkinter",
    "pandas",
    "math",
    "matplotlib",
    "webbrowser",
]

# excludesでは、パッケージ化しないライブラリやモジュールを指定する。
"""
numpy,pandas,lxmlは非常に重いので使わないなら、除く。（合計で80MBほど）
他にも、PIL(5MB)など。
"""
matches = ["LICENSE", "LICENCE.rst", "LICENSE.txt", "METADATA", "PKG-INFO"]
lics = []
print("Find 3rd party dependency license files")
for root, dir, files in os.walk(".venv/Lib/site-packages"):
    for file in files:
        if file in matches:
            src = f"{root}/{file}"
            dest = f"licenses/{os.path.basename(root)}/{file}"
            lics.append((src, dest))
            print(f"\tLicense file: {root}/{file}")
            # print(dest)
print(
    f"{len(lics)} dependency licenses found. Copying to /license folder in distribution"
)
print(["imgs", "docs", *lics])
excludes = ["cx_Freeze", "pip", "pip-license", "setuptools", "cv2"]
build_options = {
    "includes": includes,
    "packages": [],
    "excludes": excludes,
    "include_files": ["imgs", "docs", "LICENSE", *lics],
}


base = "Win32GUI" if sys.platform == "win32" else None

executables = [
    Executable(
        "app.py",
        base=base,
        icon="imgs/icon.ico",
        target_name=app_name,
        shortcut_name=f"{app_name} {version}",
        shortcut_dir="ProgramMenuFolder",
        copyright="Copyright (c) 2022 Yolyne",
    )
]

shortcut_table = [
    (
        "DesktopShortcut",  # Shortcut
        "DesktopFolder",  # Directory_
        app_name,  # Name
        "TARGETDIR",  # Component_
        f"[TARGETDIR]{app_name}",  # Target
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
    "initial_target_dir": f"[ProgramFiles64Folder]{app_name}",
}

setup(
    name=app_name,
    version=version,
    author="Yolyne",
    description="convert 2-dimention csv to Heatmap",
    options={
        "build_exe": build_options,
        "bdist_msi": bdist_msi_options,
    },
    executables=executables,
)
