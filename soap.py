from bs4 import BeautifulSoup
import csv

def parse_blast(raw_blast):

    soup = BeautifulSoup(raw_blast, 'html.parser')

    # extract all the links
    links = soup.find_all('a')

    a_tags = soup.find_all("a")

    with open("rawLinks.csv", "w", encoding="utf-8") as l:
        writer = csv.writer(l)

        csv_headers = ["header", "link"]
        writer.writerow(csv_headers)

        for atag in a_tags:
            link = atag.get("href")
            text = atag.text
            if link and text:
                writer.writerow([text, link])

    rawSoup = soup.get_text()
    ingredients = rawSoup.split('Maximum number of entries to return. If blank, no limit on number:\n\n\n\n\n\n')
    cookedSoup = ingredients[1]
    # Split the text into a list of words
    words = cookedSoup.split()
    # Get the first 500 words
    halfSoup = words[:500]
    # Join the first 2000 words back into a single string
    cookedSoup = ' '.join(halfSoup)

    print(cookedSoup)

    with open("cleanBlast.txt", 'w', encoding="utf-8") as cleanBlast:
        cleanBlast.write(cookedSoup)

