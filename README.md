# Death Penalty Tracker

A Flask app built from web-scraped data.


## To run the basic app

Clone this repo into some directory:


~~~sh
git clone https://github.com/datademofun/deathpenalty-tracker.git
cd deathpenalty-tracker
python app.py
~~~


## To interact with the data

So, you don't have to worry about doing any web scraping.

But you still need to know where the data comes from, and what the looks like when it's delivered to the app. So jump into ipython (from the top directory).

The data-munging scripts are in the [datafoo](datafoo) directory. You shouldn't have to deal with [datafoo/scrapes](datafoo/scrapes) unless you really want to know how the sausage is made.


~~~py
from datafoo import easyfetch
from datafoo import getfacts

upcoming_executions = easyfetch.upcoming_executions()
past_executions = easyfetch.historical_executions()
~~~


