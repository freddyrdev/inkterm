__version__ = "0.1.0"

from .core import write as write, label
from .config import config as config

__all__ = ["write", "config", "label"]