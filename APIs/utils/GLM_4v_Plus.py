import base64
from zhipuai import ZhipuAI

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def callAPI_meta(Prompt, base64_image):
    client = ZhipuAI(api_key="")

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
        
    response = client.chat.completions.create(
        model="glm-4v-plus",
        messages=messages,
        top_k=0.9,
        temperature=0
    )
    # print(response.choices[0].message)
    return response.choices[0].message.content