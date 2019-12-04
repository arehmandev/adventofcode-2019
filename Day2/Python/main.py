from inspect import getsourcefile
from os.path import abspath, dirname


def calculate(input_data, noun, verb):

    iterator = 0
    input_list = input_data.split(",")
    input_list[1] = noun
    input_list[2] = verb

    while input_list[iterator] != "99":
        current_index = input_list[iterator]

        if current_index not in ["1", "2"]:
            iterator += 1
            continue
        first = int(input_list[int(input_list[iterator+1])])
        second = int(input_list[int(input_list[iterator+2])])
        third = int(input_list[iterator+3])

        if current_index == "1":
            input_list[third] = str(first + second)
        elif current_index == "2":
            input_list[third] = str(first * second)

        iterator += 4

    return input_list[0]


if __name__ == '__main__':
    path = dirname(abspath(getsourcefile(lambda: 0)))
    input_data_file = open(f"{path}/../input.txt")
    lines = input_data_file.read()
    input_data_file.close()

    print("Solution 1 -", calculate(lines, 12, 2))

    for i in range(100):
        for x in range(100):
            if calculate(lines, i, x) == "19690720":
                print("Solution 2 -", 100 * i + x)
                break
