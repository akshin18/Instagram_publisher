import keyword
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium import webdriver
import os
import time
from v1 import story_reshape
from selenium.webdriver.common.keys import Keys




class instapublisher():
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.dir_path = os.getcwd()
        self.profile = os.path.join(self.dir_path+r'/selen/sele', "profile", "facebook")
        self.options.add_argument(r"user-data-dir={}".format(self.profile))
        self.mobile_emulation = {

   "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },

   "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 181.1.0.27.117 (iPhone9,4; iOS 12_4_1; es_ES; es-ES; scale=2.88; 1080x1920; 282277724)" }
        # self.options.add_argument("--headless")
        self.options.add_argument('proxy_server=localhost:8080')
        self.options.add_argument("start-maximized")
        self.options.add_argument("--auto-open-devtools-for-tabs")
        self.options.add_experimental_option("mobileEmulation", self.mobile_emulation) #For mobile
        # self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # self.options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=self.options,executable_path=r'C:\Users\Akshin\PycharmProjects\akshin\Kwork\newparsinstasend\selen\chromedriver.exe')
        self.driver.get("https://www.instagram.com")


    def publish(self,texto='hello',path=r'C:\Users\Akshin\PycharmProjects\akshin\Kwork\newparsinstasend\images\cartez.png',pop=r'C:\Users\Akshin\PycharmProjects\akshin\Kwork\newparsinstasend\images\konec.png'):

        print('start')
        WebDriverWait(self.driver, 15).until(Ec.presence_of_element_located((By.CLASS_NAME, '_0TPg')))
        try:
            no = self.driver.find_element_by_class_name('HoLwm')
            time.sleep(3)
            no.click()
        except:pass
        print('2')
        WebDriverWait(self.driver, 60).until(Ec.presence_of_element_located((By.CLASS_NAME, '_8-yf5')))
        ad = self.driver.find_elements_by_class_name('_8-yf5')[-2]
        ad.click()
        time.sleep(1)
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')
        inp = self.driver.find_elements_by_tag_name('input')[-1]
        inp.send_keys(pop)
        print('3')
        WebDriverWait(self.driver, 60).until(Ec.presence_of_element_located((By.CLASS_NAME, 'UP43G')))
        time.sleep(1)
        next = self.driver.find_element_by_class_name('UP43G')
        next.click()
        print('4')
        WebDriverWait(self.driver, 60).until(Ec.presence_of_element_located((By.TAG_NAME, 'textarea')))
        time.sleep(1)
        text = self.driver.find_element_by_tag_name('textarea')
        text.send_keys(texto[:2195]+'...')
        next = self.driver.find_element_by_class_name('UP43G')
        next.click()
        print('5')
        WebDriverWait(self.driver, 60).until(Ec.presence_of_element_located((By.CLASS_NAME, '_0TPg')))
        ############
        story_reshape()
        time.sleep(1)
        # stories = self.driver.find_elements_by_class_name('_8-yf5')[-6]
        stories = self.driver.find_element_by_class_name('mTGkH')
        time.sleep(1)
        print("31")

        stories.click()
        time.sleep(1)
        # stories
        print("32")
        # inp = self.driver.find_elements_by_tag_name('input')[2]
        #//*[@id="react-root"]/section/main/div[1]/form/input
        try:
            inp = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[1]/div/div/div/div[1]/button/form/input')
        except:
            inp = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav[1]/div/div/form/input')
        print("33")
        inp.send_keys(path)

        print("34")
        time.sleep(2)

        # webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        ############################3
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')
        pyautogui.hotkey('ctrl', 'shift', 'm')
        pyautogui.hotkey('ctrl', 'shift', 'm')
        ############################3
        publish = self.driver.find_element_by_class_name('cQjQD')
        publish.click()
        WebDriverWait(self.driver, 15).until(Ec.presence_of_element_located((By.CLASS_NAME, '_0TPg')))
