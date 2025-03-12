import pdfplumber
import os

def pdf_to_text(pdf_path):
    # Initialize an empty string to hold the extracted text
    text = ""
    # Open the PDF file using pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        # Iterate through each page in the PDF
        for page in pdf.pages:
            # Extract text from the current page and append it to the text string
            text += page.extract_text()
    # Return the extracted text
    return text

def save_text(text, output_path):
    # Open the output file in write mode with UTF-8 encoding
    with open(output_path, "w", encoding="utf-8") as file:
        # Write the extracted text to the file
        file.write(text)

def main():
    # Define the input directory containing PDF files
    input_dir = "data/raw"
    # Define the output directory to save the extracted text files
    output_dir = "data/processed"
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Iterate through each file in the input directory
    for filename in os.listdir(input_dir):
        # Check if the file has a .pdf extension
        if filename.endswith(".pdf"):
            # Construct the full path to the PDF file
            pdf_path = os.path.join(input_dir, filename)
            # Extract text from the PDF file
            text = pdf_to_text(pdf_path)
            # Construct the full path to the output text file
            output_path = os.path.join(output_dir, filename.replace(".pdf", ".txt"))
            # Save the extracted text to the output file
            save_text(text, output_path)

if __name__ == "__main__":
    main()
