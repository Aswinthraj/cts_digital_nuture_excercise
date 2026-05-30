def integer_division(total_bill,people):

    if total_bill<=0:
        print("Invalid Bill")
        return
    if people<=0:
        print("Invalid People")
        return
    share=total_bill//people
    print(f"Indiduval Share is  : {share}")
total_bill=1250
people=4
integer_division(total_bill,people)

