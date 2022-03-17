adj_list = []
num_nodes = 0
num_edges = 0
num_players = 0
num_teams = 0

#création team 
list_of_team = [[] for i in range(num_teams)]

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
    for i in range(1, num_nodes + 1):
        queue.append(i)

    min = 999999
    min_index = -1
    while(len(queue) != 0):
        current = queue.pop(dijkstra_min(queue, distances))
        for (next_edge, weight) in adj_list[current]:
            if(next_edge in queue):
                print(next_edge)
                if(distances[next_edge] > distances[current] + weight):
                    distances[next_edge] = distances[current] + weight

    print(distances)

# --------- Calculs des distances/communications ---------
def calculate_distances_AtoP():
    #Faire une liste :
        #Caluler la distance entre l'Arbtre et chaque joueur
    return 0

def calculate_distances_PtoA():
    #Faire une liste :
        #Caluler la distance entre chaque joueur et l'Arbtre
    return 0
    
def calculate_distances_P():
    #Faire une liste :
        #Sommer les distances entre le joueur et l'Arbtre
    return 0

def calculate_min_distances(list_of_team):
    #Calculer l'équipe avec les communications minimales
    return []
# ------- Fin des Calculs des distances/communications -------

# Algo pour les commmunications intra team
def make_team(distances) : 
    dist_arb = distances.sort(reverse=True)

    #On les sépare en p équipes
    for i in range(num_teams):
        #On prend les premiers sommet ayant une distance max avec l'arbitre et on les met dans p différentes équipes
        list_of_team[i].append(dist_arb.pop())
    
    #VERSION 1.0 On compare les comparaisons entre player et team_n
        # On le met dans la team ayant avec player les communications minimales
        # Si égalité, on le met dans la première team des égalités

    #VERSION 2.0 On prend le joueur avec la plus petite communication avec l'arbitre
         # Et on l'ajoute à la team_n ayant le plus petit nombre de communications actuel
         # Et on actualise et on refait tant qu'il y a des joueurs sans teams
    while(dist_arb.len() > 0):
        dist_arb.append(calculate_min_distances())

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
