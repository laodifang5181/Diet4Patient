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
    doctor = l["doctor"]

    image = ""
    prompt = f"对于{disease}患者，从{doctor}医生的角度分析患者需要忌口的食材属性，尽可能全面地列出食材类别，分类包括但不限于高糖、高脂肪、高蛋白、高钠、高嘌呤、高胆固醇、高盐、过酸、过甜等。不需要解释和举例子\n"
    lizi = f"给定学习的例子：输入：{disease}患者；输出：{disease}患者需要忌口：高糖类、高脂肪类、高热量密度食物、精制碳水化合物。仿照给定的例子学习输出格式。"
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
            time.sleep(3)
    time.sleep(3)

    t = {}
    t["dish"] = l["dish"]
    t["image"] = l["image"]
    t["disease"] = l["disease"]
    t["result"] = l["result"]
    t["wen_1"] = result
    print(t)

    temp = json.dumps(t, ensure_ascii=False)
    f = open(R"", "a", encoding="utf-8")
    f.write(temp + "\n")
    f.close()