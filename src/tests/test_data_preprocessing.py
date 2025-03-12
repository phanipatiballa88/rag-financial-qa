import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from data_preprocessing import preprocess_text

class TestDataPreprocessing(unittest.TestCase):
    def test_preprocess_text(self):
        text = "This is a sample text."
        processed_text = preprocess_text(text)
        self.assertEqual(processed_text, text)

if __name__ == "__main__":
    unittest.main()