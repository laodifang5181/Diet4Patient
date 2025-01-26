import json
import sys
import os
import Gemini
import time
import re

a = 0
i = 3

f = open(R"", 'r', encoding="utf-8")
lines = f.readlines()
f.close()
f1 = open(R"", 'r', encoding="utf-8")
lines1 = f1.readlines()
f1.close()
for line, line1 in zip (lines[:], lines1[:]):
    a = a + 1
    print(a) 
    l = json.loads(line)
    l1 = json.loads(line1)
    image_name = l["image"]
    disease = l["disease"]
    xx = l["wen_1"]
    doctor = l1["doctor"]


    image = ""
    prompt = f"请你以{doctor}医生的角色，根据给定的食材类别，列出每种类别所包含的典型代表食材，作为{disease}患者需要避免的典型食材。食材分类为：{xx}\n"
    lizi = f"给定输出的例子：高糖：糖果、巧克力、碳酸饮料、果汁、蛋糕、甜甜圈、果酱等; 高脂肪：肥肉、动物内脏、油炸食品等。仿照给定的例子输出格式。"
    p = prompt + lizi
    print(p)

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
            time.sleep(3)
    time.sleep(3)

    t = {}
    t["dish"] = l["dish"]
    t["image"] = l["image"]
    t["disease"] = l["disease"]
    t["result"] = l["result"]
    t["wen_2"] = result
    print(t)

    temp = json.dumps(t, ensure_ascii=False)
    f = open(R"", "a", encoding="utf-8")
    f.write(temp + "\n")
    f.close()