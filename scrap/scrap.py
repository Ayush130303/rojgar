# jobscraper/remoteok_scraper.py
import requests
from bs4 import BeautifulSoup

def fetch_jobs():
    url = "https://remoteok.com/remote-dev-jobs"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    jobs = []
    for row in soup.select("tr.job"):
        jobs.append({
            "external_id": row.get("data-id"),
            "title": row.select_one("h2").text.strip(),
            "company": row.select_one(".companyLink h3").text.strip(),
            "tags": [tag.text for tag in row.select(".tag")],
            "url": "https://remoteok.com" + row.get("data-href", ""),
        })
    return jobs
