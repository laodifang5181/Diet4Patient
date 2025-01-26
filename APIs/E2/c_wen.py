import json
import sys
import os
import GPT_4o

a = 0

f = open(R"", 'r', encoding="utf-8")
lines = f.readlines()
f.close()
for line in lines[:]:
    a = a + 1
    print(a) 
    l = json.loads(line)
    dish = l["dish"]
    disease = l["disease"]
    wen = l["model_result"]
    
    image=''
    prompt = f"对于在{dish}这道菜中{disease}疾病所忌口的食材，模型给出的答案为：\n{wen}。\n请你根据模型回复忌口的精确度给出模型回答的置信度。范围在0到1之间，直接给出你认为的小数不要解释。"
    result = GPT_4o.callAPI_meta(prompt, image)

    t = {}
    t["dish"] = l["dish"]
    t["disease"] = l["disease"]
    t["wen"] = wen
    t["c"] = result
    print(t)

    temp = json.dumps(t, ensure_ascii=False)
    f = open(R"", "a", encoding="utf-8")
    f.write(temp + "\n")
    f.close()