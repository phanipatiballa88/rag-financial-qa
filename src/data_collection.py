import pdfplumber
import os

def pdf_to_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def save_text(text, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)

def main():
    input_dir = "data/raw"
    output_dir = "data/processed"
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            text = pdf_to_text(pdf_path)
            output_path = os.path.join(output_dir, filename.replace(".pdf", ".txt"))
            save_text(text, output_path)

if __name__ == "__main__":
    main()