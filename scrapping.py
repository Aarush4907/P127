import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

r = requests.get(url)
htmlcontent=r.content
#print(htmlcontent)
soup = BeautifulSoup(htmlcontent,'html.parser')
#print(soup.prettify)
title = soup.title
print(title)
