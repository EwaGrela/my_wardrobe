import unittest

from wardrobe.model import DataFrameHandler

class TestDataFrameHandler(unittest.TestCase):
    def setUp(self):
        self.data = {"name": "Ewa", "surname": "Trojanowska"}
        self.handler = DataFrameHandler(self.data)

    
    def test_read_data(self):
        result = self.handler.read_data()
        self.assertTrue(result is not None)
        self.assertEqual(result, self.handler.data)
    
    def test_write_to_df(self):
        result = self.handler.write_to_df()
        print(result)
        self.assertTrue(result is not None)