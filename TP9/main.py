import sys

nb_colors, max_domino_num, max_line_length, nb_dominoes = 0, 0, 0, 0

# List of lists : Color, Up, Right, Down, Left
dominoes = []
up = {}
right = {}
down = {}
left = {}
map = []


def parse():
    global nb_colors, max_domino_num, max_line_length, nb_dominoes, dominoes
    global up, right, down, left
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        nb_colors, max_domino_num, max_line_length, nb_dominoes = [
            int(x) for x in lines[0].split()]
        for i in range(1, nb_dominoes + 1):
            dominoes.append([int(x) for x in lines[i].split()])
            n = dominoes[i - 1][1]
            if(up[n]):
                up[n].append(i - 1)
            else:
                up[n] = [i - 1]
            n = dominoes[i - 1][2]
            if(right[n]):
                right[n].append(i - 1)
            else:
                right[n] = [i - 1]
            n = dominoes[i - 1][3]
            if(down[n]):
                down[n].append(i - 1)
            else:
                down[n] = [i - 1]
            n = dominoes[i - 1][4]
            if(left[n]):
                left[n].append(i - 1)
            else:
                left[n] = [i - 1]
    return


def brute():
    global nb_colors, max_domino_num, max_line_length, nb_dominoes, dominoes, map
    global up, right, down, left
    map.append([-1] * max_line_length)
    used_dominoes = []
    cur_height = 0

    while len(used_dominoes) < nb_dominoes:
        #print("Height is : " + str(cur_height))
        for i in range(0, max_line_length):
            flag = True
            # If line is bottom, we can put any number on it
            if i == 0:
                if cur_height == 0:
                    used_dominoes.append(0)
                    map[cur_height][i] = 0
                    flag = False
                else:
                    if len(down[dominoes[map[cur_height-1][i]][1]]) > 0:
                        index = down.pop(
                            dominoes[map[cur_height-1][i]][1])[0]
                        if not index in used_dominoes:
                            used_dominoes.append(index)
                            map[cur_height][i] = index
                            flag = False
                            break

            else:
                if len(left[dominoes[map[cur_height][i-1]][2]]) > 0:
                    index = down.pop(
                        dominoes[map[cur_height][i-1]][2])[0]
                    if not index in used_dominoes:
                        used_dominoes.append(index)
                        map[cur_height][i] = index
                        flag = False
                        break
                else:
                    # for j in range(0, nb_dominoes):
                    #     if j not in used_dominoes and dominoes[j][3] == dominoes[map[cur_height-1][i]][1] and dominoes[j][4] == dominoes[map[cur_height][i-1]][2]:
                    #         #print("Added domino 4 : " + str(j))
                    #         used_dominoes.append(j)
                    #         map[cur_height][i] = j
                    #         flag = False
                    #         break
                    # Check if there is
                    if len(left[dominoes[map[cur_height][i-1]][2]]) > 0 and len(down[dominoes[map[cur_height-1][i]][1]]) > 0:
                        for i in left[dominoes[map[cur_height][i-1]][2]]:
                            for j in down[dominoes[map[cur_height-1][i]][1]]:
                                if i == j:
                                    used_dominoes.append(i)
                                    map[cur_height][i] = i
                                    flag = False
                                    break
                                else:
                                    print("No more dominoes")
                                    continue

        if(flag):
            print("No dominoes can be added")
            return
        map.append([-1] * max_line_length)
        cur_height += 1
    output(map)


def output(map):
    fname = sys.argv[1].split('.')[0] + '.out'
    f = open(fname, "w")
    for t in zip(*map):
        print(*t, file=f)
    return


if __name__ == "__main__":
    parse()
    brute()
