# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import streamlit as st
# from rag_model import load_data, retrieve_documents
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/api/query', methods=['GET'])
# def query_api():
#     query = request.args.get('text')
#     if query:
#         vectorizer, tfidf_matrix, filenames = load_data()
#         results = retrieve_documents(query, vectorizer, tfidf_matrix, filenames)
#         response = [{"filename": filename, "score": score} for filename, score in results]
#         return jsonify({"results": response})
#     return jsonify({"results": []})

# def main():
#     st.title("Financial Document QA")
#     st.write("Enter your query below to get answers from the financial documents.")

#     query = st.text_input("Enter your query:")
#     if query:
#         vectorizer, tfidf_matrix, filenames = load_data()
#         results = retrieve_documents(query, vectorizer, tfidf_matrix, filenames)
        
#         st.write("### Results")
#         for filename, score in results:
#             st.write(f"**Document:** {filename}")
#             st.write(f"**Confidence Score:** {score:.4f}")
#             st.write("---")

# if __name__ == "__main__":
#     main()
#     app.run(port=8501)
########################################################################################
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import streamlit as st
# from rag_model import load_data, retrieve_documents

# def main():
#     st.title("Financial Document QA")
#     st.write("Enter your query below to get answers from the financial documents.")

#     query = st.text_input("Enter your query:")
#     if query:
#         vectorizer, tfidf_matrix, filenames = load_data()
#         results = retrieve_documents(query, vectorizer, tfidf_matrix, filenames)
        
#         st.write("### Results")
#         for filename, score in results:
#             st.write(f"**Document:** {filename}")
#             st.write(f"**Confidence Score:** {score:.4f}")
#             st.write("---")

# if __name__ == "__main__":
#     main()
########################################################################################
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from rag_model import load_data, retrieve_documents, extract_answers

def main():
    st.title("Financial Document QA")
    st.write("Enter your query below to get answers from the financial documents.")

    query = st.text_input("Enter your query:")
    if query:
        vectorizer, tfidf_matrix, filenames, documents = load_data()
        results = retrieve_documents(query, vectorizer, tfidf_matrix, filenames, documents)
        documents = [result[1] for result in results]
        answers = extract_answers(query, documents)
        
        st.write("### Results")
        for doc, answer, score in answers:
            st.write(f"**Answer:** {answer}")
            st.write(f"**Confidence Score:** {score:.4f}")
            st.write("---")

if __name__ == "__main__":
    main()