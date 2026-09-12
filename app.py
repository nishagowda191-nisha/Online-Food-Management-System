from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = "foodzone_secret_key_123"


# ============================================================
# FOOD DATA
# ============================================================

food_data = {

    "Pizza": [
        "Margherita Pizza",
        "Farmhouse Pizza",
        "Paneer Pizza",
        "Chicken Pizza"
    ],

    "Burger": [
        "Veg Burger",
        "Cheese Burger",
        "Chicken Burger",
        "Double Patty Burger"
    ],

    "Fries": [
        "French Fries",
        "Peri Peri Fries",
        "Cheese Fries"
    ],

    "Cold Drink": [
        "Coca Cola",
        "Pepsi",
        "Sprite",
        "Fanta"
    ],

    "Pasta": [
        "White Sauce Pasta",
        "Red Sauce Pasta",
        "Penne Pasta"
    ],

    "Sandwich": [
        "Veg Sandwich",
        "Cheese Sandwich",
        "Grilled Sandwich",
        "Chicken Sandwich"
    ],

    "Biryani": [
        "Veg Biryani",
        "Chicken Biryani",
        "Mutton Biryani"
    ],

    "Chicken": [
        "Chicken Tikka",
        "Chicken Lollipop",
        "Chicken Kebab",
        "Chicken 65"
    ],

    "Veg": [
        "Paneer Tikka",
        "Veg Manchurian",
        "Veg Kebab",
        "Paneer Chilli"
    ],

    "Non-Veg": [
        "Mutton Kebab",
        "Fish Fry",
        "Chicken Curry",
        "Mutton Curry"
    ],

    "Cake": [
        "Chocolate Cake",
        "Vanilla Cake",
        "Red Velvet Cake",
        "Black Forest Cake"
    ],

    "Ice Cream": [
        "Vanilla Ice Cream",
        "Chocolate Ice Cream",
        "Strawberry Ice Cream",
        "Butterscotch Ice Cream"
    ],

    "Desserts": [
        "Gulab Jamun",
        "Rasmalai",
        "Brownie",
        "Jalebi"
    ],

    "South Indian": [
        "Masala Dosa",
        "Idli",
        "Vada",
        "Uttapam"
    ],

    "Chinese": [
        "Veg Noodles",
        "Chicken Noodles",
        "Veg Fried Rice",
        "Chicken Fried Rice"
    ],

    "Rolls": [
        "Veg Roll",
        "Paneer Roll",
        "Chicken Roll",
        "Egg Roll"
    ],

    "Momos": [
        "Veg Momos",
        "Cheese Momos",
        "Chicken Momos",
        "Fried Momos"
    ],

    "Juice": [
        "Mango Juice",
        "Orange Juice",
        "Pineapple Juice",
        "Watermelon Juice"
    ],

    "Coffee": [
        "Cold Coffee",
        "Cappuccino",
        "Espresso",
        "Mocha"
    ],

    "Tea": [
        "Masala Tea",
        "Ginger Tea",
        "Green Tea",
        "Lemon Tea"
    ]
}


# ============================================================
# PRICES
# ============================================================

