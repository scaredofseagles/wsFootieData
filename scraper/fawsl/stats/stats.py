import json
import os
import pandas as pd
from datetime import datetime

# setup file paths
todays_date = datetime.today().strftime('%Y_%m_%d')
team_title = "team_standings_{}.json".format(todays_date)
player_title = "player_standings_{}.json".format(todays_date)

base_dir = os.path.join("..", "..", "..");
team_path = os.path.join(base_dir, "data", "team_standings", team_title)
player_path = os.path.join(base_dir, "data", "player_standings", player_title)

# check if file already exists
if not os.path.exists(team_path):
    print("Scraping Team Stats")
    # scrape team stats
    url_squad_stats = f"https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F189%2Fstats%2FWomens-Super-League-Stats&div=div_stats_squads_standard_for"
    df_squad_stats = pd.read_html(url_squad_stats, header=1)[0]
    # save to file
    df_squad_stats.to_json(team_path, orient="records")

if not os.path.exists(player_path):
    print("Scraping Player Stats")
    # scrape player stats
    url_player_stats = f"https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F189%2Fstats%2FWomens-Super-League-Stats&div=div_stats_standard"
    df_player_stats = pd.read_html(url_player_stats, header=1)[0]
    # save to file
    df_player_stats.to_json(player_path, orient="records")
