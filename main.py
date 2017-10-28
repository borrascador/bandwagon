# install the Python Requests library:
# `pip install requests`

import base64
import requests
import json

def send_request():
    pull_url = r"https://api.mysportsfeeds.com/v1.1/pull/nba/2017-2018-regular/scoreboard.json"

    try:
        response = requests.get(
            url=pull_url,
            params={
                "fordate": "20171017"
            },
            headers={
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format("borrascador","temporary").encode('utf-8')).decode('ascii')
            }
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        json_data = json.loads(response.text)
        print(json.dumps(json_data, indent=4))
    except requests.exceptions.RequestException: 
        print('HTTP Request failed')

send_request()
