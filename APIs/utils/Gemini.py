import google.generativeai as genai
import requests
import os
from PIL import Image

f = open("giminikeys.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()
keys = []
for line in lines:
    line = line.strip()
    # print(line)
    keys.append(line)

def call_Gemini(image_path, question, i):

    genai.configure(api_key=keys[i])
    model = genai.GenerativeModel('gemini-1.5-pro')
    
    if image_path == "":
        response = model.generate_content(
            question,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=350,
                temperature=0
            )
        )
        return response.text
    else:
        image = Image.open(image_path)
        response = model.generate_content(
            [image, question],
            generation_config=genai.types.GenerationConfig(
                top_p=0.9,
                max_output_tokens=350,
                temperature=0
            )
        )
        return response.text
