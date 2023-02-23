import data_type
import unittest
import pandas as pd
import json
from main import SchemaEnforce

class TestSchemaEnforce(unittest.TestCase):
    
    def setUp(self):
        self.df = pd.DataFrame({'a': [1,2,3], 'b': ['a', 'b', 'c']})
        self.schema_file = 'schema.json'
        self.pattern_file = 'pattern.json'
        self.schema_enforcer = SchemaEnforce(self.df, self.schema_file, self.pattern_file)

    def test_export_schema_to_json(self):
        self.schema_enforcer.export_schema_to_json()
        with open('schema.json', 'r') as f:
            output = json.load(f)
        self.assertEqual(output['a'], 'int64')
        self.assertEqual(output['b'], 'object')
        
    def test_verify_schema(self):
        self.schema_enforcer.verify_schema()
        with open(self.schema_file, 'r') as f:
            schema = json.load(f)
        self.assertEqual(str(self.df.dtypes[0]), schema['a'])
        self.assertEqual(str(self.df.dtypes[1]), schema['b'])
        
    def test_export_pattern_to_json(self):
        self.schema_enforcer.export_pattern_to_json()
        with open('learned_pattern.json', 'r') as f:
            output = json.load(f)
        self.assertEqual(output['a']['mean'], 2)
        self.assertEqual(output['a']['median'], 2)
        self.assertEqual(output['a']['mode'], 0)
        self.assertEqual(output['a']['min'], 1)
        self.assertEqual(output['a']['max'], 3)
        self.assertEqual(output['b'][0], 'a')
        self.assertEqual(output['b'][1], 'b')
        self.assertEqual(output['b'][2], 'c')
        
    def test_verify_pattern(self):
        self.schema_enforcer.verify_pattern()
        with open(self.pattern_file, 'r') as f:
            pattern = json.load(f)
        self.assertEqual(self.df['a'].mean(), pattern['a']['mean'])
        self.assertEqual(self.df['a'].median(), pattern['a']['median'])
        self.assertEqual(self.df['a'].mode(), pattern['a']['mode'])
        self.assertEqual(self.df['a'].min(), pattern['a']['min'])
        self.assertEqual(self.df['a'].max(), pattern['a']['max'])
        self.assertEqual(self.df['b'].str.extract(r'(\w+)'), pattern['b'])

if __name__ == '__main__':
    unittest.main()
