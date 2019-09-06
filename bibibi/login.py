from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome()
browser.maximize_window()#将浏览器最大化
wait = WebDriverWait(browser, 10)
def login():
    try:
        userInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#web-content > div > div > div > div.position-rel.container.company_container > div > div.in-block.vertical-top.float-right.right_content.mt50.mr5.mb5 > div.module.module1.module2.loginmodule.collapse.in > div.modulein.modulein1.mobile_box.pl30.pr30.f14.collapse.in > div.pb30.position-rel > input')))
        passwordInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#web-content > div > div > div > div.position-rel.container.company_container > div > div.in-block.vertical-top.float-right.right_content.mt50.mr5.mb5 > div.module.module1.module2.loginmodule.collapse.in > div.modulein.modulein1.mobile_box.pl30.pr30.f14.collapse.in > div.pb40.position-rel > input')))
        userInput.send_keys('*************')#账号
        passwordInput.send_keys('**********')#密码
        changeLoginWay = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#web-content > div > div > div > div.position-rel.container.company_container > div > div.in-block.vertical-top.float-right.right_content.mt50.mr5.mb5 > div.module.module1.module2.loginmodule.collapse.in > div.modulein.modulein1.mobile_box.pl30.pr30.f14.collapse.in > div.c-white.b-c9.pt8.f18.text-center.login_btn')))
        changeLoginWay.click()
    except TimeoutException:
        login()
