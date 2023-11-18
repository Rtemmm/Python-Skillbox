class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
        except FileNotFoundError:
            self.file = open(self.filename, 'w+')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return True


with File('test.txt', 'r') as f:
    print(f.read())
