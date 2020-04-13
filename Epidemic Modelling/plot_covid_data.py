from spreadsheet import data,time
import matplotlib.pyplot as plt
import numpy as np
# dir(plt)
dates_int = np.linspace(start = 0, stop = len(time) , num=len(time))
plt.plot(dates_int, data[1],scalex=True)
plt.xticks(ticks=dates_int, labels=time , rotation=90)
plt.show()
