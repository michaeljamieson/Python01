print ('hello world')
print ('hey i did something')
print ('what happens if i do a ;');
print ('apparently nothing')


import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()

x = np.arange(0.0,10.0,0.01)
y = x

figure2, bx = plt.subplots()
bx.plot(x,y)
bx.set(xlabel='x',ylabel='y',title='My first graph')
figure2.savefig("test2.png")

plt.show()