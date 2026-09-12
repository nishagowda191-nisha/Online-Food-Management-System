# 🍔 FoodZone — Online Food Management System

A web-based **Online Food Management System** built with **Python and Flask**. FoodZone provides a simple and user-friendly platform where users can browse food items, manage their cart, place orders, complete payment/billing steps, and view their order history.

---

## 📌 Project Description

**FoodZone** is designed to simplify the online food-ordering process through a Flask-based web application.

The system allows users to:

- Create an account and log in
- Browse food items
- Search for food
- View food items by category
- Add food items to a cart
- Manage cart items
- Place orders
- Proceed through payment and billing
- View successful order confirmation
- Check previous orders through order history

The project demonstrates the use of **Python, Flask, HTML, CSS, JavaScript, and Jinja2 templates** to build a complete web application.

---

## 🎯 Objectives

- 🍽️ Provide an easy-to-use online food ordering platform
- 🔐 Implement user registration and login functionality
- 📋 Display food items in an organized menu
- 🔎 Allow users to search for food items
- 🛒 Provide shopping cart management
- 📦 Enable users to place food orders
- 💳 Provide payment and billing pages
- 🧾 Generate an order-success flow
- 📜 Maintain an order-history page
- 🖥️ Create a simple and user-friendly web interface
- 🐍 Demonstrate Python-Flask web development

---

## ✨ Features

### 🔐 User Authentication
- User registration
- User login
- Session-based user handling
- Logout functionality

### 🍕 Food Menu
- Browse available food items
- Food categories
- Food prices
- Food images
- Search functionality

### 🛒 Shopping Cart
- Add food items to cart
- View selected items
- Manage the cart before placing an order

### 📦 Order Management
- Place food orders
- Order details
- Order confirmation
- Order success page
- Order history

### 💳 Payment & Billing
- Payment page
- Billing page
- Order/payment flow

### 🎨 User Interface
- Responsive web pages
- Navigation between modules
- Food cards and menu layout
- Clean FoodZone-themed interface

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Backend programming |
| 🌐 Flask | Web application framework |
| 🧱 HTML5 | Web page structure |
| 🎨 CSS3 | Styling and layout |
| ⚡ JavaScript | Client-side interactions |
| 🧩 Jinja2 | Flask template rendering |
| 🅱️ Bootstrap | UI styling/components |

---

## 📂 Project Structure

```text
Online-Food-Management-System/
│
├── app.py
├── food_data.py
│
├── templates/
│   ├── app.py
│   ├── base.html
│   ├── billing.html
│   ├── cart.html
│   ├── index.html
│   ├── login.html
│   ├── menu.html
│   ├── order.html
│   ├── order_history.html
│   ├── order_success.html
│   ├── payment.html
│   ├── register.html
│   └── replace_images.py
│
└── static/
    ├── css/
    └── images/
```

> **Note:** The exact static-file folders may vary depending on the local project setup.

---

## 🔄 Application Flow

```text
                    ┌───────────────┐
                    │    Home Page  │
                    └───────┬───────┘
                            │
             ┌──────────────┴──────────────┐
             │                             │
      ┌──────▼──────┐               ┌──────▼──────┐
      │   Register  │               │    Login    │
      └──────┬──────┘               └──────┬──────┘
             │                             │
             └──────────────┬──────────────┘
                            │
                     ┌──────▼──────┐
                     │     Menu    │
                     └──────┬──────┘
                            │
                     ┌──────▼──────┐
                     │     Cart    │
                     └──────┬──────┘
                            │
                     ┌──────▼──────┐
                     │    Order    │
                     └──────┬──────┘
                            │
                     ┌──────▼──────┐
                     │   Payment   │
                     └──────┬──────┘
                            │
                     ┌──────▼──────┐
                     │   Billing   │
                     └──────┬──────┘
                            │
                  ┌─────────▼─────────┐
                  │  Order Successful │
                  └─────────┬─────────┘
                            │
                     ┌──────▼──────┐
                     │Order History│
                     └─────────────┘
```

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/nishagowda191-nisha/Online-Food-Management-System.git
```

### 2. Open the Project Folder

```bash
cd Online-Food-Management-System
```

### 3. Install Flask

```bash
pip install flask
```

If you use a Python virtual environment, activate it before installing dependencies.

### 4. Run the Application

```bash
python app.py
```

### 5. Open the Website

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🖥️ Main Pages

| Page | Purpose |
|---|---|
| 🏠 Home | Landing page of FoodZone |
| 📝 Register | Create a new user account |
| 🔐 Login | Log into the application |
| 🍕 Menu | Browse available food |
| 🛒 Cart | Review selected food items |
| 📦 Order | Proceed with an order |
| 💳 Payment | Payment step |
| 🧾 Billing | Billing information |
| ✅ Order Success | Confirmation after ordering |
| 📜 Order History | View previous orders |

---

## 🔗 Main Application Routes

The Flask application includes routes for the main FoodZone workflow, including:

```text
/
 /register
 /login
 /menu
 /cart
 /order
 /payment
 /billing
 /order_success
 /order_history
```

> Routes can be extended or adjusted as the project is developed further.

---

## 📊 Food Data

Food information is maintained through the project's food-data structure, including:

- Food categories
- Food names
- Food prices
- Food image names

The application prepares menu data before passing it to the Flask templates.

---

## 🔒 Security Note

For development, Flask uses a secret key for session handling.

Before deploying this project publicly or using it in production, store the secret key in an **environment variable** rather than directly in source code.

Example:

```python
import os

app.secret_key = os.environ.get("SECRET_KEY")
```

Also avoid committing passwords, API keys, database credentials, or other private information to GitHub.

---

## 🧪 Testing

The application can be tested locally by:

1. Starting the Flask server.
2. Opening the home page.
3. Registering a user.
4. Logging in.
5. Browsing the menu.
6. Adding items to the cart.
7. Placing an order.
8. Checking the payment/billing flow.
9. Verifying the order-success page.
10. Checking order history.

---

## 🔮 Future Enhancements

Possible future improvements include:

- 👨‍💼 Admin dashboard
- 🍔 Admin food management
- ➕ Add/edit/delete food items
- 📦 Advanced order tracking
- 💰 Real payment gateway integration
- 🗄️ Database integration
- 👤 User profile management
- ⭐ Food ratings and reviews
- ❤️ Wishlist/favorites
- 📧 Order confirmation emails
- 📱 Improved mobile responsiveness
- 📈 Admin sales reports
- 🔍 Advanced food filtering

---

## 📸 Project Preview

You can add screenshots of your FoodZone application here.

Example:

```markdown
![FoodZone Home Page](screenshots/home.png)

![FoodZone Menu](screenshots/menu.png)

![FoodZone Cart](screenshots/cart.png)
```

---

## 💻 Git Commands

After making changes to the project, use:

```bash
git add .
git commit -m "Update FoodZone project"
git push
```

To check the current Git status:

```bash
git status
```

---

## 👩‍💻 Developed By

**Nisha Gowda**

### 🍔 FoodZone
**Online Food Management System**

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

**© 2026 FoodZone — Online Food Management System**
