import unittest
from .utilities import parse_string_with_regex

class TestParseStringWithRegex(unittest.TestCase):
    def test_parse_string_with_regex(self):
        input_string = "SBS-0071898 has been created to fix a bug"
        regex_pattern = r"SBS-\d+"
        expected_output = "SBS-0071898"
        actual_output = parse_string_with_regex(input_string, regex_pattern)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()