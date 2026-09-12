import os
import re
import time
import hashlib
import requests

# ============================================================
# SETTINGS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "static", "images", "food")

os.makedirs(IMAGE_DIR, exist_ok=True)

WIKIMEDIA_API = "https://commons.wikimedia.org/w/api.php"

HEADERS = {
    "User-Agent": "FoodZoneCollegeProject/1.0"
}

# ============================================================
# FOOD DATA
# ============================================================
# These are the 20 categories used by your FoodZone project.
# Each category contains 20 realistic food items = 400 items.
# ============================================================

food_data = {

    "Pizza": [
        "Margherita Pizza",
        "Cheese Pizza",
        "Farmhouse Pizza",
        "Pepperoni Pizza",
        "Paneer Pizza",
        "Veggie Pizza",
        "Chicken Pizza",
        "BBQ Chicken Pizza",
        "Mushroom Pizza",
        "Corn Pizza",
        "Olive Pizza",
        "Jalapeno Pizza",
        "Mexican Pizza",
        "Italian Pizza",
        "Tandoori Pizza",
        "Spicy Chicken Pizza",
        "Double Cheese Pizza",
        "Pineapple Pizza",
        "Garlic Pizza",
        "Loaded Pizza"
    ],

    "Burger": [
        "Veg Burger",
        "Cheese Burger",
        "Chicken Burger",
        "Crispy Chicken Burger",
        "Paneer Burger",
        "Aloo Tikki Burger",
        "Double Cheese Burger",
        "Double Chicken Burger",
        "BBQ Burger",
        "Mexican Burger",
        "Mushroom Burger",
        "Spicy Burger",
        "Grilled Chicken Burger",
        "Peri Peri Burger",
        "Classic Burger",
        "Zinger Burger",
        "Veggie Burger",
        "Corn Burger",
        "Maharaja Burger",
        "Loaded Burger"
    ],

    "Fries": [
        "French Fries",
        "Cheese Fries",
        "Peri Peri Fries",
        "Masala Fries",
        "Chilli Fries",
        "Garlic Fries",
        "Loaded Fries",
        "Chicken Fries",
        "Cajun Fries",
        "Sweet Potato Fries",
        "Curly Fries",
        "Waffle Fries",
        "Spicy Fries",
        "Mexican Fries",
        "Pizza Fries",
        "Tandoori Fries",
        "Cheesy Garlic Fries",
        "Herb Fries",
        "Classic Fries",
        "Crispy Fries"
    ],

    "Cold Drink": [
        "Coca Cola",
        "Pepsi",
        "Sprite",
        "Fanta",
        "7 Up",
        "Mountain Dew",
        "Lemon Soda",
        "Masala Soda",
        "Ginger Ale",
        "Club Soda",
        "Orange Soda",
        "Lime Soda",
        "Cola Float",
        "Ice Lemon Soda",
        "Fresh Lime Soda",
        "Mint Soda",
        "Berry Soda",
        "Apple Soda",
        "Peach Soda",
        "Passion Fruit Soda"
    ],

    "Pasta": [
        "White Sauce Pasta",
        "Red Sauce Pasta",
        "Arrabbiata Pasta",
        "Alfredo Pasta",
        "Penne Pasta",
        "Spaghetti",
        "Macaroni",
        "Fettuccine Pasta",
        "Cheese Pasta",
        "Chicken Pasta",
        "Veg Pasta",
        "Pesto Pasta",
        "Creamy Pasta",
        "Tomato Pasta",
        "Mushroom Pasta",
        "Garlic Pasta",
        "Spicy Pasta",
        "Baked Pasta",
        "Lasagna",
        "Mac and Cheese"
    ],

    "Sandwich": [
        "Veg Sandwich",
        "Cheese Sandwich",
        "Grilled Sandwich",
        "Club Sandwich",
        "Chicken Sandwich",
        "Paneer Sandwich",
        "Corn Sandwich",
        "Veg Grilled Sandwich",
        "Cheese Grilled Sandwich",
        "Chicken Grilled Sandwich",
        "Tandoori Sandwich",
        "Spicy Sandwich",
        "Mayo Sandwich",
        "Egg Sandwich",
        "Bombay Sandwich",
        "Italian Sandwich",
        "Mexican Sandwich",
        "Toast Sandwich",
        "Masala Sandwich",
        "Loaded Sandwich"
    ],

    "Biryani": [
        "Chicken Biryani",
        "Mutton Biryani",
        "Veg Biryani",
        "Egg Biryani",
        "Hyderabadi Biryani",
        "Lucknowi Biryani",
        "Dum Biryani",
        "Paneer Biryani",
        "Mushroom Biryani",
        "Fish Biryani",
        "Prawn Biryani",
        "Ambur Biryani",
        "Kolkata Biryani",
        "Thalassery Biryani",
        "Donne Biryani",
        "Malabar Biryani",
        "Chicken Dum Biryani",
        "Mutton Dum Biryani",
        "Spicy Biryani",
        "Special Biryani"
    ],

    "Chicken": [
        "Chicken Tikka",
        "Chicken Tandoori",
        "Chicken 65",
        "Butter Chicken",
        "Chicken Curry",
        "Chicken Kebab",
        "Chicken Lollipop",
        "Chicken Wings",
        "Chicken Manchurian",
        "Chilli Chicken",
        "Chicken Korma",
        "Chicken Masala",
        "Chicken Fry",
        "Pepper Chicken",
        "Garlic Chicken",
        "Crispy Chicken",
        "Grilled Chicken",
        "Chicken Seekh Kebab",
        "Chicken Handi",
        "Chicken Sukka"
    ],

    "Veg": [
        "Paneer Butter Masala",
        "Palak Paneer",
        "Shahi Paneer",
        "Kadai Paneer",
        "Chilli Paneer",
        "Paneer Tikka",
        "Veg Korma",
        "Mix Veg",
        "Aloo Gobi",
        "Dal Tadka",
        "Dal Makhani",
        "Rajma Masala",
        "Chana Masala",
        "Bhindi Masala",
        "Veg Kofta",
        "Matar Paneer",
        "Malai Kofta",
        "Baingan Bharta",
        "Jeera Aloo",
        "Veg Handi"
    ],

    "Non-Veg": [
        "Mutton Curry",
        "Mutton Kebab",
        "Mutton Rogan Josh",
        "Mutton Masala",
        "Mutton Fry",
        "Fish Curry",
        "Fish Fry",
        "Fish Tikka",
        "Fish Kebab",
        "Prawn Curry",
        "Prawn Fry",
        "Prawn Masala",
        "Egg Curry",
        "Egg Masala",
        "Egg Fry",
        "Mutton Biryani",
        "Chicken Kebab",
        "Fish Fingers",
        "Seafood Platter",
        "Mixed Grill"
    ],

    "Cake": [
        "Chocolate Cake",
        "Vanilla Cake",
        "Red Velvet Cake",
        "Black Forest Cake",
        "White Forest Cake",
        "Butterscotch Cake",
        "Pineapple Cake",
        "Strawberry Cake",
        "Blueberry Cake",
        "Mango Cake",
        "Coffee Cake",
        "Carrot Cake",
        "Cheesecake",
        "Fruit Cake",
        "KitKat Cake",
        "Oreo Cake",
        "Chocolate Truffle Cake",
        "Rainbow Cake",
        "Coconut Cake",
        "Dry Fruit Cake"
    ],

    "Ice Cream": [
        "Vanilla Ice Cream",
        "Chocolate Ice Cream",
        "Strawberry Ice Cream",
        "Mango Ice Cream",
        "Butterscotch Ice Cream",
        "Pista Ice Cream",
        "Black Currant Ice Cream",
        "Cookies and Cream",
        "Coffee Ice Cream",
        "Kulfi",
        "Kesar Pista Kulfi",
        "Tender Coconut Ice Cream",
        "Blueberry Ice Cream",
        "Caramel Ice Cream",
        "Mint Chocolate Ice Cream",
        "Rocky Road Ice Cream",
        "Cookie Dough Ice Cream",
        "Salted Caramel Ice Cream",
        "Brownie Ice Cream",
        "Fruit Ice Cream"
    ],

    "Desserts": [
        "Gulab Jamun",
        "Rasgulla",
        "Rasmalai",
        "Jalebi",
        "Gajar Halwa",
        "Moong Dal Halwa",
        "Kheer",
        "Phirni",
        "Shahi Tukda",
        "Brownie",
        "Chocolate Brownie",
        "Chocolate Mousse",
        "Fruit Custard",
        "Caramel Pudding",
        "Rice Pudding",
        "Donut",
        "Churros",
        "Waffle",
        "Pancakes",
        "Apple Pie"
    ],

    "South Indian": [
        "Masala Dosa",
        "Plain Dosa",
        "Rava Dosa",
        "Set Dosa",
        "Mysore Masala Dosa",
        "Onion Dosa",
        "Cheese Dosa",
        "Idli",
        "Vada",
        "Medu Vada",
        "Sambar Vada",
        "Uttapam",
        "Onion Uttapam",
        "Pongal",
        "Upma",
        "Lemon Rice",
        "Curd Rice",
        "Tamarind Rice",
        "Vegetable Upma",
        "South Indian Thali"
    ],

    "Chinese": [
        "Veg Fried Rice",
        "Chicken Fried Rice",
        "Egg Fried Rice",
        "Schezwan Fried Rice",
        "Veg Noodles",
        "Chicken Noodles",
        "Schezwan Noodles",
        "Hakka Noodles",
        "Chilli Paneer",
        "Chilli Chicken",
        "Veg Manchurian",
        "Chicken Manchurian",
        "Spring Rolls",
        "Honey Chilli Potato",
        "Dragon Chicken",
        "Kung Pao Chicken",
        "Sweet and Sour Chicken",
        "Chinese Bhel",
        "Hot and Sour Soup",
        "Manchow Soup"
    ],

    "Rolls": [
        "Veg Roll",
        "Paneer Roll",
        "Chicken Roll",
        "Egg Roll",
        "Cheese Roll",
        "Kathi Roll",
        "Chicken Kathi Roll",
        "Paneer Kathi Roll",
        "Tandoori Chicken Roll",
        "Spicy Chicken Roll",
        "Mayo Chicken Roll",
        "Mutton Roll",
        "Seekh Kebab Roll",
        "Spring Roll",
        "Mexican Roll",
        "Cheesy Roll",
        "Veg Frankie",
        "Chicken Frankie",
        "Paneer Frankie",
        "Loaded Roll"
    ],

    "Momos": [
        "Veg Momos",
        "Chicken Momos",
        "Paneer Momos",
        "Cheese Momos",
        "Fried Momos",
        "Steamed Momos",
        "Tandoori Momos",
        "Peri Peri Momos",
        "Schezwan Momos",
        "Afghani Momos",
        "Corn Momos",
        "Mushroom Momos",
        "Chilli Momos",
        "Crispy Momos",
        "Chicken Fried Momos",
        "Chicken Tandoori Momos",
        "Veg Fried Momos",
        "Cheesy Fried Momos",
        "Mayo Momos",
        "Special Momos"
    ],

    "Juice": [
        "Orange Juice",
        "Apple Juice",
        "Mango Juice",
        "Pineapple Juice",
        "Watermelon Juice",
        "Grape Juice",
        "Guava Juice",
        "Papaya Juice",
        "Carrot Juice",
        "Beetroot Juice",
        "Mosambi Juice",
        "Pomegranate Juice",
        "Lemon Juice",
        "Mint Lemon Juice",
        "Mixed Fruit Juice",
        "Strawberry Juice",
        "Kiwi Juice",
        "Peach Juice",
        "Litchi Juice",
        "Berry Juice"
    ],

    "Coffee": [
        "Espresso",
        "Cappuccino",
        "Latte",
        "Americano",
        "Mocha",
        "Cold Coffee",
        "Iced Latte",
        "Iced Americano",
        "Caramel Latte",
        "Vanilla Latte",
        "Hazelnut Coffee",
        "Irish Coffee",
        "Filter Coffee",
        "South Indian Coffee",
        "Affogato",
        "Macchiato",
        "Flat White",
        "Cortado",
        "Frappuccino",
        "Chocolate Coffee"
    ],

    "Tea": [
        "Masala Tea",
        "Ginger Tea",
        "Cardamom Tea",
        "Milk Tea",
        "Black Tea",
        "Green Tea",
        "Lemon Tea",
        "Honey Tea",
        "Chai",
        "Elaichi Chai",
        "Kulhad Chai",
        "Kashmiri Tea",
        "Iced Tea",
        "Peach Iced Tea",
        "Lemon Iced Tea",
        "Mint Tea",
        "Herbal Tea",
        "Jasmine Tea",
        "Earl Grey Tea",
        "Special Tea"
    ]
}


