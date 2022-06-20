from node import node

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
    nodes.append(node(51.5007, 0.1246))
    nodes.append(node(40.6892, 74.0445, nodes[0]))
    nodes.append(node(0, 0, (nodes[0], nodes[1])))

    print("Distance: ", node.get_distance(nodes[0], nodes[1]), "km")

    for x in nodes:
        if x.parent != None:
            print()
