from bs4 import BeautifulSoup  
import requests

# sending request to the target website
html_source = requests.get("https://romanvm.pythonanywhere.com/").text

# parse the html from the target website and store it 
parsed_html = BeautifulSoup(html_source, 'html.parser')

# specify a section of the entire html
posts = parsed_html.find_all("div", class_="card-body")

# use for loop to iterate over every post
for post in posts:
    title = post.h3.a.text
    paragraph = post.find("div", class_="post-cut").p.text 
    print(f"-- {title} --")
    print(paragraph)
    print()
