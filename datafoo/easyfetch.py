"""
this easyfetch.py script exists so that you don't have to go into the
scrapes/ folder, which contains really esoteric webscraping code.

To make this app, all you need to realize is that:

    easyfetch.historical_executions()
    easyfetch.upcoming_executions()

Returns the parsed data that you need
"""


from datafoo.scrapes.historical import extract_historical_executions
from datafoo.scrapes.historical import STASHED_URL as historical_stale_url
from datafoo.scrapes.historical import SOURCE_URL as historical_source_url

from datafoo.scrapes.upcoming import extract_upcoming_executions
from datafoo.scrapes.upcoming import STASHED_URL as upcoming_stale_url
from datafoo.scrapes.upcoming import SOURCE_URL as upcoming_source_url
import requests

def historical_executions(refresh_data=False):
    if refresh_data is False:
        url = historical_stale_url
    else:
        url = historical_source_url
    txt = requests.get(url).text
    return extract_historical_executions(txt)

def upcoming_executions(refresh_data=False):
    if refresh_data is False:
        url = upcoming_stale_url
    else:
        url = upcoming_source_url
    txt = requests.get(url).text
    return extract_upcoming_executions(txt)



