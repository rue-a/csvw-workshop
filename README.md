# Workshop – (F.A.)I.R. tabular data for Pythons pandas library

Among researchers, the CSV format is commonly chosen to publish or archive tabular research data. Although widely known, open, and readable without specific software, parsing CSV-formatted data is error-prone. This is due to a severely lacking formalization of the format, resulting in a proliferation of formatting practices, where the choice of the separating character (,``, ;, \t`, etc.) is just the tip of the iceberg. Additionally, the format does not offer standardized methods to incorporate metadata – including the vital information about the table’s columns, such as descriptions, units, data formats, etc. The W3C recommendation [CSV on the Web (CSVW)](https://www.w3.org/TR/2015/REC-tabular-data-model-20151217/) overcomes these limitations by introducing a method to produce CSV-accompanying JSON documents that contain this missing information, thus rendering CSV files interoperable and reusable (according to the [FAIR principles](https://www.go-fair.org/fair-principles/)).

The workshop participants will implement functions that allow the import and export of CSV/CSVW data pairs for DataFrame objects of Python's pandas library. To solve this task, they will be made aware of the shortcomings of the CSV format and become acquainted with (a subset) of the CSVW standard.

## Task

Implement two python methods to import and export CSV/CSVW pairs into and from `pandas.DataFrame` objects. Suggestions of function bodies are defined in `python/read_csv_metadata.py` and `python/write_csv_metadata.py`. Find test data in the `data` folder.


## Materials

### CSV

#### Problems of the CSV format

- https://peps.python.org/pep-0305/#rationale
- https://csvw.org/guides/why-use-csvw.html
- https://news.ycombinator.com/item?id=28221654

> The format properties of a CSV file are referred to as its [dialect](https://www.w3.org/TR/tabular-metadata/#dfn-dialect-description).

#### General Recommendations

- the [RFC 4180](https://www.ietf.org/rfc/rfc4180.txt) comes closest to a format standard, use it
  - there are 0 or 1 header rows (not multiple header rows, nor other metadata)
  - after the header rows, each row is a record (not, for example, a “totals” of preceding rows; no blank rows)
  - fields are separated by commas (not tabs or pipes)
  - quotation with double quotes, always when needed (such as when a field contains a comma) and optionally when not
  - all rows have the same number of fields (do not miss off trailing commas)
  - line breaks are: `\r\n` (CRLF - Windows-style)
  - *source: https://www.gov.uk/government/publications/recommended-open-standards-for-government/tabular-data-standard#how-to-use-this-standard*

- making use of the header row is strongly recommended, since it's the only way to incorporate meaning into the file.
- use [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) for dates and times
- delimit decimals with a dot (`.`)

### CSVW

CSVW defines a schema to describe CSV files with an accompanying JSON-LD file.

CSVW is designed to not only describe CSV data file, but to also validate its contents and allow the transformation of the data into linked data formats. Additionally, CSVW allows describing multiple CSVs with one CSVW file; including the relations between the described files, by the means of primary and foreign keys.

- Overview of the documents produced by the CSVW Working Group: https://www.w3.org/2013/csvw/wiki/Main_Page.html
- Short introduction to the why and how: https://www.stevenfirth.com/csv-on-the-web-an-introduction/
- JSON-LD: https://json-ld.org/


__This workshop focuses on the subset of CSVW that allows to describe the dialect, general metadata and the tables columns in detail. We also disregard the option to describe multiple CSVs in one CSVW file.__

CSVW-Subset:
![](assets/subset.svg)
CSVW-Full: https://www.w3.org/TR/tabular-metadata/#metadata-format

#### Problems with CSVW

The dialect object cannot handle footer rows.

### Related Projects/Tools (non-exhaustive)

- Python CSVW package (read/write/validate csv(w) and convert to frictionless data package): https://github.com/cldf/csvw 
- R-language data.frame metadata: https://dataset.dataobservatory.eu/ 
- CSV-X (describe any csv, regardless of its weirdness): https://ieeexplore.ieee.org/document/7917195 
- Frictionlessdata.io supports CSV-Dialect: https://specs.frictionlessdata.io/csv-dialect/#language 


