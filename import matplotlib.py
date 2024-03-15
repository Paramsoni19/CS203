import matplotlib.pyplot as plt
from math import sqrt, cos, sin, pi
from random import uniform, randint

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
P_values = [uniform(0, RADIUS) for _ in range(NUM_POINTS)]
Q_values = [sqrt(RADIUS ** 2 - P ** 2) for P in P_values]

# Draw circle
fig, ax = plt.subplots()
circle = plt.Circle((0, 0), RADIUS, color='blue', fill=False, linewidth=2, zorder=5)
ax.add_artist(circle)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# Draw lines and calculate probability
for i in range(NUM_POINTS):
    length = 2 * Q_values[i]
    color = 'green' if length <= triangle_side_length else 'red'
    win_count += color == 'red'
    point_1 = ((P_values[i] * cos(angles[i]) + Q_values[i] * sin(angles[i])), (P_values[i] * sin(angles[i]) - Q_values[i] * cos(angles[i])))
    point_2 = ((Q_values[i] * sin(angles[i]) - P_values[i] * cos(angles[i])), (P_values[i] * sin(angles[i]) + Q_values[i] * cos(angles[i])))
    ax.plot(*zip(point_1, point_2), color=color, zorder=randint(1, 2), linewidth=1)

plt.show()
print(f"Probability is {win_count / NUM_POINTS}")
