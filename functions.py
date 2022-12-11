from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import time


class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def login(self):
        # abrir instagram
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(5)
        # capturar local e escrever credenciais de login
        user_element = driver.find_element("xpath",
                                           "//input[@name='username']")
        user_element.clear()
        time.sleep(3)
        user_element.send_keys(self.username)
        password_element = driver.find_element("xpath",
                                               "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        # capturar e clicar login button
        login_button = driver.find_element("xpath",
                                           '//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()
        time.sleep(10)
        # sair de pop-ups do instagram
        agora_nao_button = driver.find_element(
            By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button')
        time.sleep(2)
        agora_nao_button.click()
        driver.implicitly_wait(10)
        notificacao = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
        time.sleep(5)
        notificacao.click()
        driver.implicitly_wait(3)

    def seguir_target(self, nome, numeroDeLikes):
        randomNumber = randint(1, 4)
        cont = 0
        # abrir target followers
        driver = self.driver
        driver.get("https://www.instagram.com/{}/followers/".format(nome))
        time.sleep(5)
        followedTargets = []
        # pressionar tab para descer a rolagem do pop-up
        actions = ActionChains(driver)
        followButtons = driver.find_elements(
            By.XPATH, "//button[contains(.,'Follow')]")
        for i in range(15 * numeroDeLikes):
            actions.send_keys(Keys.TAB)
            actions.perform()
            time.sleep(0.1)
        for btn in range(len(followButtons)):
            # Use the Java script to click on follow because after the scroll down the buttons will be un clickeable unless you go to it's location
            if followButtons[btn+1].text in 'Seguir' or 'Follow':
                driver.execute_script(
                    "arguments[0].click();", followButtons[btn+1])
                time.sleep(randomNumber)
                cont += 1
                print("followed...")
                if cont == numeroDeLikes:
                    break
            if followButtons[btn+1].text in 'Seguindo' or 'Following' or 'Remove' or 'Remover':
                print('allready following')
        print('you have followed:\n {}'.format(followedTargets))
        '''with open('PerfisSeguidos', 'a') as arquivo:
                    arquivo.write('seguindo o perfil: {}'.format(pic_hrefs[i]))
                    arquivo.close()'''

    def curtir_fotos_porHashTag(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
        time.sleep(5)
        # abrir hashtag e capturar link das imagens
        for i in range(1, 3):
            # dar scroll 3 vezes nas publicaçoes da hashtag
            driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(3)
        # colocar os links das imagens numa lista
        hrefs = driver.find_elements(By.TAG_NAME, 'a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' fotos: ' + str(len(pic_hrefs)))
        time.sleep(5)
        # ir de link por link dando like
        for i in range(10, 50):
            driver.get(pic_hrefs[i])
            time.sleep(1.5)
            try:
                driver.find_element(By.CLASS_NAME, '_aamw').click()
                time.sleep(2)
            except:
                time.sleep(1)
                print('could not locate like button :(')

    def cancelar_seguidores():
        with open('arquivo.txt', "r") as arquivo:
            for line in arquivo:
                perfil = line


caiobot = InstaBot('mymeme0x@gmail.com', 'mymeme123!')
caiobot.login()
caiobot.seguir_target('mymeme0x', 2)

while True:
    sair = input("quer sair?")
    if sair in 'Ss':
        break
