from selenium import webdriver
import time
"""
In this file the aprroach is to use Selenim Library.
We inspect from the https://my.edu.sharif.edu which courses we want to click 
and then using their xpath's indices we will click on  them.
It worth mentioning that we must sleep for 170 miliseconds in order to not get
recognizedd as a bot.
Furthermore, we need to install and feed the correct version of ChromeDriver if you use chrome 
and feed the address to the script
"""
index = [75, 59, 53, 4, 64]
path = "entekhabVahed\chromedriver.exe"
browser = webdriver.Chrome(path)
browser.get("https://my.edu.sharif.edu/")
mmd = ''
while mmd == '':
    try:
        mmd = browser.find_element("xpath",'//*[@id="root"]/div/div/div/form/div/div[3]/div/input')
    except:
        continue

STUDENT_ID = "400101204"
PASSCODE = "123456789"
# LOGGING INTO THE WEBSITE
browser.find_element("xpath",'//*[@id="root"]/div/div/div/form/div/div[3]/div/input').send_keys(STUDENT_ID)
browser.find_element("xpath",'/html/body/div/div/div/div/form/div/div[4]/div/input').send_keys(PASSCODE)
time.sleep(6)
browser.find_element("xpath",'/html/body/div/div/div/div/form/div/button').click()

# CLICKING THE COURSES ...
mmdd = ""
admission_url = '/html/body/div[2]/div/div[3]/button[2]'
while mmdd == "":
    try:
        mmdd = browser.find_element("xpath",'/html/body/div/div/div[2]/table/tbody/tr[1]/td[1]/button[1]')
    except:
        pass 
for i in index:
    xp = '/html/body/div/div/div[2]/table/tbody/tr['+str(i)+']/td[1]/button[1]'
    browser.find_element("xpath",xp).click()
    temp = browser.find_element("xpath",admission_url)
    temp.click()
    time.sleep(0.17)


#browser.close()
