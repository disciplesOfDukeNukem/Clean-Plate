#write each event to a csv
#verify that each event has the correlating date
#make sure that there are no duplicates

import re
from datetime import datetime

def extract_todays_events():
    today_long = datetime.today().strftime("%B %d").replace(" 0", " ")
    pattern_long = re.compile(r".*" + today_long + r".*")
    today_num = datetime.today().strftime("%m/%d")
    pattern_num = re.compile(r".*" + today_num + r".*")
    with open("rawEvents.txt", "r") as f:
        log = f.read()
        events_long = pattern_long.findall(log)
        events_num = pattern_num.findall(log)
        events = events_long + events_num
    return "\n".join(events)

#test = extract_todays_events
#print(test())




