import urllib.request
import urllib.error
import json

base_url = "https://api.tenrai.org/v1/anime"
top_url = "https://api.tenrai.org/v1/top/anime"

def fetch_data(url):
    try:
        with urllib.request.urlopen(url) as response:
            result = json.load(response)
            return result["data"]
    except urllib.error.URLError:
        print("Could not reach the anime API. Check your connection.")
        return []

def search_anime(query):
    return fetch_data(f"{base_url}?q={query}&limit=5")

def get_airing_anime():
    return fetch_data(f"{top_url}?filter=airing&limit=5")

