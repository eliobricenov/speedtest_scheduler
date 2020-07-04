import pathlib


def get_script_path(file):
    return pathlib.Path(file).parent.absolute()

