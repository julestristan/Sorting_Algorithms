from example_list import example
import time
import random
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# n^2 version (naive)
def bubble_sort(L):
    for i in range(len(L)):
        for i in range (len(L)):
            if i+1< len(L):
                if L[i] > L[i+1]:
                    temp_value = L[i]
                    L[i] = L[i+1]
                    L[i+1] = temp_value
    return L

# optimized version
def optimized_bubble_sort(L):
    end = len(L)
    for i in range(len(L)):
        swapped = False
        for j in range (len(L)-i-1):
            if L[j] > L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
                swapped = True
        if not swapped:
            break
    return L
