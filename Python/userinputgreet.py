def userinput():
    name=input("Enter User name  : ")

    if name=="":
        print("Invalid Username")
        return
    print(f"Hello, {name}")
userinput()    