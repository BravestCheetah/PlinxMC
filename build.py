import PyInstaller.__main__

from os import remove, system
from shutil import rmtree, move
from os.path import exists
from termcolor import colored

system("clear")

done = colored("[ DONE ]", "green")
info = colored("[ INFO ]", "yellow")

print(info, "Starting Building Process...")
print(info, "Removing old builds...")

if exists("PlinxMC.exe"):
    remove("PLinxMC.exe")

print(info, "Building Executeable (May take a while)...")

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

print(info, "Removing Temporary Build files...")
if exists("PlinxMC.spec"):
    remove("PlinxMC.spec")

if exists("build"):
    rmtree("build")

print(info, "Moving Exe to root dir...")
if exists("dist/PlinxMC.exe"):
    move("dist/PlinxMC.exe", "PlinxMC.exe")

print(info, "Clean up folders...")
if exists("dist"):
    rmtree("dist")

print(done, "Building Process completed! Build can be found at PlinxMC.exe")
print(done, "You can now close this window")
