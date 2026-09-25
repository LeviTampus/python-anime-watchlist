import json

def load_watchlist():
    try:
        with open("data/watchlist.json", "r") as file:
            data = json.load(file)
            return data

    except (FileNotFoundError):
        print("File not found")
        return []

    except (json.JSONDecodeError):
        print("JSON file invalid")
        return []

def save_watchlist(watchlist):
    try:
        with open("data/watchlist.json", "w") as file:
            json.dump(watchlist, file)

    except OSError:
        print("Somethings wrong with the file")



