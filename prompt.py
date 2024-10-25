from dotenv import load_dotenv
from config import API_KEY
from openai import OpenAI

# Import API_KEY
client = OpenAI(api_key=API_KEY)

# Load environment variables
load_dotenv()

# Initial Prompt
system_prompt = 'You are a best friend. You are also a duck.'
user_prompt = input('What’s your question? ')

# Call the OpenAI API to get a chat completion using the correct method
response = client.chat.completions.create(model='gpt-4o',
                                          messages=[
                                              {'role': 'system',
                                                  'content': system_prompt},
                                              {'role': 'user',
                                                  'content': user_prompt}
                                          ])

# Correct way to extract the response text
response_text = response.choices[0].message.content
print(response_text)
