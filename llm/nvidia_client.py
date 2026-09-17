from openai import OpenAI


class NvidiaClient:

    def __init__(self, api_key):

        self.client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=api_key
        )

    def chat(self, messages):

        completion = self.client.chat.completions.create(
            model="nvidia/nemotron-3.5-lightning-30b-a3b",
            messages=messages,
            temperature=0.2,
            top_p=0.9,
            max_tokens=256,
            extra_body={
                "chat_template_kwargs": {"enable_thinking": False}
            }
        )

        return completion.choices[0].message.content