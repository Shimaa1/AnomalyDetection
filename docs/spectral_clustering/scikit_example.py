# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import spectral_clustering

def assign_undirected_weight(W, i, j, v):
    W[i,j] = W[j,i] = v

n = 5;
V = range(n)

W = np.zeros((n,n))
assign_undirected_weight(W,0,1,0.08)
assign_undirected_weight(W,0,2,0.09)
assign_undirected_weight(W,1,2,0.45)
assign_undirected_weight(W,1,3,0.22)
assign_undirected_weight(W,1,4,0.24)
assign_undirected_weight(W,2,3,0.2)
assign_undirected_weight(W,2,4,0.19)
assign_undirected_weight(W,3,4,1)

D = np.zeros((n,n))
for i in V:
    D[i,i] = np.sum(W[i,:])

A = D + W

labels = spectral_clustering(A, n_clusters = 2)
print labels
