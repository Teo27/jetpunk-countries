from __future__ import division
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# import requests as req


def guess_countries():

    sleep_time = 1000

    with open('countries.json') as json_data:
        countries = json.load(json_data)

    url_game = 'https://www.jetpunk.com/quizzes/how-many-countries-can-you-name'

    driver = webdriver.Chrome(executable_path='./chromedriver')

    driver.get(url_game)

    inputElement = driver.find_element_by_id('start-button')
    inputElement.click()
    inputElement = driver.find_element_by_id('txt-answer-box')

    for cnt in countries:
        inputElement.send_keys(cnt['name'])
        inputElement.send_keys(Keys.ENTER)
        if(driver.find_element_by_id('already-guessed').text == ('Not a correct answer' or 'Already guessed!')):
            print(cnt['name'])
            inputElement.clear()
            continue

    inputElement.send_keys(Keys.ENTER)
    time.sleep(sleep_time)

    driver.close()

    return 1


if __name__ == '__main__':
    guess_countries()
