# Content-Aggregator-using-Python

![License: Apache](https://img.shields.io/badge/License-Apache-yellow.svg)   <img src="https://img.shields.io/badge/made%20with-python-blue.svg" alt="made with python">

The Program aggregates, collects, and accumulates content pieces from many sorts of media channels, such as articles, social media postings, videos, photos, news, blogs and then presents all of that information via links on a single page. It substantially improves the accessibility of such content and provides users with a single location for all of the information they require.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- **[Python](https://www.python.org/)** (> Python 3.9)

- **[FastAPI](https://fastapi.tiangolo.com/)**

### Packages Used
- **[Requests](https://2.python-requests.org/en/master/)** : For fetching the source websites.
- **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)** : For scraping the source websites.

### Clone this repository

```sh
$ git clone https://github.com/amulyavarshney/Content-Aggregator-using-Python.git
or 
Download and extract the Zip-File
```

### Setting up the Virtual Environemt
Set up a virtual environment to execute, test and develop the project code.
```sh
$ cd Content-Aggregator-using-Python
$ python -m venv .env
 (Linux/Unix/Mac)
$ source .env/bin/activate
 (Windows)
$ .\.env\Scripts\activate
```

### Installing Dependencies
The Project has a few dependencies which can be installed by excuting the following command.
```sh
$ pip install -r requirements.txt 
```

## Run the Server
To start the uvicorn server run the following code
```sh
cd src
$ uvicorn main:app --reload
```

## Author
-   **Amulya Varshney**

## Contributting
Any contribution/suggestions are welcomed.
