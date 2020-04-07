# import numpy as np
import matplotlib.pyplot as plt

time = 100

alpha = 0.2  # 1/incubation period
beta = 0.5  # infection rate
gamma = 0.1  # recovery rate
delta = 0.01  # death rate

S = [0 for _ in range(time)]
E = [0 for _ in range(time)]
I = [0 for _ in range(time)]
R = [0 for _ in range(time)]
D = [0 for _ in range(time)]
T = [int(n) for n in range(time)]
S[0] = 1000
I[0] = 5
N = S[0]

t = int(0)
while t+1 < time:
    S[t+1] = S[t] - beta*I[t]*S[t]/N
    E[t+1] = E[t] + beta*I[t]*S[t]/N - alpha*E[t]
    I[t+1] = I[t] + alpha*E[t] - gamma*I[t] - delta*I[t]
    R[t+1] = R[t] + gamma*I[t]
    D[t+1] = D[t] + delta*I[t]
    t += 1

plt.grid(True)
plt.plot(T, S, color='blue', label="Suspected")
plt.plot(T, E, color='yellow', label="Exposed")
plt.plot(T, I, color='orange', label="Infected")
plt.plot(T, R, color='green', label="Recovered")
plt.plot(T, D, color='red', label="Death")
plt.legend()
plt.show()
