# CLAUDE.md — MCP Study Agent Maintenance Guide

## What This Project Does
MCP server that gives Claude access to lecture PDFs. Tools: list, read, summarize, generate flashcards/quizzes, save notes.

## Key Files
- `server.py` — All 7 MCP tools defined here
- `pdfs/` — User lecture PDFs (not in git)
- `output/` — Generated markdown files (not in git)

## Adding New Tools
1. Add `@mcp.tool()` decorated function to server.py
2. Restart server
3. Quit/reopen Claude Desktop for new tool to appear

## Common Issues
- Server won't start: Check Python path matches claude_desktop_config.json
- Claude doesn't see new tools: Restart both server and Claude Desktop
- PDF extraction fails: Verify file is in pdfs/ folder and readable

## Testing
Test all tools: "Read a PDF, generate flashcards, save them, list outputs, read saved file"

## Next Integration Points
- Week 3: Connect to RAG pipeline
- Week 5: Deploy to VPS for 24/7 access
