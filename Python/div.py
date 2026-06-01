def division_error(num1,num2):
    
    try:
        result=num1/num2
        print(f"Result : {result}")
        
    except ZeroDivisionError:
        print("Divide By Zero Error")
division_error(10,2)