import pandas as pd


def read_csv_metadata(path: str): pd.DataFrame
    """
    Search for <filename>.csv and <filename>.csv-metadata.json.
    Read metadata from metadata file and parse read csv into
    pandas.DataFrame() accordingly.

    """

    df = pd.read_csv(path, ...)
    return df
