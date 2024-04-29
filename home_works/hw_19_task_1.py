import re


class EmailClass:
    def __init__(self, email):
        self.email = email
        self.validate_email(email)

    @classmethod
    def validate_email(cls, email):
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            raise ValueError("Invalid email address format.")
        print("The format of this email address is valid.")


obj1 = EmailClass("#@example.com")
