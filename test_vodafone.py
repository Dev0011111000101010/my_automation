import time, locators
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def test_open_site(driver):
    driver.get(locators.vodafone_URL_gold_number)
    assert 'vodafone.ua/gold-number' in driver.current_url
    print(driver.current_url)

def test_site_name_text(driver):
    driver.get(locators.vodafone_URL_gold_number)
    time.sleep(2)
    # expected_site_name_H1 = 'OpenWeather'
    # placeholder_vibor_nomera = driver.find_element(By.CSS_SELECTOR, locators.number_placeholder)
    placeholder_vibor_nomera = driver.find_element(By.CSS_SELECTOR, '.mask-input')
    element_nije_placeholdera = driver.find_element(By.CSS_SELECTOR, "div[class='tab-circle-body tab-body grey-block-page'] div h3[class='block-name']")
    blok_cooke_v_futere = driver.find_element(By.CSS_SELECTOR, locators.cooke_block_in_footer)
    knopka_ok_v_futere_cookies_div = driver.find_element(By.CSS_SELECTOR, locators.cooke_ok_button)
    actions = ActionChains(driver)
    # if blok_cooke_v_futere:
    #     print("В футере был куки вопрос")
    #     actions.move_to_element(knopka_ok_v_futere_cookies_div).click(knopka_ok_v_futere_cookies_div)


    time.sleep(2)
    actions.move_to_element(element_nije_placeholdera)
    time.sleep(2)
    # placeholder_vibor_nomera.click()
    # time.sleep(2)
    # vibor_nomera_1_BACKSPACE = driver.find_element(By.CSS_SELECTOR, locators.number_placeholder).send_keys(Keys.BACKSPACE)
    # time.sleep(2)
    # vibor_nomera_1_BACKSPACE
    # time.sleep(2)
    # vibor_nomera_1_BACKSPACE
    # time.sleep(2)
    # vibor_nomera_1_BACKSPACE
    # time.sleep(2)
    # vibor_nomera_1_BACKSPACE
    # time.sleep(2)
    # vibor_nomera_1_BACKSPACE
    # time.sleep(2)
    # vibor_nomera_1_BACKSPACE
    # time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR, locators.number_placeholder).send_keys('99')
    time.sleep(2)
    # assert expected_site_name_H1 == site_name_H1_text
    # print('   #print = ', expected_site_name_H1, ' = ', site_name_H1_text)
