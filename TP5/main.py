adj_list = []
num_nodes = 0
num_edges = 0
num_players = 0
num_teams = 0


# Returns the distance of the direct edge between two nodes, else -1
def weight(a, b):
    global adj_list
    global num_nodes
    global num_edges
    global num_players
    global num_teams
    for (x, y) in adj_list[a]:
        if x == b:
            return y
    return -1


def dijkstra_min(queue, distances):
    min = 99999
    min_index = -1
    for index, v in enumerate(queue):
        print(distances[v])
        if(distances[v] < min):
            min = distances[v]
            min_index = index

    return min_index


def dijkstra(start):
    global adj_list
    global num_nodes
    global num_edges
    global num_players
    global num_teams
    distances = [9999999] * (num_nodes + 1)
    distances[start] = 0
    queue = []
    queue.append(start)
    visited = []
    visited.append(start)

    min = 999999
    min_index = -1
    while(len(queue) != 0):
        current = queue.pop(dijkstra_min(queue, distances))
        visited.append(current)
        for (next_edge, weight) in adj_list[current]:
            queue.append(next_edge)
            print(next_edge)
            if(distances[next_edge] > distances[current] + weight):
                distances[next_edge] = distances[current] + weight

    print(distances)


def solve():
    return 0


def parse():
    global adj_list
    global num_nodes
    global num_edges
    global num_players
    global num_teams
    with open("ex1.in") as f:
        lines = f.read().splitlines()
        num_nodes, num_players, num_teams, num_edges = [
            int(x) for x in lines[0].split()]
        adj_list = [[] for _ in range(0, num_nodes + 1)]
        for i in range(1, num_edges + 1):
            cur_edge, next_edge, weight = (int(x) for x in lines[i].split())
            adj_list[cur_edge].append((next_edge, weight))
    f.close()


if __name__ == "__main__":
    parse()
    print(dijkstra(1))
