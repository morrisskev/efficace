import sys

nb_colors, max_domino_num, max_line_length, nb_dominoes = 0, 0, 0, 0

# List of lists : Color, Up, Right, Down, Left
dominoes = []
map = []


def parse():
    global nb_colors, max_domino_num, max_line_length, nb_dominoes, dominoes
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        nb_colors, max_domino_num, max_line_length, nb_dominoes = [
            int(x) for x in lines[0].split()]
        for i in range(1, nb_dominoes + 1):
            dominoes.append([int(x) for x in lines[i].split()])


def brute():
    global nb_colors, max_domino_num, max_line_length, nb_dominoes, dominoes, map
    map.append([-1] * max_line_length)
    used_dominoes = []
    cur_height = 0
    while len(used_dominoes) < nb_dominoes:
        print("Height is : " + str(cur_height))
        for i in range(0, max_line_length):
            # If line is bottom, we can put any number on it
            if i == 0:
                if cur_height == 0:
                    used_dominoes.append(0)
                    map[cur_height][i] = 0
                    break
                else:
                    for j in range(0, nb_dominoes):
                        if j not in used_dominoes and dominoes[j][3] == dominoes[map[cur_height][i]][1]:
                            print("Added domino 2 : " + str(j))
                            used_dominoes.append(j)
                            map[cur_height][i] = j
                            break
            else:
                if cur_height == 0:
                    for j in range(0, nb_dominoes):
                        if j not in used_dominoes and dominoes[j][4] == dominoes[map[cur_height][i-1]][2]:
                            print("Added domino 3 : " + str(j))
                            used_dominoes.append(j)
                            map[cur_height][i] = j
                            break
                else:
                    for j in range(0, nb_dominoes):
                        if j not in used_dominoes and dominoes[j][3] == dominoes[map[cur_height-1][i]][1] and dominoes[j][4] == dominoes[map[cur_height][i-1]][2]:
                            print("Added domino 4 : " + str(j))
                            used_dominoes.append(j)
                            map[cur_height][i] = j
                            break
        map.append([-1] * max_line_length)
        cur_height += 1
    return


if __name__ == "__main__":
    parse()
    brute()
