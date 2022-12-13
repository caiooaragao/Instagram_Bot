from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import time
from bs4 import BeautifulSoup
import requests
from termcolor import colored


class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def login(self):
        try:
            randomNumber = randint(1, 4)
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
            time.sleep(10)
            notificacao = driver.find_element(
                By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
            time.sleep(6)
            notificacao.click()
        except:
            driver.close()

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

    def curtir_fotos_porHashTag(self, hashtag, numeroDeLikes):
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
        print('PIC HREFS:    ', pic_hrefs)
        # ir de link por link dando like
        for i in range(10, numeroDeLikes+10):
            driver.get(pic_hrefs[i])
            time.sleep(1.5)
            try:
                driver.find_element(By.CLASS_NAME, '_aamw').click()
                print(colored('foto curtida', 'green'))
                time.sleep(2)

            except:
                time.sleep(1)
                print('could not locate like button :(')

    def scrape_photos(self, target):
        driver = self.driver
        driver.get('https://www.instagram.com/{}/'.format(target))
        time.sleep(2)
        for i in range(1, 3):
            # dar scroll 3 vezes nas publicaçoes da hashtag
            driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(3)
        time.sleep(2)
        images = driver.find_elements(
            By.TAG_NAME, 'img')

        for image in images:
            x = image.get_attribute('src')
            print(x)

        print('='*50)
        time.sleep(5)
        print(images)

        print('='*50)

        '''for image in images:
            image_src = image.get_attribute('href')
            image_list.append(image_src)
            time.sleep(0.5)'''

        '''for image in image_list:
            wget.download(
                image_list, '/Users/caioaragao/Documents/vscode/python/instaBot/downloaded_images')'''

        print('download concluido')

    def cancelar_seguidores():
        with open('arquivo.txt', "r") as arquivo:
            for line in arquivo:
                perfil = line

    def randomScript(self):
        # python script to download instagram image
        ''' ask user to input the instagram post url '''
        link = input("Enter Instagram Image URL: ")

        ''' 
        create a webdriver chrome object by passing the path of "chromedriver.exe" file.(do not include .exe in the path).
        '''
        driver = webdriver.Chrome('chromedriver')

        ''' Open the instagram post on your chrome browser'''
        driver.get(link)

        ''' Fetch the source file of the html page using BeautifulSoup'''
        soup = BeautifulSoup(driver.page_source, 'lxml')

        ''' Extract the url of the image from the source code'''
        img = soup.find('img', class_='FFVAD')
        img_url = img['src']

        '''Download the image via the url using the requests library'''
        r = requests.get(img_url)

        with open("instagram"+str(time.time())+".png", 'wb') as f:
            f.write(r.content)

        print('success')
