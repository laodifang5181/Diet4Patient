import json
import sys
import os
import Gemini
import time

a = 0
i = 0

f = open(R"", 'r', encoding="utf-8")
lines = f.readlines()
f.close()
for line in lines[:]:
    a = a + 1
    print(a) 
    l = json.loads(line)
    image_name = l["image"]
    disease = l["disease"]

    image = f""
    prompt = f"{disease}患者可以吃图中这道菜吗？仅仅回答是或者否。"

    result = None
    while result is None:
        try:
            print(f"\n\n使用{i}号key！！\n\n")
            result = Gemini.call_Gemini(image, prompt, i)
            i = (i + 1)%50
        except Exception as e:
            i = (i + 1)%50
            print(f"\n\n切换下一个！！\n\n")
            time.sleep(10)
    time.sleep(10)

    t = {}
    t["dish"] = l["dish"]
    t["image"] = l["image"]
    t["disease"] = l["disease"]
    t["result"] = l["result"]
    t["model_result"] = result
    print(t)

    temp = json.dumps(t, ensure_ascii=False)
    f = open(R"", "a", encoding="utf-8")
    f.write(temp + "\n")
    f.close()