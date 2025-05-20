from minecraft_launcher_lib import install

#   Usage: install_version("1.21.5", "path/to/version/dir/")
def install_version(ver: str, path: str) -> None:
    install.install_minecraft_version(ver, path)