def main():
    vanity_plate = input("Enter a vanity plate: ")
    validated_plate = validate_vanity_plate01(vanity_plate)
    validated_plate = validate_vanity_plate02(validated_plate)
    print("Valid vanity plate:", validated_plate)

def validate_vanity_plate01(vanity_plate):
    if 2 <= len(vanity_plate) <= 6 and vanity_plate.isalnum() and vanity_plate[:2].isalpha():
        return vanity_plate
    else:
        print("Invalid vanity plate. Please ensure it is 2-6 characters long, starts with two letters, and contains only alphanumeric characters.")
        return None

def validate_vanity_plate02(vanity_plate):
    for i in vanity_plate:
        if i.isdigit():
            if i == '0' and vanity_plate[vanity_plate.index(i) - 1].isalpha():
                print("Invalid vanity plate. Numbers cannot start with 0.")
                return None
            else:
                if vanity_plate[vanity_plate.index(i):].isdigit():
                    print("valid. ")
                    return vanity_plate
                else:
                    print("Invalid vanity plate. Numbers must be at the end of the plate.")
                    return None
        else:
            continue
    print("Valid vanity plate.")
    return vanity_plate

if __name__ == "__main__":
    main()
