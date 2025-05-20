from os import getenv, path

class Dirs():
    def __init__(self):

        self.appdata = getenv("APPDATA")
        self.mcdir = path.join(self.appdata, "PlinxMC", "Installations")
        self.cnfgdir = path.join(self.appdata, "PLinxMC", "Config")