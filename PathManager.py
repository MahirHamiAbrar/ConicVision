import os
# from importlib.util import find_spec

# might uncomment it in the later version.
# PROJECT_DIR_PATH = os.path.dirname(
#     find_spec("ConicVision").origin
# )

PROJECT_DIR_PATH = os.path.dirname(
    __file__
)

DATA_DIR_PATH = os.path.join(PROJECT_DIR_PATH, 'data')
DEFAULT_SETTINGS_FILE_PATH = os.path.join(DATA_DIR_PATH, 'DefaultSettings.json')


def getPath(insider_path: str):
    return os.path.join(
        PROJECT_DIR_PATH,
        insider_path
    )


def getUIFilePath(file_name: str):
    return os.path.join(
        PROJECT_DIR_PATH,
        "Gui/assets/UIFiles",
        file_name
    )


def getStylesheetPath(file_name: str):
    return os.path.join(
        PROJECT_DIR_PATH,
        "Gui/assets/Stylesheets",
        file_name
    )


def getIconPath(file_name: str):
    return os.path.join(
        PROJECT_DIR_PATH,
        "Gui/assets/Icons",
        file_name
    )

def getAppDataFile(file_name: str) -> str:
    return os.path.join(
        PROJECT_DIR_PATH,
        "AppData",
        file_name
    )


if __name__ == '__main__':
    print(f"{PROJECT_DIR_PATH = }")
