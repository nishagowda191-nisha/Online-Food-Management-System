
import os
import time
import requests
from requests.exceptions import RequestException
from food_data import FOOD_DATA

IMAGE_DIR = os.path.join("static", "images", "food")
os.makedirs(IMAGE_DIR, exist_ok=True)

API_URL = "https://commons.wikimedia.org/w/api.php"

session = requests.Session()
session.headers.update({
    "User-Agent": "FoodZoneStudentProject/1.0 (food image downloader)"
})

def get_with_retry(url, params=None):
    for attempt in range(4):
        try:
            response = session.get(
                url, params=params, timeout=30
            )

            if response.status_code == 429:
                wait = 30 * (attempt + 1)
                print(f"Rate limited. Waiting {wait} seconds...")
                time.sleep(wait)
                continue

            response.raise_for_status()
            return response

        except RequestException as error:
            print("Request failed:", error)
            if attempt < 3:
                time.sleep(10 * (attempt + 1))

    return None


for category, foods in FOOD_DATA.items():
    for item in foods:
        name = item["name"]
        filename = item["image"]
        filepath = os.path.join(IMAGE_DIR, filename)

        if os.path.isfile(filepath) and os.path.getsize(filepath) > 5000:
            print("Already exists:", filename)
            continue

        print("Searching:", name)

        params = {
            "action": "query",
            "generator": "search",
            "gsrsearch": "filetype:bitmap " + name + " food",
            "gsrnamespace": 6,
            "gsrlimit": 5,
            "prop": "imageinfo",
            "iiprop": "url",
            "iiurlwidth": 700,
            "format": "json"
        }

        response = get_with_retry(API_URL, params)

        if response is None:
            print("Skipped:", name)
            continue

        pages = response.json().get(
            "query", {}
        ).get("pages", {})

        saved = False

        for page in pages.values():
            info = page.get("imageinfo", [])
            if not info:
                continue

            image_url = info[0].get("thumburl") or info[0].get("url")
            if not image_url:
                continue

            image_response = get_with_retry(image_url)

            if image_response is None:
                continue

            if not image_response.headers.get(
                "Content-Type", ""
            ).startswith("image/"):
                continue

            data = image_response.content

            if len(data) < 5000:
                continue

            if not data.startswith((
                b"\xff\xd8\xff",
                b"\x89PNG\r\n\x1a\n",
                b"GIF87a",
                b"GIF89a",
                b"RIFF"
            )):
                continue

            with open(filepath, "wb") as file:
                file.write(data)

            print("Downloaded:", filename)
            saved = True
            break

        if not saved:
            print("No image downloaded:", name)

        time.sleep(3)

print("\nFinished. Check:", os.path.abspath(IMAGE_DIR))
