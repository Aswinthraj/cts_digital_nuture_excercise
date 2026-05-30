def oddoreven(num):

    if num<0:
        print("Invalid number")
        return
    remainder=num%2
    if remainder==0:
        print("Even")
    else:
        print("Odd")   

num=17
oddoreven(num)         