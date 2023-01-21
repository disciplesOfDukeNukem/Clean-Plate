from sponge import perform_search
from soap import parse_blast
from fullEmail_gpt import fullEmail_gpt_request
from link_finder import get_clean_links
from event_gpt import get_sms
from send_sms import send_sms

rawBlastHtml = perform_search()
rawLinks, cleanBlast = parse_blast(rawBlastHtml)

#RUN THIS SECTION 3 TIMES
fullRequest = fullEmail_gpt_request(cleanBlast)
events = fullRequest[0]
shallowEvents = fullRequest[1]
print(f"Shallow events:{shallowEvents}")
cleanLinks = get_clean_links(rawLinks,events)

for link in cleanLinks:
    print(link)

sms = get_sms(cleanLinks)
#print(sms)


send_sms(sms)



