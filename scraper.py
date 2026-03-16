import os
from dotenv import load_dotenv
from firecrawl import FirecrawlApp
from groq import Groq

load_dotenv()

api_key=os.environ.get("FIRECRAWL_API_KEY")
groq_api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    raise ValueError("Firecrawl API key not found.Check your .env file.")
app=FirecrawlApp(api_key=api_key)


if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found. Check your .env file.")
groq_client = Groq(api_key=groq_api_key)

def scrape_news(url):
    try:
        scrapings=app.scrape(url,formats=['markdown'],only_main_content=True)
        print("Successfully scraped",url)

        return scrapings

    except Exception as e:
        print("Unsuccessful scraping",e)

        return None
   

def summarise_news(scrapings):
    completion=groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role":"user",
                "content":f"Summarise the website for latest advancements/news and give me a quick summary and things to learn to stay ahead of the curve:\n\n{scrapings}"
            }
        ]
    )

    summary=completion.choices[0].message.content

    return summary

result=scrape_news(r"https://www.deeplearning.ai/the-batch/")
summary=summarise_news(result.markdown)
print(summary)