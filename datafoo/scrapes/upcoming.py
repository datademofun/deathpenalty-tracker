from bs4 import BeautifulSoup
from os.path import join
from datetime import datetime
import re


"""
This is a very painful script for extracting very painful HTML.
You're not really meant to read it...
"""


SOURCE_URL = 'http://www.deathpenaltyinfo.org/upcoming-executions'
STASHED_URL = 'http://stash.compjour.org/samples/deathpenaltyinfo/upcoming-executions/'
LOCAL_FILENAME = join('static', 'stashed', 'upcoming-executions', 'index.html')

# Match on this attribute to know that a table cell is
# listing a month
MONTH_TD_STYLE = "background-color: rgb(0, 0, 51); width: 182px;"

def extract_scheduled_years(soup):
    links = soup.find_all('a', text=re.compile('Executions Scheduled for \d{4}'))
    regexmatches = [re.search(r'\d{4}',  a.attrs['href']) for a in links]
    year_numbers = [r.group() for r in regexmatches]
    return year_numbers

def extract_table_by_year(year, soup):
    el = soup.find('a', attrs={'id':year, 'name': year})
    table = el.find_parent('p').find_next_sibling('table')
    return table


def extract_months_from_year_table(table):
    month_datalist = []
    # get all the td elements with Month names
    month_tds = table.find_all('td', attrs={'style': MONTH_TD_STYLE})
    for month_td in month_tds:
        monthname = month_td.text.strip()
        monthrows = []
        # append the data as tuples
        month_datalist.append((monthname, monthrows))
        current_td = month_td
        # basically, for each month_td, keep scraping the next
        # rows until we reach the end of a table or a row with a
        # child td that contains a month name (or, rather, has similar styling)
        while True:
            # get the parent row, then the next row
            row = current_td.find_parent('tr').find_next_sibling('tr')
            # if there is no next row, or the next row contains a month
            # then break the while loop
            if not row or row.find('td', attrs={'style': MONTH_TD_STYLE}):
                break
            else:
                # add the row element to the pile
                monthrows.append(row)
                # increment current_td
                current_td = row.find('td')
    return month_datalist


def rows_to_execution_records(tablerows):
    records = []
    for row in tablerows:
        tvals = [td.text.strip() for td in row.find_all('td')]
        d = {'day': tvals[0], 'State': tvals[1], 'Name': tvals[2]}
        records.append(d)
    return records



def extract_upcoming_executions(htmltxt):
    """
    htmltxt is raw HTML of a webpage as a string

    returns: a list of dictionaries
    """
    soup = BeautifulSoup(htmltxt, 'lxml')
    execution_records = []
    for year in extract_scheduled_years(soup):
        table = extract_table_by_year(year, soup)
        monthdata = extract_months_from_year_table(table)
        # each month data member is: ('May', [a list of rows])
        for month_name, rows in monthdata:
            for record in rows_to_execution_records(rows):
                record['year'] = year
                record['month'] = month_name
                dtstr = '-'.join([year, month_name, record['day']])
                # parsing YYYY-MonthName-Day into a real date
                record['Date'] = datetime.strptime(dtstr, '%Y-%B-%d')
                execution_records.append(record)

    # let's sort them in chronological order:
    xrecords = sorted(execution_records, key=lambda r: r['Date'])
    return xrecords

