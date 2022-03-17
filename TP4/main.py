
from fileinput import close
from glob import glob
import math
import sys

warehouse_coords = []
warhouse_products = []
order_coords = []
order_quantity = []
order_items = []
number_products = 0
product_weights = []
num_warehouses = 0
num_orders = 0
rows, columns, drones, turns, max_payload = 0, 0, 0, 0, 0
drone_status = []
drone_coords = []
priority_orders = []
total_commands = 0
res_string = ""


def output():
    global res_string

    res_string = str(total_commands) + "\n" + res_string
    with open("output.out", "w") as f:
        f.write(res_string)
        f.close()


def game_over():
    print("We finished everything")
    output()
    exit(0)


def next_turn():
    for i in range(0, len(drone_status)):
        drone_status[i] -= 1


def free_drone():
    for index, val in enumerate(drone_status):
        if val == 0:
            return index
    return -1


def free_drone_excluded(excluded_drone):
    for index, val in enumerate(drone_status):
        if val == 0 and index != excluded_drone:
            return index
    return -1


def order_weight(order_index):
    order_products = order_items[order_index]
    weight = 0
    for product in order_products:
        weight += product_weights[product]
    return weight


def move_drone(drone_index, x, y):
    print("Moving drone " + str(drone_index) + " to " + str(x) + " " + str(y))
    return 0


def load_product(drone_index, warehouse_index, product_index):
    global total_commands
    total_commands += 1
    print("Loading product " + str(product_index) +
          " from warehouse " + str(warehouse_index))
    # with open("output.out", "a") as f:
    #     f.write(
    #         f"{str(drone_index)} L {str(warehouse_index)} {str(product_index)} 1\n")
    #     f.close()
    global res_string
    res_string += f"{str(drone_index)} L {str(warehouse_index)} {str(product_index)} 1\n"
    return 0


def deliver_product(drone_index, order_index, product_index):
    global total_commands
    total_commands += 1
    print("Drone " + str(drone_index) + " delivering product " + str(product_index) +
          " to order " + str(order_index))
    if(order_quantity[order_index] == 0):
        print("Order " + str(order_index) + " is now fullfilled")
    # with open("output.out", "a") as f:
    #     f.write(
    #         f"{str(drone_index)} D {str(order_index)} {str(product_index)} 1\n")
    #     f.close()
    global res_string
    res_string += f"{str(drone_index)} D {str(order_index)} {str(product_index)} 1\n"

    return 0


def distance(x1, y1, x2, y2):
    # Euclidean distance
    # Formula : sqrt(abs(x1-x2)^2 + abs(y1-y2)^2)
    t = math.sqrt(math.pow(abs(x1-x2), 2) + math.pow(abs(y1-y2), 2))
    return int(math.ceil(t))


def distance_drone_warehouse(drone_index, warehouse_index):
    return distance(drone_coords[drone_index][0], drone_coords[drone_index][1],
                    warehouse_coords[warehouse_index][0], warehouse_coords[warehouse_index][1])


def distance_drone_order(drone_index, order_index):
    return distance(drone_coords[drone_index][0], drone_coords[drone_index][1],
                    order_coords[order_index][0], order_coords[order_index][1])


def best_warehouse_for_product(drone_index, product_index):
    best_warehouse_index = 0
    best_warehouse_distance = 1000000
    for i in range(0, len(warehouse_coords)):
        warehouse_distance = distance(
            drone_coords[drone_index][0], drone_coords[drone_index][1], warehouse_coords[i][0], warehouse_coords[i][1])
        if(warehouse_distance < best_warehouse_distance and warhouse_products[i][product_index] > 0):
            best_warehouse_index = i
            best_warehouse_distance = warehouse_distance
    return best_warehouse_index


def order_weight(order_index):
    order_products = order_items[order_index]
    weight = 0
    for product in order_products:
        weight += product_weights[product]
    return weight


def best_order(drone_index):
    # v1 : Get the order with the min distance to drone

    # best_order_index = -1
    # best_order_distance = 1000000
    # for i in range(0, len(order_coords)):
    #     if order_quantity[i] > 0:
    #         order_distance = distance(
    #             drone_coords[drone_index][0], drone_coords[drone_index][1], order_coords[i][0], order_coords[i][1])
    #         if(order_distance < best_order_distance):
    #             best_order_index = i
    #             best_order_distance = order_distance
    # if best_order_index == -1:
    #     print("No more orders !!")
    #     game_over()
    # return best_order_index

    # v2 : Get the order with the min weight
    best_order_index = -1
    best_order_weight = 1000000
    cur_order_weight = 0
    for i in range(0, len(order_coords)):
        if order_quantity[i] > 0:
            cur_order_weight = order_weight(i)
            if(cur_order_weight < best_order_weight):
                best_order_index = i
                best_order_weight = cur_order_weight
    if best_order_index == -1:
        print("No more orders !!")
        game_over()

    return best_order_index


