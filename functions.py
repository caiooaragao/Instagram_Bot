from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time


class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(5)
        user_element = driver.find_element("xpath",
                                           "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element("xpath",
                                               "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        login_button = driver.find_element("xpath",
                                           '//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()
        time.sleep(3)
        driver.implicitly_wait(20)
        agora_nao_button = driver.find_element(
            "xpath", '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button')
        driver.implicitly_wait(20)
        agora_nao_button.click()
        driver.implicitly_wait(10)
        notificacao = driver.find_element(
            "xpath", "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
        notificacao.click()
        driver.implicitly_wait(3)

    def seguir_target(self, nome):
        driver = self.driver
        driver.get("https://www.instagram.com/{}/".format(nome))
        driver.implicitly_wait(10)
        followers = driver.find_element(
            "xpath", "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")
        driver.implicitly_wait(10)
        followers.click()
        driver.implicitly_wait(5)
        new_users = []
        driver.implicitly_wait(10)
        #last_heigt = driver.execute_script("return document.body.scrollHeight")
        for _ in range(1, 3):
            driver.execute_script(
                "let rolagem = documents.getElementsByClassName('._acan _acap _acas');  rolagem.scrollBy(0,180);")
            time.sleep(2)


caiobot = InstaBot('mymeme0x@gmail.com', 'mymeme123!')
caiobot.login()
time.sleep(10)
caiobot.seguir_target('9gag')
while True:
    sair = input("quer sair?")
    if sair in 'Ss':
        break
# //*[@id="mount_0_0_iS"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button
# login XPATH: //*[@id="loginForm"]/div/div[1]/div/label/input
# //input[@name='username']


# PASSWORD XPATH: //*[@id="loginForm"]/div/div[2]/div/label/input
# //input[@name='password']

# BOTAO LOGIN XPATH:  //*[@id="loginForm"]/div/div[3]/button
