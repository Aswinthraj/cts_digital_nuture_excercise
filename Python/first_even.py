def first_even(range_size):
    if range_size <0:
        print("Invalid Range")
        return
    for i in range(range_size):
        if i%2==0:
            print(f"First Even Number : {i}")
            break
range_size=10
first_even(range_size)