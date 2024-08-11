import numpy as np
import matplotlib.pyplot as plt

def plot(paths):
    fig, ax = plt.subplots(tight_layout=True, figsize=(8, 8))
    colours = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
    for i, path in enumerate(paths):
        c = colours[i % len(colours)]
        for XY in path:
            ax.plot(XY[:, 0], XY[:, 1], c=c, linewidth=2)
    ax.set_aspect('equal')
    plt.show()
