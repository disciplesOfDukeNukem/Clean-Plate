import requests

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

# Print the generated text
print(response.json()["completions"][0]["text"])