# install the Python Requests library:
# `pip install requests`

import base64
import requests
import json

from secret import *

def send_request():
    pull_url = r"https://api.mysportsfeeds.com/v1.1/pull/nba/2017-2018-regular/team_gamelogs.json"
    
    teams = [
            'HOU', 'UTA', 'LAC', 'ATL', 'CHI', 
            'LAL', 'CLE', 'NOP', 'DEN', 'SAS', 
            'NYK', 'DET', 'DAL', 'WAS', 'MIA', 
            'BOS', 'POR', 'MIN', 'BRO', 'ORL',
            'CHA', 'GSW', 'MIL', 'IND', 'PHX', 
            'SAC', 'TOR', 'PHI', 'MEM', 'OKL'
            ]

    streaks = {}
    
    for team in teams:
        try:
            response = requests.get(
                url=pull_url,
                params={
                    "team": team
                },
                headers={
                    "Authorization": "Basic " + base64.b64encode('{}:{}'.format(USERNAME,PASSWORD).encode('utf-8')).decode('ascii')
                }
            )
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            json_data = json.loads(response.text)
            streaks[team] = {
                    "wins": get_win_total(json_data),
                    "streak": get_current_streak(json_data)
                    }
        except requests.exceptions.RequestException: 
            print('HTTP Request failed')

    return streaks

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
    print(send_request())
