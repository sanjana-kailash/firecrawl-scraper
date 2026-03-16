# AI News Summariser

A Python tool that scrapes AI/tech news websites and generates a concise TLDR summary — built for professionals who want to stay on top of the AI landscape without reading through entire publications.

## Tools Used
- [Firecrawl](https://firecrawl.dev) — web scraping
- [Groq](https://groq.com) — fast LLM inference (Llama 3.1)
- Python 3.12

## Setup

1. Clone the repo
2. Install dependencies:
```
   pip install firecrawl-py groq python-dotenv
```
3. Create a `.env` file with your API keys:
```
   FIRECRAWL_API_KEY=your_key_here
   GROQ_API_KEY=your_key_here
```

## Usage
```
python scraper.py
```

## Roadmap
- [ ] Add multiple news sources
- [ ] Build a web frontend
- [ ] Host on Vercel