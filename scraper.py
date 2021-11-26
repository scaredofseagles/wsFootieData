from selenium import webdriver
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

def get_match_data(path=''):
    arr = []

    driver.get("{href}statsbomb/open-data/tree/master/data/matches/{path}".format(href=domain, path=path))
    sleep(2)
    elems = driver.find_elements(By.XPATH, "//a[@data-pjax='#repo-content-pjax-container']")
    for elem in elems:
        if (elem.get_attribute("title") != ""):
            arr.append(elem.get_attribute("title"))

    return arr

def read_raw_file(path, file):
    ''' pull json data from raw github file '''
    arr = []
    r = requests.get("{href}statsbomb/open-data/master/data/matches/{path}/{file}".format(href=raw_domain, path=path, file=file))

    data = r.json()

    for match in data:
        if match["competition"]["competition_id"] == 37:
            arr.append(match)

    return arr

def write_to_file(data):
    with open('data_file.json', 'a') as write_file:
      json.dump(data, write_file, ensure_ascii=False)

def close():
    return driver.close()

def main():
    titles_arr = get_match_data()
    # sleep(2)

    for title in titles_arr:
        files_arr=get_match_data(title)
        print("Title: %s" % title)
        for file in files_arr:
            print("File: %s" % file)
            matches = read_raw_file(title, file)
            if bool(len(matches)):
                write_to_file(matches)

    close()

main()


# with open('data_file.json', 'w') as write_file:
#   json.dump(r.json(), write_file, ensure_ascii=False)



#   "competition_name" : "FA Women's Super League",
#  "competition_id" : 37,
#  "season_id" : 90,
