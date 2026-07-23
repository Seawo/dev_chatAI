from openai import OpenAI


class NvidiaClient:

    def __init__(self, api_key):

        self.client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=api_key
        )

    def chat(self, messages):

        completion = self.client.chat.completions.create(
            model="meta/llama-3.3-70b-instruct",
            messages=messages,
            temperature=0.7,
            top_p=0.9,
            max_tokens=1024,
        )

        return completion.choices[0].message.content