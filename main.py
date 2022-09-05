# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



def print_hi(name):
    service = Service(executable_path="D:\source\chromedriver.exe")

    browser = webdriver.Chrome(service=service)
    browser.get("https://www.allenedmonds.com/shoe-care/polishes-and-cleaners?icid=TopNav_ShoeCare_Polish")
    title = browser.title
    print(title)
    browser.implicitly_wait(3.5)


    product_name = browser.find_element(by=By.CLASS_NAME, value="item-result__product-name")
    search_button = browser.find_element(by=By.CLASS_NAME, value="coveo-search-button")
    search_box = browser.find_element(by=By.XPATH, value="//div[@class='magic-box-input']/input")

    print(search_box.aria_role)
    search_box.clear()
    #search_box.send_keys("test")
    #search_button.click()

    browser.implicitly_wait(3.5)

    #message = driver.find_element(by=By.ID, value="message")
    #value = message.text

    title = browser.title
    print(title)

    browser.quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
