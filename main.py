import requests

# The API endpoint
url = "http://api.steampowered.com/ISteamApps/GetAppList/v0001/"

# A GET request to the API
response = requests.get(url)

# Print the response
response_json = response.json()
print(response_json[0][0])