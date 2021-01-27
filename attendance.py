from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import sys
import argparse
import json


def parse_users(usersFile):
    users = []
    with open(usersFile) as f:
        users = json.load(f)
    return users


def start_automation(users):
    driver = webdriver.Chrome(
        "C:/Users/aswin/auto-attendance/chromedriver.exe")

    while 1:
        for user in users:
            driver.get("http://moodle.mec.ac.in")
            username_ip = driver.find_element_by_name("username")
            username_ip.clear()
            username_ip.send_keys(user['email'])
            pass_ip = driver.find_element_by_name("password")
            pass_ip.clear()
            pass_ip.send_keys(user['password'])
            pass_ip.send_keys(Keys.RETURN)

            if not driver.current_url == "http://moodle.mec.ac.in/my/":
                print("Failed to log in")
                sys.exit(1)

            for course in user['courses']:
                driver.get(course)
                course_name_tag = driver.find_elements_by_xpath("//h1")[0]
                course_name = course_name_tag.text
                submit_attendance_btns = driver.find_elements_by_xpath(
                    "//*[contains(text(), 'Submit attendance')]")
                if len(submit_attendance_btns) == 0:
                    continue
                submit_attendance_btn = submit_attendance_btns[0]
                print("Marking " + user['email'] +
                      "'s attendance for " + course_name)
                att_link = submit_attendance_btn.get_attribute("href")
                driver.get(att_link)
                status_btn = driver.find_elements_by_xpath(
                    "//input[@type='radio']")[0]
                status_btn.click()
                driver.find_element_by_id("id_submitbutton").click()
                print("Done")

            driver.get("http://moodle.mec.ac.in/login/logout.php")
            continue_btns = driver.find_elements_by_xpath(
                "//*[contains(text(), 'Continue')]")
            if len(continue_btns) == 0:
                continue
            continue_btn = continue_btns[0]
            continue_btn.click()
        time.sleep(20 * 60)


def create_arg_parser():
    # Creates and returns the ArgumentParser object

    parser = argparse.ArgumentParser(
        description='Automate your moodle attendance.')
    parser.add_argument('--usersFile',
                        help='Path to the JSON file that contains the credentials & courses of the user accounts for which automation is to be done.')
    return parser


if __name__ == "__main__":
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    if not os.path.exists(parsed_args.usersFile):
        print("Credentials file not found")
        sys.exit(1)
    users = parse_users(parsed_args.usersFile)
    start_automation(users)
