# Anime Watchlist & Airing Tracker

A small command-line Python application for searching anime, following
currently airing shows, and keeping a personal watchlist that is saved
between sessions.

> **This is a personal Python learning / portfolio project.** It is built as
> a fundamentals exercise — using lists, dictionaries, functions, file
> handling, JSON, and basic HTTP/API usage — rather than as production
> software.

## Purpose

The project is a hands-on way to practice core Python by building something
small and genuinely useful. It is intentionally simple, dependency-light, and
easy to recreate.

## Features

- View currently airing anime
- Search anime by title and add a result to your watchlist
- Track episode progress
- Change watch status
  (`Watching`, `Completed`, `Plan to Watch`, `Dropped`, `On Hold`)
- Remove anime from the watchlist
- Persist the watchlist locally between runs

## Requirements

- Python 3 (standard library)
- An internet connection for API features
- No framework; external dependencies are avoided unless there is a strong reason

## API

[Tenrai API v1](https://api.tenrai.org/documentation) — an unofficial public
REST API for MyAnimeList catalog data. Its Jikan-compatible response format
supports the project's anime search, currently airing list, and anime details
without an API key for public requests.

## Persistence

The watchlist is stored locally as JSON at `data/watchlist.json`.

## Project Structure

```text
anime-watchlist/
├── AGENTS.md          # instructions for the AI mentor
├── PROJECT.md         # persistent source of truth for what we're building
├── README.md          # this file
├── main.py            # CLI entry point and menu
├── gui.py             # optional Tkinter GUI front-end
├── anime_api.py       # Tenrai API access
├── watchlist.py       # core watchlist logic
├── storage.py         # JSON load/save
└── data/
    └── watchlist.json # saved watchlist data
```

## Setup and Usage

Requires Python 3. No external packages are needed.

```bash
cd anime-watchlist
python main.py
```

You'll see the main menu:

```text
1. Currently Airing Anime
2. Search Anime
3. View My Watchlist
4. Update Progress
5. Change Status
6. Remove Anime
7. Exit
```

Example session:

```text
Choose an option: 2
Search anime: frieren
[1] Frieren: Beyond Journey's End (28 eps)
[2] Frieren: Beyond Journey's End Season 2 (10 eps)
Add which number? (0 to cancel): 1
Added.

Choose an option: 3
Your Watchlist
--------------
[52991] Frieren: Beyond Journey's End
	Status: Plan to Watch | Episodes: 0/28

Choose an option: 7
Goodbye
```

## GUI (optional)

A small Tkinter front-end is included as `gui.py`. It reuses the same logic
modules (`watchlist.py`, `storage.py`, `anime_api.py`) and offers the same
actions through a window with a list and buttons.

```bash
python gui.py
```

Tkinter ships with Python, so no extra installation is required.

## Limitations

- Two front-ends: a CLI (`main.py`) and a basic Tkinter GUI (`gui.py`)
- Single user, local JSON storage (no database)
- Depends on a public, unofficial API; data availability and rate limits are
  outside this project's control

## Future Improvements

- Optional SQLite storage
- Additional filtering and sorting of the watchlist
- Airing notifications

## Status

Working application with a CLI (`main.py`) and an optional Tkinter GUI
(`gui.py`). All core features are implemented, and the watchlist persists
between runs in `data/watchlist.json`.
