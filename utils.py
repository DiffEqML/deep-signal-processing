"Utilities built step-by-step in the notebooks, collected here for convenience."

import torch
from torch.nn.functional import pad 

def centered_toeplitz(h, L, M):
    T = torch.zeros(L - M + 1, L)

    T[0, :M] = h
    for i in range(1, L - M + 1): T[i] = torch.roll(T[i-1], 1)
    return T

def full_toeplitz(h, L, M):
    T = torch.zeros(L + M - 1, L)
    for i in range(M): T[i, :i+1] = h[-i-1:]
    for i in range(M, L): T[i] = torch.roll(T[i-1], 1)
    for i in range(L, L + M - 1):
        T[i, -M+i-L+1:] = h[:-i-1+L]
    return T
    
def circular_toeplitz(h, L, M):
    T = torch.zeros(L, L)
    T[0, :1] = h[0]
    T[0, -M+1:] = h[1:].flip(0)
    for i in range(1, L): T[i] = torch.roll(T[i-1], 1)
    return T

def fft_conv(u, h):
    L, M = u.shape[0], h.shape[0]
    T = circular_toeplitz(h, L + M - 1, M)
    u_pad = pad(u, (0, M - 1))
    return T @ u_pad