from example_list import example
import time
import random
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Random_List import generate_list
from Bubble_Sort import *

sizes = np.arange(0,2000,15)
bubble_naive_times = []
bubble_optimized_times = []

for size in sizes:
    unsorted_list = generate_list(size)
    # Time Naive Bubble Sort
    list_to_sort_naive = list(unsorted_list)
    start_time = time.perf_counter()
    bubble_sort(list_to_sort_naive)
    end_time = time.perf_counter()
    bubble_naive_times.append(end_time - start_time)

    # Time Optimized Bubble Sort
    list_to_sort_optimized = list(unsorted_list)
    start_time = time.perf_counter()
    optimized_bubble_sort(list_to_sort_optimized)
    end_time = time.perf_counter()
    bubble_optimized_times.append(end_time - start_time)

# Create a DataFrame to store the results
df = pd.DataFrame({
    'List Size': sizes,
    'Naive Bubble Sort Time (s)': bubble_naive_times,
    'Optimized Bubble Sort Time (s)': bubble_optimized_times
    })

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(df['List Size'], df['Naive Bubble Sort Time (s)'], label='Naive Bubble Sort', marker='o',color='r')
plt.plot(df['List Size'], df['Optimized Bubble Sort Time (s)'], label='Optimized Bubble Sort', marker='x',color='b')

plt.title('Efficiency Comparison of Bubble Sort Algorithms', fontsize=10)
plt.xlabel('List Size', fontsize=10)
plt.ylabel('Time Taken (seconds)', fontsize=10)
plt.legend()
plt.grid(True)

# Save the plot to a file
plt.savefig('bubble_sort_comparison.png')