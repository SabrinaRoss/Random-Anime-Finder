# Random-Anime-Finder
Randomly picks an anime based on selected genres.

#### This is a simple Python script made for my roomates and I's anime bingo nights.

This script is decided based on genres and/or themes. It pulls from the MyAnimeList API and filters the results based on what you want (and don’t want) to watch. 
It also caches results so you're not requesting the API every time, if you want shows from a genre you have already requested shows from.

## What It Does

- Lets you choose one or more genres to include.
- Optionally lets you exclude genres you’re not interested in.
- Picks a random anime from the filtered list.
- Saves results locally in a `cache/` folder for faster reuse.

## What You Need

- Python 3.7 or higher
- A MyAnimeList API client ID — you can grab one from your MAL account under [API settings](https://myanimelist.net/apiconfig), if having difficulties: you usually can find you API key in account settings

## Setup

1. Clone this repo:

   ```bash
   git clone https://github.com/yourusername/Random-Anime-Finder.git
   cd Random-Anime-Finder
   ```

2. Install the Dependencies

    ```bash
    pip install -r requirements.txt
    ```

3. Add the API Key

    Open the .env file in the project folder. If it doesn’t exist, create a new file named .env.
  Then add this line, replacing your_key_here with your actual MyAnimeList client ID:
    ```.env
    MAL_API_KEY=your_key_here
    ```

4. Run the Script

    ```bash
    python random_anime_finder.py
    ```


**Note:** to get the full list of genres/themes that MAL contains (and their proper spellings) go to [MAL Website](https://myanimelist.net/anime.php)

  
