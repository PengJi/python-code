import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.square.html#scipy.signal.square

t = np.linspace(0, 1, 500, endpoint=False)
'''
plt.plot(t, signal.square(2 * np.pi * 5 * t))
plt.ylim(-2, 2)
plt.show()
'''

#'''
plt.figure()
sig = np.sin(2 * np.pi * t)
print sig
pwm = signal.square(2 * np.pi * 30 * t, duty=(sig + 1)/2)
print pwm
plt.subplot(2, 1, 1)
plt.plot(t, sig)
plt.subplot(2, 1, 2)
plt.plot(t, pwm)
plt.ylim(-1.5, 1.5)
plt.show()
#'''
