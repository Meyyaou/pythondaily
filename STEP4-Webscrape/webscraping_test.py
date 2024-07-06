#from bs4 import BeautifulSoup4
from bs4 import BeautifulSoup
#import requests no needeeed

#url = "index.html"
with open("/content/index.html", 'r')as file:
  soup=BeautifulSoup(file, 'html.parser')

#soup=BeautifulSoup(r, 'html.parser')
title=soup.title.string

#head=soup.find('h1') moreopt
head=soup.h1.string
'''noms = soup.find_all("h2")
nom_txt=[]
for nom in noms:
    nom_txt.append(nom.string)
nom_txt
prices= soup.find_all("p")
price_txt=[]
descs_txt=[]
for p in prices:
  if p.string=='Prix :':
    price_txt.append(p)
  else:
    descs_txt.append(p)

descs_txt
'''
prods= soup.find_all('li')
products_li=[]
prices=[]
for prod in prods:
  name=prod.h2.string
  price= prod.find('p', string=lambda s:'Prix' in s).string
  prices.append(price)
  products_li.append((name,price))
descs_li=[]
for prod in prods:
  desc=prod.find('p', string=lambda s:'Description' in s).string
  descs_li.append(desc)
  print("the title is ", title)
print("the main text is ", head)
print("the products and their prices: ", products_li)
print("the descriptions ", descs_li)
#conversion to dollar
#dollar= euro*1.2
import re

dollar=[]
products_dolli=[]
for i in range(0,len(prices)):
  p=re.findall(r'\d+', prices[i])
  dollar.append(float(p[0]))
dollar=[d * 1.2 for d in dollar]
for i, (name, price) in enumerate(products_li):
  products_li[i]= (name, f"{dollar[i]}$")
print("the products and their prices: ", products_li)
