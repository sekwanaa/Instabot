#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as ChromeService
from time import sleep
from random import randint
import sys

#also using chromedriver, but you can use anything
def main():
    chromedriver_path = "<your driver path>"
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
        sys.exit("Couldn't find first not now button")

    sleep(5)

    notnow2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
    notnow2.click()

    try:
        i = 100
        #should cap unfollow at 100 max
        if i <= 0:
            sys.exit("Reached unfollow limit")
        while i > 0:
            i -= 1
            #go to profile page with who you are following
            driver.get('https://www.instagram.com/chinkoman88rules/following/')

            sleep(randint(22,28))

            #click following button
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div/div[3]/button').click()

            sleep(5)

            #click unfollow
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]').click()

            sleep(randint(5,8))
    except:
        sys.exit("Couldn't unfollow")

if __name__ == '__main__':
    main()
