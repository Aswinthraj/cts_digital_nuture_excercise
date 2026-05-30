def check_mark(mark):
    if mark < 0 or mark >100:
        print("Invalid Mark")
        return
    if mark >=50:
        print("Pass")
    if mark <50:
        print("Fail")
mark=75
check_mark(mark)
    