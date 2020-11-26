#!/usr/bin/env python3
"""
data file

get the data and save to disk
"""

import re
from os.path import exists
import requests
import pandas as pd
from loguru import logger
from bs4 import BeautifulSoup
from variables import data_url, data_folder, orbital_period_column, semimajor_axis_column
from utils import file_path_relative

# remove brackets regex
brackets_remove_regex = r'[\(\[].*?[\)\]]'


def _sanitize_column_name(name: str) -> str:
    """
    sanitize column names
    """
    removed_brackets: str = re.sub(brackets_remove_regex, '', name.strip())
    return removed_brackets.strip().lower().replace(' ', '_')


def get_data(data_basename: str = f'{data_folder}/data.csv') -> pd.DataFrame:
    """
    get the data from wikipedia
    """
    data_path = file_path_relative(data_basename)
    if exists(data_path):
        logger.info(f'reading data from {data_path}')
        moon_data = pd.read_csv(data_path)
        return moon_data

    res = requests.get(data_url)
    soup = BeautifulSoup(res.content, features='html.parser')

    # get second table from wikipedia
    moon_table = soup.findAll('table', {'class': 'wikitable'})[1]
    # convert to dataframe
    moon_df = pd.read_html(str(moon_table))
    moon_df = pd.DataFrame(moon_df[0])

    # sanitize column names
    moon_df.columns = [_sanitize_column_name(
        col) for col in moon_df.columns.values.tolist()]

    # sanitize orbital period
    moon_df[orbital_period_column] = moon_df[orbital_period_column].str.replace(
        brackets_remove_regex, '').str.replace('−', '-').str.strip()
    moon_df[orbital_period_column] = pd.to_numeric(
        moon_df[orbital_period_column])
    # days to seconds
    moon_df[orbital_period_column] *= (24 * 60 * 60)

    # sanitize semi-major axis
    moon_df[semimajor_axis_column] = moon_df[semimajor_axis_column].str.replace(
        brackets_remove_regex, '').str.strip()
    moon_df[semimajor_axis_column] = pd.to_numeric(
        moon_df[semimajor_axis_column])
    # km to m
    moon_df[semimajor_axis_column] *= 1000

    # sanitize mass and sort by it
    mass_column_key: str = 'mass'
    moon_df[mass_column_key] = moon_df[mass_column_key].str.replace(
        '≈', '').str.strip()
    moon_df[mass_column_key] = pd.to_numeric(moon_df[mass_column_key])
    # to kg
    moon_df[mass_column_key] *= 1e16
    moon_df = moon_df.sort_values(by=[mass_column_key], ascending=False)

    moon_df.to_csv(data_path, index=False)
    return moon_df


if __name__ == '__main__':
    data = get_data()
    logger.info(data.head())