prices = {

    "Pizza": {
        "Margherita Pizza": 199,
        "Farmhouse Pizza": 247,
        "Paneer Pizza": 276,
        "Chicken Pizza": 319
    },

    "Burger": {
        "Veg Burger": 97,
        "Cheese Burger": 143,
        "Chicken Burger": 181,
        "Double Patty Burger": 227
    },

    "Fries": {
        "French Fries": 83,
        "Peri Peri Fries": 117,
        "Cheese Fries": 136
    },

    "Cold Drink": {
        "Coca Cola": 59,
        "Pepsi": 67,
        "Sprite": 73,
        "Fanta": 81
    },

    "Pasta": {
        "White Sauce Pasta": 189,
        "Red Sauce Pasta": 171,
        "Penne Pasta": 213
    },

    "Sandwich": {
        "Veg Sandwich": 91,
        "Cheese Sandwich": 128,
        "Grilled Sandwich": 157,
        "Chicken Sandwich": 193
    },

    "Biryani": {
        "Veg Biryani": 179,
        "Chicken Biryani": 231,
        "Mutton Biryani": 297
    },

    "Chicken": {
        "Chicken Tikka": 259,
        "Chicken Lollipop": 287,
        "Chicken Kebab": 311,
        "Chicken 65": 329
    },

    "Veg": {
        "Paneer Tikka": 169,
        "Veg Manchurian": 183,
        "Veg Kebab": 205,
        "Paneer Chilli": 221
    },

    "Non-Veg": {
        "Mutton Kebab": 341,
        "Fish Fry": 267,
        "Chicken Curry": 289,
        "Mutton Curry": 357
    },

    "Cake": {
        "Chocolate Cake": 149,
        "Vanilla Cake": 163,
        "Red Velvet Cake": 197,
        "Black Forest Cake": 229
    },

    "Ice Cream": {
        "Vanilla Ice Cream": 79,
        "Chocolate Ice Cream": 93,
        "Strawberry Ice Cream": 107,
        "Butterscotch Ice Cream": 121
    },

    "Desserts": {
        "Gulab Jamun": 89,
        "Rasmalai": 113,
        "Brownie": 139,
        "Jalebi": 77
    },

    "South Indian": {
        "Masala Dosa": 99,
        "Idli": 69,
        "Vada": 87,
        "Uttapam": 127
    },

    "Chinese": {
        "Veg Noodles": 149,
        "Chicken Noodles": 191,
        "Veg Fried Rice": 167,
        "Chicken Fried Rice": 209
    },

    "Rolls": {
        "Veg Roll": 109,
        "Paneer Roll": 137,
        "Chicken Roll": 179,
        "Egg Roll": 123
    },

    "Momos": {
        "Veg Momos": 119,
        "Cheese Momos": 147,
        "Chicken Momos": 173,
        "Fried Momos": 199
    },

    "Juice": {
        "Mango Juice": 99,
        "Orange Juice": 111,
        "Pineapple Juice": 129,
        "Watermelon Juice": 87
    },

    "Coffee": {
        "Cold Coffee": 139,
        "Cappuccino": 157,
        "Espresso": 113,
        "Mocha": 181
    },

    "Tea": {
        "Masala Tea": 49,
        "Ginger Tea": 57,
        "Green Tea": 71,
        "Lemon Tea": 63
    }
}


# ============================================================
# IMAGE NAMES
# ============================================================

def make_image_name(food_name):
    """
    Converts food name into the expected image filename.

    Example:
    Margherita Pizza -> margherita-pizza.jpg
    Chicken Biryani -> chicken-biryani.jpg
    """

    return (
        food_name
        .lower()
        .replace(" ", "-")
        .replace("'", "")
        .replace("&", "and")
    ) + ".jpg"


# ============================================================
# PREPARE FOOD DATA FOR MENU
# ============================================================

def get_menu_data():

    menu_data = {}

    for category, foods in food_data.items():

        menu_data[category] = []

        for food_name in foods:

            menu_data[category].append({
                "name": food_name,
                "price": prices[category][food_name],
                "image": make_image_name(food_name)
            })

    return menu_data


# ============================================================
# HOME
# ============================================================

@app.route("/")
def home():

    return render_template("index.html")


# ============================================================
# REGISTER
# ============================================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()
        confirm_password = request.form.get(
            "confirm_password",
            ""
        ).strip()

        # Check empty fields
        if not name or not email or not password or not confirm_password:

            return render_template(
                "register.html",
                error="Please fill all the fields."
            )

        # Check password
        if password != confirm_password:

            return render_template(
                "register.html",
                error="Passwords do not match."
            )

        # Store registered user
        session["registered_user"] = {
            "name": name,
            "email": email,
            "password": password
        }

        # Automatically login after registration
        session["user"] = {
            "name": name,
            "email": email
        }

        return redirect(url_for("home"))

    return render_template("register.html")


# ============================================================
# LOGIN
# ============================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        registered_user = session.get("registered_user")

        if registered_user:

            if (
                registered_user["email"] == email
                and registered_user["password"] == password
            ):

                session["user"] = {
                    "name": registered_user["name"],
                    "email": registered_user["email"]
                }

                return redirect(url_for("home"))

        return render_template(
            "login.html",
            error="Invalid email or password."
        )

    return render_template("login.html")


# ============================================================
# LOGOUT
# ============================================================

@app.route("/logout")
def logout():

    # Keep registered user so they can login again
    registered_user = session.get("registered_user")

    session.clear()

    if registered_user:
        session["registered_user"] = registered_user

    return redirect(url_for("home"))


# ============================================================
# MENU
# ============================================================

@app.route("/menu")
def menu():

    menu_data = get_menu_data()

    return render_template(
        "menu.html",
        food_data=menu_data
    )


# ============================================================
# ADD TO CART
# ============================================================

