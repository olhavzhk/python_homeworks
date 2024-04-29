class CustomException(Exception):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg
        with open("logs.txt", "a") as file:
            file.write(msg + "\n")


try:
    raise CustomException("custom error message")
finally:
    pass






