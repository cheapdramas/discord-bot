import os
from dotenv import load_dotenv

load_dotenv()

def getenv(item: str) -> None | str | int:
    value = os.getenv(item)
    if not value: return 

    if value.isdigit():
        return int(value)
    return value