@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():

    item = request.form.get("item", "").strip()
    price = request.form.get("price", "").strip()
    category = request.form.get("category", "").strip()

    if not item or not price or not category:

        return redirect(url_for("menu"))

    try:

        price = int(price)

    except ValueError:

        return redirect(url_for("menu"))

    if "cart" not in session:

        session["cart"] = []

    cart = session["cart"]

    found = False

    for product in cart:

        if product["item"] == item:

            product["quantity"] += 1

            found = True

            break

    if not found:

        cart.append({
            "item": item,
            "price": price,
            "category": category,
            "quantity": 1
        })

    session["cart"] = cart
    session.modified = True

    return redirect(url_for("cart"))


# ============================================================
# CART
# ============================================================

@app.route("/cart")
def cart():

    cart_items = session.get("cart", [])

    total = 0

    for item in cart_items:

        total += (
            int(item["price"])
            * int(item["quantity"])
        )

    return render_template(
        "cart.html",
        cart_items=cart_items,
        total=total
    )


# ============================================================
# REMOVE FROM CART
# ============================================================

@app.route("/remove_from_cart/<int:index>")
def remove_from_cart(index):

    cart = session.get("cart", [])

    if 0 <= index < len(cart):

        cart.pop(index)

    session["cart"] = cart
    session.modified = True

    return redirect(url_for("cart"))


# ============================================================
# CLEAR CART
# ============================================================

@app.route("/clear_cart")
def clear_cart():

    session["cart"] = []

    session.modified = True

    return redirect(url_for("cart"))


# ============================================================
# BILLING
# ============================================================

@app.route("/billing")
def billing():

    cart_items = session.get("cart", [])

    if not cart_items:

        return redirect(url_for("menu"))

    subtotal = 0

    for item in cart_items:

        subtotal += (
            int(item["price"])
            * int(item["quantity"])
        )

    gst = round(subtotal * 0.05)

    delivery_charge = 40

    grand_total = (
        subtotal
        + gst
        + delivery_charge
    )

    return render_template(
        "billing.html",
        cart_items=cart_items,
        subtotal=subtotal,
        gst=gst,
        delivery_charge=delivery_charge,
        grand_total=grand_total
    )


# ============================================================
# PAYMENT
# ============================================================

@app.route("/payment", methods=["GET", "POST"])
def payment():

    cart_items = session.get("cart", [])

    if not cart_items:

        return redirect(url_for("menu"))

    subtotal = 0

    for item in cart_items:

        subtotal += (
            int(item["price"])
            * int(item["quantity"])
        )

    gst = round(subtotal * 0.05)

    delivery_charge = 40

    grand_total = (
        subtotal
        + gst
        + delivery_charge
    )

    if request.method == "POST":

        payment_method = request.form.get(
            "payment_method",
            "Cash on Delivery"
        )

        orders = session.get(
            "orders",
            []
        )

        order_number = len(orders) + 1

        order_id = f"ORD{order_number:04d}"

        order = {

            "order_id": order_id,

            "date": datetime.now().strftime(
                "%d-%m-%Y %I:%M %p"
            ),

            "order_status": "Order Placed",

            "items": cart_items.copy(),

            "payment_method": payment_method,

            "payment_status": (
                "Paid"
                if payment_method != "Cash on Delivery"
                else "Pending"
            ),

            "subtotal": subtotal,

            "gst": gst,

            "delivery_charge": delivery_charge,

            "total": grand_total
        }

        orders.append(order)

        session["orders"] = orders

        session["cart"] = []

        session.modified = True

        return redirect(
            url_for("order_success")
        )

    return render_template(
        "payment.html",
        cart_items=cart_items,
        subtotal=subtotal,
        gst=gst,
        delivery_charge=delivery_charge,
        grand_total=grand_total
    )


# ============================================================
# ORDER SUCCESS
# ============================================================

@app.route("/order_success")
def order_success():

    orders = session.get(
        "orders",
        []
    )

    if not orders:

        return redirect(
            url_for("menu")
        )

    latest_order = orders[-1]

    return render_template(
        "order_success.html",
        order=latest_order
    )


# ============================================================
# ORDER HISTORY
# ============================================================

@app.route("/order_history")
def order_history():

    orders = session.get(
        "orders",
        []
    )

    return render_template(
        "order_history.html",
        orders=orders
    )


# ============================================================
# PROFILE
# ============================================================

@app.route("/profile")
def profile():

    user = session.get(
        "user",
        {
            "name": "FoodZone User",
            "email": "user@example.com"
        }
    )

    return render_template(
        "profile.html",
        user=user
    )


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )