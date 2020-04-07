# import numpy as np
import matplotlib.pyplot as plt

time = 100

alpha = 0.2  # 1/incubation period
beta_m = 0.8  # mild infection rate
beta_s = 0.4  # severe infection rate
beta_c = 0.01  # critical infection rate
m_to_s = 0.1  # progression rate from mild to severe
s_to_c = 0.05  # progression rate from severe to critical
gamma_m = 0.3  # recovery rate asymptotic-mild infection
gamma_s = 0.2  # recovery rate severe infection
gamma_c = 0.05  # recovery rate for critical infection
delta = 0.02  # death rate from critical infection only

S = [0 for _ in range(time)]
E = [0 for _ in range(time)]
Im = [0 for _ in range(time)]  # asymptotic-mild infection
Is = [0 for _ in range(time)]  # severe infection
Ic = [0 for _ in range(time)]  # critical infection
R = [0 for _ in range(time)]
D = [0 for _ in range(time)]
T = [int(n) for n in range(time)]
S[0] = 1000
E[0] = 5
N = S[0]

t = int(0)
while t+1 < time:
    S[t+1] = S[t] - beta_m*Im[t]*S[t]/N - beta_s*Is[t]*S[t]/N - beta_c*Ic[t]*S[t]/N
    E[t+1] = E[t] + beta_m*Im[t]*S[t]/N + beta_s*Is[t]*S[t]/N + beta_c*Ic[t]*S[t]/N - alpha*E[t]
    Im[t+1] = Im[t] + alpha*E[t] - gamma_m*Im[t] - m_to_s*Im[t]
    Is[t+1] = Is[t] - s_to_c*Is[t] - gamma_s*Is[t] + m_to_s*Im[t]
    Ic[t+1] = Is[t] - delta*Ic[t] - gamma_s*Ic[t] + s_to_c*Is[t]
    R[t+1] = R[t] + gamma_s*Ic[t] + gamma_s*Is[t] + gamma_m*Im[t]
    D[t+1] = D[t] + delta*Ic[t]
    t += 1

plt.grid(True)
plt.plot(T, S, color='blue', label="Suspected")
plt.plot(T, E, color='purple', label="Exposed")
plt.plot(T, Im, color='yellow', label="Mild Infected")
plt.plot(T, Is, color='orange', label="Severe Infected")
plt.plot(T, Ic, color='red', label="Critical Infected")
plt.plot(T, R, color='green', label="Recovered")
plt.plot(T, D, color='black', label="Death")
plt.legend()
plt.show()
