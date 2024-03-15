from math import sqrt, cos, sin, pi
from random import uniform

# Constants
RADIUS = 1
NUM_POINTS = 1000
win_count = 0

# Calculate triangle side length
triangle_point_1 = [RADIUS * cos(pi / 2), RADIUS * sin(pi / 2)]
triangle_point_2 = [RADIUS * cos(pi / 2 - (2 * pi) / 3), RADIUS * sin(pi / 2 - (2 * pi) / 3)]
triangle_side_length = sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(triangle_point_1, triangle_point_2)))

# Generate random points and calculate distances
angles = [uniform(0, 2 * pi) for _ in range(NUM_POINTS)]
P_values = [sqrt(uniform(0, RADIUS)) * RADIUS for _ in range(NUM_POINTS)]
Q_values = [sqrt(RADIUS ** 2 - P ** 2) for P in P_values]

# Calculate probability
for i in range(NUM_POINTS):
    length = 2 * Q_values[i]
    win_count += length > triangle_side_length

print(f"Probability is {win_count / NUM_POINTS}")
