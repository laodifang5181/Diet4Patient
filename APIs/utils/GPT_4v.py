import base64
from io import BytesIO
from PIL import Image
from openai import OpenAI  
from tqdm import tqdm

KEY = ""
BASE_URL = ""

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def callAPI_meta(Prompt, base64_image, key=KEY, base_url=BASE_URL):

    client = OpenAI(api_key=key, base_url=base_url)
    
    if base64_image == "":
            messages = [
        {
            "role": "user",
            "content": [
            {"type": "text", "text": Prompt},
                ],
        }
        ]
        
    else:

        messages = [
        {
            "role": "user",
            "content": [
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}", "detail": "low"},}, # detail: low high auto
                {"type": "text", "text": Prompt},
                ],
        }
        ]

    response = client.chat.completions.create(
        model = "gpt-4-vision-preview",
        messages = messages,
        top_k=0.9,
        temperature=0
        )
    # print(response)

    return response.choices[0].message.content