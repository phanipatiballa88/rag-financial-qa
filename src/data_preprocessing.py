import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_text(text):
    """
    Preprocesses the given text by applying various text preprocessing steps.

    Args:
        text (str): The input text to be preprocessed.

    Returns:
        str: The preprocessed text.
    """
    # Implement any text preprocessing steps here
    return text

def split_into_chunks(text, chunk_size=500):
    """
    Splits the given text into chunks of specified size.

    Args:
        text (str): The input text to be split into chunks.
        chunk_size (int, optional): The number of words per chunk. Defaults to 500.

    Returns:
        list: A list of text chunks, each containing up to chunk_size words.
    """
    words = text.split()
    chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

def main():
    input_dir = "data/processed"
    texts = []
    filenames = []
    documents = []

    # Iterate over all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            # Read the content of the file
            with open(os.path.join(input_dir, filename), "r", encoding="utf-8") as file:
                text = file.read()
                # Preprocess the text
                text = preprocess_text(text)
                # Split the text into chunks
                chunks = split_into_chunks(text)
                # Extend the lists with the chunks and corresponding filenames
                texts.extend(chunks)
                filenames.extend([filename] * len(chunks))
                documents.extend(chunks)

    # Create a TF-IDF vectorizer and fit it to the texts
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    # Save the vectorizer, TF-IDF matrix, filenames, and documents to pickle files
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
