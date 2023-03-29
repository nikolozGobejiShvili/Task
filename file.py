import requests, json
from bs4 import BeautifulSoup

url = "https://www.home.ge/saxlebi-agarakebi/iyideba-saxlebi-agarakebi/iyideba-sakhli-saguramo-308731.html"
response= requests.get(url).text
soup = BeautifulSoup(response , "html.parser")
section = soup.find("section",  class_="content-section clearfix")


title = section.find("h1").text.strip()
price = section.find("div", class_="price-tag" ,id="df_field_price").text.strip()
square = section.find("li", class_="services").text.strip()
location = section.find("div", class_="location").text.strip()

dict_info={ 
    "title" : title,
    "df_field_price" : price,
    "services" : square,
    "location": location

}

with open("dict_info.json", "w") as file:
    json.dump(dict_info, file, ensure_ascii=False)

