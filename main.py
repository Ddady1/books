from selenium import webdriver
from selenium.webdriver.common.by import By


def tzomet(driver):
    # צומת ספרים
    driver.get(f'https://www.booknet.co.il/%D7%97%D7%99%D7%A4%D7%95%D7%A9?q={bookname}')
    prices = driver.find_elements(By.TAG_NAME, 'ins')
    books = driver.find_elements(By.XPATH, '//div[@class="products product-cube col-md-2"]')
    authors = driver.find_elements(By.XPATH, '//a[@class="book-below-title product-author"]')
    images = driver.find_elements(By.XPATH, '//img[@class="img-responsive img-lazy-load"]')
    # azal = driver.find
    in_stock = None
    is_printed = True
    is_digital = False
    in_basket = 'הוסף לסל'
    price_str = 'מחיר מכירה'
    books_image = []
    for image in images:
        books_image.append(image.get_attribute("src"))

    books_dict = {}
    looper = 0
    exc = driver.find_elements(By.XPATH, '//button/span[@class="sr-only"]')
    # print(exc[0].text)
    for book in books:
        raw_details = book.text
        book_id = book.get_attribute("data-prodid")
        book_details = raw_details.split('\n')
        print(book_details)
        if exc[looper].text in book_details:
            book_details.remove(exc[looper].text)
        if price_str in book_details:
            book_details.remove(price_str)
        print(book_details)
        if len(book_details) >= 5:
            book_details.pop(0)
        book_details.append(books_image[looper])
        print(book_details)
        if in_basket in book_details:
            in_stock = True
        else:
            in_stock = False
        book_details.pop(3)
        book_details.insert(3, in_stock)
        book_details.append(is_printed)

        i = 0
        for item in book_details:
            print(f'{i} - {item}')
            i += 1
        if looper < len(exc) - 1:
            looper += 1
            # print(looper)
        books_dict[book_id] = book_details
    '''for book in books:
        # print(item.text)
        book_details = []
        bookid = book.get_attribute("data-prodid")
        book_name = book.get_attribute("data-fullname")
        book_publish = book.get_attribute("data-manufacturer")
        book_details.append(book_name)
        book_details.append(authors[looper].text)
        book_details.append(book_publish)
        book_details.append(prices[looper].text)
        book_details.append(books_image[looper])
        looper += 1
        books_dict[bookid] = book_details
        # print(book_details)

    return books_dict'''
    print(books_dict)


driver = webdriver.Chrome()
# driver.get('https://www.booknet.co.il/')
bookname = input('Please enter books name:')

print('Books from צומת ספרים \n', tzomet(driver))


# בוקמי
# driver.get(f'https://www.bookme.co.il/%D7%97%D7%99%D7%A4%D7%95%D7%A9?q={bookname}')

# עברית
# driver.get(f'https://www.e-vrit.co.il/Search/{bookname}')


# סטימצקי

def stimazky(driver):
    # סטימצקי
    driver.get(f'https://www.steimatzky.co.il/catalogsearch/result/?q={bookname}')
    books = driver.find_elements(By.XPATH, '//form[@class="start-product-item"]')
    images = driver.find_elements(By.XPATH, '//a/span/span/img[@class="product-image-photo"]')
    book_details = []
    books_dict = {}
    regular_price = 'מחיר רגיל'
    item_price = 'מחיר מוצר'
    currency = 'ש"ח'
    club_price = ''  # NEED TO TAKE CARE OF THIS
    is_digital = 'דיגיטלי'
    is_printed = 'מודפס'
    in_stock = None
    looper = 0
    books_image = []
    for image in images:
        books_image.append(image.get_attribute('src'))

    for book in books:
        raw_details = book.text
        book_details = raw_details.split('\n')
        book_id = book.get_attribute('product_id')
        print(book_details)
        index = []
        for i in range(len(book_details)):
            if book_details[i] == regular_price:
                index.append(i)
        print(index)
        for i in sorted(index, reverse=True):
            book_details.pop(i + 1)
            book_details.pop(i)

        # print(book_details)
        '''if regular_price in book_details:
            book_details.pop(-1)
            book_details.pop(-1)'''
        for item in book_details:
            if item == item_price:
                book_details.remove(item)
        for item in book_details:
            if currency in item:
                book_details.remove(item)
        if is_digital in book_details or is_printed in book_details:
            in_stock = True
            book_details.insert(2, in_stock)
        book_details.insert(3, books_image[looper])
        print(book_details)

        i = 0
        for item in book_details:
            print(f'{i} - {item}')
            i += 1
        looper += 1

        books_dict[book_id] = book_details
    return books_dict


