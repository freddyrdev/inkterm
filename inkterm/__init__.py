__version__ = "0.1.0"

from .core.base import write as write, label as label
from .core.config import config as config

__all__ = ["write", "config", "label"]