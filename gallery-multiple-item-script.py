# import libraries
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import re

# specify the url
quote_page = ['http://www.stlawu.edu/gallery/exhibitions/f/19ipellie.php?keepThis=true&TB_iframe=true&height=500&width=920','http://www.stlawu.edu/gallery/exhibitions/f/19sunshine.php']

#for loop
data=[]
for pg in quote_page:
  # query the website and return the html to the variable 'page'
  page = urllib2.urlopen(pg)

  # parse the html using beautiful soup and store in variable 'soup'
  soup = BeautifulSoup(page, 'html.parser')

  # Take out the <div> of name and get its value
  titleh1 = soup.find('h1')
  mediadiv = soup.find('div', attrs={'class': 'left'})

  title = titleh1.text.strip() # strip() is used to remove starting and trailing
  mediaurl = mediadiv.img['src']
  mediacaption = mediadiv.text

  body = soup.find('blockquote', attrs={'type': 'cite'})
  bodytext = re.sub(r'[^\x00-\x7f]',r'', body.text)

  data.append((title,mediadiv,mediaurl))
  # open a csv file with append, so old data will not be erased
  with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([title, mediaurl, mediacaption, bodytext, datetime.now()])

#block-views-dining-menu-meal-block-block-1 .view-dining-menu-meal-block > .view-content
