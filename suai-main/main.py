from fastapi import FastAPI, HTTPException, Request
from gitlab import Gitlab
import logging
import sqlite3
from datetime import datetime

app = FastAPI()

logging.basicConfig(filename='events.log', level=logging.INFO)

conn = sqlite3.connect('events.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_type TEXT,
    event_time TEXT
)
''')
conn.commit()

gl = Gitlab('https://gitlab.com', private_token='glft-Rej-xNqEuXhcQbGjsBTs')

@app.post("/webhook")
async def webhook(request: Request):
    event_type = request.headers.get('X-Gitlab-Event')
    data = await request.json()
    if event_type == 'Push Hook':
        logging.info(f"Push event detected: {data}")
        cursor.execute('''
        INSERT INTO events (event_type, event_time) VALUES (?, ?)
        ''', (event_type, datetime.now()))
        conn.commit()
    elif event_type == 'Merge Request Hook':
        logging.info(f"Merge Request event detected: {data}")
        cursor.execute('''
        INSERT INTO events (event_type, event_time) VALUES (?, ?)
        ''', (event_type, datetime.now()))
        conn.commit()
    else:
        raise HTTPException(status_code=400, detail="Unsupported event type")
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)