driver = webdriver.Chrome()
bookname = input('Please enter books name:')

print('Books from סטימצקי \n', stimazky(driver))


def get_book_name(sku):
    link = 'https://www.steimatzky.co.il/' + sku
    name_element = driver.find_elements(By.XPATH, f'//a[@href="{link}"]')
    # print(len(name_element))
    book_name = name_element[0].get_attribute('title')
    return book_name


driver = webdriver.Chrome()
# סטימצקי
bookname = input('Please enter books name:')
driver.get(f'https://www.steimatzky.co.il/catalogsearch/result/?q={bookname}')
books_id = driver.find_elements(By.XPATH, '//form[@class="start-product-item"]')
skus = driver.find_elements(By.XPATH, '//form[@class="start-product-item"]')
# authors = driver.find_elements(By.XPATH, '//div[@class="product-category-parse product-parse"]')
authors = driver.find_elements(By.XPATH, '//div[@class="product-wrapper"]')
books_dict = {}
id_list = []
for book_id in books_id:
    theID = book_id.get_attribute('product_id')
    # print(theID)
    id_list.append(theID)
    books_dict[theID] = ''
looper = 0
# print(books_dict)
for author in authors:
    # print(author.text)
    book_clean = author.text.split('\n')
    books_dict[id_list[looper]] = book_clean  # author.text
    looper += 1
print(books_dict)
print(books_dict['74921'])

# authors = driver.find_element(By.TAG_NAME, 'a')
# print(len(books))
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

# בוקמי
def price_raw(raw):
    # print(raw)
    prices_list = raw.split(' ')
    # prices_list.pop(-1)
    num = 1000
    for item in prices_list:
        if (item.replace('.', '', 1).isdigit() and float(item) < num):
            num = float(item)

    return num


def name_raw(raw_string):
    name_list = raw_string.split('/')

    return name_list


def book_me(driver):
    driver.get(f'https://www.bookme.co.il/%D7%97%D7%99%D7%A4%D7%95%D7%A9?q={bookname}')
    books = driver.find_elements(By.XPATH, '//div[@class="products col-xs-6 col-sm-4 col-md-3 col-lg-3 product-cube"]')
    images = driver.find_elements(By.XPATH, '//img[@class="img-responsive img-lazy-load"]')
    formats = driver.find_elements(By.XPATH, '//div[@class="productPrice"]')
    book_raw_details = []
    books_dict = {}
    books_image = []
    no_stock = 'אזל'
    image_link = 'https://www.bookme.co.il'
    for image in images:
        link = image_link + image.get_attribute("data-original")
        books_image.append(link)
    is_digital = None
    is_printed = None

    currency = 'ש"ח'
    looper = 0
    price_clean = ''
    # print(len(elements))
    for book in books:
        book_details = []
        title = ''
        author = ''
        raw_details = book.text
        book_raw_details = raw_details.split('\n')
        book_id = book.get_attribute('data-prodid')
        print(book_raw_details)
        is_digital = formats[looper].get_attribute('data-digital')
        is_printed = formats[looper].get_attribute('data-print')
        if '/' in book_raw_details[0]:
            title, author = name_raw(book_raw_details[0])
        else:
            title = book_raw_details[0]
        price_clean = price_raw(book_raw_details[1])
        book_details.append(title)
        book_details.append(author)
        if no_stock in book_raw_details:
            book_details.append(False)
        else:
            book_details.append(True)
        book_details.append(books_image[looper])
        book_details.append(is_digital)
        book_details.append(None)
        book_details.append(is_printed)
        book_details.append(currency + str(price_clean))

        i = 0
        for item in book_details:
            print(f'{i} - {item}')
            i += 1
        looper += 1
        books_dict[book_id] = book_details

    print(books_dict)

    '''text1 = (books[3].text)
    text2 = (books[4].text)
    text3 = (books[6].text)
    #print(type(text))
    print(text1)
    print(text2)
    print(text3)
    print(len(text1))
    text4 = text2.split('\n')
    print(text4)
    no_stock = 'אזל'
    if no_stock in text4:
        print(no_stock)
    else:
        print('במלאי')
    print(len(text4))'''


driver = webdriver.Chrome()
# driver.get(f'https://www.bookme.co.il/%D7%97%D7%99%D7%A4%D7%95%D7%A9?q={bookname}')
bookname = input('Please enter books name:')
print('Books from בוקמי \n', stimazky(driver))