import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

t, vo = np.loadtxt("pga_input.csv", delimiter=',', skiprows=1,unpack=True)

print(len(t))

fig = plt.figure(1)
plt.plot(t,vo)

ax = plt.gca()
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax.ticklabel_format(axis='x',style='sci',scilimits=(-2,2))

for label in (ax.get_xticklabels() + ax.get_yticklabels()):
    label.set_fontsize(12)

plt.xlabel("Time (us)", size = 20)
plt.ylabel("Vo (V)", size = 20)

plt.title("V-, input to the PGA, 1V input 70C", size = 22)

fig.savefig('temp.png',dpi=fig.dpi)
plt.show()
