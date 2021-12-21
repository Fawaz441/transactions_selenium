import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from bedspace_config import *

ua = UserAgent()
userAgent = ua.random

chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("no-sandbox")

executable_path = r'chromedriver.exe' #remove
chrome_options.add_argument("--window-size=1920,1200")
user_agent = u'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
chrome_options.add_argument('user-agent={0}'.format(user_agent))
driver = webdriver.Chrome(options=chrome_options)

def apply():
    driver.get(BEDSPACE_URL)
    gender_select = WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH,SEX_SELECT )))
    gender = gender_select.find_elements_by_tag_name('option')
    gender[1].click()
    apply_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, APPLY_BTN)))
    apply_btn.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/h3')))
    failure_text = 'Sorry, Available BedSpaces For Male is exhausted.'
    if(failure_text in driver.page_source):
        print('No bedspace again!')
        apply()
    else:
        print('There might be bedspace!')


def main():
    driver.get(LOGIN_URL)
    # driver.quit()
    username_input = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, USERNAME_INPUT)))
    username_input.send_keys(USERNAME)
    password_input = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, PASSWORD_INPUT)))
    password_input.send_keys(PASSWORD)
    WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, LOGIN_BTN))).click()
    apply()
    return

main()


    






