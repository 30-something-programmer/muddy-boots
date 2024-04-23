import sys
import yaml
from pathlib import Path
from modules.runtime import get_base_path


class Config(dict):

    def __init__(self, file_path) -> None:
        self.load(file_path)

    def load(self, file_path: Path) -> dict:
        """
        Loads and validates a single config file.

        :param file_path: Path to the config file
        """
        try:
            yaml_file = yaml.safe_load(open(file_path))
            for key in yaml_file:
                self[key] = yaml_file[key]
        except Exception as e:
            print(f"Config file {str(file_path)} is invalid! -- {e}")
            sys.exit(1)

config = Config(get_base_path() / "config/config.yml")
