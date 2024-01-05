import sys
from pathlib import Path

running = True

def is_bundled_app() -> bool:
    """
    :return: Whether the app is running in a bundled app (i.e. something built by pyinstaller.)
    """
    return getattr(sys, "frozen", False)


def is_virtualenv() -> bool:
    """
    :return: Whether we are running in a virtualenv (True) or in the global Python environment (False)
    """
    return sys.prefix != sys.base_prefix


def get_base_path() -> Path:
    """
    :return: A `Path` object to the base directory of the app (where `muddyboots.py` or `muddyboots.exe`
             are located.)
    """
    if is_bundled_app():
        return Path(sys.executable).parent
    else:
        return Path(__file__).parent.parent