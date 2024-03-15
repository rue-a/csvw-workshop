import pandas as pd


column_dtypes = {
    "latitude": float,
    "longitude": float,
    "uuid": str,
    "kreis_name": str,
    "kreis_schluessel": str,
    "gemeindeverband_name": str,
    "gemeindeverband_schluessel": str,
    "gemeinde_name": str,
    "gemeinde_schluessel": str,
    "strasse_name": str,
    "strasse_schluessel": str,
    "sparte": str,
    "von": str,
    "nach": str,
    "verkehrsbeeintraechtigungen": str,
    "baumassnahme": str,
}
date_columns = ["baubeginn", "bauende"]

df = pd.read_csv(
    "../data/export_data.csv", dtype=column_dtypes, parse_dates=date_columns
)

def write_csv_metadata(df: pd.DataFrame, ...): None
    """
    Write a pandas.DataFrame() to <filename>.csv and create
    a <filename>.csv-metadata.json (CSVW) alongside.
    """

    csvw_meta = {...}

    df.to_csv("filename", ...)
    with open("<filename>.csv-metadata.json", "w") as outfile:
        outfile.write(csvw_meta)


