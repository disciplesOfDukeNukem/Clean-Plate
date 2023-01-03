import openai

openai.api_key = "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"

#TODO change to cleanBlast.txt when finished testing
read_path = "sampleDailyBlast-11-10-22.txt"
#read_path = "cleanBlast.txt"

blastPrompt = ""
#reading in and setting the blastPrompt
with open(read_path, "r", encoding="utf-8") as f:
    # Read the contents of the file as a string
    blastPrompt = f.read()

initialPrompt = "Name all of the events with free food, drinks, breakfast, lunch, or dinner in the following email. Only list the name of the event and nothing else: "
#initialPrompt = "Name and condense the first 8 events in the following email in an ordered list in the format of 1)[event1],2)[event2],...: "
final_prompt = initialPrompt + blastPrompt

#print(final_prompt)


response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=final_prompt,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
# Print the generated text
##   completions = response.json()["completions"]
#except KeyError:
#    print("The 'completions' key was not found in the response")

#print(response)

event_string = response['choices'][0]['text']
print(event_string)

#event_list = event_string.split("], [")
#for event in event_list:
#    print(event+"\n\n")

