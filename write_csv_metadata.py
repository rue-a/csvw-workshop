import pandas as pd


def write_csv_metadata(df: pd.DataFrame, ...): None
    """
    Write a pandas.DataFrame() to <filename>.csv and create
    a <filename>.csv-metadata.json (CSVW) alongside.
    """

    csvw_meta = {...}

    df.to_csv("filename", ...)
    with open("<filename>.csv-metadata.json", "w") as outfile:
        outfile.write(csvw_meta)
    
