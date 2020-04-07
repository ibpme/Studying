from spreadsheet import data, time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
#dir(plt)

x_index=np.arange(len(time))


plt.plot(x_index,data[1])
plt.xticks(ticks=x_index,labels=time,rotation=90)
plt.show()
