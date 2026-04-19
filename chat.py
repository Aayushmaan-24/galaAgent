import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

token = os.getenv("HF_TOKEN")

client = InferenceClient(model="moonshotai/Kimi-K2.5", token=token)

prompt = input("Prompt: ")
system_instruction= "You are a jester, make jokes and be funny about your prompt answer. Make sure to answer in maximum of 2 sentences."

response = client.chat.completions.create(
    messages = [
        {"role":"user", "content":prompt},
        {"role":"system", "content":system_instruction}
    ],
    stream=False,
    max_tokens=1024,
    extra_body={'thinking': {'type':'disabled'}}
)

print(response.choices[0].message.content)