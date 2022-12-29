"""import requests

# Set the API endpoint and your API key
api_endpoint = "https://api.openai.com/v1/text-davinci/completions"
api_key = "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"

#reading in and setting the blastPrompt
with open("cleanBlast.txt", "r") as f:
    # Read the contents of the file as a string
    blastPrompt = f.read()

initialPrompt = "Are there any events with free food, breakfast, lunch, dinner, or drinks in the following email? If so, when and where are they? "

# Set the model and prompt
model = "gpt-3-175b"
prompt = initialPrompt + blastPrompt

# Set the completion options
completion_options = {
    "max_tokens": 128,
    "temperature": 0.5,
    "top_p": 1,
    "presence_penalty": 0,
    "frequency_penalty": 0,
    "best_of": 1,
}

# Make the API request
response = requests.post(
    api_endpoint,
    headers={"Authorization": f"Bearer {api_key}"},
    json={
        "model": model,
        "prompt": prompt,
        "completion_options": completion_options,
    }
)
"""

import openai

openai.api_key = "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"

#TODO change to cleanBlast.txt when finished testing
read_path = "sampleDailyBlast-11-10-22.txt"
"""
#reading in and setting the blastPrompt
with open(read_path, "r") as f:
    # Read the contents of the file as a string
    blastPrompt = f.read()

initialPrompt = "Are there any events with free food, breakfast, lunch, dinner, or drinks in the following email? If so, when and where are they? "
"""
#final_prompt = initialPrompt + blastPrompt
final_prompt = "Write a 2 paragraph essay about sponges"

response = openai.Completion.create(
  model="text-davinci-003",
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
print(response.text)