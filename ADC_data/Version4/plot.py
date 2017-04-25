import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

t, vip = np.loadtxt("digital_reg_unstable.csv", delimiter=',', skiprows=1,unpack=True)

print(len(t))

plt.figure(1)
plt.plot(t,vip, label = "V-")

ax = plt.gca()
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax.ticklabel_format(axis='x',style='sci',scilimits=(-2,2))

plt.xlabel("Time (us)")
plt.ylabel("V (V)")

plt.title("Unstable Digital Regulator Output")

plt.legend()

plt.show()