# ============================================================
# HELPERS
# ============================================================

def clean_filename(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")


def image_hash(data):
    return hashlib.md5(data).hexdigest()


def search_wikimedia(query):
    """
    Search Wikimedia Commons for a real image matching the dish.
    """

    params = {
        "action": "query",
        "generator": "search",
        "gsrsearch": query,
        "gsrnamespace": 6,
        "gsrlimit": 10,
        "prop": "imageinfo",
        "iiprop": "url",
        "iiurlwidth": 700,
        "format": "json"
    }

    try:
        response = requests.get(
            WIKIMEDIA_API,
            params=params,
            headers=HEADERS,
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        pages = data.get("query", {}).get("pages", {})

        results = []

        for page in pages.values():

            imageinfo = page.get("imageinfo")

            if not imageinfo:
                continue

            info = imageinfo[0]

            url = (
                info.get("thumburl")
                or info.get("url")
            )

            if url:
                results.append(url)

        return results

    except Exception as e:

        print("Search error:", e)

        return []


def download_image(url):

    try:

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=30
        )

        response.raise_for_status()

        data = response.content

        if len(data) < 5000:
            return None

        content_type = response.headers.get(
            "Content-Type",
            ""
        ).lower()

        if "image" not in content_type:
            return None

        return data

    except Exception:

        return None


# ============================================================
# MAIN DOWNLOAD
# ============================================================

print()
print("=" * 70)
print("       FOODZONE REALISTIC FOOD IMAGE DOWNLOADER")
print("=" * 70)
print()

total_items = sum(
    len(items)
    for items in food_data.values()
)

print("Total categories:", len(food_data))
print("Total food items:", total_items)
print()
print("Saving images to:")
print(IMAGE_DIR)
print()

used_hashes = set()

downloaded = 0
failed = 0

# ============================================================
# DOWNLOAD EVERY FOOD ITEM
# ============================================================

for category_index, (category, items) in enumerate(
    food_data.items(),
    start=1
):

    print()
    print("-" * 70)
    print(f"{category_index}. {category}")
    print("-" * 70)

    for item_index, item in enumerate(
        items,
        start=1
    ):

        filename = (
            f"{category_index:02d}_"
            f"{item_index:02d}_"
            f"{clean_filename(item)}.jpg"
        )

        filepath = os.path.join(
            IMAGE_DIR,
            filename
        )

        print(
            f"[{downloaded + failed + 1}/{total_items}] "
            f"{item} ... ",
            end="",
            flush=True
        )

        # If already downloaded, don't download again
        if os.path.exists(filepath):

            try:
                with open(filepath, "rb") as f:
                    existing = f.read()

                used_hashes.add(
                    image_hash(existing)
                )

            except Exception:
                pass

            print("already exists")
            downloaded += 1
            continue

        # ----------------------------------------------------
        # Search exact food name
        # ----------------------------------------------------

        queries = [
            f"{item} food",
            f"{item} dish",
            f"{item} Indian food",
            f"{item} restaurant"
        ]

        image_data = None

        for query in queries:

            urls = search_wikimedia(query)

            for url in urls:

                data = download_image(url)

                if not data:
                    continue

                current_hash = image_hash(data)

                # Avoid duplicate photographs
                if current_hash in used_hashes:
                    continue

                image_data = data

                used_hashes.add(current_hash)

                break

            if image_data:
                break

            time.sleep(0.3)

        # ----------------------------------------------------
        # Category fallback
        # ----------------------------------------------------

        if image_data is None:

            fallback_queries = [
                f"{category} food",
                f"{category} dish",
                f"{category} restaurant food"
            ]

            for query in fallback_queries:

                urls = search_wikimedia(query)

                for url in urls:

                    data = download_image(url)

                    if not data:
                        continue

                    current_hash = image_hash(data)

                    if current_hash in used_hashes:
                        continue

                    image_data = data

                    used_hashes.add(current_hash)

                    break

                if image_data:
                    break

        # ----------------------------------------------------
        # Save
        # ----------------------------------------------------

        if image_data:

            try:

                with open(
                    filepath,
                    "wb"
                ) as f:

                    f.write(image_data)

                print("OK")

                downloaded += 1

            except Exception as e:

                print("SAVE ERROR")

                failed += 1

        else:

            print("NOT FOUND")

            failed += 1

        # Don't overload Wikimedia
        time.sleep(0.5)


# ============================================================
# FINISHED
# ============================================================

print()
print("=" * 70)
print("                 DOWNLOAD COMPLETE")
print("=" * 70)
print()
print("Total items :", total_items)
print("Downloaded  :", downloaded)
print("Failed      :", failed)
print()
print("Images are stored in:")
print(IMAGE_DIR)
print()
print("Now start Flask using:")
print()
print("    python app.py")
print()
print("=" * 70)