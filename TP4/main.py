
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

with open("example.in") as f:
    lines = f.readlines()
    # Format : First line : rows, columns, drones, turns, max payload
    rows, columns, drones, turns, max_payload = [
        int(x) for x in lines[0].split()]

    drone_status = [0 for i in range(drones)]

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


def next_turn():
    for i in range(0, len(drone_status)):
        drone_status[i] -= 1


def free_drone():
    for index, val in enumerate(drone_status):
        if val == 0:
            return index
    return -1


def assign_drone(index):

    return 0


def solve():
    turns_counter = 0
    while turns_counter != turns:
        drone_to_assign = free_drone()
        if(drone_to_assign == -1):
            print("Error")
            exit(1)
        assign_drone(drone_to_assign)
        # After turn, call next_turn

        next_turn()
