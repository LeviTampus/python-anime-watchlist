import tkinter as tk
from tkinter import simpledialog, messagebox
import storage
import watchlist
import anime_api

anime_list = storage.load_watchlist()

def refresh_list():
    listbox.delete(0, tk.END)
    for anime in anime_list:
        line = f"[{anime['mal_id']}] {anime['title']} - {anime['status']} ({anime['watched_episodes']}/{anime['episodes']})"
        listbox.insert(tk.END, line)

def search_add():
    query = simpledialog.askstring("Search Anime", "Anime title:")
    if not query:
        return
    results = anime_api.search_anime(query)
    if not results:
        messagebox.showinfo("Search", "No results found.")
        return
    lines = []
    for idx, anime in enumerate(results, start=1):
        lines.append(f"{idx}. {anime['title_english']} ({anime['episodes']})")
    pick = simpledialog.askinteger("Search Results", "\n".join(lines) + "\n\nAdd which number?")
    if pick is None or pick < 1 or pick > len(results):
        return
    selected = results[pick - 1]
    entry = {
        "mal_id": selected["mal_id"],
        "title": selected["title_english"],
        "episodes": selected["episodes"],
        "watched_episodes": 0,
        "status": "Plan to Watch",
    }
    if watchlist.add_anime(anime_list, entry):
        storage.save_watchlist(anime_list)
        refresh_list()
        messagebox.showinfo("Added", f"{entry['title']} added.")
    else:
        messagebox.showinfo("Duplicate", "Already in your watchlist.")


def get_selected():
    selection = listbox.curselection()
    if not selection:
        messagebox.showinfo("Select", "Select an anime in the list first.")
        return None
    return anime_list[selection[0]]

def update_progress_gui():
    anime = get_selected()
    if anime is None:
        return
    count = simpledialog.askinteger("Update Progress", f"Episodes watched for {anime['title']}?")
    if count is None or count < 0:
        return
    watchlist.update_progress(anime_list, anime["mal_id"], count)
    storage.save_watchlist(anime_list)
    refresh_list()
    messagebox.showinfo("Updated", f"{anime['title']}: {count} episodes.")

def change_status_gui():
    anime = get_selected()
    if anime is None:
        return
    status = simpledialog.askstring("Change Status", f"New status for {anime['title']}?")
    if status not in watchlist.STATUSES:
        messagebox.showinfo("Invalid", "Invalid status.")
        return
    watchlist.change_status(anime_list, anime["mal_id"], status)
    storage.save_watchlist(anime_list)
    refresh_list()

def remove_gui():
    anime = get_selected()
    if anime is None:
        return
    if not messagebox.askyesno("Remove", f"Remove {anime['title']}?"):
        return
    watchlist.remove_anime(anime_list, anime["mal_id"])
    storage.save_watchlist(anime_list)
    refresh_list()

root = tk.Tk()
root.title("Anime Watchlist")
root.geometry("500x400")

listbox = tk.Listbox(root, width=60, height=15)
listbox.pack(padx=10, pady=10)

refresh_button = tk.Button(root, text="Refresh", command=refresh_list)
refresh_button.pack(pady=5)

search_button = tk.Button(root, text="Search & Add", command=search_add)
search_button.pack(pady=5)

tk.Button(root, text="Update Progress", command=update_progress_gui).pack(pady=5)
tk.Button(root, text="Change Status", command=change_status_gui).pack(pady=5)
tk.Button(root, text="Remove", command=remove_gui).pack(pady=5)

refresh_list()

root.mainloop()