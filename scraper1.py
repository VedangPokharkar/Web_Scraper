import requests
from bs4 import BeautifulSoup


url = "https://www.codewithharry.com/"
# url2 = "https://www.geeksforgeeks.org/"
attem = requests.get(url)
# attem2 = requests.get(url2)
Htmlcont = attem.content
# Htmlcont2 = attem2.content


soup = BeautifulSoup(Htmlcont, 'html.parser')
# soup2 = BeautifulSoup(Htmlcont2, 'html.parser')

print(soup.prettify)
print(soup)
title = soup.title
# print(title)
# print(type(title))



# trying to capture all anchor tags
anchor = soup.find_all('a')
print(anchor)


# trying to capture all anchor tags
paras = soup.find_all('p')
print(paras)


# trying to capture all anchor tags
headings = soup.find_all('h1')
print(headings)


# trying to capture all anchor tags
quotes = soup.find_all('q')
print(quotes)


# capture first element
anchor1 = soup.find('a')
print("ANCHORS ARE - ",anchor1)

#capture class of that element
print(soup.find('p')['class'])

#searching by class
print(soup.findAll('p', class_='mt-2'))

#capture text in an element
print(soup.find('p').get_text())
