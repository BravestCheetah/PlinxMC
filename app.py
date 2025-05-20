import minecraft_launcher_lib as mc
import customtkinter as ctk

import classes.dir_paths
import classes.installations


class PlinxMC(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PlinxMC - A lightweight Launcher")
        self.geometry("1000x600")

app = PlinxMC()
app.mainloop()