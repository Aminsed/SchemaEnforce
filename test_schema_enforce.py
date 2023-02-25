import unittest
import pandas as pd
import json
import os
from schema_enforce import SchemaEnforce
class TestSchemaEnforce(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 35, 45],
            'Gender': ['Female', 'Male', 'Male'],
            'Salary': [50000, 60000, 70000],
            'Start Date': ['2022-01-01', '2021-01-01', '2020-01-01']
        })
        self.schema_file = 'schema_test.json'
        self.log_file = 'schema_enforce_test.log'
        self.schema_enforcer = SchemaEnforce(self.df, self.schema_file, self.log_file)

    def tearDown(self):
        os.remove(self.schema_file)
        os.remove(self.log_file)

    def test_export_schema_to_json(self):
        self.schema_enforcer.export_schema_to_json(self.schema_file)
        with open(self.schema_file, 'r') as f:
            schema = json.load(f)
        self.assertDictEqual(schema, {'Name': 'object', 'Age': 'int64', 'Gender': 'object', 'Salary': 'int64', 'Start Date': 'object'})

    def test_verify_schema_success(self):
        self.schema_enforcer.export_schema_to_json(self.schema_file)
        self.schema_enforcer.verify_schema(self.schema_file)
        with open(self.log_file, 'r') as f:
            logs = f.read()
        self.assertIn('Schema matches column Name.', logs)
        self.assertIn('Schema matches column Age.', logs)
        self.assertIn('Schema matches column Gender.', logs)
        self.assertIn('Schema matches column Salary.', logs)
        self.assertIn('Schema matches column Start Date.', logs)


if __name__ == '__main__':
    unittest.main()
