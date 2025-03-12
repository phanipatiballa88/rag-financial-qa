import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from guardrails.output_filtering import filter_response

class TestOutputFiltering(unittest.TestCase):
    def test_filter_response(self):
        response = "This is a sample response."
        filtered_response = filter_response(response)
        self.assertEqual(filtered_response, response)

if __name__ == "__main__":
    unittest.main()