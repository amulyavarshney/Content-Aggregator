import datetime as _dt
import scraper as _scraper
import json as _json

def _data_range(start_date: _dt.date, end_date: _dt.date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + _dt.timedelta(n)

def create_events_dict() -> dict:
    events = {}
    start_date = _dt.date(2020, 1, 1)
    end_date = _dt.date(2021, 1, 1)

    for data in _data_range(start_date, end_date):
        month = data .strftime('%B').lower()
        if month not in events:
            events[month] = {}
        events[month][data.day] = _scraper.eventsOnThisDay(month, data.day)
    return events 

if __name__ == '__main__':
    events = create_events_dict()
    with open('events.json', 'w') as events_file:
        _json.dump(events, events_file)