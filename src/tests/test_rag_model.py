import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from rag_model import retrieve_documents, load_data

class TestRAGModel(unittest.TestCase):
    def test_retrieve_documents(self):
        vectorizer, tfidf_matrix, filenames = load_data()
        results = retrieve_documents("sample query", vectorizer, tfidf_matrix, filenames)
        self.assertTrue(len(results) > 0)

if __name__ == "__main__":
    unittest.main()