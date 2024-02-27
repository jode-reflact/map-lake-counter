import unittest

from lake_counter import LakeCounter


class TestEcho(unittest.TestCase):
    def setUp(self):
        self.lake_counter = LakeCounter()

    def test_example_map(self):
        test_map = [
            [0,1,1,0,0,1,1,0],
            [0,0,0,0,1,1,0,0],
            [0,1,1,1,1,1,1,1]
        ]
        correct_lake_count = 2
        count = self.lake_counter.count_lakes(test_map)
        self.assertEqual(count, correct_lake_count)
    
    def test_map_without_lakes(self):
        test_map = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
        ]
        correct_lake_count = 0
        count = self.lake_counter.count_lakes(test_map)
        self.assertEqual(count, correct_lake_count)
    
    def test_map_with_single_lake(self):
        test_map = [
            [1]
        ]
        correct_lake_count = 1
        count = self.lake_counter.count_lakes(test_map)
        self.assertEqual(count, correct_lake_count)

    def test_big_map(self):
        test_map = [
            [0,1,1,0,0,1,1,0,1,1,0,0,1,1,1,0],
            [0,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0],
            [0,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0],
            [0,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0],
            [0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,0],
        ]
        correct_lake_count = 7
        count = self.lake_counter.count_lakes(test_map)
        self.assertEqual(count, correct_lake_count)

if __name__ == '__main__':
    unittest.main()