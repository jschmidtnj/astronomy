#!/usr/bin/env python3
"""
utils functions (utils.py)
"""

from os.path import abspath, join
from pathlib import Path


def file_path_relative(rel_path: str) -> str:
    """
    get file path relative to base folder
    """
    return join(
        abspath(join(Path(__file__).absolute(), '../..')), rel_path)
