import requests as _requests
import bs4 as _bs4

def _get_page(url: str) -> _bs4.BeautifulSoup:
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup

def eventsOnThisDay(month: str, day: int) -> list[str]:
    # url = _create_url(month, day)
    url = f'https://www.onthisday.com/day/{month}/{day}'
    page = _get_page(url)
    raw_events = page.find_all(class_="event")
    events = [event.text.strip() for event in raw_events]
    return events

def news() -> list[str]:
    url = 'https://techcrunch.com/'
    page = _get_page(url)
    raw_news = page.find_all('a', class_='post-block__title__link')
    news = [{'title': article.text.strip(), 'link': article['href']} for article in raw_news]
    return news