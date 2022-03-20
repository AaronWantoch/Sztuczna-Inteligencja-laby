import sys

from maze import Maze, path_from
def calculate_cost(start,current,end):
    return abs(start.x-current.x) + abs(start.y-current.y) + abs(end.x-current.x) + abs(end.y-current.y)

def find_best(start,end, nodes):
    min = 0
    min_node = nodes[0]
    for node in nodes:
        if calculate_cost(start, node, end) < min:
            min = calculate_cost(start, node, end)
            min_node=node
    return min_node


def AStar(maze):
    start_node = maze.find_node('S')
    end_node = maze.find_node('E')
    start_node.visited = True
    node = start_node
    q=[node]
    while len(q) > 0:
        q.remove(node)
        q += maze.get_possible_movements(node)
        child = find_best(start_node, end_node, q)
        node = child.parent
        child.parent = node
        child.visited = True

        if child.type == 'E':
            return path_from(child)
    return None


maze = Maze.from_file("maze2.txt")
maze.draw()
maze.path = AStar(maze)
print()
maze.draw()
