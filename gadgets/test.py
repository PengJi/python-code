import numpy as np
from matplotlib import pyplot as plt
from scipy import signal

t500 = np.linspace(0,5,500,endpoint=False)
s1t500 = signal.square(2*np.pi*1.0*t500)

t5 = np.linspace(0,5,25,endpoint=False)
print t5
t5 = t5 + 1e-14
print t5
s1t5 = signal.square(2.0*np.pi*1.0*t5)
print 2.0*np.pi*1.0*t5
print s1t5

'''
plt.ylim(-2,2)
plt.plot(t500,s1t500,'k',t5,s1t5,'b',t5,s1t5,'bo')
plt.show()
'''

'''
y1t5 = np.absolute(np.fft.fft(s1t5))
ff1t5 = np.fft.fftfreq(25,d=0.2)
plt.plot(ff1t5,y1t5)
plt.show()
'''
