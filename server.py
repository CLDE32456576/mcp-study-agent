import os
import pdfplumber
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Study Agent")

PDFS_DIR = os.path.join(os.path.dirname(__file__), "pdfs")

@mcp.tool()
def list_lectures() -> str:
    """List all available lecture PDFs."""
    files = [f for f in os.listdir(PDFS_DIR) if f.endswith(".pdf")]
    if not files:
        return "No PDFs found in the pdfs/ folder."
    return "\n".join(f"- {f}" for f in sorted(files))

@mcp.tool()
def read_lecture(filename: str) -> str:
    """Read and extract text from a lecture PDF."""
    path = os.path.join(PDFS_DIR, filename)
    if not os.path.exists(path):
        return f"File not found: {filename}"
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text[:8000]

@mcp.tool()
def generate_summary(filename: str) -> str:
    """Get a structured study summary prompt for a lecture."""
    content = read_lecture(filename)
    if content.startswith("File not found"):
        return content
    return f"""Lecture content extracted. Now do the following:
1. Write a 5-bullet summary of the key concepts
2. List 3 things a student must absolutely know for an exam
3. Identify any formulas, frameworks, or models mentioned

Content:
{content}"""

@mcp.tool()
def generate_flashcards(filename: str, num_cards: int = 5) -> str:
    """Generate Anki-style flashcards from a lecture PDF."""
    content = read_lecture(filename)
    if content.startswith("File not found"):
        return content
    return f"""Create exactly {num_cards} Anki flashcards from this lecture.
Format each one as:
Front: [question]
Back: [answer]
---

Lecture content:
{content}"""

@mcp.tool()
def generate_quiz(filename: str) -> str:
    """Generate 5 exam-style questions from a lecture PDF."""
    content = read_lecture(filename)
    if content.startswith("File not found"):
        return content
    return f"""Generate 5 exam-style questions from this lecture.
Mix question types: multiple choice, short answer, application.
Include the correct answer below each question.

Lecture content:
{content}"""


@mcp.tool()
def save_study_notes(filename: str, content: str) -> str:
    """Save study notes or materials to a markdown file in the output folder."""
    output_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(output_dir, exist_ok=True)

    # Clean filename
    clean_name = filename.replace(".pdf", "").replace(" ", "_")
    output_path = os.path.join(output_dir, f"{clean_name}_notes.md")

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"✓ Saved to {output_path}"
    except Exception as e:
        return f"Error saving file: {str(e)}"


@mcp.resource("file://{path}")
def read_output_file(path: str) -> str:
    """Read a file from the output folder."""
    output_dir = os.path.join(os.path.dirname(__file__), "output")
    file_path = os.path.join(output_dir, path)

    if not os.path.exists(file_path):
        return f"File not found: {file_path}"

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"


@mcp.tool()
def list_output_files() -> str:
    """List all files in the output folder."""
    output_dir = os.path.join(os.path.dirname(__file__), "output")
    if not os.path.exists(output_dir):
        return "Output folder is empty."
    files = os.listdir(output_dir)
    if not files:
        return "No files in output folder yet."
    return "\n".join(f"- {f}" for f in sorted(files))

if __name__ == "__main__":
    mcp.run()

