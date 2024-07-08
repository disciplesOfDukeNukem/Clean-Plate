# Clean-Plate 🍽️

## Purpose 🎯
The goal of this project is to create a service that sends daily text messages about free food events on campus.

## Example 📸
![image](https://github.com/disciplesOfDukeNukem/Clean-Plate/assets/98796321/aa228538-8d3a-4022-87cc-74a32b87c63e)

## Background 📚
Students at Mines receive a daily newsletter called "The Daily Blast". Many events offering free food are included, but the lengthy email is rarely read in its entirety by students. To address this, we leveraged the OpenAI API to summarize the email and send a text message highlighting events with free food.

## Architecture 🏗️
![image](https://github.com/disciplesOfDukeNukem/Clean-Plate/assets/98796321/22a5fb62-640a-49f6-a5fb-ec1aeab2d33a)

A diagram of the architecture can be found in cleanPlate.png.

1. **Pub/Sub**: A daily timer using GCP triggers at 7:00 am, initiating the process on a Linux virtual machine.
2. **Sponge**: An API call is made to ScaleSerp to scrape the Daily Blast. The raw HTML is stored in `rawBlast.txt`.
3. **Soap**: BeautifulSoup is used to parse the HTML. The extracted text is saved in `cleanBlast.txt`, and a log of all links is saved in `rawLinks.txt`.
4. **fullEmail-gpt**: The script reads `cleanBlast.txt` and asks GPT-3 which events offer free food. These events are saved in `events.txt`.
5. **link-finder**: Matches events with free food to their corresponding links. The event links are saved in `cleanLinks.txt`.
6. **event-gpt**: For each event, another OpenAI call is made to obtain the time, date, and location. These details are saved in `finalSMS.txt`.
7. **twilio**: Uses the Twilio API to send the final SMS to our phone numbers.

These components were initially developed as separate files but were eventually consolidated into functions within a single script.

## Outcome 🎉
This program saved us an estimated $200 in food costs. However, the project eventually fizzled out due to inconsistent results from the OpenAI calls and depletion of API credits.

## Learned Technologies 💡
This project was developed to refresh and learn the following technologies:
- Python
- Google Cloud Platform (GCP)
- Web Scraping
- API calls
- HTML parsing with BeautifulSoup
- Prompt Engineering

GCP had a steeper learning curve than expected. Porter focused on GCP, while Zach contributed to most of the smaller components and the overall architecture.
