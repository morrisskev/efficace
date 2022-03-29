import sys

nb_in = 0
nb_out = 0
times_in = []
times_out = []
number_times = {

}


def solve():
    global nb_in, nb_out, times_in, times_out, number_times
    for i in range(0, nb_in):
        for j in range(0, nb_out):
            diff = times_out[j] - times_in[i]
            if diff > 0:
                if diff in number_times:
                    number_times[diff] += 1
                else:
                    number_times[diff] = 1

    # print(number_times)
    max_times = 0
    max_times_index = 0
    equal_values = {

    }
    for key in number_times:
        if number_times[key] == max_times:
            equal_values[key] = number_times[key]
        elif number_times[key] > max_times:
            equal_values = {}
            max_times = number_times[key]
            max_times_index = key

    if len(equal_values) == 0:
        return max_times_index
    else:
        return min(equal_values.keys())


def parse():
    global nb_in, nb_out, times_in, times_out
    file_name = "data-tp8/Cuisson/" + sys.argv[1]
    with open(file_name, "r") as f:
        data = f.readlines()
        nb_in = int(data[0])
        nb_out = int(data[1])
        times_in = [int(x) for x in data[2].split(" ")]
        times_out = [int(x) for x in data[3].split(" ")]


def main():
    parse()
    res = solve()
    print(res)


if __name__ == "__main__":
    main()
