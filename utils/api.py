import requests

def search_city(city_name):
    url = f"https://search.reservamos.mx/api/v2/places?q={city_name}&result_type=city"
    response = requests.get(url)
    print(f"Request URL: {url}")
    print(f"Response Status Code: {response.status_code}")
    if response.status_code in [200, 201]:
        print(f"Response JSON: {response.json()}")
        return response.json()[0]
    else:
        print("Failed to retrieve data")
        return None