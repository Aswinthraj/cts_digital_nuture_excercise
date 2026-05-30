def sumoreven(rng):
    if rng<0:
        print("Invalid range")
        return
    total=0
    for i in range(10):
        if i%2==0:
            continue
        total+=i
    print(f"Sum of Odd Values :{total}")

rng=10
sumoreven(rng)