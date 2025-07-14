import pdfplumber
# This function extracts text from a PDF file using pdfplumber.
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open("../../dummy.pdf") as pdf:
        for pages in pdf.pages:
            print(pages.extract_text())
    return pdf.pages