from bs4 import BeautifulSoup
from time import sleep
import requests
from urllib.request import urlopen
import os
import json

def read_soup(path="/wiki/FA_Women%27s_Super_League"):
    url = "https://en.wikipedia.org{}".format(path)
    html = urlopen(url)
    return BeautifulSoup(html, 'html.parser')

def get_teams(soup):
    teams_table = soup.find_all(class_="sortable")[0]
    teams_body = teams_table.find('tbody')

    teams = []

    for team in teams_body.find_all('tr'):
        team_data = team.find_all('a')
        if bool(team_data) != False:
            teams.append({
                "href": team_data[0]["href"],
                "name": team_data[0]["title"],
                "location": team_data[1]["title"],
                "stadium": team_data[2]["title"]
            })

    return teams

def get_manager_data(teams):
    # loop through teams to get head coach
    i = 0
    for team in teams:
        sleep(2)
        soup = read_soup(team["href"])
        coach_data = soup.find_all(class_="wikitable")[4]
        coach_data_arr = coach_data.find_all('a')
        teams[i]["head_coach"] = {
            "country": coach_data_arr[0]["title"],
            "first_name": coach_data_arr[1]["title"].split(" ")[0],
            "last_name": coach_data_arr[1]["title"].split(" ")[1]
        }
        i+=1

def write_to_file(data):
    with open('data/teams.json', 'a') as write_file:
      json.dump(data, write_file, ensure_ascii=False)

def main():
    soup = read_soup()
    teams = get_teams(soup)
    # get_manager_data(teams)
    write_to_file(teams)
    # print(teams)

main()
