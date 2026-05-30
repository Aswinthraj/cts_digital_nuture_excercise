def login(user,pwd):
    if user=="" or pwd=="":
        print("Invalid User")
        return
    if user=='admin':
        if pwd=="pass123":
           print("Login Successful")
        else:
            print("Invalid Login")

    else:
        print("Invalid Username")
user="admin"
pwd="pass123"
login(user,pwd)