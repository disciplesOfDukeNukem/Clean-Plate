#read in rawlinks and create a dictionary
#read in events and store as an array

import csv

cleanLinks = []

#reading in rawLinks and storing in dictionary link_dict
with open("rawLinks.csv") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    link_dict = {}
    for row in reader:
        #have to check if a row exists since every other row is blank
        if row:
            link_dict[row[0]] = row[1]

#print(link_dict)
with open("sampleEvents.txt", "r", encoding = "utf-8") as e:
    events = []
    for line in e:
        events.append(line.strip())

#print(events)

#checking each event
for event in events:
    if event in link_dict:
        cleanLinks.append(link_dict[event])

print(cleanLinks)
    

