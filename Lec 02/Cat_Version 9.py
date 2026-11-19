def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            return n  # 既有break的作用，还返回了 n 值，完成了函数的输出

def meow(n):
    print("meow\n" * n, end="")

if __name__ == "__main__":
    main()