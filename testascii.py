import urllib.request
import urllib.parse
from urllib.parse import quote
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

bookname = input('Please enter book name: ')
bookencoded = urllib.parse.quote(bookname)
url = "https://www.steimatzky.co.il/catalogsearch/result/?q=" + bookencoded
print(url)
page = urllib.request.urlopen(url)
soup = bs(page)

print(soup)