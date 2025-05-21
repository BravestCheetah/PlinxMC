import minecraft_launcher_lib as mc
import customtkinter as ctk
from PIL import Image

import classes.dir_paths
import classes.asset_paths
import classes.installations

dir_paths = classes.dir_paths.Dirs()
asset_paths = classes.asset_paths.Assets()

# a566ff

class PlinxMC(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PlinxMC - A lightweight Launcher")
        self.geometry("1000x600")
        ctk.set_appearance_mode("dark")
        self.configure(fg_color='#663f9e')

        self.grid_columnconfigure((0, 1), weight=1)

        self.bgimg = Image.open(asset_paths.splashscreen)
        self.bg = ctk.CTkImage(self.bgimg, size=(1000, 525))
        self.bg_label = ctk.CTkLabel(self, image=self.bg, text="")
        self.bg_label.place(relx=0.5, y=0, anchor="n")

        



        

app = PlinxMC()
app.mainloop()