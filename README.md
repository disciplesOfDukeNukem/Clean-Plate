# Clean-Plate

Purpose:
The purpose of this project is to create a service to send daily text messages of free food events on campus

Background:
Mines students receive a daily newsletter email, called "The Daily Blast". Many events offer free food, however, the email is quite long and is rarely fully read by students. We decided to leverage the OpenAI API in order to summarize this email, and send us a text about which events have free food.

Architecture:
A diagram of the architecture can be found in cleanPlate.png
 - Pub/Sub: A daily timer using GCP fires at 7:00 am, launching the process on a Linux virtual machine
 - Sponge: An API call is made to ScaleSerp to scrape the Daily Blast. This returns a raw HTML, which is stored in rawBlast.txt.
 - 
