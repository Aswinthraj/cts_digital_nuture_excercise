def weight_convertor():
    weight=input("Enter the weigth in kg :")
    try:
        kg=float(weight)
        if kg<=0:
            print("Invalid weight")
            return
        lbs=kg*2.20462
        print(f"Weight in Pounds :{lbs:.2f}")
    except ValueError:
        print("Invalid input")
weight_convertor()