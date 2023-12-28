class FileRepository:
    def __init__(self, filename):
        self.filename = filename

    def read_lines(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]