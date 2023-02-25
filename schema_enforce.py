import pandas as pd
import json
import logging

class SchemaEnforce:
    """Class for enforcing schema and pattern on a given dataframe.

    Args:
        df (pandas.DataFrame): Dataframe to be enforced.
        schema_file (str): Path to the schema file.
        log_file (str): Path to the log file.
        log_level (str): Log level (default: 'INFO')
    """
    def __init__(self, df: pd.DataFrame, schema_file: str = None, log_file: str = 'schema_enforce.log', log_level: str = 'INFO'):
        self.df = df
        self.schema_file = schema_file

        # Create a logger instance for the class
        self.logger = logging.getLogger('schema_enforce')
        self.logger.setLevel(log_level)

        # Create a file handler if a log file is specified, and add it to the logger
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
            self.logger.addHandler(file_handler)

        # Export the schema to JSON if no schema file is specified
        if schema_file is None:
            schema_file = self.schema_file
            self.export_schema_to_json(schema_file)

    def export_schema_to_json(self, file_path: str) -> None:
        """Export the schema of the dataframe to a JSON file.

        Args:
            file_path (str): Path to the output JSON file.
        """
        try:
            output = {}
            for col_name in self.df.columns:
                data_type = str(self.df[col_name].dtype)
                output[col_name] = data_type

            with open(file_path, 'w') as f:
                json.dump(output, f)
        except Exception as e:
            self.logger.exception(f'Error while exporting schema to JSON: {e}')
            raise

    def verify_schema(self, schema_file: str) -> None: 
        """Verify the schema of the dataframe against the schema file.

        Args:
            schema_file (str): Path to the schema file.
        """
        try:
            with open(schema_file) as f: 
                schema = json.load(f)

            for col_name, data_type in self.df.dtypes.items(): 
                if col_name in schema.keys(): 
                    if str(data_type) != schema[col_name]: 
                        self.logger.warning(f'Schema mismatch for column {col_name}. Expected {schema[col_name]}, but found {data_type}.')
                    else:
                        self.logger.info(f'Schema matches column {col_name}.')
                else:
                    self.logger.warning(f'Column {col_name} is not found in the schema.')
        except Exception as e:
            self.logger.exception(f'Error while verifying schema: {e}')
            raise e

