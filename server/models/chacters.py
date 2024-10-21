import requests, json, os

# Create and get items

url = 'https://assets.deadlock-api.com/v2/heroes'
popular_items = []
ability_order = []


def get_characters():
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()  
        print(data)  
    else:
        print(f"Error: {response.text}") 

get_characters()