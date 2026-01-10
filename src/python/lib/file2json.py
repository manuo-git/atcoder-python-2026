lines = []

with open("answer.py", mode = "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("lib/result.txt", mode = "w", encoding="utf-8") as f:
    for li in lines:
        nli = "\""
        for c in li:
            if c == "\t":
                nli += "    "
            elif c == "\n":
                break
            elif c == "\"":
                nli += "\\\""
            else:
                nli += c
        nli += "\",\n"
        f.write(nli)