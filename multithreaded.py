from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import threading
import time
delay = 10
options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument('--headless')
def bot():
    prefix = pre
    botint = 27
    while True:
        botint = botint+1
        botstr = str(botint)
        driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        driver.minimize_window()
        driver.get("https://plurality.fun/user/signup")
        try:
            email = driver.find_element(By.NAME, "email")
        except:
            driver.get("https://plurality.fun/user/signup")
            email = driver.find_element(By.NAME, "email")
        password = driver.find_element(By.NAME, "password")
        verify = driver.find_element(By.NAME, "verify")
        button = driver.find_element(By.XPATH, "/html/body/div/main/section[1]/article[1]/form/button")
        email.send_keys("testemail" + prefix + botstr + "@gmail.com")
        print(botstr)
        password.send_keys("12345678")
        verify.send_keys("12345678")
        button.click()
        buttonpath = "/html/body/div[1]/div[2]/main/section[4]/div/div[2]/a[1]/button"
        WebDriverWait(driver, delay).until(ec.presence_of_element_located((By.XPATH, buttonpath)))
        respond = driver.find_element(By.XPATH, buttonpath)
        respond.click()
        WebDriverWait(driver, delay).until(ec.presence_of_element_located((By.NAME, "vote")))
        WebDriverWait(driver, delay).until(ec.presence_of_element_located((By.NAME, "_action")))
        ans = driver.find_element(By.NAME, "vote")
        enterans = driver.find_element(By.NAME, "_action")
        ans.send_keys("yourmum")
        enterans.click()
        othersurv = "/html/body/div[1]/div[2]/main/section/div/a[1]/div/div"
        WebDriverWait(driver, delay).until(ec.presence_of_element_located((By.XPATH, othersurv)))
        driver.delete_cookie("plurality.fun")
        driver.close()


t1 = threading.Thread(target=bot)
t2 = threading.Thread(target=bot)
t3 = threading.Thread(target=bot)
t4 = threading.Thread(target=bot)
t5 = threading.Thread(target=bot)
t6 = threading.Thread(target=bot)



pre = "t1"
t1.start()
time.sleep(0.5)
pre = "t2"
t2.start()
time.sleep(0.5)
pre = "t3"
t3.start()
time.sleep(0.5)
pre = "t4"
t4.start()
time.sleep(0.5)
pre = "t1"
t5.start()
time.sleep(0.5)
pre = "t2"
t6.start()
