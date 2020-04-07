# import numpy as np
import matplotlib.pyplot as plt

time = 200
beta = 0.5  # infection rate
gamma = 0.3  # recovery rate
teta = 1000  # travel rate from cluster 1 to 2 =number of people traveling per  day

S_1 = [0 for _ in range(time)]
S_2 = [0 for _ in range(time)]
S_3 = [0 for _ in range(time)]
S_4 = [0 for _ in range(time)]
S_M = [0 for _ in range(time)]
S = [0 for _ in range(time)]
I_1 = [0 for _ in range(time)]
I = [0 for _ in range(time)]
I_2 = [0 for _ in range(time)]
I_3 = [0 for _ in range(time)]
I_4 = [0 for _ in range(time)]
I_M = [0 for _ in range(time)]
R_1 = [0 for _ in range(time)]
R_2 = [0 for _ in range(time)]
R_3 = [0 for _ in range(time)]
R_4 = [0 for _ in range(time)]
R_M = [0 for _ in range(time)]
R = [0 for _ in range(time)]
travel = [0 for _ in range(time)]


T = [int(n) for n in range(time)]
S_1[0] = 10000000
I_1[0] = 200
S_2[0] = 120000000
I_2[0] = 10
S_3[0] = S_1[0]
I_3[0] = I_1[0]
S_4[0] = S_2[0]
I_4[0] = I_4[0]
N_1 = S_1[0]
N_2 = S_2[0]
N_3 = S_3[0]
N_4 = S_4[0]

waktu_mudik = 65
t = int(0)
while t+1 < time:
    S_M[t] = S_1[t] + S_2[t]
    I_M[t] = I_1[t] + I_2[t]
    R_M[t] = R_1[t] + R_2[t]
    S[t] = S_3[t] + S_4[t]
    I[t] = I_3[t] + I_4[t]
    R[t] = R_3[t] + R_4[t]
    S_3[t + 1] = S_3[t] - beta * I_3[t] * S_1[t] / N_3
    I_3[t + 1] = I_3[t] + beta * I_3[t] * S_1[t] / N_3 - gamma * I_3[t]
    R_3[t + 1] = R_3[t] + gamma * I_3[t]
    S_4[t + 1] = S_4[t] - beta * I_4[t] * S_4[t] / N_4
    I_4[t + 1] = I_4[t] + beta * I_4[t] * S_4[t] / N_4 - gamma * I_4[t]
    R_4[t + 1] = R_4[t] + gamma * I_4[t]
    if t > waktu_mudik :
        S_1[t+1] = teta*(S_2[t] / N_2) - teta*(S_1[t] / N_1) + S_1[t] - beta*I_1[t]*S_1[t]/N_1
        I_1[t+1] = teta*(I_2[t] / N_2) - teta*(I_1[t] / N_1) + I_1[t] + beta*I_1[t]*S_1[t]/N_1 - gamma*I_1[t]
        R_1[t+1] = teta*(R_2[t] / N_2) - teta*(R_1[t] / N_1) + R_1[t] + gamma*I_1[t]
        S_2[t + 1] = teta*(S_1[t] / N_1) - teta*(S_2[t] / N_2) + S_2[t] - beta * I_2[t] * S_2[t] / N_2
        I_2[t + 1] = teta*(I_1[t] / N_1) - teta*(I_2[t] / N_2) + I_2[t] + beta * I_2[t] * S_2[t] / N_2 - gamma * I_2[t]
        R_2[t + 1] = teta*(R_1[t] / N_1) - teta*(R_2[t] / N_2) + R_2[t] + gamma * I_2[t]
        if teta > 0 :
            teta -= 500
    else:
        S_1[t + 1] = S_1[t] - beta * I_1[t] * S_1[t] / N_1
        I_1[t + 1] = I_1[t] + beta * I_1[t] * S_1[t] / N_1 - gamma * I_1[t]
        R_1[t + 1] = R_1[t] + gamma * I_1[t]
        S_2[t + 1] = S_2[t] - beta * I_2[t] * S_2[t] / N_2
        I_2[t + 1] = I_2[t] + beta * I_2[t] * S_2[t] / N_2 - gamma * I_2[t]
        R_2[t + 1] = R_2[t] + gamma * I_2[t]
    t += 1



S_M[t] = S_1[t] + S_2[t]
I_M[t] = I_1[t] + I_2[t]
R_M[t] = R_1[t] + R_2[t]
S[t] = S_3[t] + S_4[t]
I[t] = I_3[t] + I_4[t]
R[t] = R_3[t] + R_4[t]
plt.grid(True)
plt.plot(T, I_M, color='red', label="Infeksi Jika Mudik")
plt.plot(T, I, color='orange', label="Infeksi Jika Tidak Mudik")
#plt.plot(T, R_M, color='green', label="Recovered Jika Mudik")
plt.plot(T[waktu_mudik], I[waktu_mudik],'o', color='black', label="Waktu Mudik")
#plt.plot(T, I_2, color='red', label="Infeksi Di Region 2 Jika Mudik")

#plt.plot(T, R_1, color='green', label="Recovered")
plt.legend()
plt.show()
