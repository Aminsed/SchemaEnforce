import pandas as pd
import json
class SchemaEnforce:
    """Class for enforcing schema and pattern on a given dataframe.
    
    Args:
        df (pandas.DataFrame): Dataframe to be enforced.
        schema_file (str): Path to the schema file.
        pattern_file (str): Path to the pattern file.
    """
    def __init__(self, df: pd.DataFrame, schema_file: str = None, pattern_file: str):
        self.df = df
        self.schema_file = schema_file
        self.pattern_file = pattern_file
    
    def export_schema_to_json(self) -> None:
        """Export the schema of the dataframe to a json file.
        """
        output = {} 
        for col_name, data_type in self.df.dtypes: 
            output[col_name] = str(data_type) 
    
        with open('schema.json', 'w') as f: 
            print(output)
            json.dump(output, f) 
    
    def verify_schema(self) -> None: 
        """Verify the schema of the dataframe against the schema file.
        """
        with open(self.schema_file) as f: 
            schema = json.load(f) 

        for col_name, data_type in self.df.dtypes: 
            if col_name in schema.keys(): 
                if str(data_type) != schema[col_name]: 
                    print('Warning: schema mismatch for column {}'.format(col_name))
                else:
                    print('Schema matches column {}'.format(col_name))
                    
    def export_pattern_to_json(self) -> None:
        """Export the pattern of the dataframe to a json file.
        """
        if self.pattern_file:
            output = {}
            for col_name, data_type in self.df.dtypes:
                if data_type == 'int' or data_type == 'float':
                    output[col_name] = {
                        'mean': self.df[col_name].mean(),
                        'median': self.df[col_name].median(),
                        'mode': self.df[col_name].mode(),
                        'min': self.df[col_name].min(),
                        'max': self.df[col_name].max()
                    }
                elif data_type == 'string':
                    output[col_name] = self.df[col_name].str.extract(r'(\w+)')
                elif data_type == 'date':
                    output[col_name] = {
                        'min': self.df[col_name].min(),
                        'max': self.df[col_name].max()
                    }
            with open('learned_pattern.json', 'w') as f:
                json.dump(output, f)
    
    def verify_pattern(self) -> None:
        """Verify the pattern of the dataframe against the pattern file.
        """
        with open(self.pattern_file) as f:
            pattern = json.load(f)

        for col_name, data_type in self.df.dtypes:
            if col_name in pattern.keys():
                if data_type == 'int' or data_type == 'float':
                    if self.df[col_name].mean() != pattern[col_name]['mean'] or self.df[col_name].median() != pattern[col_name]['median'] or self.df[col_name].mode() != pattern[col_name]['mode'] or self.df[col_name].min() != pattern[col_name]['min'] or self.df[col_name].max() != pattern[col_name]['max']:
                        print('Warning: pattern mismatch for column {}'.format(col_name))
                    else:
                        print('Pattern matches column {}'.format(col_name))
                elif data_type == 'string':
                    if self.df[col_name].str.extract(r'(\w+)') != pattern[col_name]:
                        print('Warning: pattern mismatch for column {}'.format(col_name))
                    else:
                        print('Pattern matches column {}'.format(col_name))
                elif data_type == 'date':
                    if self.df[col_name].min() != pattern[col_name]['min'] or self.df[col_name].max() != pattern[col_name]['max']:
                        print('Warning: pattern mismatch for column {}'.format(col_name))
                    else:
                        print('Pattern matches column {}'.format(col_name))

