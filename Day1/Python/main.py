from inspect import getsourcefile
from os.path import abspath, dirname


def calculate(input_data):
    counter = 0
    counter_two = 0
    for mass in input_data:
        mass = int((int(mass)/3) - 2)
        counter += mass
        counter_two += mass

        while int((mass/3) - 2) > 0:
            counter_two += int(mass/3) - 2
            mass = mass/3 - 2

    print(f"Part 1 - {counter}")
    print(f"Part 2 - {counter_two}")


if __name__ == '__main__':
    path = dirname(abspath(getsourcefile(lambda: 0)))
    input_data_file = open(f"{path}/../input.txt")
    lines = input_data_file.readlines()
    input_data_file.close()
    calculate(lines)
