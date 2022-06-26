from node import *
from graph import *
import json
import sys
import os

# Code Written by Kyle Sherman
# Completed 6/25/2022

# check if a neighbor should be added to the opened_nodes list
def append_open_list(opened_nodes, neighbor):
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
            path.reverse()
            return path

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
            if append_open_list(opened_nodes, neighbor) == True:
                opened_nodes.append(neighbor)

    return None # return none if no path was found

# The main entry point for this module
def main(file, start_city, end_city):

    try:
        f = open(os.path.join(sys.path[0], file))
    except IOError:
        print('There was an error opening the file:', file)
        return
    
    data = json.load(f)

    # START AND GOAL CITIES
    start = start_city
    end = end_city

    coordinates = {}
    heuristics = {}

    for i in data["cities"]:
        coordinates[i['name']] = (i['lat'], i['long'])

    for i in data["cities"]:
        heuristics[i['name']] = node.get_distance(coordinates[start], (i['lat'], i['long']))

    # Create a graph
    node_graph = graph()
    # Create graph connections (Actual distance)
    for i in data["connections"]:
        node_graph.connect(i['from'], i['to'], node.get_distance(coordinates[i['from']], coordinates[i['to']]))

    # Make graph undirected, create symmetric connections
    node_graph.convert_undirected()

    # Run the search algorithm
    path = astar_search(node_graph, heuristics, start, end)

    print("Shortest route from", start, "to", end + ":\n")
    if path != None:
        for i in path:
            print(i)
    else:
        print("No path could be found")

# Tell python to run main method
if __name__ == "__main__":
    # data is stored in data.json
    # change start variable to the city you want to start from
    # change end variable to the city you want to end at
    file = 'data.json'
    start = 'Ulm'
    end = 'Bern'

    n = len(sys.argv)
    if n == 1:
        main(file, start, end)
    elif n == 4:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Wrong arguments. Expected main.py [file].json [start city] [end city]")