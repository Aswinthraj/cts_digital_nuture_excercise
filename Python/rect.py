def area(length,width):

    if length <=0 or width<=0:
        print("Invalid input")
        return
    return length+width

result=area(5,7)
print(f"Area Of Rectangle : {result}")