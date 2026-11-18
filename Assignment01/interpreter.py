expression = input("Enter your expression: ").strip()
x, y, z = expression.split(" ")
x = int(x)
z = int(z)
while True:
    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        if z != 0:
            result = x / z
        else:
            print("Error: Division by zero.")
            break
    else:
        print("Error: Invalid operator.")
        break

    print(f"Result: {result}")
    break