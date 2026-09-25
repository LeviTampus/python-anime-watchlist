import storage
import watchlist
import anime_api

def ask_number(prompt):
    while True:
        text = input(prompt)
        try:
            return int(text)
        except ValueError:
            print("Please enter a number.")


def main():
    anime_list = storage.load_watchlist()
    menu = """
1. Currently Airing Anime
2. Search Anime
3. View My Watchlist
4. Update Progress
5. Change Status
6. Remove Anime
7. Exit
"""
    header = """
Your Watchlist
--------------
"""
    airing_header = """
Currently Airing
----------------
"""

    while True:
        print(menu)
        choice = ask_number("Choose an option: ")

        if choice == 1:
            print(airing_header)
            result = anime_api.get_airing_anime()
            for idx, i in enumerate(result, start=1):
                print(f"[{idx}] {i['title_english']} | {i['episodes'] if i['episodes'] is not None else '?'} eps | {i['status']}")

        elif choice == 2:
            query = input("Type the anime name: ")
            result = anime_api.search_anime(query)
            if result == []:
                print("There is no match")
            else:
                print(f"Search anime: {query}")
                for idx, i in enumerate(result, start=1):
                    print(f"[{idx}] {i['title_english']} ({i['episodes'] if i['episodes'] is not None else '?'} eps)")

                add = ask_number("Add which number? (0 to cancel): ")
                if add == 0:
                    print("Cancelled")
                elif 1 <= add <= len(result):
                    selected = result[add - 1]
                    entry = {
                        "mal_id": selected["mal_id"],
                        "title": selected["title_english"],
                        "episodes": selected["episodes"],
                        "watched_episodes": 0,
                        "status": "Plan to Watch",
                    }
                    if watchlist.add_anime(anime_list, entry):
                        print("Added.")
                    else:
                        print("Already in your watchlist.")


                else:
                    print("Invalid choice.")

        elif choice == 3:
            print(header)
            if len(anime_list) == 0:
                print("Your watchlist is empty.")
            else:
                for i in anime_list:
                    print(f"[{i['mal_id']}] {i['title']}")
                    print(f"\tStatus: {i['status']} | Episodes: {i['watched_episodes']}/{i['episodes']}")

        elif choice == 4:
            mal_id = ask_number("What anime ID? ")
            count = ask_number("What episode? ")

            if watchlist.find_anime(anime_list, mal_id) is None:
                print("Anime not found")
            elif count < 0:
                print("Invalid Episode count")
            else:
                watchlist.update_progress(anime_list, mal_id, count)
                print("Updated.")

        elif choice == 5:
            mal_id = ask_number("What anime ID? ")
            status = input("What's the status? ")


            if watchlist.find_anime(anime_list, mal_id) is None:
                print("Anime not found")
            elif status not in watchlist.STATUSES:
                print("Invalid status.")
            else:
                watchlist.change_status(anime_list, mal_id, status)
                print("Status Updated.")

        elif choice == 6:
            mal_id = ask_number("What anime ID? ")
            entry = watchlist.find_anime(anime_list, mal_id)
            if entry is None:
                print("Anime not found")
            else:
                remove = input(f'Remove "{entry["title"]}"? (y/n) ')
                if remove.lower().strip() == "y":
                    watchlist.remove_anime(anime_list, mal_id)
                    print("Removed")
                else:
                    print("Cancelled")

        elif choice == 7:
            print("Goodbye")
            break

        else:
            print("Invalid Range")

    storage.save_watchlist(anime_list)

if __name__ == "__main__":
    main()

