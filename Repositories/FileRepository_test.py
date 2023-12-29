import unittest
from unittest.mock import mock_open, patch

from Repositories.FileRepository import * 

class TestFileRepository(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='line1\nline2\nline3\n')
    def test_read_lines(self, mock_file):
        file_repository = FileRepository('testfile')
        expected_output = ['line1', 'line2', 'line3']
        actual_output = file_repository.read_lines()
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()