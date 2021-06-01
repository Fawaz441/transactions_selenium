import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from config import *
from credentials import USERNAME,PASSWORD

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


def main():
    driver.get(URL)
    username_input = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))
    username_input.send_keys(USERNAME)
    WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, USERNAME_SENDER))).click()
    password_input = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, PASSWORD_INPUT)))
    password_input.send_keys(PASSWORD)
    WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, PASSWORD_SENDER))).click()
    slideshow = WebDriverWait(driver, 12).until(EC.element_to_be_clickable((By.CLASS_NAME,SLIDESHOW_CONTAINER )))
    proceeder = driver.find_element_by_xpath(PROCEED)
    driver.execute_script('arguments[0].click();',proceeder)
    driver.find_element_by_xpath(STATEMENT_DIV).click()
    account_select = WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[2]/ui-view/div[3]/div[2]/ui-view/div[2]/div[2]/div[3]/div/div[1]/div[2]/select' )))
    accounts = account_select.find_elements_by_tag_name('option')
    accounts[1].click()
    try:
        last_30_days = WebDriverWait(driver,12).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="manage_third_party_container"]/div[2]/input[3]'))).click()
    except:
        pass
    js = "var aa=document.getElementsByClassName('global-spinner ng-isolate-scope')[0];aa.parentNode.removeChild(aa)"
    driver.execute_script(js)
    export = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="btn_export"]'))).click()
    file_name_input = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/form[1]/div[1]/input'))).clear()
    driver.find_element_by_xpath('/html/body/div[1]/div/form[1]/div[1]/input').send_keys('transactions_since_may')
    final_export = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/form[1]/div[2]/input[2]')))
    final_export.click()
    time.sleep(10)
    driver.quit()


    


main()


    






