from flask import Flask, render_template, session, redirect, url_for, request
import os
import re
from datetime import datetime

app = Flask(__name__)
app.secret_key = "foodzone-secret-key"


# ============================================================
# FOOD DATA
# ============================================================

FOOD_DATA = {
    "Pizza": [
        "Margherita", "Farmhouse", "Veggie Deluxe", "Paneer Pizza",
        "Cheese Burst", "Mexican Green Wave", "Pepperoni", "BBQ Chicken",
        "Tandoori Chicken", "Chicken Supreme", "Italian Special",
        "Double Cheese", "Mushroom Pizza", "Corn Pizza", "Onion Capsicum",
        "Spicy Paneer", "Chicken Tikka", "Chicken Sausage", "Seafood Pizza",
        "Peri Peri Pizza"
    ],

    "Burger": [
        "Veg Burger", "Cheese Burger", "Chicken Burger", "Double Patty",
        "Paneer Burger", "Aloo Tikki", "BBQ Burger", "Beef Burger",
        "Fish Burger", "Spicy Chicken", "Mexican Burger", "Classic Burger",
        "Maharaja Burger", "Grilled Burger", "Mushroom Burger", "Egg Burger",
        "Crispy Burger", "Loaded Burger", "Jumbo Burger", "American Burger"
    ],

    "Fries": [
        "French Fries", "Peri Peri Fries", "Cheese Fries", "Loaded Fries",
        "Masala Fries", "Curly Fries", "Garlic Fries", "Potato Wedges",
        "Cajun Fries", "Spicy Fries", "Sweet Potato Fries", "Cheesy Wedges",
        "BBQ Fries", "Chilli Fries", "Corn Fries", "Nacho Fries",
        "Mayo Fries", "Crunchy Fries", "Crinkle Fries", "Classic Fries"
    ],

    "Cold Drink": [
        "Coca Cola", "Pepsi", "Sprite", "Fanta", "Thums Up", "Mountain Dew",
        "7 Up", "Mirinda", "Limca", "Maaza", "Slice", "Frooti", "Appy Fizz",
        "Red Bull", "Cold Coffee", "Chocolate Shake", "Vanilla Shake",
        "Strawberry Shake", "Mango Shake", "Oreo Shake"
    ],

    "Pasta": [
        "White Sauce Pasta", "Red Sauce Pasta", "Pink Sauce Pasta",
        "Arrabbiata Pasta", "Alfredo Pasta", "Pesto Pasta", "Cheese Pasta",
        "Veg Pasta", "Paneer Pasta", "Mushroom Pasta", "Corn Pasta",
        "Spicy Pasta", "Garlic Pasta", "Italian Pasta", "Chicken Pasta",
        "Chicken Alfredo", "Chicken Arrabbiata", "Creamy Chicken Pasta",
        "Mac and Cheese", "Baked Pasta"
    ],

    "Sandwich": [
        "Veg Sandwich", "Cheese Sandwich", "Grilled Sandwich", "Club Sandwich",
        "Paneer Sandwich", "Corn Sandwich", "Veg Mayo Sandwich",
        "Cheese Corn Sandwich", "Aloo Sandwich", "Masala Sandwich",
        "Chutney Sandwich", "Mushroom Sandwich", "Chicken Sandwich",
        "Grilled Chicken Sandwich", "Chicken Club Sandwich",
        "BBQ Chicken Sandwich", "Egg Sandwich", "Cheese Chicken Sandwich",
        "Spicy Chicken Sandwich", "Triple Decker Sandwich"
    ],

    "Biryani": [
        "Veg Biryani", "Chicken Biryani", "Mutton Biryani", "Egg Biryani",
        "Hyderabadi", "Lucknowi", "Paneer Biryani", "Fish Biryani",
        "Prawn Biryani", "Dum Biryani", "Kolkata Biryani", "Mughlai",
        "Spicy Chicken", "Boneless Chicken", "Family Pack", "Special Dum",
        "Andhra Biryani", "Kebab Biryani", "Keema Biryani", "Royal Biryani"
    ],

    "Chicken": [
        "Chicken Tikka", "Chicken Kebab", "Chicken 65", "Chicken Lollipop",
        "Chicken Wings", "Chicken Popcorn", "Tandoori Chicken",
        "Butter Chicken", "Chicken Curry", "Chicken Masala", "Chicken Handi",
        "Chicken Korma", "Chicken Chilli", "Chicken Manchurian",
        "Chicken Fried Rice", "Chicken Noodles", "Chicken Seekh Kebab",
        "Chicken Tangdi", "Chicken Malai Tikka", "Chicken Afghani"
    ],

    "Veg": [
        "Paneer Tikka", "Paneer Butter Masala", "Shahi Paneer", "Kadai Paneer",
        "Palak Paneer", "Chilli Paneer", "Veg Manchurian", "Veg Kolhapuri",
        "Mix Veg", "Veg Handi", "Dal Tadka", "Dal Makhani", "Rajma Masala",
        "Chole Masala", "Aloo Gobi", "Bhindi Masala", "Matar Paneer",
        "Malai Kofta", "Veg Korma", "Mushroom Masala"
    ],

    "Non-Veg": [
        "Chicken Curry", "Mutton Curry", "Mutton Masala", "Mutton Korma",
        "Mutton Kebab", "Mutton Biryani", "Fish Curry", "Fish Fry",
        "Fish Tikka", "Fish Masala", "Prawn Curry", "Prawn Fry",
        "Prawn Masala", "Egg Curry", "Egg Masala", "Egg Bhurji",
        "Chicken Keema", "Mutton Keema", "Chicken Do Pyaza", "Mutton Handi"
    ],

    "Cake": [
        "Black Forest", "White Forest", "Chocolate Cake", "Red Velvet",
        "Pineapple", "Butterscotch", "Vanilla", "Strawberry", "Blueberry",
        "Fruit Cake", "Truffle", "Coffee Cake", "KitKat Cake", "Oreo Cake",
        "Ferrero Cake", "Mango Cake", "Rasmalai Cake", "Rainbow Cake",
        "Ice Cream Cake", "Designer Cake"
    ],

    "Ice Cream": [
        "Vanilla", "Chocolate", "Strawberry", "Mango", "Butterscotch",
        "Black Currant", "Kulfi", "Pista", "Kesar", "Coffee", "Oreo",
        "Belgian Chocolate", "Cookies & Cream", "Mint", "Blueberry",
        "Cotton Candy", "Bubblegum", "Fruit Mix", "Choco Chips",
        "Falooda Ice Cream"
    ],

    "Desserts": [
        "Gulab Jamun", "Rasmalai", "Jalebi", "Kheer", "Gajar Halwa",
        "Moong Dal Halwa", "Rabri", "Basundi", "Shrikhand", "Malpua",
        "Rasgulla", "Sandesh", "Brownie", "Chocolate Brownie",
        "Chocolate Mousse", "Fruit Custard", "Caramel Pudding",
        "Cheesecake", "Donut", "Churros"
    ],

    "South Indian": [
        "Plain Dosa", "Masala Dosa", "Cheese Dosa", "Mysore Masala Dosa",
        "Rava Dosa", "Onion Dosa", "Paneer Dosa", "Set Dosa", "Idli",
        "Medu Vada", "Sambar Vada", "Uttapam", "Onion Uttapam",
        "Tomato Uttapam", "Pongal", "Upma", "Appam", "Neer Dosa",
        "Pesarattu", "Curd Rice"
    ],

    "Chinese": [
        "Veg Fried Rice", "Chicken Fried Rice", "Schezwan Fried Rice",
        "Veg Hakka Noodles", "Chicken Hakka Noodles", "Schezwan Noodles",
        "Veg Manchurian", "Chicken Manchurian", "Chilli Paneer",
        "Chilli Chicken", "Spring Rolls", "Veg Momos", "Chicken Momos",
        "Honey Chilli Potato", "Dragon Chicken", "American Chopsuey",
        "Chinese Bhel", "Kung Pao Chicken", "Hot Garlic Noodles",
        "Schezwan Chicken"
    ],

    "Rolls": [
        "Veg Roll", "Paneer Roll", "Cheese Roll", "Aloo Roll", "Spring Roll",
        "Mayo Roll", "Schezwan Roll", "Mushroom Roll", "Corn Roll",
        "Tandoori Roll", "Chicken Roll", "Chicken Kathi Roll",
        "Chicken Tikka Roll", "Chicken Seekh Roll", "Egg Roll",
        "Egg Chicken Roll", "Mutton Roll", "BBQ Chicken Roll",
        "Cheese Chicken Roll", "Spicy Chicken Roll"
    ],

    "Momos": [
        "Veg Momos", "Steamed Momos", "Fried Momos", "Cheese Momos",
        "Paneer Momos", "Corn Momos", "Mushroom Momos", "Schezwan Momos",
        "Tandoori Momos", "Afghani Momos", "Chicken Momos",
        "Chicken Fried Momos", "Chicken Tandoori Momos",
        "Chicken Cheese Momos", "Chicken Schezwan Momos", "Peri Peri Momos",
        "Chilli Momos", "Kurkure Momos", "Mayo Momos", "Maharaja Momos"
    ],

    "Juice": [
        "Orange Juice", "Mango Juice", "Pineapple Juice", "Watermelon Juice",
        "Apple Juice", "Mosambi Juice", "Pomegranate Juice", "Grape Juice",
        "Papaya Juice", "Guava Juice", "Carrot Juice", "Beetroot Juice",
        "Lemon Juice", "Lemon Mint Juice", "Amla Juice", "Mixed Fruit Juice",
        "Sugarcane Juice", "Coconut Water", "Kiwi Juice", "Strawberry Juice"
    ],

    "Coffee": [
        "Hot Coffee", "Cold Coffee", "Cappuccino", "Espresso", "Latte",
        "Mocha", "Americano", "Macchiato", "Flat White", "Irish Coffee",
        "Hazelnut Coffee", "Vanilla Latte", "Caramel Latte",
        "Chocolate Coffee", "Filter Coffee", "South Indian Coffee",
        "Iced Coffee", "Frappe", "Caramel Frappe", "Mocha Frappe"
    ],

    "Tea": [
        "Milk Tea", "Masala Tea", "Ginger Tea", "Cardamom Tea", "Lemon Tea",
        "Green Tea", "Black Tea", "Elaichi Tea", "Tulsi Tea", "Mint Tea",
        "Honey Tea", "Lemon Ginger Tea", "Kashmiri Kahwa", "Irani Chai",
        "Cutting Chai", "Adrak Chai", "Chocolate Tea", "Peach Tea",
        "Iced Tea", "Lemon Iced Tea"
    ]
}


