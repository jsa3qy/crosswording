from __future__ import print_function
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as BS
from urllib.parse import urlparse
from chromedriver_py import binary_path
import time
import re
import csv
import sys
import random

DELAY = 5 # seconds, max wait time when we mutate observe
USERNAME = "jesseboy624@aol.com"
PASSWORD = "PASSWORD"

def main(username=USERNAME, password=PASSWORD):
    
    options = webdriver.ChromeOptions()
    #options.add_argument('headless') #open a headless browser 
    browser = webdriver.Chrome(executable_path=binary_path, options=options)
    wait = WebDriverWait(browser, get_delay())
    browser.set_window_size(1440, 900) #defining window size stops headless from erroring for .click() functions

    #login page to access the root page of interest
    browser.get("https://www.nytimes.com/puzzles/leaderboards")
    browser.find_element_by_class_name('lbd-button.black')
    try:
        login_btn = browser.find_element_by_class_name('lbd-button.black')
        time.sleep(get_delay())
        login_btn.click()
    except NoSuchElementException:
            eprint("NoSuchElementException: element id 'lbd-button.black' not found")
            sys.exit(1)

    time.sleep(get_delay())
    try:
        username_input = browser.find_element_by_id("username")
        password_input = browser.find_element_by_id("password")
    except NoSuchElementException:
        eprint("NoSuchElementException: username or password field not found")
        sys.exit(1)

    username_input.send_keys(USERNAME)
    time.sleep(get_delay())
    password_input.send_keys(PASSWORD)
    time.sleep(get_delay())

    #submit login credential
    try:
        submit_btn = browser.find_element_by_class_name('css-nrhj9s-buttonBox-buttonBox-primaryButton-primaryButton-Button')
        time.sleep(get_delay())
        submit_btn.click()
    except NoSuchElementException:
            eprint("NoSuchElementException: element class 'css-nrhj9s-buttonBox-buttonBox-primaryButton-primaryButton-Button' not found")
            sys.exit(1)

    time.sleep(DELAY)
    html = BS(browser.page_source, 'html.parser')
    potential_btns = html.find_all(class_='lbd-score')

    for btn in potential_btns:
        print(btn)

def get_delay():
    return random.randint(4,8)

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

#main
if __name__ == "__main__":
    if sys.argv[1]:
        username = sys.argv[1]
    if sys.argv[2]:
        password = sys.argv[2]
    if username and password:
        main(username, password)
    else:
        main()
