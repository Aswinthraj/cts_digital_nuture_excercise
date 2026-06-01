from math import *
def math_op(num):
    if num<=0:
        print("Invalid Number")
        return
    
    print(f"Square root  : {sqrt(num):.2f}")
    print(f"Power (num² ) : {pow(num,2):.2f}")
    print(f"Square root Pi : {pi:.2f}")

num=16
math_op(num)    