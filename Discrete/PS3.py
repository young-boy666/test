import matplotlib.pyplot as plt
import numpy as np 

## PARAMETERS  
p = 1/7
u = 1.1
d = 0.9
n = 20
r = 0.05
s0 = 10
nsims = 100000
k = 1.5
#############

q = (1+r-d)/(u-d)
print('q =', q)

Path = np.random.choice((0,1), size=n, p = [1-p, p])
example = [s0]
for j in range(n):
    if Path[j] == 1:
        example.append(example[-1]*u)
    else:
        example.append(example[-1]*d)



Finals = []
Payoffs = []
for i in range(nsims):
    Path = np.random.choice((0,1), size=n, p = [q, 1-q])
    S = [s0]
    for j in range(n):
        if Path[j] == 1:
            S.append(S[-1]*u)
        else:
            S.append(S[-1]*d)
    Finals.append(S[-1])
    Payoffs.append(S[-1]-k)

Payoffs = np.array(Payoffs)
Payoffs[Payoffs < 0] = 0


print('Mean payoff of call option, k=1.5: ', np.mean(Payoffs))
print('The discounted price of C0 is: ', np.mean(Payoffs)*((1+r)**(-n)))

plt.plot(range(n+1), example)
plt.xticks(range(0, n + 1, 2))
plt.yticks(range(0, 14, 1))
plt.xlabel('Time')
plt.ylabel('Asset Price')
plt.title('Example asset price over time')
plt.savefig('examplepath.png')
plt.close()

print('For the example path, the payoff of the call option was: ', max(0,example[-1]-k))
