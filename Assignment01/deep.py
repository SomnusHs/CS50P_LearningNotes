def main():
    answer = input("What's your comprehension about life and the universe? ").lower().strip()
    if answer == "42":
        print("Correct! The answer to life, the universe, and everything is 42.")
    else:
        print("Incorrect. The answer to life, the universe, and everything is 42.")

if __name__ == "__main__":
    main()