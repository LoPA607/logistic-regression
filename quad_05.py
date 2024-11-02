import numpy as np

# Function to check if a point is inside or on the edge of a quadrilateral
def is_point_in_quadrilateral(point, vertices):
    x, y = point
    n = len(vertices)
    inside = False

    px, py = vertices[0]
    for i in range(n + 1):
        vx, vy = vertices[i % n]
        if ((vy > y) != (py > y)) and (x < (px - vx) * (y - vy) / (py - vy) + vx):
            inside = not inside
        px, py = vx, vy

    return inside

# Function to filter nodes that are inside the quadrilateral
def nodes_inside_quadrilateral(vertices, nodes):
    inside_nodes = [node for node in nodes if is_point_in_quadrilateral(node, vertices)]
    return inside_nodes
