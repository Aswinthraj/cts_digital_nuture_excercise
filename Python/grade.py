def grade(mark):
    if mark <0 or mark >100:
        print("Invalid Mark")
        return
    if mark >=90:
        print("Grade A")
    elif mark >=75:
        print("Grade B")
    else:
        print("Grade C")
mark=88
grade(mark)