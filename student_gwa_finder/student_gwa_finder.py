class StudentGWA:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_highest_gwa(self):
        highest_name = ""
        highest_gwa = -1  # better starting value

        with open(self.file_name, 'r') as file:
            for line in file:
                name, gwa = line.strip().split(',')
                gwa = float(gwa)

                if gwa > highest_gwa:
                    highest_gwa = gwa
                    highest_name = name

        print(f"Top Student: {highest_name} ({highest_gwa})")


if __name__ == "__main__":
    obj = StudentGWA("students.txt")
    obj.get_highest_gwa()