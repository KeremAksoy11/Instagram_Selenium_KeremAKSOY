from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
from faker import Faker
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import locale
locale.setlocale(locale.LC_ALL, 'turkish')


driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.instagram.com/?hl=tr"
driver.get(url)
time.sleep(3)

kullaniciad1 = "kullanıcıadı"
password1 = "şifre"

kullaniciad = driver.find_element_by_name("username")
time.sleep(1)
kullaniciad.send_keys(kullaniciad1)
time.sleep(1)


sifre = driver.find_element_by_name("password")
time.sleep(1)
sifre.send_keys(password1)
time.sleep(3)

giris = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div").click()

time.sleep(3)


url1 = ("https://www.instagram.com/"+kullaniciad1)
driver.get(url1)
time.sleep(1)

TakipciGör = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
time.sleep(3)

takipciler = driver.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
scroll = 0
while scroll < 500: # scroll 5 times
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
    time.sleep(0)
    scroll += 1

# fList  = driver.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
# for i in fList:  
#     takipci = ("https://www.instagram.com/"+i.text)
#     print(takipci)
#     with open("instagramTakipciler.txt","a+",encoding="utf-8") as file:
#         file.write("\nBeni Takip Eden Hesaplar\n{}".format(takipci))

tarihsaat = datetime.datetime.now().strftime("%d %B %Y saat %H:%M:%S")
fList  = driver.find_elements_by_xpath("//div[@class='isgrP']//li")
for i in fList:
     takipci = ("https://www.instagram.com/"+i.text)
     print(takipci)
     with open("instagramTakipciler.txt","a+",encoding="utf-8") as file:
        file.write("\nBeni Takip Eden Hesap:\n{}\n Zaman Bilgisi: {}".format(takipci,tarihsaat))
# driver.quit()
driver.quit()  
