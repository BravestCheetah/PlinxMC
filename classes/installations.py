from minecraft_launcher_lib import install, command, utils
from subprocess import Popen

#   Usage: install_version("1.21.5", "path/to/version/dir/")
def install_version(ver: str, path: str) -> None:
    install.install_minecraft_version(ver, path)

#   Usage: launch_version("1.21.5", "path/to/version/dir/", your_options)
def launch_version(ver: str, mcdir: str, options: dict) -> None:
    cmd = command.get_minecraft_command(ver, mcdir, options)
    Popen(cmd)

def get_versions(mcdir: str, include_snapshots: bool = False):
    all_versions = utils.get_available_versions(mcdir)
    versions = []
    for version in all_versions:
        if version["type"] == "snapshot" and include_snapshots:
            versions.append(version["id"])
        elif version["type"] == "release":
            versions.append(version["id"])

    return versions

def get_latest_version():
    return utils.get_latest_version()["release"]
