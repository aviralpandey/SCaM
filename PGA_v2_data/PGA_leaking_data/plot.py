import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

t, vo = np.loadtxt("unstable_PGA_200mVstep.csv", delimiter=',', skiprows=1,unpack=True)

print(len(t))

plt.figure(1)
plt.plot(t,vo)

ax = plt.gca()
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax.ticklabel_format(axis='x',style='sci',scilimits=(-2,2))

plt.xlabel("Time (us)")
plt.ylabel("Vo (V)")

plt.title("Vo, Output of the PGA")


t, vo = np.loadtxt("stable_PGA_200mVstep.csv", delimiter=',', skiprows=1,unpack=True)

print(len(t))

plt.figure(2)
plt.plot(t,vo)

ax = plt.gca()
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax.ticklabel_format(axis='x',style='sci',scilimits=(-2,2))

plt.xlabel("Time (us)")
plt.ylabel("Vo (V)")

plt.title("Vo, Output of the PGA")

t, vo = np.loadtxt("stable_opamp_unity_gain.csv", delimiter=',', skiprows=1,unpack=True)

print(len(t))

plt.figure(3)
plt.plot(t,vo)

ax = plt.gca()
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax.ticklabel_format(axis='x',style='sci',scilimits=(-2,2))

plt.xlabel("Time (us)")
plt.ylabel("Vo (V)")

plt.title("Vo, Output of the PGA")
plt.show()
