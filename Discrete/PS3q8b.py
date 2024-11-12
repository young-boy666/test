import matplotlib.pyplot as plt
import numpy as np 

## PARAMETERS  
p = 1/2
u = 2
d = 0.5
n = 20
r = 0
s0 = 10
nsims = 1000
k = 1.5

Threshold = 0.4
#############

fstar = p/(1-d) - (1-p)/(u-1)
print('f* = ', fstar)

InitialValue = 100


Under40 = np.zeros(len(range(nsims)))
for i in range(nsims):
    Path = np.random.choice((0,1), size=n, p = [1-p, p])
    stockprice = [s0]
    Values = [InitialValue]
    for j in range(n):
        if Path[j] == 1:
            stockprice.append(stockprice[-1]*u)
            Values.append(fstar*Values[-1]*u + (1-fstar)*Values[-1]*(1+r))
        else:
            stockprice.append(stockprice[-1]*d)
            Values.append(fstar*Values[-1]*d + (1-fstar)*Values[-1]*(1+r))
    if min(Values) < Threshold * InitialValue:
        Under40[i] = 1


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(range(n+1), stockprice, color='red', label='Stock Price')
ax1.legend()
ax1.set_title('Stock Price')
ax1.set_xlabel('Time')
ax1.set_ylabel('Price')

ax2.plot(range(n+1), Values, color='blue', label='Value of Portfolio')
ax2.legend()
ax2.set_title('Value of Portfolio')
ax2.set_xlabel('Time')
ax2.set_ylabel('Value')

plt.tight_layout()  # Adjust layout to prevent overlap
plt.savefig('q8b.png')
plt.close()

print('The value of the portfolio went under 40 percent of the og inverstemnt with frequency ', sum(Under40)/len(Under40))