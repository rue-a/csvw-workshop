import json

import pandas as pd

ACCESSOR_NAME = "csvw"

@pd.api.extensions.register_dataframe_accessor(ACCESSOR_NAME)
class CSVWDataFrameAccessor:
    """Accessor for pandas data frame with metadata as attrs property."""

    def __init__(self, pandas_obj):
        self._obj = pandas_obj


    def write(self, file_path, **kwargs):
        """Write DataFrame to csv file, and metadata to json."""
        self._obj.to_csv(file_path, **kwargs)
        if len(self._obj.attrs) > 0:
            json_path = file_path.replace(".csv", ".json")
            with open(json_path, 'w') as fobj:
                json.dump(self._obj.attrs, fobj)

