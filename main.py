import numpy as np
import matplotlib.pyplot as plt
import circle_fitting05 as cf5
import quad_05 as quad5
import polygon_05 as poly5
import pathplan_04 as pp4
import itertools

def plot_circles_and_quadrilateral(centers, quadrilaterals, r, zigzag_paths):
    """Plot quadrilaterals, circles, and unique-color zig-zag paths."""
    plt.figure(figsize=(10, 10))

    # Define colors for each path
    colors = itertools.cycle(['blue', 'green', 'brown', 'purple'])

    # Plot each quadrilateral
    for i, quad in enumerate(quadrilaterals):
        # Close the quadrilateral by appending the first point
        quad.append(quad[0])
        x_quad, y_quad = zip(*quad)
        plt.fill(x_quad, y_quad, alpha=0.3, label=f'Quadrilateral {i + 1}', edgecolor='black')

    # Plot circles and zig-zag path for each quadrilateral
    for i, (circle_centers, zigzag_path, color) in enumerate(zip(centers, zigzag_paths, colors)):
        for (cx, cy) in circle_centers:
            circle = plt.Circle((cx, cy), r, color='r', fill=False, linestyle='--', linewidth=1.5)
            plt.gca().add_patch(circle)
            plt.plot(cx, cy, 'bo', markersize=5)  # Circle centers marked in blue

        # Plot zig-zag path for each quadrilateral's circles in unique color
        x_coords, y_coords = zip(*zigzag_path)
        plt.plot(x_coords, y_coords, marker="o", linestyle="-", color=color, markersize=5, label=f'Path {i + 1}')

    # Plot settings
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Path Planning in individual quadrilateral', fontsize=14)
    plt.xlabel('X-axis', fontsize=12)
    plt.ylabel('Y-axis', fontsize=12)
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()

# Main code
r = 1
R = 20
quadrilaterals, common_vertex, vertices = poly5.gen_quad(R)
centers = cf5.calculate_circle_centers_polygon(vertices, r)

# Populate `n` with nodes inside each quadrilateral
n = []
for quad in quadrilaterals:
    n.append(quad5.nodes_inside_quadrilateral(quad, centers))

# Generate zig-zag paths for each quadrilateral's nodes
zigzag_paths = [pp4.zigzag_raster_scan(nodes) for nodes in n]

# Plot results
plot_circles_and_quadrilateral(n, quadrilaterals, r, zigzag_paths)