import pyperclip

line = pyperclip.paste()
lines = line.split("\r\n")

with open("inout/input.txt", "w", encoding="utf-8") as f:
    for l in lines:
        f.write(l+"\n")
