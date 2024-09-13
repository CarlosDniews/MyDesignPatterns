class FileManager():

    def __init__(self, filePath, mode):
        self.file = open(filePath, mode)

    def getLinesFromFile(self):
        return self.file.readlines()

    def write(self, text):
        self.file.write(text)

    def close(self):
        self.file.close()