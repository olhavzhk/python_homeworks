new_number = "6705432166"


def check_phone_number(phone_number):
        if new_number.isnumeric() and len(phone_number) == 10:
            print("It is a valid phone number format.")
        else:
            print("The phone number format is not correct")


check_phone_number(new_number)
