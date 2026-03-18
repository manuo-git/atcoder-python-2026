import json
snipet = "C:\\Users\\saintmanuo\\AppData\\Roaming\\Code\\User\\snippets\\python.json"

mac = []
with open(snipet) as f:
    d = json.load(f)
    mac = d["Macro"]["body"]
mac.pop()

answer = "D:\\PythonScripts\\atcoder\\python\\src\\python\\answer.py"
with open(answer, mode = "w") as f:
    for l in mac:
        f.write(l+"\n")