# ============================================================
# DIFFERENT PRICE FOR EVERY FOOD ITEM
# ============================================================

FOOD_PRICES = {}

price = 89

for category, items in FOOD_DATA.items():

    for item in items:
        FOOD_PRICES[item] = price
        price += 10

        # Restart range after higher values
        if price > 499:
            price = 99


# ============================================================
# IMAGE FINDER
# ============================================================

FOOD_IMAGE_FOLDER = os.path.join(
    app.root_path,
    "static",
    "images",
    "food"
)


def clean_name(text):
    text = text.lower().strip()
    text = text.replace("&", "and")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def build_image_index():

    index = {}

    if not os.path.isdir(FOOD_IMAGE_FOLDER):
        return index

    for filename in os.listdir(FOOD_IMAGE_FOLDER):

        full_path = os.path.join(
            FOOD_IMAGE_FOLDER,
            filename
        )

        if not os.path.isfile(full_path):
            continue

        name, extension = os.path.splitext(filename)

        if extension.lower() not in {
            ".jpg",
            ".jpeg",
            ".png",
            ".webp",
            ".gif"
        }:
            continue

        index.setdefault(
            clean_name(name),
            filename
        )

    return index


def get_food_images():

    image_index = build_image_index()

    result = {}

    for category, items in FOOD_DATA.items():

        result[category] = {}

        for item in items:

            item_key = clean_name(item)

            filename = image_index.get(item_key)

            if not filename:
                filename = image_index.get(
                    clean_name(category + "-" + item)
                )

            if not filename:
                filename = image_index.get(
                    clean_name(item + "-" + category)
                )

            if filename:

                result[category][item] = (
                    "images/food/" + filename
                )

    return result


