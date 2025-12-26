import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

titles = []
prices = []
ratings = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.p["class"][1]

    titles.append(title)
    prices.append(price)
    ratings.append(rating)

data = {
    "Title": titles,
    "Price": prices,
    "Rating": ratings
}

df = pd.DataFrame(data)

df.to_csv("books_data.csv", index=False)

print("Data scraped and saved successfully!")
