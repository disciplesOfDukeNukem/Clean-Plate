import csv

def get_clean_links(links, event_string):
    cleanLinks = []
    link_dict = {}
    for row in links:
        #have to check if a row exists since every other row is blank
        if row:
            link_dict[row[0]] = row[1]

    events = event_string.split("#####")

    #checking each event
    for event in events:
        if event in link_dict:
            cleanLinks.append(link_dict[event])

    return cleanLinks
    

