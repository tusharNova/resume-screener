from io import BytesIO
from pdfminer.high_level import extract_text

def extract_text_from_pdf(file_bytes : bytes) -> str:
    try:
        pass
        fake_file = BytesIO(file_bytes)
        text = extract_text(fake_file)
        return text.split()

    except Exception as e:
        return f"Error parsing PDF: {str(e)}"