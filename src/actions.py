import os
import time
from pathlib import Path

def progress_print(output) -> None:
    print()
    print(output)

def get_immediate_subdirectories(a_dir) -> list[str]:
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def get_roblox_folder() -> Path:
    """Gets correct Roblox folder in Versions folder"""
    roblox_folder = Path(os.getenv("LOCALAPPDATA"), "Roblox", "Versions")

    # Get all version folders
    immediate_subdirs = get_immediate_subdirectories(roblox_folder)

    # Find `RobloxPlayerLauncher.exe` in folders
    for subdir in immediate_subdirs:
        if Path(roblox_folder, subdir, "RobloxPlayerLauncher.exe").exists():
            roblox_folder = Path(roblox_folder, subdir)
            break

    return roblox_folder

def unlock_fps() -> None:
    # Get Roblox versions folder -> C:\Users\{USER}\AppData\Local\Roblox\Versions\{whatever folder `RobloxPlayerLauncher.exe` is in}
    roblox_folder = get_roblox_folder()

    # Make ClientSettings folder and copy ClientAppSettings.json file into there
    os.mkdir(Path(roblox_folder, "ClientSettings"))

    # Wait until folder exists
    while not Path.exists(Path(roblox_folder, "ClientSettings")):
        time.sleep(.1)

    with open("ClientAppSettings.json", "r") as file:
        # Gets text from ClientAppSettings.json
        text = file.read()
        with open(Path(roblox_folder, "ClientSettings", "ClientAppSettings.json"), "w+") as file2:
            # Creates the same file and contents into the roblox folder
            file2.write(text)
            file2.close()
        file.close()

def nothing() -> None:
    """For tasks that are just informative and do nothing"""
    pass