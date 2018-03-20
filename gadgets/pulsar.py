import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# http://www.jb51.net/article/132067.htm

# Fixing random state for reproducibility
np.random.seed(19680801)

# Generate random data
data = np.random.uniform(0, 1, (64, 75))
X = np.linspace(-1, 1, data.shape[-1])
G = 1.5 * np.exp(-4 * X ** 2)
 
# Generate line plots
lines = []
for i in range(len(data)):
  # Small reduction of the X extents to get a cheap perspective effect
  xscale = 1 - i / 200.
  line = xscale * X, i + G * data[i]
  lines.append(line)

print lines

