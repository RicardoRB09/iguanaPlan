import requests, json

holidays = []

api_colombia_base_path_url = 'https://image.tmdb.org/t/p/w200'


def get_holidays_by_year(year):
  

    url = f"https://api-colombia.com/api/v1/Holiday/year/{year}"
    
    
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = json.loads(response.content.decode('utf-8'))
        
        return data
    
    except requests.exceptions.HTTPError as http_error:
        if response.status_code == 404:
            print("❌ Error: The requested resource was not found.")
        elif response.status_code == 500:
            print("❌ Error: Internal server error.")
        else:
            print(f"❌ HTTP error occurred: {http_error}")
        
    except requests.exceptions.RequestException as req_error:
        print(f"❌ Network error: {req_error}")
        
    except json.JSONDecodeError as json_error:
        print(f"❌ Failed to decode JSON: {json_error}")
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        
        return []



 
