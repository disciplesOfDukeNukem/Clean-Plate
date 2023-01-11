from bs4 import BeautifulSoup

def parse_blast(raw_blast):

    soup = BeautifulSoup(raw_blast, 'html.parser')

    # extract all the links
    links = soup.find_all('a')

    a_tags = soup.find_all("a")

    link_dict = {}

    for atag in a_tags:
        link = atag.get("href")
        text = atag.text
        if link and text:
            link_dict[text] = link

    rawSoup = soup.get_text()
    ingredients = rawSoup.split('Maximum number of entries to return. If blank, no limit on number:\n\n\n\n\n\n')
    cookedSoup = ingredients[1]
    # Split the text into a list of words
    words = cookedSoup.split()
    # Get the first 500 words
    halfSoup = words[:500]
    # Join the first 2000 words back into a single string
    cleaned_blast = ' '.join(halfSoup)

    return link_dict, cleaned_blast


