from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Instagram:
    """
        This class is used to open Instagram
    """

    def __init__(self, url="https://www.instagram.com/guviofficial/"):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        """
            This method is used to open the browser and go to Guvi Instagram.
        """
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(3)

    def quit(self):
        self.driver.quit()

    def getInfo(self):
        """
                This method is used to get the Instagram followers and followings
        """
        print("Instagram followers of Guvi are :" , self.driver.find_element(by=By.XPATH,
                                       value="//*[contains(@id, 'mount')]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button/span").text)


        print("Guvi follows " , self.driver.find_element(by=By.XPATH, value="//*[contains(@id, 'mount')]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button/span/span").text , " accounts on Instagram")

obj = Instagram("https://www.instagram.com/guviofficial/")
obj.boot()
obj.getInfo()
obj.quit()
