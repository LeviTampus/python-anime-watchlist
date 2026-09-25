# PROJECT.md — Anime Watchlist & Airing Tracker

Persistent source of truth for **what** we are building. If the original
conversation is lost, this file recovers the project context.

## Project Name

**Anime Watchlist & Airing Tracker**

## Purpose

A small, useful command-line Python application that lets a user:

- Search for anime
- View currently airing anime
- Add anime to a personal watchlist
- Track episode progress
- Change watch status
- Remove anime
- Save the watchlist between program sessions

Realistic enough to publish as a small portfolio project, small enough to
build in roughly 24 hours.

## Constraint

**~24-hour scope.** The project is primarily a Python fundamentals exercise.
If a feature risks exceeding the time budget or requires advanced concepts,
it is out of scope.

## Core Features

1. **Main Menu** — simple CLI menu driving the program.
2. **Currently Airing Anime** — fetch and display currently airing anime.
3. **Search Anime** — search by term and pick from results.
4. **Add to Watchlist** — add a selected anime; prevent duplicates.
5. **Watch Status** — `Watching`, `Completed`, `Plan to Watch`, `Dropped`, `On Hold`.
6. **Episode Progress** — record episodes watched; validate against invalid values.
7. **View Watchlist** — show title, status, and episode progress.
8. **Remove Anime** — remove an entry, with confirmation.
9. **Persistence** — load on start, save on exit via JSON.

### Expected Menu

```text
1. Currently Airing Anime
2. Search Anime
3. View My Watchlist
4. Update Progress
5. Change Status
6. Remove Anime
7. Exit
```

Wording may change if there is a good reason.

## Python Concepts Practiced

variables · strings · integers · booleans · lists · dictionaries ·
conditions · loops · functions · user input · formatted output ·
exception handling · file handling · JSON · basic HTTP/API usage.

Advanced concepts are **not** introduced just to look sophisticated.

## API

**Tenrai API v1** — an unofficial public REST API for MyAnimeList catalog data.

- Base URL: `https://api.tenrai.org/v1`
- Public requests need no API key or user authentication.
- Its response schema is compatible with Jikan v4, including the `mal_id`,
  `title`, `episodes`, and `status` fields used by this project.
- Search uses `/anime?q=...`; currently airing rankings use
  `/top/anime?filter=airing`; anime details use `/anime/{id}`.

Out of scope: API keys, OAuth, API account management, multiple APIs, and
complex abstraction layers.

## Persistence

- Local JSON file: `data/watchlist.json`
- Loaded on startup, saved on exit; survives program restarts.
- Intentionally simple. No database in the core project (SQLite only as a
  possible future extension).

### Planned Entry Schema (not implemented yet)

Each watchlist entry is planned to look like:

```json
{
  "mal_id": 52991,
  "title": "Frieren: Beyond Journey's End",
  "episodes": 28,
  "watched_episodes": 20,
  "status": "Watching"
}
```

The file starts as an empty JSON array: `[]`.

## Interface

**CLI for the core project.** No GUI/Tkinter in the original 24-hour core.
After the core was completed and tested, an optional **Tkinter GUI** was added
as a v2 extension (`gui.py`). It reuses the core modules and does not change
the CLI.

## Python Files (core 4 + optional GUI)

| File           | Responsibility |
|----------------|----------------|
| `main.py`      | Start the app, show the menu, read input, control flow, call other modules, display results. Must NOT contain all logic. |
| `anime_api.py` | Talk to the Tenrai API: build requests, send HTTP, parse JSON, search, fetch airing anime, extract fields, handle API/network errors. |
| `watchlist.py` | Core logic: add/remove/find anime, update progress, change status, filter/search the watchlist, validate operations. |
| `storage.py`   | Load/save the watchlist JSON and handle basic file errors. Keep it simple. |
| `gui.py` *(v2)* | Optional Tkinter front-end: a list of the watchlist plus buttons that call the core modules. Not part of the original core. |

## Target Approximate LOC

| File           | Target lines |
|----------------|--------------|
| `main.py`      | ~80–110 |
| `anime_api.py` | ~50–80 |
| `watchlist.py` | ~80–120 |
| `storage.py`   | ~30–50 |

Total: roughly **200–300 lines** of Python, excluding blank lines/comments.
Do not artificially increase the line count.

## Folder Structure

```text
anime-watchlist/
├── AGENTS.md
├── PROJECT.md
├── README.md
├── main.py
├── gui.py
├── anime_api.py
├── watchlist.py
├── storage.py
└── data/
    └── watchlist.json
```

## In-Scope Features

Search, airing list, add, view, update progress, change status, remove,
JSON persistence, input validation, graceful API/network errors.

## Out-of-Scope Features

AI · recommendations · chatbot · streaming · video playback · user accounts ·
authentication · OAuth · cloud database · PostgreSQL · MySQL · web app ·
Flask · FastAPI · React · JavaScript frontend · Docker · multiple APIs ·
notifications · Discord integration · advanced caching · asynchronous
programming · complex OOP · unnecessary design patterns · database (SQLite
only as a later optional extension).

If such a feature is suggested before the core is finished, it should be
flagged as outside scope.

## Error Handling Requirements

Gracefully handle: invalid menu input, invalid numbers, negative episodes,
duplicate anime, API unavailable, no internet, missing watchlist file,
invalid JSON. No elaborate error framework.

## Milestones

1. **Documentation & scaffolding** — docs, empty files, empty JSON. *(done)*
2. **Storage** — load/save `data/watchlist.json`. *(done)*
3. **Watchlist core** — add/view/update/change status/remove (in memory). *(done)*
4. **Main menu / CLI loop** — wire menu to watchlist + storage.
5. **Anime API** — search and currently-airing via Tenrai. *(done)*
6. **Validation & error handling** — harden all input/network paths. *(done)*
7. **README & review** — finalize docs, test end-to-end. *(done)*

Priority order: Core program → watchlist → JSON persistence → API →
validation/error handling → testing/README.

## Success Criteria

- Runs from the command line.
- Search anime; see currently airing anime.
- Add, view, update progress, change status, remove anime.
- Watchlist persists between runs.
- Common invalid inputs do not crash the program.
- API failures handled reasonably.
- Code is understandable; every major part can be explained.
- Small enough to recreate independently.
