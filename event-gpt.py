#will make an API call for each event, and add it a finalSMS.txt
    #input: cleanLinks.csv
    #output: finalSMS.txt

links = []

with open("cleanLinks.csv", "r") as cl:
    for line in cl:
        links.append(line.strip())

