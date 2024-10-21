import requests, os
from pymongo import MongoClient # type: ignore
from dotenv import load_dotenv  # type: ignore

load_dotenv()

search_active_matches = "https://data.deadlock-api.com/v1/active-matches"
#url = "https://analytics.deadlock-api.com/v1/matches/search" also all active matches


api_key = os.getenv('api_key')
headers = {
<<<<<<< HEAD
    "api_key": api_key,  
=======
    "api_key": "ENTER API KEY HERE",  
>>>>>>> 9c32e7101ad1fcdb3b99f7baea64fc40303efe62
    "Content-Type": "application/json"
}

connection_string = 'mongodb://localhost:27017/'
client = MongoClient(connection_string)
db = client["deadlock"]
active_game_ids_collection = db["active_game_ids"]

def check_db(match_id):
    value_exist = active_game_ids_collection.find_one({ "match_id": match_id })
    if value_exist:
        print('game still going on')
        return match_id
    else:
        active_game_ids_collection.insert_one( { "match_id": match_id })
        print('new game id added')



def get_active_matches(ongoing_games):
    response = requests.get(search_active_matches, headers=headers)
    

    if response.status_code == 200:
        data = response.json()  
        for match in data:
            match_id = match.get('match_id') 
            ongoing_games.append(check_db(match_id))
        
        return ongoing_games

    else:
        print(f"Error: {response.status_code} - {response.text}")


def look_up_results(finished_matches):
    #get winners characters, builds
    #database for items and characters, with relevant information imgs
    pass