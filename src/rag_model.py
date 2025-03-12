import pickle
from sklearn.metrics.pairwise import cosine_similarity
from rank_bm25 import BM25Okapi
from transformers import pipeline

def load_data():
    # Load precomputed data from pickle files
    with open("vectorizer.pkl", "rb") as file:
        vectorizer = pickle.load(file)
    with open("tfidf_matrix.pkl", "rb") as file:
        tfidf_matrix = pickle.load(file)
    with open("filenames.pkl", "rb") as file:
        filenames = pickle.load(file)
    with open("documents.pkl", "rb") as file:
        documents = pickle.load(file)
    return vectorizer, tfidf_matrix, filenames, documents

def retrieve_documents(query, vectorizer, tfidf_matrix, filenames, documents):
    # Transform the query using the vectorizer
    query_vec = vectorizer.transform([query])
    # Compute cosine similarities between the query and the TF-IDF matrix
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    # Get the top 5 most similar documents based on cosine similarity
    top_indices = similarities.argsort()[-5:][::-1]
    
    # Initialize BM25 with tokenized documents
    bm25 = BM25Okapi([doc.split() for doc in documents])
    # Compute BM25 scores for the query
    bm25_scores = bm25.get_scores(query.split())
    # Get the top 5 documents based on BM25 scores
    bm25_top_indices = bm25_scores.argsort()[-5:][::-1]
    
    # Combine indices from both cosine similarity and BM25
    combined_indices = list(set(top_indices).union(set(bm25_top_indices)))
    # Sort combined indices based on the sum of cosine similarity and BM25 scores
    combined_indices.sort(key=lambda x: (similarities[x] + bm25_scores[x]), reverse=True)
    
    # Return the top 5 documents based on the combined scores
    return [(filenames[i], documents[i], similarities[i] + bm25_scores[i]) for i in combined_indices[:5]]

def extract_answers(query, documents):
    # Initialize the question-answering pipeline
    qa_pipeline = pipeline("question-answering")
    answers = []
    # Extract answers from each document using the QA pipeline
    for doc in documents:
        answer = qa_pipeline(question=query, context=doc)
        answers.append((doc, answer['answer'], answer['score']))
    return answers

def main():
    # Load data
    vectorizer, tfidf_matrix, filenames, documents = load_data()
    # Get user query
    query = input("Enter your query: ")
    results = retrieve_documents(query, vectorizer, tfidf_matrix, filenames, documents)
    documents = [result[1] for result in results]
    # Extract answers from the retrieved documents
    answers = extract_answers(query, documents)
    # Print the answers
    for doc, answer, score in answers:
        print(f"Document: {doc}, Answer: {answer}, Score: {score}")

if __name__ == "__main__":
    main()
