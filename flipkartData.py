import requests
from bs4 import BeautifulSoup



productName = []
Prices = []
description = []
reviws = []


url = "https://www.flipkart.com/search?q=wireless+headphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"
att = requests.get(url)
soup = BeautifulSoup(att.text, "html")


names = soup.find_all("a", class_="wjcEIp")

for i in names:
    newname = i.text
    productName.append(newname)

print(productName)    
print(len(productName))
prices = soup.find_all("div", class_="Nx9bqj")

for i in prices:
    pricelist = i.text
    Prices.append(pricelist)

print(Prices) 
print(len(Prices))   
# print(names)
# print(soup)
# np = soup.find('a', class_="_9QVEpD").get("href")
# fnp = "https://www.flipkart.com"+np
# print(fnp)
