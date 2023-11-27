import unittest
import pandas as pd
import os
from bcc import prepare_json_file, load_json_file_to_pandas_df, load_csv_file_to_pandas_df, process_data, prepare_output

class TestBccFunctions(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = 'test_output'
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        # Remove the temporary directory after testing
        os.rmdir(self.test_dir)

    def test_prepare_json_file(self):
        source_file = 'test_data/decodes_test.json'
        destination_file = os.path.join(self.test_dir, 'decodes_preprocessed_test.json')
        prepare_json_file(source_file, destination_file)
        self.assertTrue(os.path.isfile(destination_file))

    def test_load_json_file_to_pandas_df(self):
        json_file_path = 'test_data/decodes_preprocessed_test.json'
        json_df = load_json_file_to_pandas_df(json_file_path)
        self.assertIsInstance(json_df, pd.DataFrame)

    def test_load_csv_file_to_pandas_df(self):
        csv_file_path = 'test_data/encodes_test.csv'
        encode_df = load_csv_file_to_pandas_df(csv_file_path)
        self.assertIsInstance(encode_df, pd.DataFrame)

    def test_process_data(self):
        decode_df = pd.DataFrame({
            'bitlink': ['https://bit.ly/31Tt55y'],
            'timestamp': ['22021-05-22T00:00:00Z']
        })
        encode_df = pd.DataFrame({
            'bitlink': ['https://bit.ly/31Tt55y'],
            'long_url': ['https://google.com/']
        })
        result_df = process_data(decode_df, encode_df)
        self.assertIsInstance(result_df, pd.DataFrame)

    def test_prepare_output(self):
        process_df = pd.DataFrame({
            'long_url': ['https://google.com/'],
            'count': [502]
        })
        result_file_path = os.path.join(self.test_dir, 'result_test.json')
        prepare_output(process_df, result_file_path)
        self.assertTrue(os.path.isfile(result_file_path))


if __name__ == '__main__':
    unittest.main()
