from io import StringIO
import json
from pathlib import Path

import pandas as pd

ACCESSOR_NAME = "csvw"


@pd.api.extensions.register_dataframe_accessor(ACCESSOR_NAME)
class CSVWDataFrameAccessor:
    """Accessor for pandas data frame with metadata as attrs property."""

    METADATA_FILE_SUFFIX = "-metadata.json"

    def __init__(self, pandas_obj):
        self._obj = pandas_obj

    def write(self, file_path, **kwargs):
        """Write DataFrame to csv file, and metadata to json."""
        self._obj.to_csv(file_path, **kwargs)
        if len(self._obj.attrs) > 0:
            json_path = file_path + self.METADATA_FILE_SUFFIX
            with open(json_path, "w", encoding="utf-8") as fobj:
                json.dump(self._obj.attrs, fobj)

    def read(self, file_path, **kwargs):
        metadata_file = file_path + self.METADATA_FILE_SUFFIX
        if not Path(metadata_file).exists():
            return self._obj

        with open(metadata_file, "r") as file_obj:
            self._obj.attrs = json.load(file_obj)

        buffer = StringIO()
        self._obj.to_csv(buffer)
        buffer.seek(0)

        return pd.read_csv(
            buffer,
            sep=self._obj.attrs["dialect"]["delimiter"],
            decimal=",",
            names=[
                column["titles"] if "titles" in column else ""
                for column in self.meta.data["tableSchema"]["columns"]
            ],
            **kwargs
        )
