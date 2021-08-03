import requests
from bs4 import BeautifulSoup
import json

url = "https://mc.gizex.ru/"

headers = {

    "Accept": "*/*",

  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"

}

req = requests.get(url, headers=headers)

src= req.text




with open("index.html", "w", encoding='utf-8') as file:
  file.write(src)
  
with open("index.html", encoding='utf-8') as file:
    src = file.read()
    
soup = BeautifulSoup(src, "lxml")

all_news_headers = soup.find_all(class_= "news-log")
news = 12
news_header_dict = {}
for item in all_news_headers:
    news_header = item.text
    # print(news_header)
news_header_dict[news_header] = news_header_dict

print(news_header)

with open("resuls.json", "w") as file:
     json.dump(news_header_dict, file, indent=4, ensure_ascii=False)