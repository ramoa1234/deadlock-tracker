import requests
from pymongo import MongoClient

search_active_matches = "https://data.deadlock-api.com/v1/active-matches"
#url = "https://analytics.deadlock-api.com/v1/matches/search" also all active matches



headers = {
    "api_key": "HEXE-2eee2244-c350-487c-99f7-983a9ba02fc2",  
    "Content-Type": "application/json"
}


def send_to_db(match_id):
    url = 'mongodb://localhost:27017/deadlock/active_game_ids'



def get_active_matches():
    response = requests.get(search_active_matches, headers=headers)


    if response.status_code == 200:
        data = response.json()  # Parse the JSON response

        # Print the data in a readable format
        for match in data:
            match_id = match.get('match_id')  # Use get to avoid KeyError
            

    else:
        print(f"Error: {response.status_code} - {response.text}")
