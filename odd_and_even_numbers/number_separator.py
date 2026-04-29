class NumberSeparator:
    def __init__(self, input_file):
        self.input_file = input_file

    def separate_numbers(self):
        even_numbers = []
        odd_numbers = []

        try:
            with open(self.input_file, 'r') as file:
                content = file.read()

                # Replace commas and newlines with spaces
                numbers = content.replace(',', ' ').split()

                for num in numbers:
                    num = int(num)
                    if num % 2 == 0:
                        even_numbers.append(str(num))
                    else:
                        odd_numbers.append(str(num))

            with open('even.txt', 'w') as even_file:
                even_file.write('\n'.join(even_numbers))

            with open('odd.txt', 'w') as odd_file:
                odd_file.write('\n'.join(odd_numbers))

            print("Files created successfully!")

        except FileNotFoundError:
            print(f"Error: {self.input_file} not found.")
        except ValueError:
            print("Error: File contains non-integer values.")


if __name__ == "__main__":
    obj = NumberSeparator("numbers.txt")
    obj.separate_numbers()