import pdfplumber
import re

def clean_text(text):
    """Remove (cid:xxx) encoding issues and non-ASCII characters."""
    text = re.sub(r"\(cid:\d+\)", "", text)  # Remove (cid:xxx) patterns
    text = re.sub(r"[^\x00-\x7F]+", " ", text)  # Remove non-ASCII characters
    # text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces
    return text

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"  # Extract selectable text
    return text

pdf_path = "/Users/wilfried/Downloads/user_resume.pdf"
extracted_text = extract_text_from_pdf(pdf_path)
cleaned_text = clean_text(extracted_text)

with open("/Users/wilfried/Downloads/resume_text.txt", "w+", encoding="utf-8") as f:
    f.write(cleaned_text)

print("Extracted text saved to resume_text.txt")