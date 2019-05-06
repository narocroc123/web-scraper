# import libraries
import urllib
from bs4 import BeautifulSoup

# specifying the url
url = 'INPUT URL HERE'

# query the website and return html to the variable 'page'
data = []
for pg in url:
    r = urllib.request.urlopen(pg)

# parse the HTML Using Beuatiful Soup and Store the Variable 'soup'
soup = BeautifulSoup(r, ‘html.parser’)

# find value of name <div>
name_box = soup.find('h1', attrs={'class': 'name'})

# extract text data
name = name_box.text.strip() # strip() used to remove starting and trailing
print(name)

# get price index
price_box = soup.find('div', attrs={'class':'price'})
    price = price_box.text
    print (price)

data.append((name, price))

# export to csv
import csv 
from datetime import datetime

with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for name, price in data:
    writer.writerow([name, price, datetime.now()])
    writer.writerow('')