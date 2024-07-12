import requests
from bs4 import BeautifulSoup

url = "https://www.geeksforgeeks.org/"
attem = requests.get(url)
Htmlcont = attem.content
soup = BeautifulSoup(Htmlcont, 'html.parser')
print(soup.prettify)


# trying to capture all anchor tags
anchor = soup.find_all('a')
print(anchor)

#capture all links in the anchors
for link in anchor:
    print(link.get('href'))
