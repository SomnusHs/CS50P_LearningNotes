def main():
    text = input("Enter text: ")
    text = shorten(text)
    print("text")

def shorten(str):
    rules = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for i in str:
        if i in rules:
            str = str.replace(i, "")
            return str
        else:
            return str

if __name__ == "__main__":
    main()