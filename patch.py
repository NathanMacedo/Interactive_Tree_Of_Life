with open("d:/TreeOfLife/gen.py", "r", encoding="utf-8") as f:
    src = f.read()

# Replace curly/smart apostrophes (U+2019) with straight apostrophes
src = src.replace("\u2019", "\\'")

with open("d:/TreeOfLife/gen.py", "w", encoding="utf-8") as f:
    f.write(src)

print("Patched!")
