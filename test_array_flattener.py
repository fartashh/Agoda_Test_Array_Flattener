import unittest
import json
from array_flattener import ArrayFlattener


class ArrayFlattenerTestCase(unittest.TestCase):
    def test_2_level_nested_array(self):
        sample = [4, [3, 2], [1, 2, 3]]
        expected_result = [4, 3, 2, 1, 2, 3]
        array_flattner = ArrayFlattener(sample)
        array_flattner.process()
        result = array_flattner.get_result()
        self.assertListEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
