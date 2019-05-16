# import libraries
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import re

# specify the url
urls = open('pages.txt', 'r').read().splitlines()
print urls

#for loop
data=[]
for url in urls:
  baseurl = re.sub(r"[^/]*(\?.*)?$", "", url)
  # query the website and return the html to the variable 'page'
  page = urllib2.urlopen(url)

  # parse the html using beautiful soup and store in variable 'soup'
  soup = BeautifulSoup(page, 'html.parser')

  # Take out the <div> of name and get its value
  titleh1 = soup.find('h1')
  if titleh1 and titleh1.text:
    title = titleh1.text.strip().encode("ascii", "ignore") # strip() is used to remove starting and trailing
  else:
    title = "No Title"

  images = soup.find().findAll('img')
  imagedata = ""
  delimiter = ""
  for image in images:
    if image['src'] != "../../design/images/web-logo.gif" and image['src'] != "../design/images/web-logo.gif":
      imagedata = imagedata+delimiter+baseurl+image['src']
      delimiter = "|"

  data.append((title,imagedata))
  # open a csv file with append, so old data will not be erased
  with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([title, imagedata, url, datetime.now()])

#block-views-dining-menu-meal-block-block-1 .view-dining-menu-meal-block > .view-content
