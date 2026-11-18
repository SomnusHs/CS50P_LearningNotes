name = input("What is your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case "Luna":
        print("Ravenclaw")
    case "Cedric":
        print("Hufflepuff")
    case _:
        print("Who?")