# Clean-Plate

## Purpose:
The purpose of this project is to create a service to send daily text messages of free food events on campus

## Background:
Mines students receive a daily newsletter email, called "The Daily Blast". Many events offer free food, however, the email is quite long and is rarely fully read by students. We decided to leverage the OpenAI API in order to summarize this email, and send us a text about which events have free food.

## Architecture:
![image](https://github.com/disciplesOfDukeNukem/Clean-Plate/assets/98796321/22a5fb62-640a-49f6-a5fb-ec1aeab2d33a)

A diagram of the architecture can be found in cleanPlate.png
 - Pub/Sub: A daily timer using GCP fires at 7:00 am, launching the process on a Linux virtual machine
 - Sponge: An API call is made to ScaleSerp to scrape the Daily Blast. This returns a raw HTML, which is stored in rawBlast.txt
 - Soap: BeatifulSoup is used to parse the HTML. This outputs two files, the text extracted from the email ("cleanBlast.txt") and a log of all links from the email ("rawLinks.txt")
 - fullEmail-gpt: Reads in the cleanBlast, and asks GPT-3 which events have free food. These events are saved in events.txt
 - link-finder: Matches the events that have free food to the links that match the events. The links to events are saved in cleanLinks.txt
 - event-gpt: For every event, another OpenAI call is made, asking for the time, date, and location of each event. These descriptions are all saved into finalSMS.txt
 - twilio: Uses the twilio API to send out the finalSMS to our phone numbers

 These components were developed as separate files, but eventually saved into functions that are called in one script.

 ## Outcome:
 This program saved us an estimated $200 in food savings. Eventually, the project fizzled out due to inconsitent results from the OpenAI calls, and running out of API credits.

 ## Learned Technologies
 This project was developed to refresh and learn the following new technologies:
  - Google Cloud Platform (GCP)
  - WebScraping
  - API calls
  - HTML parsing using BeautifulSoup
  - Prompt Engineering

GCP had a much steeper learning curve than expected. Porter spent most of his time on GCP, while Zach contributed to most of the smaller components and architecture.
