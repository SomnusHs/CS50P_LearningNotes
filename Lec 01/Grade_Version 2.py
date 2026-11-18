score = int(input("Enter your score: "))

if 90 <= score <= 100:
    print("Grade: A")
if 80 <= score < 90:
    print("Grade: B")
if 70 <= score < 80:
    print("Grade: C")
if 60 <= score < 70:
    print("Grade: D")
if score < 60:
    print("Grade: F")