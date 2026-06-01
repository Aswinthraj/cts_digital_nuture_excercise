def add(num1,num2):
    if num1<0 or num2<0:
        print("Invalid Number")
        return
    
    return num1+num2
result=add(5,7)
print(f"Sum : {result}")