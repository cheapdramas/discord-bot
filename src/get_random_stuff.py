import requests
import json
import env
from random import randint 


TENOR_API_KEY = env.getenv("TENOR_KEY")   
TENOR_CLIENT_KEY = "bot" 
TENOR_URL = "https://tenor.googleapis.com/v2/search?q=post-irony&key=%s&client_key=%s&limit=1&random=true"


def random_gif() -> str | None:

    r = requests.get(
        TENOR_URL % (TENOR_API_KEY,TENOR_CLIENT_KEY)
    )
    if r.status_code == 200:
        gifs = json.loads(r.content)
        return gifs['results'][0]['media_formats']['webp']['url']
    return None
    
