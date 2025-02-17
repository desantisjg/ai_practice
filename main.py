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
  model="gpt-4o-mini",
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