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
                path.append('City: ' + current_node.name + ' - Distance ' + str(round(current_node.g, 2)) + ' km')
                current_node = current_node.parent
                
            path.append('City: ' + start_node.name + ' - Distance ' + str(round(start_node.g, 2)) + ' km')

            # return the path, but reversed to correct order
            return path[::-1]

        neighbors = graph.get(current_node.name) # get all neighbors

        # loop neighbors
        for key, value in neighbors.items():
            #print(key, value, current_node)
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

    # START AND GOAL CITIES
    start = 'Ulm'
    end = 'Frankfurt'

    coordinates = {}
    coordinates['Basel'] = (47.5581077,7.5878261)
    coordinates['Bern'] = (46.9482713,7.4514512)
    coordinates['Frankfurt'] = (50.1106444,8.6820917)
    coordinates['Karlsruhe'] = (49.0068705,8.4034195)
    coordinates['Linz'] = (48.3059078,14.286198)
    coordinates['Mannheim'] = (49.4892913, 8.4673098)
    coordinates['Munchen'] = (48.1371079, 11.5753822)
    coordinates['Memmingen'] = (47.9867696, 10.181319)
    coordinates['Nurnberg'] = (49.453872, 11.077298)
    coordinates['Passau'] = (48.5748229, 13.4609744)
    coordinates['Rosenheim'] = (47.8539273, 12.127262)
    coordinates['Stuttgart'] = (48.7784485, 9.1800132)
    coordinates['Salzburg'] = (7.7981346, 13.0464806)
    coordinates['Wurzburg'] = (49.79245, 9.932966)
    coordinates['Zurich'] = (47.376888, 8.541694)
    coordinates['Ulm'] = (48.399620, 9.996610)


    # Create a graph
    node_graph = graph()
    # Create graph connections (Actual distance)
    node_graph.connect('Frankfurt', 'Wurzburg', node.get_distance(coordinates['Frankfurt'], coordinates['Wurzburg'])) #
    node_graph.connect('Frankfurt', 'Mannheim', node.get_distance(coordinates['Frankfurt'], coordinates['Mannheim'])) #
    node_graph.connect('Wurzburg', 'Nurnberg', node.get_distance(coordinates['Wurzburg'], coordinates['Nurnberg'])) #
    node_graph.connect('Wurzburg', 'Stuttgart', node.get_distance(coordinates['Wurzburg'], coordinates['Stuttgart'])) #
    node_graph.connect('Wurzburg', 'Ulm', node.get_distance(coordinates['Wurzburg'], coordinates['Ulm'])) #
    node_graph.connect('Mannheim', 'Nurnberg', node.get_distance(coordinates['Mannheim'], coordinates['Nurnberg'])) #
    node_graph.connect('Mannheim', 'Karlsruhe', node.get_distance(coordinates['Mannheim'], coordinates['Karlsruhe'])) #
    node_graph.connect('Karlsruhe', 'Basel', node.get_distance(coordinates['Karlsruhe'], coordinates['Basel'])) #
    node_graph.connect('Karlsruhe', 'Stuttgart', node.get_distance(coordinates['Karlsruhe'], coordinates['Stuttgart'])) #
    node_graph.connect('Nurnberg', 'Ulm', node.get_distance(coordinates['Nurnberg'], coordinates['Ulm'])) #
    node_graph.connect('Nurnberg', 'Munchen', node.get_distance(coordinates['Nurnberg'], coordinates['Munchen'])) #
    node_graph.connect('Nurnberg', 'Passau', node.get_distance(coordinates['Nurnberg'], coordinates['Passau'])) #
    node_graph.connect('Stuttgart', 'Ulm', node.get_distance(coordinates['Stuttgart'], coordinates['Ulm'])) #
    node_graph.connect('Basel', 'Bern', node.get_distance(coordinates['Basel'], coordinates['Bern'])) #
    node_graph.connect('Basel', 'Zurich', node.get_distance(coordinates['Basel'], coordinates['Zurich'])) #
    node_graph.connect('Bern', 'Zurich', node.get_distance(coordinates['Bern'], coordinates['Zurich'])) #
    node_graph.connect('Zurich', 'Memmingen', node.get_distance(coordinates['Zurich'], coordinates['Memmingen'])) #
    node_graph.connect('Memmingen', 'Ulm', node.get_distance(coordinates['Memmingen'], coordinates['Ulm'])) #
    node_graph.connect('Memmingen', 'Munchen', node.get_distance(coordinates['Memmingen'], coordinates['Munchen'])) #
    node_graph.connect('Munchen', 'Ulm', node.get_distance(coordinates['Munchen'], coordinates['Ulm'])) #
    node_graph.connect('Munchen', 'Passau', node.get_distance(coordinates['Munchen'], coordinates['Passau'])) #
    node_graph.connect('Munchen', 'Rosenheim', node.get_distance(coordinates['Munchen'], coordinates['Rosenheim'])) #
    node_graph.connect('Rosenheim', 'Salzburg', node.get_distance(coordinates['Rosenheim'], coordinates['Salzburg'])) #
    node_graph.connect('Passau', 'Linz', node.get_distance(coordinates['Passau'], coordinates['Linz'])) #
    node_graph.connect('Salzburg', 'Linz', node.get_distance(coordinates['Salzburg'], coordinates['Linz'])) #

    # Make graph undirected, create symmetric connections
    node_graph.make_undirected()

    # Create heuristics (straight-line distance, air-travel distance)
    heuristics = {}
    heuristics['Basel'] = node.get_distance(coordinates[start], coordinates['Basel'])
    heuristics['Bern'] = node.get_distance(coordinates[start], coordinates['Bern'])
    heuristics['Frankfurt'] = node.get_distance(coordinates[start], coordinates['Frankfurt'])
    heuristics['Karlsruhe'] = node.get_distance(coordinates[start], coordinates['Karlsruhe'])
    heuristics['Linz'] = node.get_distance(coordinates[start], coordinates['Linz'])
    heuristics['Mannheim'] = node.get_distance(coordinates[start], coordinates['Mannheim'])
    heuristics['Munchen'] = node.get_distance(coordinates[start], coordinates['Munchen'])
    heuristics['Memmingen'] = node.get_distance(coordinates[start], coordinates['Memmingen'])
    heuristics['Nurnberg'] = node.get_distance(coordinates[start], coordinates['Nurnberg'])
    heuristics['Passau'] = node.get_distance(coordinates[start], coordinates['Passau'])
    heuristics['Rosenheim'] = node.get_distance(coordinates[start], coordinates['Rosenheim'])
    heuristics['Stuttgart'] = node.get_distance(coordinates[start], coordinates['Stuttgart'])
    heuristics['Salzburg'] = node.get_distance(coordinates[start], coordinates['Salzburg'])
    heuristics['Wurzburg'] = node.get_distance(coordinates[start], coordinates['Wurzburg'])
    heuristics['Zurich'] = node.get_distance(coordinates[start], coordinates['Zurich'])
    heuristics['Ulm'] = node.get_distance(coordinates[start], coordinates['Ulm'])

    # Run the search algorithm
    path = astar_search(node_graph, heuristics, start, end)

    print("Shortest route from", start, "to", end + ":\n")
    for i in path:
        print(i)

# Tell python to run main method
if __name__ == "__main__":
    main()