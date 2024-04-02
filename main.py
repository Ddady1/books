from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#driver.get('https://www.booknet.co.il/')
bookname = input('Please enter books name:')

# צומת ספרים
driver.get(f'https://www.booknet.co.il/%D7%97%D7%99%D7%A4%D7%95%D7%A9?q={bookname}')

# סטימצקי
#driver.get(f'https://www.steimatzky.co.il/catalogsearch/result/?q={bookname}')

# בוקמי
#driver.get(f'https://www.bookme.co.il/%D7%97%D7%99%D7%A4%D7%95%D7%A9?q={bookname}')

# עברית
#driver.get(f'https://www.e-vrit.co.il/Search/{bookname}')

price = driver.find_element(By.TAG_NAME, 'ins').text
prices = driver.find_elements(By.TAG_NAME, 'ins')
bookid = driver.find_elements(By.XPATH, '//div[@data-prodid]')
print(type(bookid))
books = driver.find_elements(By.XPATH, '//span[@class="sr-only"]')
ext = driver.find_elements(By.XPATH, '//div[@class="products product-cube col-md-2"]')
#books_list = []
for book in books:
    print(book.text)

#print(books_list)
#price
'''i = 0
for item in prices:
    #print(item.text)
    #print(ext[i].text)
    #print(bookid[i].text)
    i += 1

for item in ext:
    #print(item.text)
    ls.append(item.get_attribute("data-prodid"))

ls'''
#bookid[0].text
#print(ext[1])
#print(len(ext))