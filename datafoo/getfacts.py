from datetime import datetime


def next_execution(executiondata):
    # you need to write this yourself
    # fill this out with real data
    # use the upcoming_executions list
    d = {
        'Name': 'Jon Snow',
        'State': 'TX',
        'Date': datetime(2016, 4, 25)
    }
    return d




def state_upcoming_executions(state_abbrev, executiondata):
    records = [d for d in executiondata if d['State'] == state_abbrev]
    h = {'upcoming_executions_count': len(records)}
    # find the record with the "smallest" date
    if records:
        h['next_execution_date'] = sorted([r['Date'] for r in records])[0]
    else:
        h['next_execution_date'] = None
    return h

def state_past_executions(state_abbrev, executiondata):

    records = [d for d in executiondata if d['State'] == state_abbrev]
    h = {'past_executions_count': len(records)}
    # find the record with the "biggest" date
    if records:
        h['last_execution_date'] = sorted([r['Date'] for r in records])[-1]
    else:
        h['last_execution_date'] = None
    return h



def state_execution_stats(past_data, upcoming_data):
    """
        returns a dictionary of dictionaries:
        {
            'TX': { 'past_executions_count': 42, 'upcoming_executions_count': 5,
                    'last_execution_date': datetime(2016, 4, 4),
                    'next_execution_date': datetime(2016, 5, 1),
                    'name': 'TX'
                   }
        }
    """
    # get a list of all state names:
    datadicts = {}
    all_names = [d['State'] for d in past_data] + [d['State'] for d in upcoming_data]
    for statename in set(all_names):
        obj = {'name': statename}
        obj.update(state_past_executions(statename, past_data))
        obj.update(state_upcoming_executions(statename, upcoming_data))
        datadicts[statename] = obj
    # all done
    return datadicts
