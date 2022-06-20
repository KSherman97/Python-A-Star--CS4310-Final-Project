from node import node
from astar import astar
from graph import graph

def test():
    node1 = node(51.5007, 0.1246)
    node2 = node(40.6892, 74.0445)

    print("Distance: ", node.get_distance(node1, node2), "km")

if __name__ == "__main__":
    test() # this is a test function. Should return 5,574.8405 km

    # perform main driver functions here
    # A* algorithm uses F = H + G
    # H = Heuristic - distance from current node to the end node
    # G = Distance from the current node to the starting node
    # F represents the total cost of the current node

    # create an array of nodes
    nodes = []
    nodes.append(node(0, 0, start = True)) # 0 START NODE

    nodes.append(node(1, 0, nodes[0])) # 1
    nodes.append(node(1, 1, nodes[0])) # 2

    nodes.append(node(2, 0, nodes[1])) # 3
    nodes.append(node(2, 1, nodes[1])) # 4
    nodes.append(node(2, 2, nodes[2])) # 5
    nodes.append(node(2, 3, nodes[2])) # 6

    nodes.append(node(3, 0, (nodes[0], nodes[3], nodes[4], nodes[5], nodes[6]), goal = True)) # 7 END NODE

    for i in nodes:
        if i.goal==True:
            print(i.lat, i.long)

    ## PERFORM ALGORITHM HERE
    closed_nodes = []
    opened_nodes = [nodes[0]]

    while len(opened_nodes) > 0:
        print("test")
        opened_nodes.pop()
