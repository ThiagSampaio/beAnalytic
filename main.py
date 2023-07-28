import requests
import pandas as pd

# The API endpoint
url = "http://api.steampowered.com/ISteamApps/GetAppList/v0001/"

# A GET request to the API
response = requests.get(url)

# Print the response
response_json = response.json()

new_data = response_json['applist']['apps']['app']

teste = pd.json_normalize(new_data)
print(type(teste))
