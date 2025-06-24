from pdfminer.high_level import extract_text
from io import BytesIO
from docx import Document

def extract_text_from_file(filename: str, file_bytes: bytes) -> str:
    """Extract text from .pdf or .docx files."""
    if filename.endswith(".pdf"):
        return extract_text_from_pdf(file_bytes)
    elif filename.endswith(".docx"):
        return extract_text_from_docx(file_bytes)
    else:
        raise ValueError("Unsupported file type. Only .pdf or .docx supported.")


def extract_text_from_pdf(file_bytes: bytes) -> str:
    try:    
        text = extract_text(BytesIO(file_bytes))
        if not text:
            raise ValueError("PDF text extraction returned empty result.")
        return text.strip()  # ✅ Always a STRING
    except Exception as e:
        print(f"Error extracting text: {e}")
        raise


def extract_text_from_docx(file_bytes: bytes) -> str:
    
    doc = Document(BytesIO(file_bytes))
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return '\n'.join(text).strip()