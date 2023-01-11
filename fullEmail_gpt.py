import openai

def fullEmail_gpt_request(clean_blast):
    openai.api_key = "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"

    initialPrompt = "Name all of the events with free food, drinks, breakfast, lunch, or dinner in the following email. Only list the name of the event and nothing else. Write the characters ##### between each event: "
    final_prompt = initialPrompt + clean_blast

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=final_prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    event_string = response['choices'][0]['text']
    """
    secondPrompt = "Name all of the events with free food, drinks, breakfast, lunch, or dinner in the following email. Use this format [event name, time, date, location, type of food/drink]"
    final_prompt = secondPrompt + clean_blast

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=final_prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    shallowEvents = response['choices'][0]['text']"""
    return event_string#, shallowEvents


