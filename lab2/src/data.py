#!/usr/bin/env python3
"""
data file

get the data and save to disk
"""

from os.path import exists
from typing import Tuple, List
import pandas as pd
import numpy as np
from loguru import logger
from variables import data_folder, light_curve_file, luminosity_file, apparent_magnitude_column, absolute_magnitude_column
from utils import file_path_relative


def get_data(light_curve_basename: str = f'{data_folder}/light_curve.csv',
             luminosity_basename: str = f'{data_folder}/luminosity.csv') -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    get the data from wikipedia
    """
    light_curve_data_path = file_path_relative(light_curve_basename)
    luminosity_data_path = file_path_relative(luminosity_basename)
    if exists(light_curve_data_path) and exists(luminosity_data_path):
        logger.info(
            f'reading data from {light_curve_data_path} and {luminosity_data_path}')
        return pd.read_csv(light_curve_data_path, index_col=0), pd.read_csv(luminosity_data_path, index_col=0)

    dataframes: List[pd.DataFrame] = []

    for i, filename_basename in enumerate([light_curve_file, luminosity_file]):
        index: List[int] = []
        values: List[float] = []
        filepath = file_path_relative(f'{data_folder}/{filename_basename}')
        with open(filepath) as current_file:
            for line in current_file:
                line = line.strip()
                if line.startswith('#'):
                    # a comment
                    continue
                elements: List[str] = line.split()
                if len(elements) != 2:
                    # it's an invalid line
                    continue
                index.append(int(elements[0].strip()))
                values.append(float(elements[1].strip()))

        data = np.array([values]).T
        current_dataframe = pd.DataFrame(data, index=index, columns=[
                                         apparent_magnitude_column if i == 0 else absolute_magnitude_column])
        dataframes.append(current_dataframe)

    for i, filepath in enumerate([light_curve_data_path, luminosity_data_path]):
        dataframes[i].to_csv(filepath)

    return tuple(dataframes)


if __name__ == '__main__':
    light_curve, luminosity = get_data()
    logger.info(light_curve.head())
    logger.info(luminosity.head())
