This repository contains code for the SchemaEnforce class, which is used for enforcing schema and pattern on a given dataframe.

## Requirements

- Python 3.x
- Pandas
- JSON

## Usage

First, create an instance of the SchemaEnforce class, passing in the dataframe to be enforced and the paths to the schema file and pattern file:

```
schema_enforcer = SchemaEnforce(df, schema_file, pattern_file)
```

To export the schema of the dataframe to a JSON file, use the `export_schema_to_json` method:

```
schema_enforcer.export_schema_to_json()
```

To verify the schema of the dataframe against the schema file, use the `verify_schema` method:

```
schema_enforcer.verify_schema()
```

To export the pattern of the dataframe to a JSON file, use the `export_pattern_to_json` method:

```
schema_enforcer.export_pattern_to_json()
```

To verify the pattern of the dataframe against the pattern file, use the `verify_pattern` method:

```
schema_enforcer.verify_pattern()
```

## Tests

Tests for the SchemaEnforce class are included in the `test_schema_enforce.py` file. To run the tests, use the following command:

```
python test_schema_enforce.py
```
