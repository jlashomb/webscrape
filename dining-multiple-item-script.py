# import libraries
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# specify the url
quote_page = ['https://www.stlawu.edu/dana-dining-center','https://www.stlawu.edu/northstar-cafe']

#for loop
data=[]
for pg in quote_page:
  # query the website and return the html to the variable 'page'
  page = urllib2.urlopen(pg)

  # parse the html using beautiful soup and store in variable 'soup'
  soup = BeautifulSoup(page, 'html.parser')

  # Take out the <div> of name and get its value
  titleh1 = soup.find('h1', attrs={'class': 'page-header'})
  menudiv = soup.find('div', attrs={'class': 'view-dining-menu-meal-block'})

  title = titleh1.text.strip() # strip() is used to remove starting and trailing
  menu = menudiv

  data.append((title,menu))
  # open a csv file with append, so old data will not be erased
  with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([title, menu, datetime.now()])

#block-views-dining-menu-meal-block-block-1 .view-dining-menu-meal-block > .view-content
