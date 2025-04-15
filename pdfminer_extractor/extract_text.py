from pdfminer.high_level import extract_text
import os

def extract_text_from_pdf(pdf_path):
    """
    Extract text from PDF using pdfminer.six
    """
    try:
        # Extract text from PDF
        text = extract_text(pdf_path)
        return text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # Example usage
    pdf_path = "sample.pdf"  # Replace with your PDF file path
    if os.path.exists(pdf_path):
        extracted_text = extract_text_from_pdf(pdf_path)
        print("Extracted Text:")
        print(extracted_text)
    else:
        print(f"Error: File {pdf_path} not found")
        #ss