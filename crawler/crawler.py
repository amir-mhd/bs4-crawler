from bs4 import BeautifulSoup  
import requests
import csv

# sending request to the target website
html_source = requests.get("https://romanvm.pythonanywhere.com/").text

# parse the html from the target website and store it 
parsed_html = BeautifulSoup(html_source, 'html.parser')

# specify a section of the entire html
posts = parsed_html.find_all("div", class_="card-body")

# writting the scraped data to a csv file
data_csv_file = open("data.csv", "w")
csv_writer = csv.writer(data_csv_file)
csv_writer.writerow(["title", "summary"])

# use for loop to iterate over every post
for post in posts:
    try:
        title = post.h3.a.text
        summary = post.find("div", class_="post-cut").p.text 
    except Exception:
        pass
    
    print(f"-- {title} --")
    print(summary)
    print()

    csv_writer.writerow([title, summary])


data_csv_file.close()