import os
from typing import Union

from engine.cacher import cached, conf_cache


def detect_project_path(override_flag_file: Union[str, None] = None) -> str:
    """
    Get project path from by detecting a flag file. 'main.py' by default
    :param override_flag_file: specificy an alternative file to be used as the flag of the root directory
    :return: string of the path or raises *FileNotFoundError*
    """
    current_dir = os.path.abspath(os.curdir)
    while True:
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        # print([parent_dir])
        if os.path.isfile(os.path.join(current_dir, 'main.py' if override_flag_file is None else override_flag_file)):
            return current_dir
        elif current_dir == parent_dir:
            raise FileNotFoundError(f'Could not find this file '
                                    f'({"main.py" if override_flag_file is None else override_flag_file}).')
        else:
            current_dir = parent_dir


@cached(conf_cache)
def get_project_path(detect_file: Union[str, None] = None) -> str:
    """
    Checks INVESTIFY_PATH environment variable to see if it exists, otherwise performs detection method.
    :return:
    """
    if os.environ.get('INVESTIFY_PATH', None) is None:
        os.environ['INVESTIFY_PATH'] = detect_project_path(detect_file if detect_file is not None else None)
    #
    return os.environ['INVESTIFY_PATH']


print(get_project_path())
