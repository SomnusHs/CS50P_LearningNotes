demonstrations = input("Enter your coins: ")
rules = [
    {"demonstration":"5", "remiander":"45"},
    {"demonstration":"10", "remiander":"40"},
    {"demonstration":"25", "remiander":"25"}, 
]

for i in rules:
    if demonstrations == i["demonstration"]:
        print(f"you should give {i["remiander"]} dollars")
        break
    elif int(demonstrations) >= 50:
        print(f"I will give you {int(demonstrations) - int(50)} dollars")
        break
    else:
        print("your demonstrations are invalid")
        break