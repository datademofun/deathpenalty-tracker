import csv
from datetime import datetime
from os.path import join
SOURCE_URL = 'http://www.deathpenaltyinfo.org/exec-xls-export'
STASHED_URL = 'http://stash.compjour.org/samples/deathpenaltyinfo/executions-db.csv'
LOCAL_FILENAME = join('static', 'stashed', 'executions-db.csv')


def extract_historical_executions(txt):
    """
    `txt` is the deathpenaltyinfo executions database as a big text string

    Returns a list of dicts
    """
    lines = txt.splitlines()
    records = []
    for r in csv.DictReader(lines):
        r['Date'] = datetime.strptime(r['Date'], '%m/%d/%Y')
        r['Age'] = int(r['Age'])
        records.append(r)
    # let's sort them in reverse-descending order:
    xrecords = sorted(records, key=lambda r: r['Date'],
                      reverse=True)
    return xrecords
