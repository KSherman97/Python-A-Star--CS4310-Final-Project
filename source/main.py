from node import *
from graph import *

# check if a neighbor should be added to the opened_nodes list
def append_open(opened_nodes, neighbor):
    for node in opened_nodes:
        if neighbor == node and neighbor.f > node.f:
            return False
    return True

def astar_search(graph, heuristics, start, end):
    # opened and closed node lists (initialize empty)
    opened_nodes = []
    closed_nodes = []

    # create the start and end nodes
    start_node = node(start, None)
    goal_node = node(end, None)

    # add the start node to the opened list
    opened_nodes.append(start_node)

    while len(opened_nodes) > 0:
        opened_nodes.sort() # sort the opened list to get the node w/ lowest cost first
        current_node = opened_nodes.pop(0) # current node is the node with the lowest cost
        closed_nodes.append(current_node) # add the current node to the closed list

        # base case
        # check if we have reached a goal, if yes then return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.name + ': ' + str(current_node.g))
                current_node = current_node.parent
            path.append(start_node.name + ': ' + str(start_node.g))

            # return the path, but reversed to correct order
            return path[::-1]

        neighbors = graph.get(current_node.name) # get all neighbors

        # loop neighbors
        for key, value in neighbors.items():
            neighbor = node(key, current_node) # create a neighbor node

            # check if neighbor is in the closed list
            if neighbor in closed_nodes:
                continue

            # calculate the full cost of the path
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = neighbor.g + neighbor.h

            # check for two conditions; both must be true
            # 1. neighbor is in the open list
            # 2. neighbor has a lower f value
            if append_open(opened_nodes, neighbor) == True:
                opened_nodes.append(neighbor)

    return None # return none if no path was found

# The main entry point for this module
def main():
    # Create a graph
    node_graph = graph()
    # Create graph connections (Actual distance)
    node_graph.connect('Frankfurt', 'Wurzburg', 111)
    node_graph.connect('Frankfurt', 'Mannheim', 85)
    node_graph.connect('Wurzburg', 'Nurnberg', 104)
    node_graph.connect('Wurzburg', 'Stuttgart', 140)
    node_graph.connect('Wurzburg', 'Ulm', 183)
    node_graph.connect('Mannheim', 'Nurnberg', 230)
    node_graph.connect('Mannheim', 'Karlsruhe', 67)
    node_graph.connect('Karlsruhe', 'Basel', 191)
    node_graph.connect('Karlsruhe', 'Stuttgart', 64)
    node_graph.connect('Nurnberg', 'Ulm', 171)
    node_graph.connect('Nurnberg', 'Munchen', 170)
    node_graph.connect('Nurnberg', 'Passau', 220)
    node_graph.connect('Stuttgart', 'Ulm', 107)
    node_graph.connect('Basel', 'Bern', 91)
    node_graph.connect('Basel', 'Zurich', 85)
    node_graph.connect('Bern', 'Zurich', 120)
    node_graph.connect('Zurich', 'Memmingen', 184)
    node_graph.connect('Memmingen', 'Ulm', 55)
    node_graph.connect('Memmingen', 'Munchen', 115)
    node_graph.connect('Munchen', 'Ulm', 123)
    node_graph.connect('Munchen', 'Passau', 189)
    node_graph.connect('Munchen', 'Rosenheim', 59)
    node_graph.connect('Rosenheim', 'Salzburg', 81)
    node_graph.connect('Passau', 'Linz', 102)
    node_graph.connect('Salzburg', 'Linz', 126)

    # Make graph undirected, create symmetric connections
    node_graph.make_undirected()

    # Create heuristics (straight-line distance, air-travel distance)
    heuristics = {}
    heuristics['Basel'] = 204
    heuristics['Bern'] = 247
    heuristics['Frankfurt'] = 215
    heuristics['Karlsruhe'] = 137
    heuristics['Linz'] = 318
    heuristics['Mannheim'] = 164
    heuristics['Munchen'] = 120
    heuristics['Memmingen'] = 47
    heuristics['Nurnberg'] = 132
    heuristics['Passau'] = 257
    heuristics['Rosenheim'] = 168
    heuristics['Stuttgart'] = 75
    heuristics['Salzburg'] = 236
    heuristics['Wurzburg'] = 153
    heuristics['Zurich'] = 157
    heuristics['Ulm'] = 0

    # Run the search algorithm
    path = astar_search(node_graph, heuristics, 'Frankfurt', 'Ulm')
    
    print("complete path:\n ")
    index = 0
    for i in path:
        print("step ", index, ": ", i)
        index += 1
    print()

# Tell python to run main method
if __name__ == "__main__":
    main()