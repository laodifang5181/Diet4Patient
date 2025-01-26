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
    prompt = f"请你以美食评论家的角色，根据输入的图片和制作图中菜肴的关键核心食材，对食材进行合理分类，判断是否有食材属于下面类别：高糖、高脂肪、高蛋白、高钠、高嘌呤、高胆固醇。"
    lizi = "给定输出的例子： 输出：豆腐：不属于上述食材类别； 辣椒：不属于上述食材类别。仿照给定的例子学习输出格式。"
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
    t["tu_2"] = result
    print(t)

    temp = json.dumps(t, ensure_ascii=False)
    f = open(R"", "a", encoding="utf-8")
    f.write(temp + "\n")
    f.close()