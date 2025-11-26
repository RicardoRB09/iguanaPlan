import yaml, os, requests
from utils import open_config_file


open_cage_base_url = "https://api.opencagedata.com/geocode/v1/json"


def get_city_lat_long(city):
    config = open_config_file()
    if not config:
        return None
    
    api_key = config['open_cage']['api_key']
    
    url = f'{open_cage_base_url}?q={city}&key={api_key}&language=en&no_annotations=1&pretty=1'
    
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f'🚨 Error: {response.status_code}')
        return None
    
    data = response.json()
    
    if not data:
        print("⚠️ No data returned for the given city.")
        return None
    
    if data['results']:
        return data['results'][0]['geometry']
    
    return []
    
    
        

