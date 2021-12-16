# wsFootie App API

## The Plan

- Sort through .json files in data/ folder for NWSL data (if not FAWSL)

- Will need to write program to watch for changes to repo

- Will need to store player, team, and competition data in DB

  - can store data as JSON on Github (or cdn??)

  - Can get base info scraping from wikipedia
    - league, teams, players (name, pos, number, country), coaching staff

- Game and gameday data will need to be temporarily stored (but where??)

  - redis or memcached

- How to determine player value?

  - Form (range of [very bad, bad, ok, good, very good, superb])
  - Fixture difficulty
  - Availability
  - Home/Away

- Will need to save team id but how to check if lineups are recent??

  - might use team name

- Will need table standings (maybe)

+++++++++++++++++++++++++++++++++++++++++++++++

- Save players and team data in json file that will be stored here on Github
  - Data will rarely change (probably only during transfer windows and new seasons)
  - maybe add a admin table on client that can change json files
