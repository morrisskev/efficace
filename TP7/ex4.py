import sys

nb_in = 0
nb_out = 0
times_in = []
times_out = []
number_times = [0] * 1000


def solve():
    global nb_in, nb_out, times_in, times_out, number_times
    for i in range(0, nb_in):
        for j in range(0, nb_out):
            diff = times_out[j] - times_in[i]
            if diff > 0:
                number_times[diff] += 1

    return number_times.index(max(number_times))


def parse():
    global nb_in, nb_out, times_in, times_out
    with open(sys.argv[1], "r") as f:
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
