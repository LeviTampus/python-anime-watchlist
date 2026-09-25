STATUSES = ["Watching", "Completed", "Plan to Watch", "Dropped", "On Hold"]

def find_anime(watchlist, mal_id):
    for i in watchlist:
        if i["mal_id"] == mal_id:
            return i
    return None


def add_anime(watchlist, anime):
    if find_anime(watchlist, anime["mal_id"]):
        return False
    watchlist.append(anime)
    return True


def update_progress(watchlist, mal_id, count):
    entry = find_anime(watchlist, mal_id)
    if entry is None:
        return False
    if count < 0:
        return False
    entry["watched_episodes"] = count
    return True


def change_status(watchlist, mal_id, status):
    entry = find_anime(watchlist, mal_id)
    if entry is None:
        return False
    if status not in STATUSES:
        return False
    entry["status"] = status
    return True

def remove_anime(watchlist, mal_id):
    entry = find_anime(watchlist, mal_id)
    if entry is not None:
        watchlist.remove(entry)
        return True
    return False



