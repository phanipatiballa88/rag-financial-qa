# import pickle
# from sklearn.metrics.pairwise import cosine_similarity

# def load_data():
#     with open("vectorizer.pkl", "rb") as file:
#         vectorizer = pickle.load(file)
#     with open("tfidf_matrix.pkl", "rb") as file:
#         tfidf_matrix = pickle.load(file)
#     with open("filenames.pkl", "rb") as file:
#         filenames = pickle.load(file)
#     return vectorizer, tfidf_matrix, filenames

# def retrieve_documents(query, vectorizer, tfidf_matrix, filenames):
#     query_vec = vectorizer.transform([query])
#     similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
#     top_indices = similarities.argsort()[-5:][::-1]
#     return [(filenames[i], similarities[i]) for i in top_indices]

# def main():
#     vectorizer, tfidf_matrix, filenames = load_data()
#     query = input("Enter your query: ")
#     results = retrieve_documents(query, vectorizer, tfidf_matrix, filenames)
#     for filename, score in results:
#         print(f"Document: {filename}, Score: {score}")

# if __name__ == "__main__":
#     main()

import pickle
from sklearn.metrics.pairwise import cosine_similarity
from rank_bm25 import BM25Okapi
from transformers import pipeline

def load_data():
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
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = similarities.argsort()[-5:][::-1]
    
    bm25 = BM25Okapi([doc.split() for doc in documents])
    bm25_scores = bm25.get_scores(query.split())
    bm25_top_indices = bm25_scores.argsort()[-5:][::-1]
    
    combined_indices = list(set(top_indices).union(set(bm25_top_indices)))
    combined_indices.sort(key=lambda x: (similarities[x] + bm25_scores[x]), reverse=True)
    
    return [(filenames[i], documents[i], similarities[i] + bm25_scores[i]) for i in combined_indices[:5]]

def extract_answers(query, documents):
    qa_pipeline = pipeline("question-answering")
    answers = []
    for doc in documents:
        answer = qa_pipeline(question=query, context=doc)
        answers.append((doc, answer['answer'], answer['score']))
    return answers

def main():
    vectorizer, tfidf_matrix, filenames, documents = load_data()
    query = input("Enter your query: ")
    results = retrieve_documents(query, vectorizer, tfidf_matrix, filenames, documents)
    documents = [result[1] for result in results]
    answers = extract_answers(query, documents)
    for doc, answer, score in answers:
        print(f"Document: {doc}, Answer: {answer}, Score: {score}")

if __name__ == "__main__":
    main()