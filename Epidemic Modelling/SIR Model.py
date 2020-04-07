# import numpy as np
import matplotlib.pyplot as plt

time = 47

beta = 0.2013  # infection rate
gamma = 0.04  # recovery rate

S = [0 for _ in range(time)]
I = [0 for _ in range(time)]
R = [0 for _ in range(time)]
#C = [0 for _ in range(time)]
T = [int(n) for n in range(time)]
S[0] = 3710
I[0] = 1
N = S[0] + I[0]
t = int(0)
while t+1 < time:
    S[t+1] = S[t] - beta*I[t]*S[t]/N
    I[t+1] = I[t] + beta*I[t]*S[t]/N - gamma*I[t]
    R[t+1] = R[t] + gamma*I[t]
    # C[t+1]=I[t+1]+R[t+1]
    t += 1


plt.grid(True)
#plt.plot(T, I, color='red', label="Infected")
#plt.plot(T, S, color='blue', label="Suspected")
plt.plot(T, R, color='green', label="Recovered")
#plt.plot(T, C, color='black', label="Total Cases")
print("Jumlah Kasus:", I[t]+R[t])
print("Jumlah Sembuh:", R[t])
print("Jumlah Terinfeksi:", I[t])
plt.legend()
plt.show()
