import minecraft_launcher_lib as mc
import customtkinter as ctk
from PIL import Image

import classes.dir_paths
import classes.asset_paths
import classes.installations

dir_paths = classes.dir_paths.Dirs()
asset_paths = classes.asset_paths.Assets()

class PlinxMC(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.selected_version = ctk.StringVar(value=classes.installations.get_latest_version())

        self.title("PlinxMC - A lightweight Launcher")
        self.geometry("1000x600")
        ctk.set_appearance_mode("dark")
        self.configure(fg_color='#663f9e')

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.bgimg = Image.open(asset_paths.splashscreen)
        self.bg = ctk.CTkImage(self.bgimg, size=(1000, 525))
        self.bg_label = ctk.CTkLabel(self, image=self.bg, text="", corner_radius=15)
        self.bg_label.place(relx=0.5, y=0, anchor="n")

        self.play_button = ctk.CTkButton(self, width=150, height=45, text="Play!", fg_color="#522492", hover_color="#5C2D9E")
        self.play_button.grid(row=1, column=1, sticky="se", padx=20, pady=15)

        self.all_versions = classes.installations.get_versions(dir_paths.mcdir)

        visible_versions = self.all_versions[:15] + ["More..."]

        self.version_select = ctk.CTkComboBox(
            self,
            values=visible_versions,
            variable=self.selected_version,
            width=150,
            height=45,
            fg_color="#522492",
            border_color="#522492",
            button_color="#522492",
            button_hover_color="#5C2D9E",
            dropdown_fg_color="#522492",
            dropdown_hover_color="#5C2D9E",
            dropdown_text_color="#dfdfdf"
        )
        self.version_select.set(classes.installations.get_latest_version())
        self.version_select.grid(row=1, column=0, sticky="sw", padx=20, pady=15)
        self.version_select.configure(command=self.handle_version_change)

    def handle_version_change(self, choice):
        if choice == "More...":
            self.open_full_version_picker()
        else:
            self.selected_version.set(choice)

    def open_full_version_picker(self):
        popup = ctk.CTkToplevel()
        popup.configure(fg_color='#663f9e')
        popup.title("Version Select | PLinxMC")
        popup.grid_columnconfigure(0, weight=1)
        popup.grid_rowconfigure(0, weight=1)

        scroll_frame = ctk.CTkScrollableFrame(popup, width=300, height=360, fg_color="#522492", scrollbar_button_color="#663f9e")
        scroll_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        for version in self.all_versions:
            btn = ctk.CTkButton(scroll_frame, text=version, width=280,
                                command=lambda v=version: self.select_version(popup, v),
                                fg_color="#522492", hover_color="#5C2D9E")
            btn.pack(pady=2, anchor="w")
        
    def select_version(self, window, version):
        self.selected_version.set(version)
        self.version_select.set(version)
        window.destroy()




app = PlinxMC()
app.mainloop()
