from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import sys
import argparse
import json


def parse_config(config_file):
    config = {}
    with open(config_file) as f:
        config = json.load(f)
    if "interval" not in config:
        config["interval"] = 20
    if "driver" not in config:
        print('"driver" field not found in config')
        sys.exit(1)
    if "users" not in config:
        print('"users" field not found in config')
        sys.exit(1)

    return config


def start_automation(users, driver):
    driver = webdriver.Chrome(driver)

    while 1:
        for user in users:
            driver.get("http://moodle.mec.ac.in")
            username_ip = driver.find_element_by_name("username")
            username_ip.clear()
            username_ip.send_keys(user["email"])
            pass_ip = driver.find_element_by_name("password")
            pass_ip.clear()
            pass_ip.send_keys(user["password"])
            pass_ip.send_keys(Keys.RETURN)

            if not driver.current_url == "http://moodle.mec.ac.in/my/":
                print("Failed to log in")
                sys.exit(1)

            for course in user["courses"]:
                driver.get(course)
                course_name_tag = driver.find_elements_by_xpath("//h1")[0]
                course_name = course_name_tag.text
                submit_attendance_btns = driver.find_elements_by_xpath(
                    "//*[contains(text(), 'Submit attendance')]"
                )
                if len(submit_attendance_btns) == 0:
                    continue
                submit_attendance_btn = submit_attendance_btns[0]
                print("Marking " + user["name"] + "'s attendance for " + course_name)
                att_link = submit_attendance_btn.get_attribute("href")
                driver.get(att_link)
                status_btn = driver.find_elements_by_xpath("//input[@type='radio']")[0]
                status_btn.click()
                driver.find_element_by_id("id_submitbutton").click()
                print("Done")

            driver.get("http://moodle.mec.ac.in/login/logout.php")
            continue_btns = driver.find_elements_by_xpath(
                "//*[contains(text(), 'Continue')]"
            )
            if len(continue_btns) == 0:
                continue
            continue_btn = continue_btns[0]
            continue_btn.click()
        time.sleep(10 * 60)


def create_arg_parser():
    # Creates and returns the ArgumentParser object

    parser = argparse.ArgumentParser(description="Automate your moodle attendance.")
    parser.add_argument("--config", help="Path to the JSON config file")
    return parser


if __name__ == "__main__":
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    if not os.path.exists(parsed_args.config):
        print("Config file not found")
        sys.exit(1)

    config = parse_config(parsed_args.config)
    users = config["users"]
    driver = config["driver"]
    start_automation(users, driver)
