from selenium import webdriver
from selenium.webdriver.common.by import By


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
    no_stock = 'חסר זמנית'
    update_when = 'עדכנו כשחוזר'
    in_stock = 'במלאי'
    looper = 0
    books_image = []
    for image in images:
        books_image.append(image.get_attribute('src'))

    for book in books:
        raw_details = book.text
        book_details = raw_details.split('\n')
        book_id = book.get_attribute('product_id')
        print(book_details)
        if book_details[0] == no_stock:
            in_stock = 'חסר במלאי'
            book_details.pop(0)
        if book_details[0] == update_when:
            book_details.pop(0)
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
            book_details.insert(2, in_stock)
        book_details.insert(3, books_image[looper])
        print(book_details)

        i = 0
        for item in book_details:
            print(f'{i} - {item}')
            i += 1
        looper += 1

        books_dict[book_id] = book_details
    del_items = []
    for key in books_dict:
        if bookname not in books_dict[key][0]:
            del_items.append(key)
    #print(del_items)
    for item in del_items:
        books_dict.pop(item, None)
    #print(del_items)
    return books_dict


driver = webdriver.Chrome()
bookname = input('Please enter books name:')

print('Books from סטימצקי \n', stimazky(driver))