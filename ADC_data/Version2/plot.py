import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

t, vip, t1, il  = np.loadtxt("leakage_current.csv", delimiter=',', skiprows=1,unpack=True)

print(len(t))

plt.figure(1)
plt.plot(t[3000:6500],vip[3000:6500])

ax = plt.gca()
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax.ticklabel_format(axis='x',style='sci',scilimits=(-2,2))

plt.xlabel("Time (us)")
plt.ylabel("V- (V)")

plt.title("V-, input to comparator")

plt.figure(2)
plt.plot(t[3000:6500],il[3000:6500])

ax = plt.gca()
ax.ticklabel_format(axis='y',style='sci',scilimits=(-2,2))
ax.ticklabel_format(axis='x',style='sci',scilimits=(-2,2))

plt.title("Current into PMOS source")
plt.xlabel("Time (us)")
plt.ylabel("I_leak (A)")

plt.show()
