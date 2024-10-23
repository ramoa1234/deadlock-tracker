import requests, json, os

#ONLY HANDLES CREATING CHARACTER OBJECT NOT ANY DATA ABOUT THE CHARACTERS
#needs a function to handle adding new ones and sort not in game

# popular items = schema with item winrate and pick rates
def character_schema(name, description, images, abilitys, popular_items):
    
    name = {
        'name': name,
        'description': description.lore,
        'winrate': 0,
        'role': description.lore,
        'role': description.role,
        'images': images,
        'abilitys': abliltys,
        'popular_items': popular_items
    }
    return name

url = 'https://assets.deadlock-api.com/v2/heroes'
def get_names(url):
    response = requests.get(url)
    data = response.json()
    parsed_names = [{"id": item["id"], "name": item["name"]} for item in data]
    print(parsed_names)        
    return parsed_names




character_count = get_names()
#get all chacter info and store it in the database
def characters_db():
        for id in character_names:
            url =f'https://assets.deadlock-api.com/v2/heroes/{id}'
            response = requests.get(url)
            if response.status_code == 200:
                data = respons.json()
            
            else:
                print(f'error {response.status_code}')