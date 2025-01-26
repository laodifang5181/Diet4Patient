import json
import sys
import os
import Gemini
import time
import re

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
    prompt = f"请你以中餐高级厨师的角色，根据输入的图片，识别出图中菜肴，并输出这道菜包含的所有关键核心的食材。\n"
    lizi = "给定学习的例子：识别出是麻婆豆腐，则输出为：这道菜包含的食材有豆腐。仿照给定的例子学习输出格式。"
    p = prompt + lizi

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
    t["tu_1"] = result
    print(t)

    temp = json.dumps(t, ensure_ascii=False)
    f = open(R"", "a", encoding="utf-8")
    f.write(temp + "\n")
    f.close()