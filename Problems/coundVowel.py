string = "AlokrAI"#6
count=0
for i in string:
    if i.lower() in ("a","e","i","o","u") and i.upper() in ("A","E","I","O","U"):
        count += 1

print(count)