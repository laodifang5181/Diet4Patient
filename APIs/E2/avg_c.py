import json

total = 1500

f = open(R"D:\fei\course\新多模态推理\EE\E4\gpt4o\gpt4o_tu1_c.jsonl", 'r', encoding="utf-8")
lines = f.readlines()
f.close()
ct = 0.0

for line in lines[:]:
    l = json.loads(line)
    c = l["c"]
    ct = ct + float(c)
avg_c = ct/total    
print(avg_c)