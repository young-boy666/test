import matplotlib.pyplot as plt
import numpy as np 

## PARAMETERS  
p = 1/2
u = 2
d = 0.5
n = 20
r = 0
s0 = 10
nsims = 100000
k = 1.5
#############

q = (1+r-d)/(u-d)
print('q =', q)

fstar = p/(1-d) - (1-p)/(u-1)


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

print('Mean Final Price of Stock: ', np.mean(Finals))
print('Mean payoff of call option, k=1.5: ', np.mean(Payoffs))
print('The discounted price of C0 is: ', np.mean(Payoffs)*((1+r)**(-n)))