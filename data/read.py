import numpy as np

data = np.empty((0, 1982), dtype=float)
with open('data.txt') as f:
    for line in f:
        currentline = line.strip('\n')
        currentline = currentline.split(',')
        currentline = currentline[0:len(currentline) - 1]
        data = np.vstack((data, currentline))
print(data.shape)
