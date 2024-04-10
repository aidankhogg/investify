import os
from pathlib import Path
from typing import Union
from omegaconf import OmegaConf, DictConfig

from engine.tools.places import local_paths
from engine.cacher import cached, conf_cache
from engine.ignition import get_project_path

accepted_file_extensions = [".yaml", ".yml", '.conf']

if os.environ.get('INVESTIFY_PATH', None) is None:
    os.environ['INVESTIFY_PATH'] = get_project_path('requirements.txt')


def is_as_conf_file(filepath: Union[str, Path, os.PathLike]) -> bool:
    """
    Checks if a file exist and a valid extension
    :param filepath:
    :return:
    """

    if os.path.isfile(filepath):
        if os.path.splitext(filepath)[1] in accepted_file_extensions:
            return True
    #
    return False


@cached(conf_cache)
def load_single_conf_file(filepath: Union[Path, os.PathLike, str],
                          keep_filename: bool = True) -> Union[OmegaConf, DictConfig]:
    """
    Load a single config file.

    (accepted extensions are .yaml, .yml, or .conf)
    :param filepath: full path to config file (will attempt a relative load if not found).
    :param keep_filename: use the filename without extension as the parent key for the config file.
    :return: an omegaconf object with the loaded configuration.
    """""

    # Make sure the path is a Path object and exists
    filepath = Path(filepath)
    if not filepath.is_file():
        raise FileNotFoundError(f"File not found: {filepath}")

    # Load the configuration file
    config = OmegaConf.load(filepath)

    if keep_filename:
        # Get filename without extension
        filename_key = filepath.stem
        # Return a new OmegaConf with the filename as the parent key
        return OmegaConf.create({filename_key: config})

    else:
        return OmegaConf.create(config)


def load_multiple_conf_files(filepaths: Union[str, Path, os.PathLike, list]) -> Union[OmegaConf, DictConfig]:
    """
    Load multiple config files.
    :param filepaths:
    :return:
    """
    loaded = OmegaConf.create()
    if isinstance(filepaths, list):
        for filepath in filepaths:
            # Does it exist?
            if not os.path.exists(filepath):
                raise FileNotFoundError(f"{filepath} is not a file.")
            conf = load_single_conf_file(filepath)
            loaded.merge(conf)

    return loaded


def load_conf_directory(filepath: Union[str, Path, os.PathLike],
                        keep_dir_name: bool = True,
                        keep_filenames: bool = True) -> Union[OmegaConf, DictConfig]:
    """

    :param filepath:
    :param keep_dir_name:
    :param keep_filenames:
    :return:
    """
    if not os.path.isdir(filepath):
        raise NotADirectoryError(filepath)

    loaded = OmegaConf.create()

    return loaded


if __name__ == '__main__':
    pass
