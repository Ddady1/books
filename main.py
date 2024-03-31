from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
bookname = input('Please enter books name:')
# צומת ספרים
driver.get(f'https://www.booknet.co.il/%D7%97%D7%99%D7%A4%D7%95%D7%A9?q={bookname}')

# סטימצקי
#driver.get(f'https://www.steimatzky.co.il/catalogsearch/result/?q={bookname}')

# בוקמי
#driver.get(f'https://www.bookme.co.il/%D7%97%D7%99%D7%A4%D7%95%D7%A9?q={bookname}')

# עברית
#driver.get(f'https://www.e-vrit.co.il/Search/{bookname}')
