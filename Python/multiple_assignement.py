def display_coordinates(cords):
    if len(cords) !=2:
        print("Invalid Coordinates")
        return
    x,y=cords
    print(f"X Coordinates:{x}")
    print(f"Y Coordinates:{y}")

cordinates=(10,20)
display_coordinates(cordinates)