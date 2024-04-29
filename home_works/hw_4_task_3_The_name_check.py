def check_name(name):
    stored_name = "olha"
    if stored_name == str(name).lower():
        print("True")
    else:
        print("False")



check_name(name=input("Please, enter your name: "))


