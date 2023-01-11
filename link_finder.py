

def get_clean_links(rawLinkDict, event_string):
    cleanLinks = []
    events = event_string.split("#####")

    #checking each event
    for event in events:
        if event in rawLinkDict:
            cleanLinks.append(rawLinkDict[event])

    return cleanLinks
    

