#!/usr/bin/env python3
"""
analyze file

analyze the moon data
"""

from typing import List, Any
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from loguru import logger
from scipy.constants import G
from variables import output_folder, orbital_period_column, semimajor_axis_column
from utils import file_path_relative


def to_power(arr: np.array, power: int) -> List[Any]:
    """
    raise list to power
    avoids integer overflow errors
    """
    return [pow(elem, power) for elem in arr.tolist()]


def analyze(data: pd.DataFrame, num_moons_analyze: int) -> None:
    """
    analyze the dataframe
    """
    if num_moons_analyze > len(data):
        raise ValueError(f'jupiter has less than {num_moons_analyze} moons')
    moons = data[0:num_moons_analyze]
    logger.info(f"analyzing {num_moons_analyze} moon(s):\n\n{moons['name']}")

    # x
    semimajor_axis_cubed = to_power(moons[semimajor_axis_column].to_numpy(), 3)
    # y
    orbital_periods_squared = to_power(
        moons[orbital_period_column].to_numpy(), 2)

    arr_float = np.vstack([semimajor_axis_cubed, np.ones(
        len(semimajor_axis_cubed))]).T.astype('float')
    slope, y_intercept = np.linalg.lstsq(
        arr_float, orbital_periods_squared, rcond=None)[0]
    logger.info(f'least square fit slope: {slope}')

    plt.plot(semimajor_axis_cubed, orbital_periods_squared, 'o', label='Data')
    x_float = np.array(semimajor_axis_cubed).astype('float')
    plt.plot(x_float, slope * x_float + y_intercept,
             'r', label=f'Least Square Fit,\ny = {slope} * x\n+ {y_intercept}')
    plt.title(
        f'Orbital Period vs Semi-Major Axis for {num_moons_analyze} moon(s)')
    plt.xlabel('R^3 (m^3)')
    plt.ylabel('T^2 (s^2)')
    plt.legend()
    plt.savefig(file_path_relative(
        f'{output_folder}/plot_{num_moons_analyze}.png'))
    plt.close()

    estimated_mass = 4 * np.power(np.pi, 2) / (G * slope)
    logger.info(f'estimated mass: {estimated_mass} kg')


if __name__ == '__main__':
    raise ValueError('cannot run analyze standalone')
