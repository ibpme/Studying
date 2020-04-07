import matplotlib.pyplot as plt

time = 45

beta = 0.166  # infection rate

S = [0 for _ in range(time)]
I = [0 for _ in range(time)]
T = [int(n) for n in range(time)]
S[0] = 3710
I[0] = 1
N = S[0] + I[0]

t = int(0)
while t+1 < time:
    S[t+1] = S[t] - beta*I[t]*S[t]/N
    I[t+1] = I[t] + beta*I[t]*S[t]/N
    t += 1

plt.grid(True)
plt.plot(T, I, color='red', label="Infected")
plt.plot(T, S, color='blue', label="Suspected")
print("Jumlah Infeksi/Kasus",I[t])
#plt.plot(T, R, color='green', label="Recovered")
plt.legend()
plt.show()
