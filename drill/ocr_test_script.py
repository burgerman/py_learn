import pytesseract
import os
import numpy as np
import cv2
os.environ["TESSDATA_PREFIX"] = "/Users/wilfried/homebrew/share/tessdata/"
pytesseract.pytesseract.tesseract_cmd = "/Users/wilfried/homebrew/bin/tesseract"
print(pytesseract.get_languages(config=''))
from pdf2image import convert_from_path
from PIL import Image


def remove_non_text_regions(img):
    """Remove small icons, logos, and symbols using contour detection."""
    img_cv = np.array(img)
    gray = cv2.cvtColor(img_cv, cv2.COLOR_RGB2GRAY)

    # Apply thresholding to separate text from background
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Find contours (shapes) in the image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = w / float(h)

        # Remove very small regions (likely icons, logos)
        if w < 20 or h < 20 or aspect_ratio > 10:
            cv2.rectangle(img_cv, (x, y), (x + w, y + h), (255, 255, 255), -1)  # Fill with white

    return Image.fromarray(img_cv)


def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path=pdf_path, poppler_path="/Users/wilfried/homebrew/bin")  # Convert PDF pages to images
    text = ""
    for img in images:
        processed_img = remove_non_text_regions(img)
        text += pytesseract.image_to_string(processed_img, config="--psm 6")+"\n"  # OCR processing
    return text

# Usage
pdf_path = "/Users/wilfried/Downloads/user_resume.pdf"  # Path to your PDF resume
extracted_text = extract_text_from_pdf(pdf_path)

# Save extracted text to a file
with open("/Users/wilfried/Downloads/resume_text.txt", "w+", encoding="utf-8") as f:
    f.write(extracted_text)

print("Extracted text saved to resume_text.txt")
