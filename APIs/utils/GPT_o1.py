import base64
from io import BytesIO
from PIL import Image
from openai import OpenAI  #1.14.2
from tqdm import tqdm

MAX_TOKENS = 1024

KEY = ""
BASE_URL = ""


def callAPI_meta(Prompt, key=KEY, base_url=BASE_URL, max_tokens=MAX_TOKENS):

    client = OpenAI(api_key=key, base_url=base_url)

    messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": Prompt},
            ],
    }
    ]

    response = client.chat.completions.create(
        # model = "gpt-4-vision-preview",
        # model = "o1-preview",
        model = "o1-preview",
        # model = "gpt-4o",
        messages = messages,
        temperature=0,
        # seed=42,
        max_tokens=max_tokens,
        )
    # print(response)

    return response.choices[0].message.content