# ============================================================
# HOME
# ============================================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ============================================================
# LOGIN
# ============================================================

@app.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        username = request.form.get(
            "username",
            ""
        ).strip()

        password = request.form.get(
            "password",
            ""
        ).strip()

        if username and password:

            session["user"] = username

            return redirect(
                url_for("menu")
            )

    return render_template(
        "login.html"
    )


# ============================================================
# REGISTER
# ============================================================

@app.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    if request.method == "POST":

        username = request.form.get(
            "username",
            ""
        ).strip()

        if username:

            session["user"] = username

            return redirect(
                url_for("menu")
            )

    return render_template(
        "register.html"
    )


# ============================================================
# LOGOUT
# ============================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("home")
    )


# ============================================================
# MENU
# ============================================================

@app.route("/menu")
def menu():

    food_images = get_food_images()

    return render_template(
        "menu.html",
        food_data=FOOD_DATA,
        food_images=food_images,
        food_prices=FOOD_PRICES
    )


# ============================================================
# CART
# ============================================================

@app.route("/cart")
def cart():

    cart_items = session.get(
        "cart",
        []
    )

    subtotal = sum(
        item["price"] * item["quantity"]
        for item in cart_items
    )

    tax = round(
        subtotal * 0.05
    )

    delivery = 40 if subtotal > 0 else 0

    total = subtotal + tax + delivery

    return render_template(
        "cart.html",
        cart_items=cart_items,
        subtotal=subtotal,
        tax=tax,
        delivery=delivery,
        total=total
    )


