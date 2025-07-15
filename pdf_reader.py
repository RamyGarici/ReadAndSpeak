import pdfplumber
# This function extracts text from a PDF file using pdfplumber.
def extract_text_from_pdf(uploaded_file):
    with pdfplumber.open(uploaded_file) as pdf:
        text=""
        for pages in pdf.pages:
            text+=pages.extract_text()
        if not text:
            raise ValueError("No text found in the PDF file.")
            
            
    return text