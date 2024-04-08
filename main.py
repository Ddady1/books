from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get('https://www.booknet.co.il/')
bookname = input('Please enter books name:')

# צומת ספרים
driver.get(f'https://www.booknet.co.il/%D7%97%D7%99%D7%A4%D7%95%D7%A9?q={bookname}')

# סטימצקי
# driver.get(f'https://www.steimatzky.co.il/catalogsearch/result/?q={bookname}')

# בוקמי
# driver.get(f'https://www.bookme.co.il/%D7%97%D7%99%D7%A4%D7%95%D7%A9?q={bookname}')

# עברית
# driver.get(f'https://www.e-vrit.co.il/Search/{bookname}')

price = driver.find_element(By.TAG_NAME, 'ins').text
prices = driver.find_elements(By.TAG_NAME, 'ins')
# books = driver.find_elements(By.XPATH, '//span[@class="sr-only"]')
books = driver.find_elements(By.XPATH, '//div[@class="products product-cube col-md-2"]')
authors = driver.find_elements(By.XPATH, '//a[@class="book-below-title product-author"]')
images = driver.find_elements(By.XPATH, '//img[@class="img-responsive img-lazy-load"]')
books_image = []
for image in images:
    books_image.append(image.get_attribute("src"))

'''for book in books:
    book_str = (book.text)
    print(book_str)'''

books_dict = {}
looper = 0
for book in books:
    # print(item.text)
    book_details = []
    bookid = book.get_attribute("data-prodid")
    book_name = book.get_attribute("data-fullname")
    book_publish = book.get_attribute("data-manufacturer")
    # book_details.append(bookid)
    book_details.append(prices[looper].text)
    book_details.append(authors[looper].text)
    book_details.append(books_image[looper])
    looper += 1
    book_details.append(book_name)
    book_details.append(book_publish)
    books_dict[bookid] = book_details
    # print(book_details)
    # book_author =

print(books_dict)
# ls
# bookid[0].text
# print(ext[1])
# print(len(ext))