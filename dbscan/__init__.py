# -*- coding: utf-8 -*-
import pkg_resources

try:
    __version__ = pkg_resources.get_distribution(__name__).version
except Exception:
    __version__ = '0.0.1'

from .algorithm import *
from .metrics import *

try:
    from .visualization import *
except ImportError:
    print("Please install matplotlib for visualization data")
