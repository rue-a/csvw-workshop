# %%
import pandas as pd

df = pd.read_csv("../data/german_cities.csv")
df.head()

# %%
import pandas as pd

df = pd.read_csv(
    "../data/german_cities.csv",
    sep="\t",
    decimal=",",
    dtype={"Postal Code": str},
)
df.head()

# %%

"""Bruttoanlageninvestitionen - kreisfreie Städte und Kreise -Jahr: 
https://www.govdata.de/web/guest/suchen/-/details/bruttoanlageninvestitionen-kreisfreie-stadte-und-kreise-jahr-1
https://www.landesdatenbank.nrw.de/ldbnrwws/downloader/00/tables/44211-11i_00.csv

Amtlicher Gemindeschlüssel:
https://de.wikipedia.org/wiki/Amtlicher_Gemeindeschl%C3%BCssel
"""

import pandas as pd

df = pd.read_csv(
    "../data/44211-11i_00.csv",
    encoding="windows-1252",
    skiprows=6,
    skipfooter=3,
    sep=";",
    header=None,
    decimal=",",
    dtype={1: str},
    names=[
        "Jahr",
        "Amtlicher Gemindeschlüssel",
        "Bundesland",
        "Aktivierte Bruttoanlageinvestitionen [Tsd. EUR]",
        "Aktivierte Bruttoanlageninvestitionen je Beschäftigten [EUR]",
        "Verhältnis zum Umsatz (Akt. Bruttoanlageninvestitionen) [%]",
    ],
)

# Display the imported DataFrame
df.info(verbose=True)
df.head()

# %%
