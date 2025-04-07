import matplotlib.pyplot as plt
import numpy as np
grid_size = 10
grid = np.zeros((grid_size, grid_size))
nodes = {
    "Base": (1, 1),
    "Server A": (3, 4),
    "Firewall": (6, 6),
    "Target": (8, 2)
}
mission_path = [
    nodes["Base"],
    nodes["Server A"],
    nodes["Firewall"],
    nodes["Target"]
]
def plot_mission_grid(nodes, path):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    ax.set_xticks(np.arange(0, grid_size + 1, 1))
    ax.set_yticks(np.arange(0, grid_size + 1, 1))
    ax.grid(True)
    for name, (x, y) in nodes.items():
        ax.plot(x, y, 'ro') 
        ax.text(x + 0.2, y + 0.2, name, fontsize=9, color='black')
    path_x, path_y = zip(*path)
    ax.plot(path_x, path_y, 'b--', linewidth=2)  
    plt.title("Cyber Mission Planar App - Mission Path View")
    plt.tight_layout()
    plt.show()
plot_mission_grid(nodes, mission_path)
