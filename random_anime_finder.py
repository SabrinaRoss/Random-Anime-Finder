# This is a script created by Rowan Althorp (Sabrina Ross)
import requests
import random
import json
import os
from dotenv import load_dotenv

load_dotenv()
MAL_API_KEY = os.getenv("MAL_API_KEY")
BASE_URL = "https://api.myanimelist.net/v2/anime"

def get_anime_genre(genres, offset=0):
    headers = {
        'X-MAL-Client-ID': MAL_API_KEY  # Go on Mal, loggin and create your own Client_Id, it's pretty easy to do, you find it in account settings, the id will look something like 'A48fhjHLKfjkhdlLFHDJ5hd' etc etc 
    }
    query = ",".join(genres)
    params = {
        'q': query,
        'limit': 100,
        'offset': offset,
        'type': 'tv',
        'fields': 'id, title, genres, type'
    }
    response = requests.get(BASE_URL, headers=headers, params=params)
    if response.status_code == 200:
        anime_data = response.json()
        return anime_data.get('data', [])
    else:
        print(f"Nothing: {response.status_code}")
        print(response.text)
        return []

def get_anime_genre_per_page(genres):
    offset = 0
    anime_data = []
    while True:
        page_anime = get_anime_genre(genres, offset)
        if not page_anime:
            break
        offset += 100
        anime_data.extend(page_anime)
    return anime_data

def filter_matching_genres(anime_list, required_genres):
    filtered_anime = []
    for anime in anime_list:
        try:
            genres = [genre['name'].lower() for genre in anime['node'].get('genres', [])]
            if all(genre in genres for genre in required_genres):
                filtered_anime.append(anime)
        except Exception as e:
            print(f"{e}") 
    return filtered_anime

def filter_banned_genres(anime_list, banned_genres):
    filtered_anime = []
    for anime in anime_list:
        genres = [genre['name'].lower() for genre in anime['node'].get('genres', [])]
        if any(banned in genres for banned in banned_genres):
            continue
        filtered_anime.append(anime)
    return filtered_anime

def input_genres():
    clean_screen()
    print("Please enter your desired genres of anime, please make sure the genres are accoring to MyAnimeList's actual genre names")
    genres = input("Enter genres here (separated by comma): ").strip().lower()
    if not genres:
        return []
    return [genre.strip() for genre in genres.split(',')]

def input_banned_genres():
    clean_screen()
    print("Please enter the genres of anime from the seach you want to exclude, please make sure the genres are accoring to MyAnimeList's actual genre names")
    banned_genres = input("Enter banned genres here (separated by comma): ").strip().lower()
    if not banned_genres:
        return []
    return [banned_genre.strip() for banned_genre in banned_genres.split(',')]

def clean_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    genres = input_genres()
    banned_genres = input_banned_genres()
    cache_dir = "cache"
    os.makedirs(cache_dir, exist_ok=True)
    json_file_name = ",".join(genres) + ".json" 
    json_file_name = os.path.join(cache_dir, json_file_name)
  
    if os.path.exists(json_file_name):
        with open(json_file_name, 'r') as file:
            filtered_anime = json.load(file)
    else:
        anime_list = get_anime_genre_per_page(genres)
        if anime_list:
            filtered_anime = filter_matching_genres(anime_list, genres)
            filtered_anime = filter_banned_genres(filtered_anime, banned_genres)
            if filtered_anime:
                with open(json_file_name, 'w') as file:
                    json.dump(filtered_anime, file)
    if filtered_anime:
        filtered_size = len(filtered_anime)
        random_anime = random.randint(0, filtered_size-1)
        title = filtered_anime[random_anime]['node']['title']
        clean_screen()
        print("With the Genre(s): ", genres)
        print("With the Banned Genre(s): ", banned_genres)
        print("Your Random Anime is: \n")
        print(title)
            #for anime in filtered_anime: 
            #    title = anime['node']['title']
            #    print(title)  
                    
    else:
        clean_screen
        print("No anime found")
