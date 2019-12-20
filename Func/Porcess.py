from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from Func.Controller import *
from Func.picManager import *


class process():
    def __init__(self, username, passwd):

        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-images')
        self.driver = webdriver.Chrome(
            './chromedriver.exe', chrome_options=self.options)
        self.driver.set_window_size(1024, 960)
        self.ProcessFalse = False
        self.username = username
        self.passwd = passwd

    def run(self):
        self.Openpage()
        self.Login()
        self.banner()
        self.openActivePage()
        self.openRpage()
        self.openShoppage()
        self.buyGift()
        self.driver.quit()

    def Openpage(self):
        self.driver.get("https://www.majsoul.com/1/")
        data = {(775, 650): "#FFFFFF", (860, 645): "#FFFFFF"}
        count = 0
        while count < 99:
            self.driver.save_screenshot('screenshot.png')
            if checkColor("screenshot.png", data):
                return
            time.sleep(5)
            count = count+1

        print("打开网页成功_Openpage")
        self.ProcessFalse = True

    def Login(self):
        if self.ProcessFalse:
            return

        click_locxy(self.driver, 680, 370)
        strinput(self.driver, self.username)
        click_locxy(self.driver, 700, 430)
        strinput(self.driver, self.passwd)
        click_locxy(self.driver, 750, 550)

        self.driver.save_screenshot('screenshot.png')
        count = 0
        data = {(987, 742): "#AD2E2D", (989, 742): "#AD2E2D"}
        while count < 99:
            self.driver.save_screenshot('screenshot.png')
            if checkColor("screenshot.png", data):
                return
            time.sleep(5)
            count = count+1
        self.ProcessFalse = True
        print("登录_Login")

    def banner(self):
        if self.ProcessFalse:
            return

        data = [(931, 285), (950, 285)]
        count = 0
        while count < 99:
            time.sleep(5)
            self.driver.save_screenshot('screenshot.png')
            if not checkColor_Block("screenshot.png", data):
                return
            click_locxy(self.driver, 931, 285)
            count = count+1
        self.ProcessFalse = True
        print("关闭banner成功_banner")

    def openActivePage(self):

        if self.ProcessFalse:
            return

        data = [(931, 285), (950, 285)]
        count = 0
        while count < 99:
            time.sleep(5)
            self.driver.save_screenshot('screenshot.png')
            if checkColor_Block("screenshot.png", data):
                return
            click_locxy(self.driver, 770, 240)
            count = count+1
        self.ProcessFalse = True
        print("打开活动页面成功_openActivePage")

    def openRpage(self):

        if self.ProcessFalse:
            return

        click_locxy(self.driver, 229, 477)
        time.sleep(1)
        click_locxy(self.driver, 223, 535)
        time.sleep(1)
        click_locxy(self.driver, 800, 615)
        time.sleep(1)
        data = [(931, 285), (950, 285)]
        count = 0
        while count < 99:
            time.sleep(3)
            self.driver.save_screenshot('screenshot.png')
            if not checkColor_Block("screenshot.png", data):
                return
            click_locxy(self.driver, 931, 285)
            count = count+1
        self.ProcessFalse = True

        print("打开复活页面成功_openRpage")

    def buyGift(self):
        if self.ProcessFalse:
            return
        count = 0
        while count < 10:
            if int(getCoin()) > 15000:
                click_locxy(self.driver, 320, 525)
                time.sleep(1)
                click_locxy(self.driver, 490, 650)
                time.sleep(1)
                self.driver.save_screenshot('screenshot.png')
            else:
                return
            count = count+1
        
        print("购买商品成功_buyGift")

    def openShoppage(self):
        if self.ProcessFalse:
            return
        data = [(48, 310), (55, 310)]
        count = 0
        while count < 99:
            time.sleep(5)
            self.driver.save_screenshot('screenshot.png')
            if checkColor_Block("screenshot.png", data):
                return
            click_locxy(self.driver, 885, 725)
            count = count+1
        self.ProcessFalse = True
        print("打开商店页面成功_openShoppage")
