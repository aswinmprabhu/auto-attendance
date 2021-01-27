from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import sys

moodle_pass = "test"
moodle_mail = "test"

driver = webdriver.Chrome("C:/Users/aswin/auto-attendance/chromedriver.exe")
driver.get("http://moodle.mec.ac.in")
username_ip = driver.find_element_by_name("username")
username_ip.clear()
username_ip.send_keys(moodle_mail)
pass_ip = driver.find_element_by_name("password")
pass_ip.clear()
pass_ip.send_keys(moodle_pass)
pass_ip.send_keys(Keys.RETURN)

if not driver.current_url == "http://moodle.mec.ac.in/my/":
    print("Failed to log in")
    sys.exit(1)

courses = ["http://moodle.mec.ac.in/mod/attendance/view.php?id=685",
           "http://moodle.mec.ac.in/mod/attendance/view.php?id=353",
           "http://moodle.mec.ac.in/mod/attendance/view.php?id=557",
           "http://moodle.mec.ac.in/mod/attendance/view.php?id=425",
           "http://moodle.mec.ac.in/mod/attendance/view.php?id=1970",
           "http://moodle.mec.ac.in/mod/attendance/view.php?id=683",
           "http://moodle.mec.ac.in/mod/attendance/view.php?id=938"]

while 1:
    for course in courses:
        print(course)
        driver.get(course)
        submit_attendance_btns = driver.find_elements_by_xpath(
            "//*[contains(text(), 'Submit attendance')]")
        if len(submit_attendance_btns) == 0:
            continue
        submit_attendance_btn = submit_attendance_btns[0]
        print("Marking...")
        att_link = submit_attendance_btn.get_attribute("href")
        driver.get(att_link)
        status_btn = driver.find_elements_by_xpath("//input[@type='radio']")[0]
        status_btn.click()
        driver.find_element_by_id("id_submitbutton").click()
        print("Done")
    time.sleep(10 * 60)
