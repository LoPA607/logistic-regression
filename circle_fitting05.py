import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Function to calculate circle centers within a bounding box of the polygon
def calculate_circle_centers_polygon(vertices, r):
    centers = []

    # Get bounding box for the entire polygon
    x_coords, y_coords = zip(*vertices)
    x_min, x_max = min(x_coords), max(x_coords)
    y_min, y_max = min(y_coords), max(y_coords)

    xw = abs(x_max - x_min)
    yw = abs(y_max - y_min)

    # Calculate grid dimensions for circle placement
    m = (int((xw - r) / (1.5 * r)) + 1) if ((xw - r) % (1.5 * r)) == (1.5 * r) else (int((xw - r) / (1.5 * r)) + 2)
    n1 = int((yw / (np.sqrt(3) * r)) - (np.sqrt(3) / 2)) + 2
    n2 = n1 if (yw / (np.sqrt(3) * r)) % 1 <= 0.5 else n1 - 1

    for l in range(1, m + 1):
        if l % 2 == 1:  # Odd column
            for k in range(1, n1 + 1):
                x = ((1.5 * l) - 1) * r
                y = round((k - 1) * np.sqrt(3) * r, 2)
                if is_point_in_polygon((x + x_min, y + y_min), vertices):
                    centers.append((x + x_min, y + y_min))
        else:  # Even column
            for k in range(1, n2 + 1):
                x = ((1.5 * l) - 1) * r
                y = round((k - 1) * np.sqrt(3) * r + (np.sqrt(3) / 2) * r, 2)
                if is_point_in_polygon((x + x_min, y + y_min), vertices):
                    centers.append((x + x_min, y + y_min))

    return centers

# Function to check if a point is inside or on the edge of a polygon
def is_point_in_polygon(point, vertices):
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

# Function to plot circles and polygon
def plot_circles_and_polygon(centers, vertices, r):
    fig, ax = plt.subplots()
    
    # Plot the polygon
    polygon = Polygon(vertices, closed=True, fill=None, edgecolor='b', label='Polygon')
    ax.add_patch(polygon)
    
    # Plot the circles
    for (cx, cy) in centers:
        circle = plt.Circle((cx, cy), r, color='r', fill=False)
        ax.add_patch(circle)
        ax.plot(cx, cy, 'ko')  # Mark the center of the circle

    ax.set_aspect('equal', 'box')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Circles inside the Polygon')
    plt.legend()
    plt.grid(True)
    plt.show()
