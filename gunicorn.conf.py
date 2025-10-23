# Simple Gunicorn production config (Render will run: gunicorn app:app)
bind = "0.0.0.0:10000"  # Render routes traffic to $PORT; it sets PORT env, but binding to 0.0.0.0 is key
workers = 2
threads = 2
timeout = 120
loglevel = "info"
