import pandas as pd
import numpy as np

from pathlib import Path


class PreProcess:

    def clean_crypto_price(price_string):
        price = price_string
        if type(price_string) == str:
            price_string = price_string.replace('$', '')
            price_string = price_string.replace(',', '')
            price = float(price_string)
        else:
            price = float(price_string)
        return price

    def clean_crypto_cap(market_cap_string):
        cap = market_cap_string
        if type(market_cap_string) == str:
            if market_cap_string[-1] == 'M':
                million = 1000000
                market_cap_string = market_cap_string.replace(' ', '')
                market_cap_string = market_cap_string.replace('$', '')
                market_cap_string = market_cap_string.replace('M', '')
                cap = float(market_cap_string)
                cap *= million
            else:
                billion = 1000000000
                market_cap_string = market_cap_string.replace(' ', '')
                market_cap_string = market_cap_string.replace('$', '')
                market_cap_string = market_cap_string.replace('B', '')
                cap = float(market_cap_string)
                cap *= billion
            return cap

    def clean_crypto_volume(volume_string):
        volume = volume_string
        if type(volume_string) == str:
            if volume_string[-1] == 'K':
                thousand = 1000
                volume_string = volume_string.replace('$', '')
                volume_string = volume_string.replace('K', '')
                volume = float(volume_string)
                volume *= thousand
            elif volume_string[-1] == 'M':
                million = 1000000
                volume_string = volume_string.replace('$', '')
                volume_string = volume_string.replace('M', '')
                volume = float(volume_string)
                volume *= million
            else:
                billion = 1000000000
                volume_string = volume_string.replace('$', '')
                volume_string = volume_string.replace('B', '')
                volume = float(volume_string)
                volume *= billion
            return volume

    def new_supply(dirty_dataframe):
        dataframe = dirty_dataframe
        # new data frame with split 'Available Supply' into columns
        new = dataframe['Available Supply'].str.split(' ', n=2, expand=True)
        # making separate numeric column from new data frame
        dataframe['number'] = new[0]
        # making separate Unit value column from new data frame
        dataframe['unit'] = new[1]
        # transform contents of 'Available Supply' column from new data frame
        dataframe['Available Supply'] = dataframe['number'] + dataframe['unit']
        # Dropping old Name columns
        dataframe.drop(columns=['number', 'unit'], inplace=True)
        clean_dataframe = dataframe
        return clean_dataframe

    def clean_crypto_supply(supply_string):
        supply = supply_string
        if type(supply_string) == str:
            if supply_string[-1] == 'K':
                thousand = 1000
                supply_string = supply_string.replace('K', '')
                supply = float(supply_string)
                supply *= thousand
            elif supply_string[-1] == 'M':
                million = 1000000
                supply_string = supply_string.replace('M', '')
                supply = float(supply_string)
                supply *= million
            elif supply_string[-1] == 'B':
                billion = 1000000000
                supply_string = supply_string.replace('B', '')
                supply = float(supply_string)
                supply *= billion
            else:
                trillion = 1000000000000
                supply_string = supply_string.replace('T', '')
                supply = float(supply_string)
                supply *= trillion
            return supply
