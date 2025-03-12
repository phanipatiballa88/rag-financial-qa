import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from rag_model import load_data, retrieve_documents, extract_answers

def main():
    # Set the title of the Streamlit app
    st.title("RAG Financial QA Chatbot")
    st.write("Ask Questions Related To FY23, FY24 Financial Results Of the Company Medtroinic Inc.")

    # Input field for the user to enter their query
    query = st.text_input("Enter your query:")
    if query:
        # Load the data required for the model
        vectorizer, tfidf_matrix, filenames, documents = load_data()
        
        # Retrieve relevant documents based on the query
        results = retrieve_documents(query, vectorizer, tfidf_matrix, filenames, documents)
        documents = [result[1] for result in results]
        
        # Extract answers from the retrieved documents
        answers = extract_answers(query, documents)
        
        # Display the results
        st.write("### Results")
        for doc, answer, score in answers:
            st.write(f"**Answer:** {answer}")
            st.write(f"**Confidence Score:** {score:.4f}")
            st.write("---")

if __name__ == "__main__":
    main()
