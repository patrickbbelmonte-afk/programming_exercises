class LifeWriter:
    def __init__(self, file_name="mylife.txt"):
        self.file_name = file_name

    def write_lines(self):
        with open(self.file_name, 'w') as file:
            while True:
                line = input("Enter line: ")

                # capitalize first letter
                line = line.capitalize()
                file.write(line + "\n")

                choice = input("Are there more lines y/n? ").lower()
                if choice != 'y':
                    break


if __name__ == "__main__":
    obj = LifeWriter()
    obj.write_lines()