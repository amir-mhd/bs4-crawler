from bs4 import BeautifulSoup  
import requests
import lxml

html_source = requests.get("https://news.ycombinator.com/news").text

soup = BeautifulSoup(html_source, 'html.parser')

print(soup.prettify())


