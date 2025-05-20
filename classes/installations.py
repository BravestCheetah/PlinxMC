from minecraft_launcher_lib import install, command
from subprocess import Popen

#   Usage: install_version("1.21.5", "path/to/version/dir/")
def install_version(ver: str, path: str) -> None:
    install.install_minecraft_version(ver, path)

#   Usage: launch_version("1.21.5", "path/to/version/dir/", your_options)
def launch_version(ver: str, mcdir:str, options:dict) -> None:
    cmd = command.get_minecraft_command(ver, mcdir, options)
    Popen(cmd)