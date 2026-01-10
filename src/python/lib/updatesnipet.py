lines = []

with open("C:\\Users\\saintmanuo\\AppData\\Roaming\\Code\\User\\snippets\\python.json", encoding="utf-8") as f:
    lines = f.readlines()

with open("D:\\PythonScripts\\atcoder\\python\\snippets.json", "w", encoding="utf-8") as f:
    f.writelines(lines)
