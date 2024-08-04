import os
import sys


# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
class PathName:
    def __init__(self):
        pass

    @staticmethod
    def resource_path(relative_path):
        """
        Get absolute path to resource, works for dev and for PyInstaller
        """

        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS2
            base_path = sys._MEIPASS2

        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
