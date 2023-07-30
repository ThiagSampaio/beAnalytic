import time
import pandas as pd
import requests
import json
import os
import threading

# applist":{"apps":{"app":[{

STEAM_ID_ENDPOINT = 'http://api.steampowered.com/ISteamApps/GetAppList/v0001/'

def get_all_app_ids_as_list(return_in_batches=True, batch_size=500):
    app_id_list = requests.get(STEAM_ID_ENDPOINT).json().get("applist").get("apps").get("app")
    if return_in_batches:
        app_id_list = [app_id_list[i:i + batch_size] for i in range(0, len(app_id_list), batch_size)] 
    return app_id_list

def get_app_data_by_id(app_ids_chunk, country_code="BR"):
    try:
        app_ids = ",".join([str(app.get("appid")) for app in app_ids_chunk])
        game_name_by_id = {str(e.get("appid")):e.get("name") for e in app_ids_chunk}
        STEAM_URL = f'http://store.steampowered.com/api/appdetails?appids={app_ids}&cc={country_code}&filters=price_overview'
        res = requests.get(STEAM_URL)
        return res.json(), game_name_by_id
    except Exception as e:
        print(f"Request status: {res.status_code}")
        

def format_and_extract_data(steam_data, lookup_name):

    total_data = []
    for k, v in steam_data.items():
        if isinstance(v.get("data"), list) or v.get("data") is None:
            # no info entry
            continue

        total_data.append( {
            'name': lookup_name.get(k),
            'id': k,
            'is_free': v.get("data").get("is_free"),
            'currency': v.get("data").get("price_overview", {}).get("currency", "FREE"),
            'initial_price': v.get("data").get("price_overview", {}).get("initial", 0.0),
            'final_price': v.get("data").get("price_overview", {}).get("final", 0.0),
            'discount_percent': v.get("data").get("price_overview", {}).get("discount_percent", 0)
        })
    return total_data
    

def download_data_to_local_file(app_id_list):

    all_data = []
    for app_id in app_id_list:
        print(f"Downloading {app_id}")
        all_data.append(format_and_extract_data(get_app_data_by_id(app_id)))

    with open("local_temp_steam_data.json", "w") as f:
        f.write(json.dumps(all_data))
    

game_list = get_all_app_ids_as_list()
game_list_size = len(game_list)

def run_batch(cn, chunk):
    print(f"Processing chunk number {cn+1} of {game_list_size}")
    raw_data, lookup = get_app_data_by_id(chunk)
    total_data = format_and_extract_data(raw_data, lookup)
    
    with open(f"extract_data_{cn}.json", "w") as f:
        f.write(json.dumps(total_data))

                                                                                                                                                                                                                  


