import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from data_collection import pdf_to_text

class TestDataCollection(unittest.TestCase):
    def test_pdf_to_text(self):
        pdf_path = os.path.join(os.path.dirname(), 'data\\raw\\MEDTRONIC PLC_10K_2024 ARS.pdf')
        text = pdf_to_text(pdf_path)
        self.assertTrue(len(text) > 0)

if __name__ == "__main__":
    unittest.main()