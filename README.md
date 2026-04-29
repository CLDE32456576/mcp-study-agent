# MCP Study Agent

An AI-powered study tool that reads university lecture PDFs and generates flashcards, summaries, and quiz questions on demand.

Built with the **Model Context Protocol (MCP)**, this server gives Claude direct access to your lecture files. Ask Claude to "read Sesión 1 and generate flashcards" — it autonomously reads the PDF, extracts content, generates study materials, and saves them back to disk.

## Features

- **List lectures** — View all available lecture PDFs
- **Read PDFs** — Extract text from lecture files
- **Generate flashcards** — Create Anki-style study cards
- **Generate quizzes** — Produce exam-style questions
- **Summarize** — Create structured study summaries
- **Save notes** — Write all outputs as markdown files
- **Read back** — Access saved files via MCP resources

## Setup

### Prerequisites
- Python 3.8+
- Anthropic API key
- Claude Desktop (for MCP integration)

### Installation

```bash
git clone https://github.com/CLDE32456576/mcp-study-agent.git
cd mcp-study-agent

pip3 install mcp anthropic pdfplumber --break-system-packages
```

### Add to Claude Desktop

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "study-agent": {
      "command": "/opt/anaconda3/bin/python3",
      "args": ["/Users/YOUR_USERNAME/Desktop/mcp-study-agent/server.py"]
    }
  }
}
```

Replace `YOUR_USERNAME` with your Mac username.

### Run Locally

```bash
python3 server.py
```

Then restart Claude Desktop.

## Usage

In Claude Desktop:
Read any lecture PDF and ask Claude to generate flashcards, summaries, or quizzes.

Claude will:
1. List available PDFs
2. Read the requested file
3. Generate flashcards
4. Save them to `output/`

## Tools Available

- `list_lectures()` — List all PDFs in the pdfs/ folder
- `read_lecture(filename)` — Extract text from a PDF
- `generate_summary(filename)` — Create a study summary
- `generate_flashcards(filename, num_cards)` — Generate Anki cards
- `generate_quiz(filename)` — Create exam questions
- `save_study_notes(filename, content)` — Save output to markdown
- `list_output_files()` — List all saved files
- `read_output_file(path)` — Read saved markdown files

## Project Structure
mcp-study-agent/
├── server.py              # MCP server with all tools
├── pdfs/                  # Your lecture PDFs
├── output/                # Generated study materials
├── README.md              # This file
└── .gitignore

## Next Steps

- Week 3: Integrate with RAG (Retrieval-Augmented Generation)
- Week 4: Add evals and monitoring
- Week 5: Deploy to production VPS

## Tech Stack

- **Python** — Core language
- **Anthropic Claude API** — AI backbone
- **MCP (Model Context Protocol)** — Tool integration
- **pdfplumber** — PDF text extraction

---

**Week 2 deliverable** — Part of a 60-day AI acceleration roadmap.