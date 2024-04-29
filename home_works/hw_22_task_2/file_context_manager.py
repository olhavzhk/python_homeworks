import logging


class FileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.counter = 0
        self.logger = logging.getLogger(__name__)

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        self.counter += 1
        self.logger.info(f"File {self.filename} opened. Counter: {self.counter}")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.counter -= 1
        self.logger.info(f"File {self.filename} closed. Counter: {self.counter}")
        if exc_type is not None:
            self.logger.error(f"Exception occurred: {exc_val}")
        return True
