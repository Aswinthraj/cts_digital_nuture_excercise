def display_cord(cords):
    if len(cords)!=2:
        print("Invalid Coordinates")
        return
    x,y=cords
    print(f"Coordinates of X is : {x}")
    print(f"Coordinates of y is : {y}")

coordinates=(10,20)
display_cord(coordinates)
