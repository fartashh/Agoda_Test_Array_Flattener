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

    def test_3_level_nested_array(self):
        sample = [4,[3,2,[9,0]],[1,2,3,[8,7]]]
        expected_result =[4,3,2,9,0,1,2,3,8,7]
        array_flattner = ArrayFlattener(sample)
        array_flattner.process()
        result = array_flattner.get_result()
        self.assertListEqual(result, expected_result)

    def test_n_level_nested_array(self):
        sample = [4,[3,2,[9,0,[1,2]]],[1,[5,6,7],2,3,[8,7]],[9,8,[1,[4,5,[7]]]]]
        expected_result =[4,3,2,9,0,1,2,1,5,6,7,2,3,8,7,9,8,1,4,5,7]
        array_flattner = ArrayFlattener(sample)
        array_flattner.process()
        result = array_flattner.get_result()
        self.assertListEqual(result, expected_result)

    def test_get_result_invalid_key(self):
        sample = [[1,2,[3]],4]
        result_type = 'invalid_key'
        array_flattner = ArrayFlattener(sample)
        array_flattner.process()
        with self.assertRaises(KeyError):
            array_flattner.get_result(result_type)

    def test_get_result_obj_json(self):
        sample = [[1,2,[3]],4]
        result_type = 'json'
        array_flattner = ArrayFlattener(sample)
        array_flattner.process()
        json.loads(array_flattner.get_result(result_type))
        self.assert_(True)

if __name__ == "__main__":
    unittest.main()
