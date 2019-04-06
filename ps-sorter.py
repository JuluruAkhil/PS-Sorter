from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import csv
import sys

def Sorter():
	line_count=0
	with open('PS1.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			if line_count == 0:
				line_count += 1
			else:
				pointer_mover="""//span[contains(text(), "{}")]/ancestor::li[contains(@class,'col-sm-12 item-blue clearfix ui-state-default')]""".format(row[0])
				draggable=driver.find_element_by_xpath(pointer_mover)
				droppable=driver.find_element_by_xpath("""//*[@id="sortable_nav"]/li[312]""")
				ActionChains(driver).click_and_hold(draggable).move_by_offset(-1,-1).move_to_element(droppable).move_by_offset(-1,-1).pause(1).release().perform()
				line_count += 1
			driver.execute_script("scroll(0, 0);")

def Clicker():
	with open('PS1.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			if (row[1] == "1"):
				pointer_selector="""//span[contains(text(), "{}")]/ancestor::li[contains(@class,'col-sm-12 item-blue clearfix ui-state-default')]/input[@name='accomoPreference']""".format(row[0])
				driver.find_element_by_xpath(pointer_selector).click()
			driver.execute_script("scroll(0, 0);")

email=sys.argv[1]
password=sys.argv[2]
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.get('http://psd.bits-pilani.ac.in/Login.aspx')
time.sleep(1)
driver.find_element_by_xpath("""//*[@id="TxtEmail"]""").send_keys(email)
driver.find_element_by_xpath("""//*[@id="txtPass"]""").send_keys(password)
driver.find_element_by_xpath("""//*[@id="login-box"]/div/div[1]/fieldset/div[2]/label/input""").click()
driver.find_element_by_xpath("""//*[@id="Button1"]""").click()
driver.get("http://psd.bits-pilani.ac.in/Student/StudentStationPreference.aspx")
time.sleep(2)

Sorter()

Clicker()

print("Please sort these stations yourself (Finance and Mgmt-AP Govt Mee Seva, Vijayawada, Mechanical-Lumax Auto Technologies Limited, Gurgaon)")
print("Stations sorted. PLEASE CHECK TWICE FOR ANY DISCREPANCIES BEFORE SUBMITTING!!!!!!!!!")
