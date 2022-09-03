#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as ChromeService
from time import sleep
from random import randint
import pandas as pd
import os.path
import sys

#I am using chromedriver for this example since it works best, but you can use whatever driver you wish. 
def main():
    chromedriver_path = "<your driver directory>"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    service = ChromeService(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)

    sleep(2)

    driver.get('https://www.instagram.com/accounts/login/')

    sleep(5)

    username = driver.find_element(By.NAME, "username")
    username.send_keys('your username')
    password = driver.find_element(By.NAME, 'password')
    password.send_keys('your password')

    sleep(5)

    button_login = driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(3)')
    button_login.click()

    sleep(5)

    try:
        notnow = driver.find_element(By.CSS_SELECTOR, '#react-root > section > main > div > div > div > div > button')
        notnow.click()
    except:
        sys.exit(1)

    sleep(5)

    notnow2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
    notnow2.click()
    
    #feel free to put whatever hastags you wish
    hashtag_list = ['travelblog', 'travelblogger', 'traveler', 'travelphotography', 'europetravel', 'landscapephotography', 'portraitphotography', 'sonyphotography', 'moodyphotography']

    prev_user_list = [] #- if it's the first time you run it, use this line and comment the two below
    if os.path.isfile('users_followed_list.csv'):
        with open('users_followed_list.csv') as f:
            for user in f:
                prev_user_list.append(user)
    else:
        with open('users_followed_list.csv', 'w+') as f:
            for user in f:
                prev_user_list.append(user)

    new_followed = []
    tag = -1
    followed = 0

    for hashtag in hashtag_list:
        tag += 1
        driver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
        
        sleep(5)
        
        first_thumbnail = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
        first_thumbnail.click()

        sleep(randint(3,6))    
        
        try:  
            followed_in_tag = 0      
            for x in range(1,200):
                username = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/h2/div/span/a').text
                if username not in prev_user_list:
                    #should cap us at 100 follows per hastag
                    if followed_in_tag >= 10:
                        continue
                    while followed_in_tag < 10 or followed < 10:
                        try:
                            # If we already follow, do not unfollow
                            if driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div/div').text == 'Follow':
                                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div/div').click()
                                
                                new_followed.append(username)
                                followed += 1
                                followed_in_tag += 1

                                sleep(randint(7, 15))

                                # Next picture
                                try:
                                    next_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button')
                                    next_button.click()
                                    sleep(randint(7,15))
                                except:
                                    next_button1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button')
                                    next_button1.click()
                                    sleep(randint(7,15))
                            else:
                                try:
                                    next_button2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button')
                                    next_button2.click()
                                    sleep(randint(7,15))
                                except:
                                    next_button3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button')
                                    next_button3.click()
                                    sleep(randint(7,15))
                        except:
                            try:
                                next_button2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button')
                                next_button2.click()
                                sleep(randint(7,15))
                            except:
                                next_button3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button')
                                next_button3.click()
                                sleep(randint(7,15))
                else:
                    next_button5 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button')
                    next_button5.click()
                    sleep(randint(7,15))
            # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
        except:
            continue

    for n in range(0,len(new_followed)):
        prev_user_list.append(new_followed[n])
        
    updated_user_df = pd.DataFrame(prev_user_list)
    updated_user_df.to_csv('users_followed_list.csv')
    print('Followed {} new people.'.format(followed))

if __name__ == '__main__':
    main()
