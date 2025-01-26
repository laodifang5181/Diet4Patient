import json
import sys
import os
import Gemini
import re
import time

a = 0
m = 0

f = open(R"gemini_tu1.jsonl", 'r', encoding="utf-8")
tu1s = f.readlines()
f.close()
f = open(R"gemini_tu2.jsonl", 'r', encoding="utf-8")
tu2s = f.readlines()
f.close()
f = open(R"gemini_wen1.jsonl", 'r', encoding="utf-8")
wen1s = f.readlines()
f.close()
f = open(R"gemini_wen2.jsonl", 'r', encoding="utf-8")
wen2s = f.readlines()
f.close()

for i in range(0, 225):
    a = a + 1
    print(a) 
    tu1 = json.loads(tu1s[i])["tu_1"]
    disease = json.loads(tu1s[i])["disease"]
    image_name = json.loads(tu1s[i])["image"]
    tu2 = json.loads(tu2s[i])["tu_2"]
    wen1 = json.loads(wen1s[i])["wen_1"]
    wen2 = json.loads(wen2s[i])["wen_2"]
    # print(tu1)
    # print(tu2)
    # print(wen1)
    # print(wen2)
    
    image = f"{image_name}"
    # 实验二的prompt
    prompt1 = f"请你以医生的角色，根据以下四个角度的信息综合判断{disease}疾病患者是否可以食用图中这道菜。\n粗粒度信息：1b：{tu2} 2a:{wen1}\n细粒度信息：1a：{tu1} 2b：{wen2}\n然后对上述的信息进行对齐，粗粒度的以2a为主,细粒度的以1a为主，请仔细分析并结合粗粒度与细粒度的信息得出结论:\n仅仅回答是或者否一个字。"
    print(prompt1)

    result = None
    while result is None:
        try:
            print(f"\n\n使用{m}号key！！\n\n")
            result = Gemini.call_Gemini(image, prompt1, m)
            print(result)
            m = (m + 1)%50
        except Exception as e:
            print(e)
            m = (m + 1)%50
            print(f"\n\n切换下一个！！\n\n")
            time.sleep(5)
    time.sleep(5)

    t = {}
    t["dish"] = json.loads(tu1s[i])["dish"]
    t["disease"] = disease
    t["result"] = json.loads(tu1s[i])["result"]
    t["model_result"] = result
    print(t)

    temp = json.dumps(t, ensure_ascii=False)
    f = open(R"", "a", encoding="utf-8")
    f.write(temp + "\n")
    f.close()