from sponge import perform_search
from soap import parse_blast
from fullEmail_gpt import fullEmail_gpt_request
from link_finder import get_clean_links
from event_gpt import get_deep_events
from send_sms import send_sms
from smsCleaner import extract_todays_events

rawBlastHtml = perform_search()
rawLinks, cleanBlast = parse_blast(rawBlastHtml)

deepEvents = fullEmail_gpt_request(cleanBlast)
cleanLinks = get_clean_links(rawLinks,deepEvents)

for link in cleanLinks:
    print(link)

get_deep_events(cleanLinks)
#print(sms)
sms = extract_todays_events()

send_sms(sms)



