from fastapi import FastAPI
import crud as _crud
import traceback as _traceback

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to My App"}

@app.get("/events")
async def all_events():
    return _crud.get_all_events()

@app.get("/events/{month}")
async def month_events(month: str):
    return _crud.get_month_events(month)

@app.get("/events/{month}/{day}")
async def day_events(month: str, day: int):
    return _crud.get_day_events(month, day)

@app.get("/news")
async def search_news(limit: int = 10):
    try:
        return _crud.get_news(limit)
    except:
        return _traceback.format_exc()