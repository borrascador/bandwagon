# install the Python Requests library:
# `pip install requests`

import base64
import requests
import json

from secret import *

def save_data_to_file():
    data = send_request()
    best_streak = max(data, key=lambda x: x["streak"])
    most_wins = max(data, key=lambda x: x["wins"])
    stats = {"best_streak": best_streak, "most_wins": most_wins}
    filename = "stats.json"
    with open(filename, 'w') as outfile:
        json.dump(stats, outfile)
    print("Wrote data to " + filename)

def send_request():
    # TODO: store running tally of relevant stats
    # TODO: only request data that is not already stored
    
    pull_url = r"https://api.mysportsfeeds.com/v1.1/pull/nba/2017-2018-regular/team_gamelogs.json"
    
    teams = [
        'HOU', 'UTA', 'LAC', 'ATL', 'CHI', 'LAL', 
        'CLE', 'NOP', 'DEN', 'SAS', 'NYK', 'DET',
        'DAL', 'WAS', 'MIA', 'BOS', 'POR', 'MIN',
        'BRO', 'ORL', 'CHA', 'GSW', 'MIL', 'IND',
        'PHX', 'SAC', 'TOR', 'PHI', 'MEM', 'OKL'
    ]
    
    league_summary = []
    
    for team in teams:
        try:
            response = requests.get(
                url = pull_url,
                params = {
                    "team": team
                },
                headers = {
                    "Authorization": "Basic " + base64.b64encode('{}:{}'.format(USERNAME,PASSWORD).encode('utf-8')).decode('ascii')
                }
            )
            print('Response HTTP Status Code: {status_code}, Loaded {count}/{total} Teams'.format(
                status_code = response.status_code,
                count = len(league_summary) + 1,
                total = len(teams)
            ), end="\r")
            json_data = json.loads(response.text)
            league_summary.append({
                "team": team,
                "name": json_data['teamgamelogs']['gamelogs'][0]['team']['Name'],
                "wins": get_win_total(json_data),
                "streak": get_current_streak(json_data)
            })
        except requests.exceptions.RequestException: 
            print('HTTP Request failed')
            
    print("\nRequest Complete")
    return league_summary

def get_win_total(json_data):
    wins = 0
    for gamelog in json_data['teamgamelogs']['gamelogs']:
        if gamelog['stats']['Wins']['#text'] == '1':
            wins += 1
    return wins

def get_current_streak(json_data):
    streak = 0
    for gamelog in json_data['teamgamelogs']['gamelogs']:
        if gamelog['stats']['Wins']['#text'] == '1':
            streak += 1
        else:
            streak = 0
    return streak

if __name__ == '__main__':
    save_data_to_file()
