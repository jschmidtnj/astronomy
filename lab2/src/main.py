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
    light_curve_data, luminosity_data = get_data()
    logger.info(f'sample of light curve data:\n\n{light_curve_data.head()}')
    logger.info(f'sample of luminosity data:\n\n{luminosity_data.head()}')

    analyze(light_curve_data, luminosity_data)


if __name__ == '__main__':
    main()
