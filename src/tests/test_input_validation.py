import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from guardrails.input_validation import validate_query

class TestInputValidation(unittest.TestCase):
    def test_validate_query(self):
        self.assertTrue(validate_query("What is the revenue?"))
        self.assertFalse(validate_query("What is the revenue?!"))

if __name__ == "__main__":
    unittest.main()