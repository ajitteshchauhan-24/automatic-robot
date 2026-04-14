import openai

class OpenAIChat:
    def __init__(self, api_key):
        openai.api_key = api_key

    def chat(self, prompt):
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['choices'][0]['message']['content']

# Example usage:
# chat = OpenAIChat(api_key='your-api-key')
# print(chat.chat('Hello, how are you?'))