from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def click_locxy(dr, x, y, left_click=True):

    if left_click:
        ActionChains(dr).move_by_offset(x, y).click().perform()
    else:
        ActionChains(dr).move_by_offset(x, y).context_click().perform()
    ActionChains(dr).move_by_offset(-x, -y).perform()

def strinput(dr,strr):
    ActionChains(dr).send_keys(strr).perform()
    
