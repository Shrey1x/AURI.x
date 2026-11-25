import re
from io import BytesIO
from pathlib import Path

SKILL_DICTIONARY = [
    "python", "java", "c++", "c", "javascript", "typescript", "sql", "mysql",
    "postgresql", "mongodb", "html", "css", "react", "node.js", "django",
    "flask", "streamlit", "machine learning", "deep learning", "natural language processing",
    "nlp", "data analysis", "data visualization", "pandas", "numpy", "scikit-learn",
    "tensorflow", "pytorch", "power bi", "tableau", "excel", "statistics",
    "git", "github", "docker", "aws", "azure", "linux", "api", "rest api",
    "computer vision", "generative ai", "large language models", "llm"
]

def extract_resume_text(uploaded_file, filename):
    """Extract text from PDF, DOCX or TXT uploaded through Streamlit."""
    suffix = Path(filename).suffix.lower()
    content = uploaded_file.getvalue()

    if suffix == ".pdf":
        import fitz
        document = fitz.open(stream=content, filetype="pdf")
        return "\n".join(page.get_text("text") for page in document)

    if suffix == ".docx":
        from docx import Document
        doc = Document(BytesIO(content))
        return "\n".join(p.text for p in doc.paragraphs)

    if suffix == ".txt":
        return content.decode("utf-8", errors="ignore")

    raise ValueError("Unsupported file format. Please upload PDF, DOCX or TXT.")

def extract_skills(text):
    """Find known skills using case-insensitive whole-term matching."""
    normalized = text.lower()
    found = []
    for skill in SKILL_DICTIONARY:
        pattern = r"(?<![a-z0-9+#.])" + re.escape(skill.lower()) + r"(?![a-z0-9+#.])"
        if re.search(pattern, normalized):
            found.append(skill)
    return sorted(set(found))
