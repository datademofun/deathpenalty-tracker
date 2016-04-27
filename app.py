from flask import Flask, render_template
from datafoo import easyfetch, getfacts
from datetime import datetime


app = Flask(__name__)
upcoming_executions = easyfetch.upcoming_executions()
past_executions = easyfetch.historical_executions()
state_statistics = getfacts.state_execution_stats(past_executions, upcoming_executions)
# hardcode the date for now so that this app
# returns consistent results when fetching from stale data
ETERNAL_DATE = datetime(2016, 4, 23)



@app.route('/')
def homepage():
    next_ex = getfacts.next_execution(['data-needs-to-go-here, i.e. upcoming_executions'])
    next_state = state_statistics[next_ex['State']]
    htmltxt = render_template('index.html',
                today=ETERNAL_DATE,
                next_execution=next_ex,
                next_state=next_state,
                upcoming_executions=upcoming_executions,
                past_executions=past_executions,
                state_execution_statistics=state_statistics
              )
    return htmltxt

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
