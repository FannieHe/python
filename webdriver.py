# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


LocalName = ('EN','ZH-CN','ZH-TW','JA','KO','FR','DE')
choose = int(raw_input("please select the localse:"))

if choose < 8:
	tempLocaleName = LocalName[choose-1]
	print 'Local Name is:', LocalName[choose-1]
else:
	print "invalied choose"

def getFirefoxProfile(tempLocaleName):
    profile = webdriver.FirefoxProfile()
    profile.set_preference('intl.accept_languages',tempLocaleName)
    profile.update_preferences()
    driver = webdriver.Firefox(profile)
    return driver


def getChromeProfile(tempLocaleName):
	chrome_options = Options()
	chrome_options.add_argument('-lang='+ tempLocaleName)
	chrome_options.add_argument('--ignore-certificate-errors')
	driver = webdriver.Chrome(chrome_options=chrome_options)
	return driver

def getIeProfile():
	iedriver = "C:\Program Files\Internet Explorer\IEDriverServer.exe"
	os.environ["webdriver.ie.driver"] = iedriver
	driver = webdriver.Ie(iedriver)
	return driver
'''def createIEProfile(tempLocaleName,desiredCapabilities):
	preferenceRegisterNode = "Locale"
	customRegisterKey = "HKCU\\SOFTWARE\\Microsoft\\Internet Explorer\\International"
	registerEntry = "AcceptLanguage"
	registerValue = tempLocaleName'''


driver = getFirefoxProfile(tempLocaleName)
driver.get('https://10.10.32.156')
#driver.find_element_by_xpath("//a[@id='overridelink']").click() #application menu icon.
driver.maximize_window()
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys('admin')
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys('1qaz@WSX')
driver.find_element_by_xpath("//*[@id='login-button']").click()

