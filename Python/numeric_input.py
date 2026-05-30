def numeric_input():
    age=input("Enter the age : ")

    if not age.isdigit():
        print("Invalid Digit")
        return
    age=int(age)
    print(f"Next year you'll be {age+1}")
numeric_input()