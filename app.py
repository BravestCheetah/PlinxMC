import minecraft_launcher_lib as mc

import classes.dir_paths
import classes.installations


paths = classes.dir_paths.Paths()

if input(":::->  ") == "1":
    classes.installations.install_version("1.20.4", paths.mcdir)
else:
    classes.installations.launch_version("1.20.4", paths.mcdir, mc.utils.generate_test_options())