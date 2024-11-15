###### Back up code
import numpy as np
import matplotlib.pyplot as plt


###### Q1  #################################################################################################

def softmax(W):
    M = W.shape[0]  # Number of rows
    K = W.shape[1]  # Number of columns
    P = np.zeros((M,K))  # Making empty array to be filled in
    for i in range(M):
        for j in range(K):
            P[i,j] = (np.exp(W[i,j])) / (sum(np.exp(W[i,:])))
    return P

############################################################################################################
