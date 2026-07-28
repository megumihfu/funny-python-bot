# Funny Bot for Stoat & Discord

A funny project created to explore building interactive bots in Python and experimenting with asynchronous programming (`asyncio`/`aiohttp`) across two different platforms: Discord and Stoat (its open source version).

The bot listens to messages sent in text channels and responds with dynamic animated GIFs by querying the Giphy API directly.

---

## Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Discord.py](https://img.shields.io/badge/Discord.py-5865F2?style=for-the-badge&logo=discord&logoColor=white)
![Stoat.py](https://img.shields.io/badge/Stoat-FF4654?style=for-the-badge&logo=revolt&logoColor=white)
![aiohttp](https://img.shields.io/badge/aiohttp-2C5BB4?style=for-the-badge&logo=python&logoColor=white)
![Giphy API](https://img.shields.io/badge/Giphy_API-SS1111?style=for-the-badge&logo=giphy&logoColor=white)

---

## Features

The project contains two separate scripts (`discord_bot.py` and `stoat_bot.py`) sharing the same core logic:

* **`!gif`** : Returns the current trending GIF on Giphy.
* **`!gif <keywords>`** : Searches for and returns the first matching GIF for the given terms (e.g., `!gif cute cat`).

---

## Installation

### 1. Prerequisites

Make sure you have Python 3.10+ installed and install the required dependencies:

```bash
pip install discord.py stoat aiohttp python-dotenv certifi
```

### 2. Environment variables
Create a `.env` file at the root of your project with those key/tokens:
```bash
DISCORD_TOKEN=your_discord_token_here
BOT_TOKEN=your_stoat_token_here

GIPHY_API_KEY=your_giphy_api_key_here
SEARCH_ENDPOINT=[https://api.giphy.com/v1/gifs/search](https://api.giphy.com/v1/gifs/search)
TRENDING_ENDPOINT=[https://api.giphy.com/v1/gifs/trending](https://api.giphy.com/v1/gifs/trending)
```

### 3, Run it!
For the Discord bot:
```bash
python3 discord_bot.py
```

For the Stoat bot:
```bash
python3 stoat_bot.py
```

### 4, Roadmap & TODOS
Here are the next steps:
- [ ] Voice Channel Automation (Discord): 
  - Automatically detect when a user joins a specific voice channel and play matching audio/music.
  - *Example:* Trigger a League of Legends hyped playlist when a user joins the "LoL" voice channel.
  - *Example:* Trigger a relaxing Lofi stream/playlist when joining a "Work" or "Study" voice channel.

- [ ] Expanded Media Support:
  - Add sticker search and sending capabilities alongside GIFs.
  - Provide users with more interactive media choices (e.g., custom reaction stickers, memes,