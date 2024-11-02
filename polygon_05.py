import random
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate the area of a quadrilateral given four vertices
def quadrilateral_area(quad):
    x_coords, y_coords = zip(*quad)
    area = 0.5 * abs(
        x_coords[0]*y_coords[1] + x_coords[1]*y_coords[2] + x_coords[2]*y_coords[3] + x_coords[3]*y_coords[0] 
        - (y_coords[0]*x_coords[1] + y_coords[1]*x_coords[2] + y_coords[2]*x_coords[3] + y_coords[3]*x_coords[0])
    )
    return area

# Generate quadrilaterals with a common vertex that balances areas
def gen_quad(r):
    # Calculate the minimum distance between vertices
    min_distance = (np.pi * r) / 10

    # Generate angles ensuring the distance condition
    angles = []
    while len(angles) < 10:
        angle = random.uniform(0, 2 * np.pi)
        if len(angles) == 0 or all(
            np.abs(angle - a) >= min_distance / r for a in angles
        ):
            angles.append(angle)

    # Sort the angles to ensure they are in order
    angles = sorted(angles)

    # Calculate the x, y coordinates of the vertices on the circle
    vertices = [(r * np.cos(angle), r * np.sin(angle)) for angle in angles]

    # Try different vertices as the common vertex to find the optimal one
    best_vertex = None
    min_area_diff = float('inf')
    best_quadrilaterals = None

    # Loop through each vertex as a potential common vertex
    for p in range(len(vertices)):
        common_vertex = vertices[p]
        quadrilaterals = [
            [common_vertex, vertices[(p + 1) % len(vertices)], vertices[(p + 2) % len(vertices)], vertices[(p + 3) % len(vertices)]],
            [common_vertex, vertices[(p + 3) % len(vertices)], vertices[(p + 4) % len(vertices)], vertices[(p + 5) % len(vertices)]],
            [common_vertex, vertices[(p + 5) % len(vertices)], vertices[(p + 6) % len(vertices)], vertices[(p + 7) % len(vertices)]],
            [common_vertex, vertices[(p + 7) % len(vertices)], vertices[(p + 8) % len(vertices)], vertices[(p + 9) % len(vertices)]],
        ]

        # Calculate the areas of the quadrilaterals
        areas = [quadrilateral_area(quad) for quad in quadrilaterals]
        area_diff = max(areas) - min(areas)  # Measure of balance across areas

        # Check if this choice of vertex minimizes area difference
        if area_diff < min_area_diff:
            min_area_diff = area_diff
            best_vertex = common_vertex
            best_quadrilaterals = quadrilaterals

    return best_quadrilaterals, best_vertex, vertices
