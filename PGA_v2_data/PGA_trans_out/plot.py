
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

t, v_0,v_25,v_70 = np.loadtxt("temp_vs_error.txt", delimiter=',', skiprows=1,unpack=True)

good = np.array([0,100,200,300,400,500,600,700,800,900,1000])
v_0 -= good
v_25 -= good
v_70 -= good

print(len(t))

plt.figure(1)
plt.plot(t,abs(v_0), label="Temp = 0 C")
plt.plot(t,abs(v_25), label="Temp = 25C")
plt.plot(t,abs(v_70), label="Temp = 70C")

ax = plt.gca()
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax.ticklabel_format(axis='x',style='sci',scilimits=(-2,2))


plt.xlabel("Input Votlage (mV)", size = 20)
plt.ylabel("Abs Output Error (mV)", size = 20)

plt.title("Vo, Output of the PGA")
plt.legend()

plt.show()
