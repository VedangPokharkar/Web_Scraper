import requests
from bs4 import BeautifulSoup

url = "https://www.geeksforgeeks.org/"
attem = requests.get(url)
Htmlcont = attem.content
soup = BeautifulSoup(Htmlcont, 'html.parser')


# print(soup.prettify)


# trying to capture all anchor tags
anchor = soup.find_all('a')
# print(anchor)

#capture all links in the anchors
for link in anchor:
    print(link.get('href'))




#fetching div data using id of the div
datamode = soup.find(id='data-mode')
# print(datamode.contents)

#contents saves list in memory

for ele in datamode.contents:
    print(ele)

#children does not save data in memory and works as a generator instead
for ele in datamode.children:
    print(ele)


#printing out the individual items of the div as strings use stripped_strings in case the strings are disjointed.
for item in datamode.strings:
    print(item)



#printing out the names of the parent classes of the captured class
#print next_sibling.next_sibling or previous_sibling.previous_sibling to parse content of divs with the same parent div.

for item in datamode.parents:
    print(item.name)    



#capture CSS selector
elem = soup.select('#topMainHeader')
print(elem)    
# for x in elem:
#     print(x.name)
