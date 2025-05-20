import minecraft_launcher_lib as mc
from os import getenv, path


appdata = getenv("APPDATA")
mcdir = path.join(appdata, "PlinxMC", "Installations")
cnfgdir = path.join(appdata, "PLinxMC", "Config")
