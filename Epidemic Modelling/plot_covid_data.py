from spreadsheet import data, time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


plt.bar(time,data[1])
plt.xticks(rotation=90)
plt.show()
