def main():
    camelName = input("Enter a camelName: ")
    name = snake_name(camelName)
    print(name)

def snake_name(camelName):
    for i in camelName:
        if i.isupper():
            camelName = camelName.replace(i, "_" + i.lower())
            return camelName

if __name__ == "__main__":
    main()