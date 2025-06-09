import requests
import json
import config 
from random import randint,choice
from bs4 import BeautifulSoup
import re


TENOR_API_KEY = config.getenv("TENOR_KEY")   
TENOR_CLIENT_KEY = "bot" 
TENOR_URL = "https://tenor.googleapis.com/v2/search?q=post-irony&key=%s&client_key=%s&limit=1&random=true"

SOUND_URL_BASE = "https://www.myinstants.com"
SOUND_URL = SOUND_URL_BASE + "/en/search/?name=%s"

def random_gif() -> str | None:

    r = requests.get(
        TENOR_URL % (TENOR_API_KEY,TENOR_CLIENT_KEY)
    )
    if r.status_code == 200:
        gifs = json.loads(r.content)
        return gifs['results'][0]['media_formats']['webp']['url']
    return None

def random_sound() -> str | None:
    r = requests.get(
        SOUND_URL % config.SOUND_TOPIC
    )
    bs = BeautifulSoup(r.text, "html.parser")
    buttons = bs.find_all('button', class_='small-button')

    sound_urls = []
    for button in buttons:
        onclick = button.get("onclick", "")
        match = re.search(r"play\(\s*'([^']+)'", onclick)
        if match:
            sound_urls.append(match.group(1))

    if sound_urls:
        return SOUND_URL_BASE + choice(sound_urls)
    return None
