# import os
# from sklearn.feature_extraction.text import TfidfVectorizer
# import pickle

# def preprocess_text(text):
#     # Implement any text preprocessing steps here
#     return text

# def main():
#     input_dir = "data/processed"
#     texts = []
#     filenames = []

#     for filename in os.listdir(input_dir):
#         if filename.endswith(".txt"):
#             with open(os.path.join(input_dir, filename), "r", encoding="utf-8") as file:
#                 text = file.read()
#                 texts.append(preprocess_text(text))
#                 filenames.append(filename)

#     vectorizer = TfidfVectorizer()
#     X = vectorizer.fit_transform(texts)

#     with open("vectorizer.pkl", "wb") as file:
#         pickle.dump(vectorizer, file)
#     with open("tfidf_matrix.pkl", "wb") as file:
#         pickle.dump(X, file)
#     with open("filenames.pkl", "wb") as file:
#         pickle.dump(filenames, file)

# if __name__ == "__main__":
#     main()

import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_text(text):
    # Implement any text preprocessing steps here
    return text

def split_into_chunks(text, chunk_size=500):
    words = text.split()
    chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

def main():
    input_dir = "data/processed"
    texts = []
    filenames = []
    documents = []

    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(input_dir, filename), "r", encoding="utf-8") as file:
                text = file.read()
                text = preprocess_text(text)
                chunks = split_into_chunks(text)
                texts.extend(chunks)
                filenames.extend([filename] * len(chunks))
                documents.extend(chunks)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    with open("vectorizer.pkl", "wb") as file:
        pickle.dump(vectorizer, file)
    with open("tfidf_matrix.pkl", "wb") as file:
        pickle.dump(X, file)
    with open("filenames.pkl", "wb") as file:
        pickle.dump(filenames, file)
    with open("documents.pkl", "wb") as file:
        pickle.dump(documents, file)

if __name__ == "__main__":
    main()