from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

#CHROME BROWSER DRIVER DOWNLOAD LINK:-https://chromedriver.chromium.org/

CHROME_DRIVER_PATH = "ENTER HERE YOUR chromedriver.exe PATH OR OTHER BROWSER DRIVER PATH"
SIMILAR_ACCOUNT = "pythoncodess"
USERNAME = "Enter your instagram username."
PASSWORD = "Enter your instagram password."
class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.get("https://www.instagram.com/")

    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(5)
        name = self.driver.find_element_by_name("username")
        pass_word = self.driver.find_element_by_name("password")
        name.send_keys(USERNAME)
        pass_word.send_keys(PASSWORD)
        pass_word.send_keys(Keys.ENTER)
        sleep(5)

    def find_followers(self):
        try:
            name=self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
            name.send_keys(USERNAME)
            password=self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
            password.send_keys(PASSWORD)
        except Exception:    
            self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}/')
            sleep(5)
        else:
            sleep(5)
            self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}/f')
            sleep(5)
        followers_popup = self.driver.find_element_by_css_selector('header a')
        followers_popup.click()
        sleep(5)
          # Holds the div in which the followers are appearing
  # Holds the div in which the followers are appearing
        # follower = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_x5"]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]')
        # for i in range(10):
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower)
        #     sleep(2)
    def follow(self):
        get_followers = self.driver.find_elements(By.XPATH, '//li/div/div/button')
        num = 0
        while num < len(get_followers):
            while num < len(get_followers):
                print(len(get_followers))
                follower = get_followers[num]
                while get_followers[num].text == "Follow":
                    try:
                        follower.click()
                        sleep(5)
                    except ElementClickInterceptedException:
                        cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                        cancel_button.click()
                    sleep(2)
                    get_followers = self.driver.find_elements(By.XPATH, '//li/div/div/button')
                num += 1

bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
