import sys
sys.setrecursionlimit(20000)
import json
import time
import matplotlib.pyplot as plt
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

with open('ex2.json', 'r') as f:
    inputs_arrays = json.load(f)

timings = []

for arr in inputs_arrays:
    start_timing = time.time()
    func1(arr, 0, len(arr)-1)
    end_timing = time.time()
    timings.append(end_timing - start_timing)

plt.plot(range(len(inputs_arrays)), timings)
plt.xlabel('Input Number')
plt.ylabel('Time (s)')
plt.title("EX 2.2")
plt.show()