def best_first_product(drone_index, order_index):
    # Just get the min weight product of the order
    min = 999999999
    min_index = -1
    for index, item in enumerate(order_items[order_index]):
        if(product_weights[item] < min):
            min = product_weights[item]
            min_index = index
    return min_index


def load_more(warehouse_index, cur_weight, order_index):
    to_load = []
    temp_warehouse_products = warhouse_products[warehouse_index].copy()
    for index, item in enumerate(order_items[order_index]):
        if(temp_warehouse_products[item] > 0):
            if cur_weight + product_weights[item] <= max_payload:
                to_load.append(item)
                cur_weight += product_weights[item]
                temp_warehouse_products[item] -= 1

    return to_load


def assign_drone(index):
    print("----------------------------------------------------")
    print("Assigning drone " + str(index))
    print("Coords: " + str(drone_coords[index]))
    best_order_index = best_order(index)
    best_first_product_index = best_first_product(index, best_order_index)
    order_item_index = order_items[best_order_index].pop(
        best_first_product_index)
    cur_drone_weight = product_weights[order_item_index]
    order_quantity[best_order_index] -= 1
    best_warehouse_index = best_warehouse_for_product(index, order_item_index)
    warhouse_products[best_warehouse_index][order_item_index] -= 1
    distance = distance_drone_warehouse(index, best_warehouse_index)
    if distance > 0:
        move_drone(index, warehouse_coords[best_warehouse_index]
                   [0], warehouse_coords[best_warehouse_index][1])
    load_product(index, best_warehouse_index, order_item_index)
    # Check if warehouse has other products from the order
    to_load = load_more(best_warehouse_index,
                        cur_drone_weight, best_order_index)
    print("To load: " + str(to_load))
    for item in to_load:
        order_items[best_order_index].remove(item)
        load_product(index, best_warehouse_index, item)
        order_quantity[best_order_index] -= 1
        print("Removing item " + str(item) + " From warehouse")
        print(warhouse_products[best_warehouse_index])
        warhouse_products[best_warehouse_index][item] -= 1
    drone_status[index] = distance
    drone_coords[index] = warehouse_coords[best_warehouse_index]
    print("Drone is at Warehouse. Now moving to delivery")
    distance = distance_drone_order(index, best_order_index)
    move_drone(index, order_coords[best_order_index]
               [0], order_coords[best_order_index][1])
    drone_status[index] += distance
    drone_coords[index] = order_coords[best_order_index]
    deliver_product(index, best_order_index, order_item_index)
    for item in to_load:
        deliver_product(index, best_order_index, item)
    print("Drone is at order coordinates. Delivered product")
    print("----------------------------------------------------\n")
    return 0


def solve():
    turns_counter = 0
    while turns_counter != turns:
        print("Current turn : " + str(turns_counter))
        drone_to_assign = free_drone()
        if(drone_to_assign == -1):
            # No more drones available
            next_turn()
            turns_counter += 1
        else:
            assign_drone(drone_to_assign)

    game_over()


with open(sys.argv[1]) as f:
    # with open(str(sys.argv[1])) as f:
    lines = f.readlines()
    # Format : First line : rows, columns, drones, turns, max payload
    rows, columns, drones, turns, max_payload = [
        int(x) for x in lines[0].split()]

    drone_status = [0 for i in range(drones)]

    drone_coords = [[0, 0] for i in range(drones)]

    # Format : Second line : product weights
    number_products = int(lines[1])

    # Format : Third line : product weights
    product_weights = [int(x) for x in lines[2].split()]

    num_warehouses = int(lines[3])

    i = 0
    cur_line = 4
    while i != num_warehouses:
        warehouse_coords.append([int(x) for x in lines[cur_line].split()])
        cur_line += 1
        warhouse_products.append([int(x) for x in lines[cur_line].split()])
        cur_line += 1
        i += 1

    num_orders = int(lines[cur_line])
    cur_line += 1

    i = 0
    while i != num_orders:
        order_coords.append([int(x) for x in lines[cur_line].split()])
        cur_line += 1
        order_quantity.append(int(lines[cur_line]))
        cur_line += 1
        order_items.append([int(x) for x in lines[cur_line].split()])
        cur_line += 1

        i += 1

    total_commands = 0

    '''
    print(rows, columns, drones, turns, max_payload)
    print(number_products)
    print(product_weights)
    print(warehouse_coords)
    print(warhouse_products)
    print(num_orders)
    print(order_coords)
    print(order_quantity)
    print(order_items)
    print(drone_status)
    '''
    solve()
    f.close()
    exit(0)
