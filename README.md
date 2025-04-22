# CarForum 🏎️💬

**CarForum** is a Django-based web forum for car enthusiasts. It allows users to register, log in, create posts, and engage in discussions. The app uses a simple and clean design with built-in Django templating.

---

## 🔧 Tech Stack

- [Python 3.13](https://www.python.org/)
- [Django 5.1](https://www.djangoproject.com/)
- HTML5 / CSS3 / Tailwind
- SQLite (default Django DB)

---

## 🚀 Features

- ✅ User registration and login
- ✅ Create and view forum posts
- ✅ Add comments to posts
- ✅ Template inheritance and reusable layout
- ✅ Responsive design

---

## 🗂️ Project Structure

```text
CarForum/
├── CarForum/                # Django project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── forum/                   # Main app: views, models, forms, URLs
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/              # Global templates (base.html, etc.)
│   ├── forum/
│   │   ├── base.html
│   │   ├── index.html
│   │   └── post_detail.html
│   └── registration/
│       ├── login.html
│       └── signup.html
│
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
└── requirements.txt        # Python package dependencies
```
## ⚙️ Local Setup
Follow the steps below to run CarForum on your local machine:

1. Clone the repository
```bash
git clone https://github.com/Fenix2911/CarForum.git
cd CarForum
```
2. Create and activate a virtual environment
```bash
python -m venv env
source env/bin/activate       # On Windows: .\env\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run migrations
```bash
python manage.py migrate
```
5. Start the development server
```bash
python manage.py runserver
```
6. Open in browser
Visit http://127.0.0.1:8000

## 🤝 Contributing
# Contributions are welcome!
To contribute: </br>
* Fork the repo
* Create a new branch: git checkout -b feature/your-feature-name
* Commit your changes: git commit -m "Add your message here"
* Push and open a pull request

## 📄 License
This project is licensed under the MIT License.

## 📬 Contact
If you have questions or suggestions, feel free to open an issue on GitHub Issues.

> Built with 💻 and ❤️ for cars. by @Fenix2911