# ============================================================
# ADD TO CART
# ============================================================

@app.route(
    "/add_to_cart",
    methods=["POST"]
)
def add_to_cart():

    item = request.form.get(
        "item",
        ""
    ).strip()

    if not item:
        return redirect(
            url_for("menu")
        )

    # Get price from server
    price = FOOD_PRICES.get(
        item,
        99
    )

    cart = session.get(
        "cart",
        []
    )

    found = False

    for cart_item in cart:

        if cart_item["item"] == item:

            cart_item["quantity"] += 1

            found = True

            break

    if not found:

        cart.append({

            "item": item,

            "price": price,

            "quantity": 1

        })

    session["cart"] = cart

    session.modified = True

    return redirect(
        url_for("cart")
    )


# ============================================================
# INCREASE QUANTITY
# ============================================================

@app.route(
    "/increase/<item>"
)
def increase(item):

    cart = session.get(
        "cart",
        []
    )

    for cart_item in cart:

        if cart_item["item"] == item:

            cart_item["quantity"] += 1

            break

    session["cart"] = cart

    return redirect(
        url_for("cart")
    )


# ============================================================
# DECREASE QUANTITY
# ============================================================

@app.route(
    "/decrease/<item>"
)
def decrease(item):

    cart = session.get(
        "cart",
        []
    )

    for cart_item in cart:

        if cart_item["item"] == item:

            cart_item["quantity"] -= 1

            if cart_item["quantity"] <= 0:

                cart.remove(cart_item)

            break

    session["cart"] = cart

    return redirect(
        url_for("cart")
    )


# ============================================================
# REMOVE ITEM
# ============================================================

@app.route(
    "/remove/<item>"
)
def remove(item):

    cart = session.get(
        "cart",
        []
    )

    cart = [
        x for x in cart
        if x["item"] != item
    ]

    session["cart"] = cart

    return redirect(
        url_for("cart")
    )


# ============================================================
# CLEAR CART
# ============================================================

@app.route("/clear_cart")
def clear_cart():

    session["cart"] = []

    return redirect(
        url_for("cart")
    )


# ============================================================
# PLACE ORDER
# ============================================================

@app.route(
    "/order",
    methods=["GET", "POST"]
)
def order():

    cart_items = session.get(
        "cart",
        []
    )

    if not cart_items:

        return redirect(
            url_for("menu")
        )

    subtotal = sum(
        item["price"] * item["quantity"]
        for item in cart_items
    )

    tax = round(
        subtotal * 0.05
    )

    delivery = 40

    total = subtotal + tax + delivery

    if request.method == "POST":

        customer_name = request.form.get(
            "customer_name",
            ""
        ).strip()

        phone = request.form.get(
            "phone",
            ""
        ).strip()

        address = request.form.get(
            "address",
            ""
        ).strip()

        payment = request.form.get(
            "payment",
            ""
        )

        if not customer_name or not phone or not address:

            return render_template(
                "order.html",
                cart_items=cart_items,
                subtotal=subtotal,
                tax=tax,
                delivery=delivery,
                total=total,
                error="Please fill all details."
            )

        order_data = {

            "order_id":
                "FZ"
                + datetime.now().strftime(
                    "%Y%m%d%H%M%S"
                ),

            "customer_name":
                customer_name,

            "phone":
                phone,

            "address":
                address,

            "payment":
                payment,

            "items":
                cart_items,

            "subtotal":
                subtotal,

            "tax":
                tax,

            "delivery":
                delivery,

            "total":
                total,

            "date":
                datetime.now().strftime(
                    "%d-%m-%Y %H:%M"
                )

        }

        session["last_order"] = order_data

        session["cart"] = []

        return redirect(
            url_for("billing")
        )

    return render_template(
        "order.html",
        cart_items=cart_items,
        subtotal=subtotal,
        tax=tax,
        delivery=delivery,
        total=total
    )


# ============================================================
# BILLING
# ============================================================

@app.route("/billing")
def billing():

    order_data = session.get(
        "last_order"
    )

    if not order_data:

        return redirect(
            url_for("menu")
        )

    return render_template(
        "billing.html",
        order=order_data
    )


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    print("=" * 60)

    print(
        "       FOODZONE ONLINE FOOD MANAGEMENT SYSTEM"
    )

    print("=" * 60)

    print(
        "Food categories:",
        len(FOOD_DATA)
    )

    print(
        "Food items:",
        sum(
            len(items)
            for items in FOOD_DATA.values()
        )
    )

    print(
        "Image folder:",
        FOOD_IMAGE_FOLDER
    )

    print("=" * 60)

    app.run(debug=True)