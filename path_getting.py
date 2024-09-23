import os
import sys


# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
class PathName:
    def __init__(self):
        """
        Get absolute path to resource, works for dev and for PyInstaller
        """
        pass

    @staticmethod
    def resource_path(relative_path: str) -> str:
        """
        Get absolute path to resource, works for dev and for PyInstaller
        :param relative_path: relative path
        :return: os relative path
        """

        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS2
            base_path = sys._MEIPASS2

        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
