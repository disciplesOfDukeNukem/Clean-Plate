import openai

openai.api_key = "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"

#TODO change to cleanBlast.txt when finished testing
#read_path = "sampleDailyBlast-11-10-22.txt"
read_path = "cleanBlast.txt"

blastPrompt = ""
#reading in and setting the blastPrompt
with open(read_path, "r") as f:
    # Read the contents of the file as a string
    blastPrompt = f.read()

#initialPrompt = "Name all of the events with free food, drinks, breakfast, lunch, or dinner in the following email, as well as when and where they are.  "
initialPrompt = "Name the first 8 events in the following email: "
final_prompt = initialPrompt + blastPrompt

#print(final_prompt)


response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=final_prompt,
  temperature=0.3,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
# Print the generated text
##   completions = response.json()["completions"]
#except KeyError:
#    print("The 'completions' key was not found in the response")

event_string = response['choices'][0]['text']

print("test" + event_string)

#event_list = event_string.split("], [")
#for event in event_list:
#    print(event+"\n\n")

