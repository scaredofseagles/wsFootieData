from bs4 import BeautifulSoup
from time import sleep
import requests
from urllib.request import urlopen
import os
import json

def read_team_file():
    with open('data/teams.json', 'r') as read_file:
      return json.load(read_file)

def read_soup(path="/wiki/FA_Women%27s_Super_League"):
    url = "https://en.wikipedia.org{}".format(path)
    html = urlopen(url)
    return BeautifulSoup(html, 'html.parser')

def write_to_file(data):
    with open('data/players.json', 'w') as write_file:
      json.dump(data, write_file, ensure_ascii=False)

def get_players(teams):
    players = []
    for team in teams:
        soup = read_soup(team["href"])
        sleep(2)
        print("Adding Team: %s" % team["name"])
        player_data_arr = soup.find_all('tr', class_="vcard")
        for data in player_data_arr:
            player_data = data.find_all('td')
            players.append({
                "name" : {
                    "first_name":  player_data[3].find('a')["title"].split(" ")[0] if bool(player_data[3].find('a')) else player_data[3].find('span').string.split(" ")[0],
                    "last_name": player_data[3].find('a')["title"].split(" ")[1] if bool(player_data[3].find('a')) else player_data[3].find('span').string.split(" ")[1]
                },
                "team": {
                    "team_name": team["name"]
                },
                "position": player_data[1].find('abbr')["title"],
                "jersey_number": player_data[0].string.replace("\n", ""),
                "country": player_data[2].find("img")["alt"]
            })

    return players

def main():
    try:
        teams = read_team_file()
        players = get_players(teams)
        write_to_file(players)
    except KeyboardInterrupt:
            exit()

main()
