# 🌤️ API Testing & Weather Dashboard

Live site: [https://api-testing-pif0.onrender.com](https://api-testing-pif0.onrender.com)

A lightweight, browser-based API testing playground + weather dashboard.  
Built with **Flask** (backend) and **vanilla HTML/JS** (frontend).  
Deployed seamlessly on **Render** with secure, temporary API key handling.

---

## 🚀 Features

- **Secure client-only API key entry** (never saved or sent to server)
- **OpenWeatherMap integration**
  - Search any city
  - Quick-select popular cities
  - Displays temperature, humidity, conditions, wind speed
- **Temporary key storage**
  - Stored only in `sessionStorage`
  - Cleared when tab closes
- **Self-contained web app** — no database, no permanent secrets
- **Optional Flask backend** for testing or extending APIs

---

## 🧠 How It Works

1. Open [https://api-testing-pif0.onrender.com](https://api-testing-pif0.onrender.com)
2. Enter your **OpenWeatherMap API key** — it stays **only in your browser memory**
3. Type a city name or select one from the dropdown
4. The app calls OpenWeatherMap directly and shows live weather data

---

## 🧩 Local Development

### 1. Clone the repo
```bash
git clone https://github.com/bailo167/API-Testing.git
cd API-Testing
```

### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run locally
```bash
python app.py
```
Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌐 Render Deployment Configuration

**Language:** Python  
**Build Command:** `pip install -r requirements.txt`  
**Start Command:** `gunicorn -b 0.0.0.0:$PORT app:app`  
**Instance Type:** Free  

### Environment Variables (optional)
| Name | Example | Description |
|------|----------|-------------|
| `FLASK_ENV` | `production` | Flask environment mode |
| `THIRD_PARTY_API_URL` | `https://jsonplaceholder.typicode.com/todos/1` | optional external API for testing |
| `EXTERNAL_API_KEY` | `<secret>` | optional for protected API tests |

Render automatically redeploys on pushes to `main`.

---

## 🔒 Security Notes

- The OpenWeatherMap API key is **never stored**, **logged**, or **sent to the server**.  
- Keys live only in the browser’s `sessionStorage` and disappear when you close the tab.  
- Safe for demos and temporary usage, not for long-term key sharing.

---

## 📦 Project Structure
```
api-testing/
├── app.py
├── requirements.txt
├── static/
│   └── index.html
├── gunicorn.conf.py
├── .env.example
├── tests/
│   └── test_health.py
└── README.md
```

---

## 🧩 Future Enhancements
- 5-day weather forecast (OpenWeatherMap `/forecast`)
- Persistent theme or user settings
- Integrate additional public APIs for experimentation
- Proxy mode using Flask backend (for API rate-limiting or key hiding)

---

## 🧑‍💻 Author
**bailo167**  
Deployed on: [Render](https://render.com)  
Live site: [https://api-testing-pif0.onrender.com](https://api-testing-pif0.onrender.com)