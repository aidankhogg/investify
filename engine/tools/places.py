from abc import ABC, abstractmethod
from glob import glob
import os.path
from pathlib import Path
from typing import Union

from omegaconf import OmegaConf

from engine.ignition import get_project_path

local_paths = {
    "root": get_project_path(),
    "logs": os.path.join(get_project_path(), ".logs"),
    "conf": os.path.join(get_project_path(), ".conf"),
}

