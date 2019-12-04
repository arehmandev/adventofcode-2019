from inspect import getsourcefile
from os.path import abspath, dirname


def iterator(position, index, quantity, multiple, tuple_dict, counter):
    last_entry = None

    for i in range(quantity*(multiple*multiple)):
        i = i + 1
        counter += 1

        entry = [None] * 2
        entry[index] = (multiple * i) + position[index]
        entry[1-index] = position[1-index]
        entry = tuple(entry)
        tuple_dict[entry] = counter
        last_entry = entry
    return tuple_dict, entry, counter


def create_dict(inst_list):
    current_position = [0, 0]
    mega_dict = dict()
    counter = 0

    for item in inst_list:
        split = list(item)
        direction = split[0]
        quantity = int("".join(split[1:]))

        if direction == "U":
            index = 1
            multiple = 1
        elif direction == "D":
            index = 1
            multiple = -1
        elif direction == "R":
            index = 0
            multiple = 1
        else:
            index = 0
            multiple = -1

        mega_dict, last_entry, counter = iterator(current_position, index,
                                                  quantity, multiple, mega_dict, counter)
        current_position = last_entry

    return mega_dict


def manhattan_distance(dict_one, dict_two):
    lowest = float('inf')
    lowest_intersection = float('inf')
    for key in dict_one.keys():
        if key in dict_two.keys():
            xdist = abs(key[0])
            ydist = abs(key[1])
            man_dist = xdist + ydist

            if man_dist < lowest:
                lowest = man_dist

            if dict_one[key] + dict_two[key] < lowest_intersection:
                lowest_intersection = dict_one[key] + dict_two[key]

    return lowest, lowest_intersection


if __name__ == "__main__":

    path = dirname(abspath(getsourcefile(lambda: 0)))
    input_data_file = open(f"{path}/../input.txt")
    lines = input_data_file.readlines()
    input_data_file.close()

    mega_dict_one = create_dict(lines[0].split(","))
    mega_dict_two = create_dict(lines[1].split(","))

    manhat_dist, lowest_intersection = manhattan_distance(
        mega_dict_one, mega_dict_two)

    print("Solution 1 -", manhat_dist)
    print("Solution 2 -", lowest_intersection)
