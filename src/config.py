import os
from dotenv import load_dotenv

load_dotenv()

#https://<sound_url>?name=<sound_topic>
SOUND_TOPIC = "girl"
DEFAULT_SOUND_TOPIC = "girl"
def getenv(item: str) -> None | str | int:
    value = os.getenv(item)
    if not value: return 

    if value.isdigit():
        return int(value)
    return value
