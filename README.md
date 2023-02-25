# SchemaEnforce

This class is used for enforcing schema and pattern on a given dataframe. It can be used to verify the schema of the dataframe against a schema file, as well as export the schema of the dataframe to a JSON file.

## Usage

```python
import pandas as pd
import json
import logging

from schema_enforce import SchemaEnforce

# Initialize the class
df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
schema_enforce = SchemaEnforce(df)

# Verify the schema
schema_enforce.verify_schema('schema.json')

# Export the schema to JSON
schema_enforce.export_schema_to_json('schema.json')
```

## Arguments

The SchemaEnforce class takes the following arguments:

- `df` (pandas.DataFrame): Dataframe to be enforced
- `schema_file` (str): Path to the schema file (default: None)
- `log_file` (str): Path to the log file (default: 'schema_enforce.log')
- `log_level` (str): Log level (default: 'INFO')

## Logging

The SchemaEnforce class has a logger that can be used to log any errors or warnings encountered while verifying the schema or exporting the schema to JSON. The log file can be specified using the `log_file` argument, and the log level can be specified using the `log_level` argument. The default log level is 'INFO'.

## Tests

Tests for the SchemaEnforce class are included in the `test_schema_enforce.py` file. To run the tests, use the following command:

```
python test_schema_enforce.py
```
