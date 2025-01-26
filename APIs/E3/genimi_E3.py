import json
import sys
import os
import Gemini
import time
import re

a = 0
i = 9

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
    prompt = f"{disease}患者可以吃图中这道菜吗？你需要先回答图中这道菜的名称、这道菜中所使用的食材、{disease}所需要忌口的食材。然后回答问题，回答的格式为：答案是：(是或者否)。\n"
    lizi = "这是一个例子，按照例子的格式回答：\n图中这道菜是夫妻肺片。\n它主要使用的食材包括牛肉、牛肚、牛舌、花生、香菜、辣椒油、芝麻等。\n肾上腺癌患者在饮食上需要注意避免高脂肪、辛辣刺激以及高胆固醇的食物。答案是：否。"
    p = prompt+lizi

    result = None
    while result is None:
        try:
            print(f"\n\n使用{i}号key！！\n\n")
            result = Gemini.call_Gemini(image, p, i)
            print(result)
            i = (i + 1)%50
        except Exception as e:
            i = (i + 1)%50
            print(f"\n\n切换下一个！！\n\n")
            time.sleep(5)
    time.sleep(5)

    t = {}
    t["dish"] = l["dish"]
    t["image"] = l["image"]
    t["disease"] = l["disease"]
    t["result"] = l["result"]
    try:
        final_result = re.search(R"答案是：(.+?)([。\n]|$)", result)
        t["model_result"] = final_result.group(1)
    except:
        t["model_result"] = ""
    t["model_result_all"] = result
    print(t)

    temp = json.dumps(t, ensure_ascii=False)
    f = open(R"D:\fei\course\新多模态推理\EE\E3\gemini_E3.jsonl", "a", encoding="utf-8")
    f.write(temp + "\n")
    f.close()