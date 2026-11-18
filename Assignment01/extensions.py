def main():
    name = input("What's the name of the file? ")
    valid_extensions = ['.gif', '.jpg', '.jpeg', '.png', '.pdf', '.txt', '.zip']
    if name in valid_extensions:
        print(f"{name}")
    else:
        print(f"Your file extension is: application/octet-stream")

if __name__ == "__main__":
    main()