import os
import shutil


def copy_and_replace(source_path, destination_path):
    if os.path.exists(destination_path):
        os.remove(destination_path)
    shutil.copy2(source_path, destination_path)


file_need_to_remove = 'settings/test.txt'
file_for_copy = 'settings/default/test.txt'

copy_and_replace(file_for_copy, file_need_to_remove)