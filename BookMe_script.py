from selenium import webdriver
from selenium.webdriver.common.by import By


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
print('Books from בוקמי \n', book_me(driver))