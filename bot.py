from selenium import webdriver
from selenium import *
import os
import time

username = input("Enter your username: ")
password = input("Enter your password: ")




class InstagramBot:
# this is where all of our log in credentials are entered as class
    def __init__(self, username, password):
        #initializes an instance of the InstagramBot class, authenticates the user with instagram using credential passed in as args
      
      
      #Args: 
      #username:str: The users Instagram username,   password:str: The users Instagram Password
      
      #Attributes: 
      #driver: selenium.webdriver.Chrome(): This is the driver we are using to automate browser actions
       
        
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome('./chromedriver')
        self.login()
        self.get_unfollowers()
        
        
    
    def login(self):   
        self.driver.get("https://www.instagram.com/?hl=en")
       # fucntion that opens instagram in a chrome window and logs in using the credentials we passed in the class 
        time.sleep(2)
        # must make function sleep in order to keep up with the slow speed of webpage
        self.driver.find_element_by_name('username').send_keys(self.username)
    
        self.driver.find_element_by_name('password').send_keys(self.password)

        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()

        time.sleep(5)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()

        time.sleep(2)

        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

    
    def get_unfollowers(self):

        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()

        time.sleep(2)
        
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()

        time.sleep(2)

        following = self.get_names()

        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        
        followers = self.get_names()

        not_following_back = [user for user in following if user not in followers]
        
        print(not_following_back)

    
    

    
    def get_names(self):
        
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        
        time.sleep(1)
        
        t = 1

        timeout = time.time() + 30
        while t==1:    
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_box)
            time.sleep(0.5)
            if time.time() > timeout:
                break
            
        links = scroll_box.find_elements_by_tag_name('a')
        
        names = [name.text for name in links if name.text != '']
        
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")\
            .click()
        
        return names


        
        

if __name__ == '__main__':
    ig_bot = InstagramBot( username, password)
# pass in your login credentials in the ig_bot variable
    






