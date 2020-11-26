#!/usr/bin/env python3
"""
main file

entry point for running assignment 1
"""

import pandas as pd
from loguru import logger
from data import get_data
from analyze import analyze


def initialize() -> None:
    """
    initialize config
    """
    pd.set_option('mode.chained_assignment', None)


def main() -> None:
    """
    main entry point for program
    """
    initialize()
    moon_data = get_data()
    logger.info(f'sample of data:\n\n{moon_data.head()}')
    logger.info(f'data columns: {moon_data.columns}')

    analyze(moon_data, 20)
    analyze(moon_data, 4)


if __name__ == '__main__':
    main()
