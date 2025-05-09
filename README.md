# 🌿 Greenary Project - Django-based E-commerce for Eco Products

The **Greenary Project** is a Django-powered web application designed to sell eco-friendly products such as plants, seeds, pots, and garden tools. It features user registration, product browsing, cart management, order placement, and admin controls for product and order management.

---

## 🚀 Features

- User registration and login
- Product listing and detailed view
- Shopping cart and checkout process
- Order history and invoice generation
- Admin panel to manage:
  - Products (Add/Edit/Delete)
  - Orders
  - Users
- Product categories (e.g., Plants, Seeds, Tools, Fertilizers)
- Optional: Search, Filter, and Rating features

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Database**: SQLite (Default, switchable to MySQL/PostgreSQL)
- **Authentication**: Django built-in auth system
- **Others**: Pillow for image handling, crispy-forms (optional)

---

## 🧰 Installation & Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/greenary-project.git
   cd greenary-project
2. Create Virtual Environment

python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
3. Install Dependencies

pip install -r requirements.txt
4. Database Migration

python manage.py makemigrations
python manage.py migrate

5. Create Superuser

python manage.py createsuperuser
6. Run Server

python manage.py runserver
