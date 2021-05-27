from selenium import webdriver
from typing import final


class Searching:

    def __init__(self):
        self.CHROME_DRIVER_PATH: final(str) = 'C:/Development/chromedriver.exe'
        self.RENTAL_LINK: final(str) = 'https://www.cian.ru/'
        self.op = webdriver.ChromeOptions()
        self.op.add_argument('headless')
        self.browser = webdriver.Chrome(executable_path=self.CHROME_DRIVER_PATH, options=self.op)

    def get_rental(self):
        self.browser.get(self.RENTAL_LINK)
        rental_input = self.browser.find_element_by_id('geo-suggest-input')
        btn = self.browser.find_elements_by_class_name('_025a50318d--button--1sI1I')
        price_btn = self.browser.find_element_by_class_name('_025a50318d--button--empty--2RA1G')
        rent = self.browser.find_elements_by_class_name('_025a50318d--list-element--2-qFY')

        price_btn.click()

        price_inputs = self.browser.find_elements_by_class_name('_025a50318d--input--suffix--3he7o')

        price_inputs[1].send_keys(40000)

        for x in rent:
            x.find_element_by_tag_name('a')
            if x.text == 'Снять':
                x.click()

        rental_input.send_keys('Москва, ул. Мусы Джалиля')

        for x in btn:
            if x.text == 'Найти':
                x.click()

        try:
            frontend = self.browser.find_element_by_id('frontend-serp')
            link = frontend.find_elements_by_css_selector('article ._93444fe79c--link--39cNw')

            for x in link:
                print(x.get_attribute('href'))
        except:
            pass
        # return self.browser.current_url
