import json as _json
import scraper as _scraper

def get_all_events() -> dict:
    with open('events.json') as events_file:
        data = _json.load(events_file)
    return data

def get_month_events(month: str) -> dict:
    events = get_all_events()
    month = month.lower()
    try:
        month_events = events[month]
        return month_events
    except KeyError:
        return "Invalid Entry: Please enter a correct month."

def get_day_events(month: str, day: int) -> dict:
    events = get_all_events()
    month = month.lower()
    try:
        day_events = events[month][str(day)]
        return day_events
    except KeyError:
        return "Invalid Entry: Please enter a correct month and day."

def get_news(limit: int) -> dict:
    news = _scraper.news()
    return news[:limit]