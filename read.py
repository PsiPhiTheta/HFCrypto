import numpy as np

data = np.empty((0, 5596), dtype=float)
with open('data.txt') as f:
    for line in f:
        currentline = line.strip('\n')
        currentline = currentline.split(',')
        data = np.vstack((data, currentline))
