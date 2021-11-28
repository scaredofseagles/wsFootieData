rom selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import requests
from time import sleep

domain = "https://github.com/"
raw_domain = "https://raw.githubusercontent.com/"

opts = Options()
opts.add_argument("--headless")

driver = webdriver.Chrome(options=opts)

def get_lineup_data(path=''):
    arr = []

    driver.get("{href}statsbomb/open-data/tree/master/data/lineups/{path}".format(href=domain, path=path))
    sleep(2)
    elems = driver.find_elements(By.XPATH, "//a[@data-pjax='#repo-content-pjax-container']")
    for elem in elems:
        if (elem.get_attribute("title") != ""):
            arr.append(elem.get_attribute("title"))

    return arr

def read_raw_file(file):
    ''' pull json data from raw github file '''
    arr = []
    r = requests.get("{href}statsbomb/open-data/master/data/lineups/{file}".format(href=raw_domain, file=file))

    data = r.json()

    for match in data:
        if match["competition"]["competition_id"] == 37 and match["season"]["season_id"] == 90:
            arr.append(match)

    return arr

def write_to_file(data):
    with open('lineups.json', 'a') as write_file:
      json.dump(data, write_file, ensure_ascii=False)

def close():
    return driver.close()

def main():
    files_arr = get_lineup_data()

    for file in files_arr:
        print("File: %s" % file)
        lineups = read_raw_file(file)
        if bool(len(lineups)):
            write_to_file(lineups)

    close()

main()
