zakupy = {
    "piekarnia": ["chleb", "bulka","paczek"],
    "warzywniak": ["marchew","seler", "rukola"]
}


print("Lista zakupow")
for i in zakupy:
    print(f"Ide do {i.capitalize()}, kupuje tu nastepujace rzeczy {str(zakupy[i]).title()}")

items = [len(x) for x in zakupy.values()]
print(f"W sumie kupuje {sum(items)} produktow")




print("Commit 1 jak i rowniez Commit 2")