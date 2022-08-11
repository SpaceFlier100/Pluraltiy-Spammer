from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
botint = 0
delay = 10
options = Options()
othersurv = "/html/body/div[1]/div[2]/main/section/div/a[1]/div/div"
#options.add_argument("--window-size=1920,1080")
#options.add_argument("--start-maximized")
#options.add_argument("--headless")
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
    email.send_keys("spamserver" + botstr + "@gmail.com")
    print(botstr)
    password.send_keys("12345678")
    verify.send_keys("12345678")
    button.click()
    buttonpath = "/html/body/div[1]/div[2]/main/section[4]/div/div[2]/a[1]/button"
    WebDriverWait(driver, delay).until(ec.presence_of_element_located((By.XPATH, buttonpath)))
    respond = driver.find_element(By.XPATH, buttonpath)
    respond.click()

    def nextsurv():

        WebDriverWait(driver, delay).until(ec.presence_of_element_located((By.NAME, "vote")))
        WebDriverWait(driver, delay).until(ec.presence_of_element_located((By.NAME, "_action")))
        ans = driver.find_element(By.NAME, "vote")
        enterans = driver.find_element(By.NAME, "_action")
        ans.send_keys("yourmum")
        enterans.click()
        WebDriverWait(driver, delay).until(ec.presence_of_element_located((By.XPATH, othersurv)))
        clickothersurv = driver.find_element(By.XPATH, othersurv)
        clickothersurv.click()

    time.sleep(100000)
    driver.delete_cookie("plurality.fun")
    driver.close()