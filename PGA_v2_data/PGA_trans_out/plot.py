import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import matplotlib.font_manager as font_manager

t, v_0,v_25,v_70 = np.loadtxt("temp_vs_error.txt", delimiter=',', skiprows=1,unpack=True)

good = np.array([0,100,200,300,400,500,600,700,800,900,1000])
v_0 -= good
v_25 -= good
v_70 -= good

print(len(t))

fig = plt.figure(1)
plt.plot(t,abs(v_0), label="Temp = 0 C")
plt.plot(t,abs(v_25), label="Temp = 25C")
plt.plot(t,abs(v_70), label="Temp = 70C")

ax = plt.gca()
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax.ticklabel_format(axis='x',style='sci',scilimits=(-2,2))

for label in (ax.get_xticklabels() + ax.get_yticklabels()):
    label.set_fontsize(12)


plt.xlabel("Input Votlage (mV)", size = 20)
plt.ylabel("Abs Output Error (mV)", size = 20)

plt.title("Vo, Output of the PGA", size = 22)
plt.legend(loc='upper left', prop=font_manager.FontProperties(size=18))

fig.savefig('temp.png',dpi=fig.dpi)
plt.show()
