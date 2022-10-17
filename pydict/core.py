import os
import requests
from typing import Optional


URL = "https://od-api.oxforddictionaries.com/api/v2"
APP_ID = os.getenv("OXFORD_API_ID")
APP_KEY = os.getenv("OXFORD_API_KEY")


def fetch(endpoint: str, language_code: str, word_id: str) -> Optional[dict]:
    url = f"{URL}/{endpoint}/{language_code}/{word_id.lower()}"
    if APP_ID and APP_KEY:
        r = requests.get(url, headers={"app_id": APP_ID, "app_key": APP_KEY})
        if r.status_code == 200:
            return r.json()
    return None