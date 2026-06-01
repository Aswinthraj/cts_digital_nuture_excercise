import math
def validate_circle(radius):
    if radius<=0:
        print("Invalid radius")
        return
    
    area=math.pi*radius**2
    print(f"Area Of Circle : {area:.2f}")
radius=5
validate_circle(radius)