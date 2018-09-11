# for loop
# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
quote_page = ['https://www.admin.ch/opc/en/classified-compilation/19110009/index.html#indexni1']


data = []
for pg in quote_page:
     # query the website and return the html to the variable page
     page = urllib2.urlopen(pg)
    # parse the html using beautiful soap and store in variable `soup`
     soup = BeautifulSoup(page, 'html.parser')
    # Take out the <div> of name and get its value
     name_box = soup.find('h5')
     name = name_box.text.strip() # strip() is used to remove starting and trailing
    # get the index price
     price_box = soup.find('div', attrs={'class':'collapseableArticle'})
     price = price_box.text
    # save the data in tuple
     data.append((name, price))

print(data[-1])