import json
import sys
import os
import GPT_4o

a = 0

f = open(R"", 'r', encoding="utf-8")
lines = f.readlines()
f.close()
f1 = open(R"", 'r', encoding="utf-8")
lines1 = f1.readlines()
f1.close()
for line in lines[:]:
    a = a + 1
    print(a) 
    l = json.loads(line)
    dish = l["dish"]
    tu_1 = l["tu_1"]

    for line1 in lines1:
        l1 = json.loads(line1)
        if l1["name"] == dish:
            ingredients = l1["ingredients"]
    print(ingredients)
    
    image=''
    prompt = f"对于{dish}这道菜所包含的食材，标注的标准答案为：{ingredients}，模型给出的答案为：{tu_1}。\n请你给出一个根据模型回答的句子完整度、流畅度和精确度等方面给出模型回答的置信度，范围在0到1之间，只需要给出小数不需要其他回复。"
    print(prompt)
    result = GPT_4o.callAPI_meta(prompt, image)
    print(result)

    t = {}
    t["dish"] = l["dish"]
    # t["image"] = l["image"]
    # t["ingredients"] = ingredients
    t["tu_1"] = tu_1
    t["c"] = result
    print(t)

    temp = json.dumps(t, ensure_ascii=False)
    f = open(R"", "a", encoding="utf-8")
    f.write(temp + "\n")
    f.close()