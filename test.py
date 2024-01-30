import unittest
from main import process_list

class TestProcessList(unittest.TestCase):
    def test_valid_input(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        result = process_list(input_list)
        self.assertEqual(result, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])

    def test_invalid_length(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]  # Not a multiple of 10
        result = process_list(input_list)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
