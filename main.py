from selenium import webdriver
from selenium.webdriver.common.by import By

def tzomet(driver):
    # צומת ספרים
    driver.get(f'https://www.booknet.co.il/%D7%97%D7%99%D7%A4%D7%95%D7%A9?q={bookname}')
    prices = driver.find_elements(By.TAG_NAME, 'ins')
    books = driver.find_elements(By.XPATH, '//div[@class="products product-cube col-md-2"]')
    authors = driver.find_elements(By.XPATH, '//a[@class="book-below-title product-author"]')
    images = driver.find_elements(By.XPATH, '//img[@class="img-responsive img-lazy-load"]')
    books_image = []
    for image in images:
        books_image.append(image.get_attribute("src"))

    books_dict = {}
    looper = 0
    for book in books:
        # print(item.text)
        book_details = []
        bookid = book.get_attribute("data-prodid")
        book_name = book.get_attribute("data-fullname")
        book_publish = book.get_attribute("data-manufacturer")
        book_details.append(prices[looper].text)
        book_details.append(authors[looper].text)
        book_details.append(books_image[looper])
        looper += 1
        book_details.append(book_name)
        book_details.append(book_publish)
        books_dict[bookid] = book_details
        # print(book_details)

    return books_dict


driver = webdriver.Chrome()
# driver.get('https://www.booknet.co.il/')
bookname = input('Please enter books name:')

print('Books from צומת ספרים \n', tzomet(driver))



# סטימצקי
# driver.get(f'https://www.steimatzky.co.il/catalogsearch/result/?q={bookname}')

# בוקמי
# driver.get(f'https://www.bookme.co.il/%D7%97%D7%99%D7%A4%D7%95%D7%A9?q={bookname}')

# עברית
# driver.get(f'https://www.e-vrit.co.il/Search/{bookname}')



# סטימצקי
def get_book_name(sku):
    link = 'https://www.steimatzky.co.il/' + sku
    name_element = driver.find_elements(By.XPATH, f'//a[@href="{link}"]')
    #print(len(name_element))
    book_name = name_element[0].get_attribute('title')
    return book_name
driver = webdriver.Chrome()
# סטימצקי
bookname = input('Please enter books name:')
driver.get(f'https://www.steimatzky.co.il/catalogsearch/result/?q={bookname}')
books_id = driver.find_elements(By.XPATH, '//form[@class="start-product-item"]')
skus = driver.find_elements(By.XPATH, '//form[@class="start-product-item"]')
#authors = driver.find_elements(By.XPATH, '//div[@class="product-category-parse product-parse"]')
authors = driver.find_elements(By.XPATH, '//div[@class="product-wrapper"]')
for author in authors:
    print
    print(author.text)
#authors = driver.find_element(By.TAG_NAME, 'a')
#print(len(books))
'''books_name = []
for sku in skus:
    #print(sku.get_attribute('data-product-sku'))
    book_sku = sku.get_attribute('data-product-sku')
    books_name.append(get_book_name(book_sku))
for book_id in books_id:
    print(book_id.get_attribute('product_id'))

#books_name = driver.find_elements(By.XPATH, '//a[@href="https://www.steimatzky.co.il/011411684"]')
print(books_name)
print(authors)'''
'''for author in authors:
    print(author.text)'''


def book_me(driver):
    driver.get(f'https://www.bookme.co.il/%D7%97%D7%99%D7%A4%D7%95%D7%A9?q={bookname}')
    elements = driver.find_elements(By.XPATH,
                                    '//div[@class="products col-xs-6 col-sm-4 col-md-3 col-lg-3 product-cube"]')
    print(len(elements))
    '''for element in elements:
        print(element.text)'''
    print(elements[3].text)


driver = webdriver.Chrome()
# driver.get(f'https://www.bookme.co.il/%D7%97%D7%99%D7%A4%D7%95%D7%A9?q={bookname}')
bookname = input('Please enter books name:')
print('Books from בוקמי \n', book_me(driver))