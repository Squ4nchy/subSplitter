class InputFile:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file_contents = self.read_file_contents()

    def read_file_contents(self):
        with open(self.file_path, 'r', encoding='utf8') as f:
            return f.read()
