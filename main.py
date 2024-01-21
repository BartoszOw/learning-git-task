zakupy = {
    "piekarnia": ["chleb", "bulka","paczek"],
    "warzywniak": ["marchew","seler", "rukola"]
}


print("Lista zakupow")
for i in zakupy:
    print(f"Ide do {i.capitalize()}, kupuje tu nastepujace rzeczy {str(zakupy[i]).title()}")