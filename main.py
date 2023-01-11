from sponge import perform_search
from soap import parse_blast
from fullEmail_gpt import fullEmail_gpt_request
from link_finder import get_clean_links
from event_gpt import get_sms
from send_sms import send_sms

rawBlastHtml = perform_search()
#print(rawBlastHtml)
rawLinks, cleanBlast = parse_blast(rawBlastHtml)
#print(cleanBlast)

#for key, value in rawLinks.items():
#    print(key, value)
#seems to properly generate up to here
events = fullEmail_gpt_request(cleanBlast)
print(events)
cleanLinks = get_clean_links(rawLinks,events)

#for link in cleanLinks:
#    print(link)
#print("cleanLinks: \n\n")
#for link in cleanLinks:
#    print(link)

sms = get_sms(cleanLinks)
print(sms)
send_sms(sms)



