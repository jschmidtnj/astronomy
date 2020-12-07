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
from scipy.signal import find_peaks
from scipy.interpolate import interp1d
from variables import output_folder, apparent_magnitude_column, absolute_magnitude_column, star_name, actual_distance
from utils import file_path_relative


def analyze(light_curve_data: pd.DataFrame, luminosity_data: pd.DataFrame) -> None:
    """
    analyze the data
    """
    plt.plot(light_curve_data.index,
             light_curve_data[apparent_magnitude_column])
    plt.title('Light Curve - Apparent Magnitude vs Time')
    plt.xlabel('Time (hours)')
    plt.ylabel('Apparent Magnitude m')
    plt.gca().invert_yaxis()
    plt.savefig(file_path_relative(
        f'{output_folder}/plot_light_curve.png'))
    plt.close()

    peak_indexes, _ = find_peaks(
        light_curve_data[apparent_magnitude_column], width=5, prominence=1e-1)
    peaks = light_curve_data.index[peak_indexes]
    if len(peaks) < 2:
        raise RuntimeError('found less than 2 peaks in light curve data')
    pulsation_period = peaks[1] - peaks[0]
    pulsation_period_days = pulsation_period / 24.0
    logger.info(
        f'pulsation period of {star_name}: {pulsation_period:.1f} or {pulsation_period_days:.3f} days')

    average_apparent_magnitude = (max(light_curve_data[apparent_magnitude_column]) - min(
        light_curve_data[apparent_magnitude_column])) / 2.0
    logger.info(
        f'average apparent magnitude of {star_name}: {average_apparent_magnitude:.3f}')

    plt.plot(luminosity_data.index,
             luminosity_data[absolute_magnitude_column])
    plt.title('Luminosity Period Type I Curve - Absolute Magnitude vs Period')
    plt.xlabel('Period (days)')
    plt.ylabel('Absolute Magnitude M')
    plt.gca().invert_yaxis()
    plt.savefig(file_path_relative(
        f'{output_folder}/plot_luminosity.png'))
    plt.close()

    interpolate_func = interp1d(
        luminosity_data.index, luminosity_data[absolute_magnitude_column])
    absolute_magnitude = interpolate_func(pulsation_period_days)
    logger.info(f'absolute magnitude of {star_name}: {absolute_magnitude:.3f}')

    distance: float = (
        10 ** (((average_apparent_magnitude - absolute_magnitude) / 2.5) ** 0.5)) * 10
    logger.info(f'calculated distance: {distance:.3f} parsec')
    logger.info(f'accepted distance: {actual_distance:.3f} parsec')


if __name__ == '__main__':
    raise ValueError('cannot run analyze standalone')
