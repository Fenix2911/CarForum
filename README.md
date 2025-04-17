# CarForum 🏎️💬

**CarForum** is a web-based discussion platform built for car enthusiasts. Powered by Django, it allows users to register, create posts, comment, and engage in automotive-related discussions in a clean, minimal interface.

## 🔧 Tech Stack

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- HTML5 / CSS3 (TailwindCSS v4.1 and DaisyUI v5.0)
- SQLite (default Django DB)

## 🚀 Features

- ✅ User registration & authentication
- ✅ Create and browse discussion posts
- ✅ Add comments to posts
- ✅ Template-based rendering with HTML inheritance
- ✅ Responsive and user-friendly UI

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

1. Clone the repository:

```bash
git clone https://github.com/Fenix2911/CarForum.git
cd CarForum
```
2. Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run migrations:
```bash
python manage.py migrate
```
5. Start the development server:
```bash
python manage.py runserver
```
6. Open your browser and go to:
```cpp
http://127.0.0.1:8000/
```
## 🤝 Contributing
Contributions are welcome! Feel free to fork the repo, create a new branch, and submit a pull request. Bug fixes, feature ideas, or improvements are all appreciated.

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 📬 Contact
For questions, suggestions, or issues, open a discussion or create an issue on GitHub.

>Made with passion for programming and cars ❤️🚗
