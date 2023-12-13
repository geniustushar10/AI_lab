def depth_limited_search(node, goal, depth_limit, visited):

    if node == goal:

        return True

    

    if depth_limit == 0:

        return False

    

    if depth_limit > 0:

        for child in graph[node]:

            if child not in visited:

                visited.add(child)

                if depth_limited_search(child, goal, depth_limit - 1, visited):

                    return True

    return False



def iterative_deepening_search(start, goal, graph_size):

    if start not in graph or goal not in graph:

        return False, 0



    depth_limit = 0

    while depth_limit <= graph_size:

        visited = set()

        if depth_limited_search(start, goal, depth_limit, visited):

            return True, depth_limit

        depth_limit += 1



    return False, 0



# Example graph

graph = {

    'A': ['B', 'C'],

    'B': ['A', 'D', 'E'],

    'C': ['A', 'F', 'G'],

    'D': ['B'],

    'E': ['B', 'H'],

    'F': ['C'],

    'G': ['C'],

    'H': ['E']

}



graph_size = len(graph)



# Example usage:

start_node = 'A'

goal_node = 'G'

result, depth =  iterative_deepening_search(start_node, goal_node, graph_size)



if result:

    print(f"Goal reached at depth {depth}")

else:

    print("Goal not found.")
