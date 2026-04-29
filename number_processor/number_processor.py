class NumberProcessor:
    def __init__(self, file_name):
        self.file_name = file_name

    def process_numbers(self):
        squares = []
        cubes = []

        with open(self.file_name, 'r') as file:
            numbers = file.read().split()

            for num in numbers:
                num = int(num)
                if num % 2 == 0:
                    squares.append(str(num ** 2))
                else:
                    cubes.append(str(num ** 3))

        with open('double.txt', 'w') as file:
            file.write('\n'.join(squares))

        with open('triple.txt', 'w') as file:
            file.write('\n'.join(cubes))


if __name__ == "__main__":
    obj = NumberProcessor("integers.txt")
    obj.process_numbers()