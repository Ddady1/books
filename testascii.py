import urllib.request
import urllib.parse
from urllib.parse import quote
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

bookname = input('Please enter book name: ')
bookencoded = urllib.parse.quote(bookname)
url = "https://www.booknet.co.il/%D7%97%D7%99%D7%A4%D7%95%D7%A9?q=" + bookencoded
page = urllib.request.urlopen(url)
soup = bs(page)

print(soup)