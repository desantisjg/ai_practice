from openai import OpenAI
# Create the OpenAI client
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Completions endpoint
response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Who developed ChatGPT?"
  message = [{"role": "user",
    "content": prompt"
    }]
)

# How to extract response from OpenAI
responses = response.choices[0].message.content

### Here is another example in action
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

prompt="""Replace car with plane and adjust phrase:
A car is a vehicle that is typically powered by an internal combustion engine or an electric motor. 
It has four wheels, and is designed to carry passengers and/or cargo on roads or highways. 
Cars have become a ubiquitous part of modern society, and are used for a wide variety of purposes, s
uch as commuting, travel, and transportation of goods. Cars are often associated with freedom,
independence, and mobility."""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4-turbo",
  messages=[{"role": "user", "content": prompt}],
  max_tokens=100
)

# Extract and print the response text
print(response.choices[0].message.content)


### More examples
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

prompt="""Summarize the following text into two concise bullet points:
Investment refers to the act of committing money or capital to an enterprise with the 
expectation of obtaining an added income or profit in return. There are a variety of 
investment options available, including stocks, bonds, mutual funds, real estate, 
precious metals, and currencies. Making an investment decision requires careful analysis, 
assessment of risk, and evaluation of potential rewards. Good investments have the ability 
to produce high returns over the long term while minimizing risk. Diversification of 
investment portfolios reduces risk exposure. Investment can be a valuable tool for 
building wealth, generating income, and achieving financial security. It is 
important to be diligent and informed when investing to avoid losses."""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}],
  max_tokens=400, #controls amount of tokens
  temperature=0.1 #makes the model more deterministic 0.0 --> 1.0 maximum randomness
)

print(response.choices[0].message.content)


## Zero-shot prompts = no examples, one-shot has one example, few-shot has multiple examples

# Multi-turn conversations

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  max_tokens=150,
  messages=[
    {"role": "system",
     "content": "You are a helpful data science tutor."},
    {"role": "user",
     "content": "What is the difference between a for loop and a while loop"}
  ]
)

# Extract the assistant's text response
print(response.choices[0].message.content)

# Creating an AI Chatbot and Mult-Turn Conversations
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

messages = [{"role": "system", "content": "You are a helpful math tutor."}]
user_msgs = ["Explain what pi is.", "Summarize this in two bullet points."]

for q in user_msgs:
    print("User: ", q)
    
    # Create a dictionary for the user message from q and append to messages
    user_dict = {"role": "user", "content": q}
    messages.append(user_dict)
    
    # Create the API request
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=100
    )
    
    # Convert the assistant's message to a dict and append to messages
    assistant_dict = {"role": "assistant", "content": response.choices[0].message.content}
    messages.append(assistant_dict)
    print("Assistant: ", response.choices[0].message.content, "\n")


# Text Moderation
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Moderation endpoint
response = client.moderations.create(
    model="text-moderation-latest",
    input="My favorite book is To Kill a Mockingbird."
)

# Print the category scores
print(response.results[0].category_scores)


### Speech-to-Text Transcription with Whisper

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Open the openai-audio.mp3 file
audio_file = open("openai-audio.mp3", "rb")

# Create a transcript from the audio file
response = client.audio.transcriptions.create(model="whisper-1", file=audio_file)

# Extract and print the transcript text
print(response.text)

### Speech Translation Transcription with Whisper
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Open the audio.wav file
audio_file = open("audio.wav", "rb")

# Write an appropriate prompt to help the model
prompt = "audio relates to a recent World Bank report"

# Create a translation from the audio file
response = client.audio.translations.create(model="whisper-1",
                                            file=audio_file,
                                            prompt=prompt)

print(response.text)

### Combining Models Together
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Open the audio.wav file
audio_file = open("audio.wav", "rb")

# Create a transcription request using audio_file
audio_response = client.audio.transcriptions.create(model="whisper-1", file=audio_file)

transcript = audio_response.text

prompt = "What language was used in the audio file: " + transcript

# Create a request to the API to identify the language spoken
chat_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)
print(chat_response.choices[0].message.content)


### THrow it in a function
def get_response(prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}], 
    temperature = 0)
  return response.choices[0].message.content

# Test the function with your prompt
response = get_response("When was openAI founded?")
print(response)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that follows the instructions
prompt = "Write a poem about ChatGPT in basic english that a child can understand"

# Get the response
response = get_response(prompt)

print(response)
print(response.choices[0].message.content)
