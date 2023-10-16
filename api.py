import requests
from bs4 import BeautifulSoup

from fastapi import FastAPI
app = FastAPI()
URL = "https://genshin-impact.fandom.com/wiki/Spiral_Abyss"


def getAbyssEndDate():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    date = soup.find(string= lambda text: "Duration:" in text)
    realDate = date[date.find('–') + 2: len(date)-1]
    print(realDate)
    return realDate

@app.get("/get-abyss-end-date")
def get_abyss_end_date():
    return getAbyssEndDate()

def main():
    getAbyssEndDate()

if __name__ == '__main__':
    main()