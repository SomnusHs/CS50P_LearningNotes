def main():
    Greeting = input("What's your greeting? ").lower().strip()
    if Greeting == "hello":
        print("$0")
    elif Greeting[0] == "h":
        print("$20")
    else:
        print("$100")

main()
