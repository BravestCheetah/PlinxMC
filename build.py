import PyInstaller.__main__

from os import remove
from shutil import rmtree, move
from os.path import exists

print("[ INFO ] Starting Building Process...")
print("[ INFO ] Removing old builds...")

if exists("PlinxMC.exe"):
    remove("PLinxMC.exe")

print("[ INFO ] Building Executeable (May take a minute)...")

PyInstaller.__main__.run([
    'app.py',
    '--onefile',
    '--name=PlinxMC',
    '--noconfirm',
    '--clean',
    # '--windowed',

    "--icon=assets/exeicon.ico",
    '--log-level=ERROR',

])

print("[ INFO ] Removing Temporary Build files...")
if exists("PlinxMC.spec"):
    remove("PlinxMC.spec")

if exists("build"):
    rmtree("build")

print("[ INFO ] Moving Exe to root dir...")
if exists("dist/PlinxMC.exe"):
    move("dist/PlinxMC.exe", "PlinxMC.exe")

print("[ INFO ] Clean up folders...")
if exists("dist"):
    rmtree("dist")

print("[ DONE ] Building Process completed! Build can be found at PlinxMC.exe")
print("[ DONE ] You can now close this window")
