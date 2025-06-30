# 📈 Stocker

**Stocker** is a Django-powered live stock price dashboard that uses Chart.js for visualization, Celery and Redis for background tasks, and yFinance for fetching real-time stock data.

---

## 🔧 Features

- Live stock price tracking with auto-refresh
- Historical price chart using Chart.js
- Periodic updates via Celery + Redis + django-celery-beat
- Beautiful UI styled with Tailwind CSS
- Easily add and monitor new stocks

---

## 🚀 Tech Stack

- **Backend:** Django, Celery, Redis, yFinance
- **Frontend:** Chart.js, Tailwind CSS, HTML/JS
- **Scheduler:** django-celery-beat

---

## 📦 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/stocker.git
cd stocker

#Create a virtual environment and install dependencies

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

#Configure Redis
CELERY_BROKER_URL = 'redis://localhost:6379/0'

#Run Migrations

python manage.py migrate

#Start Celery Worker & Beat

celery -A stocker worker --loglevel=info
celery -A stocker beat --loglevel=info

#Run the Django Server
python manage.py runserver

🌐 Live Demo
(Coming soon if you deploy to PythonAnywhere, Heroku, or Render)

🖼️ Screenshots
(Include screenshots of your UI and chart output here)

🔁 API Endpoints
/api/price-history/<symbol>/ – Returns price + timestamp history for Chart.js

/stocks/ – Main dashboard view


📄 License
MIT License. Feel free to fork and improve the project.

👨‍💻 Author
Albert Hlelesi – @Albert802







