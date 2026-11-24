#File Handling Using Constructor and Destructor

class FileHandler:
    def __init__(self):
        self.file = open("data.txt", "w")

    def write_data(self, data):
        self.file.write(data)

    def __del__(self):
        self.file.close()
        print("File closed")


obj = FileHandler()
obj.write_data("Hello Python")

del obj