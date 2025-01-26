from openai import OpenAI
import os
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def callAPI_meta(Prompt, base64_image):
    client = OpenAI(
        api_key="",
        base_url="",
    )
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
         messages =[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}, 
                    },
                    {"type": "text", "text": Prompt},
                ],
            }
        ]
    completion = client.chat.completions.create(
        model="qwen-vl-max",
        messages=messages,
        top_k=0.9,
        temperature=0
    )
    # print(completion.choices[0].message.content)
    return completion.choices[0].message.content