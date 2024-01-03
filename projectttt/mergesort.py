'''Merge sort logic'''
import random
import time
import sys
import math
from multiprocessing.pool import ThreadPool

SUB_PROCESSES=5

def merge(left,right):
    left_length = len(left)
    right_length = len(right)
    start_index1 = 0
    start_index2 = 0
    merged = []
    while start_index1 < left_length and start_index2 < right_length:
        if left[start_index1] <= right[start_index2]:
            merged.append(left[start_index1])
            start_index1 += 1
        else:
            merged.append(right[start_index2])
            start_index2 += 1
    if start_index1 == left_length:
        merged.extend(right[start_index2:])
    else:
        merged.extend(left[start_index1:])
    return merged


def merge_sort(data):
    length = len(data)
    if length <= 1:
        return data
    middle = int(length / 2)
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])
    return merge(left, right)


def merge_sort_parallel(data):
    pool = ThreadPool(SUB_PROCESSES)
    size = int(math.ceil(float(len(data)) / SUB_PROCESSES))
    data = [data[i * size:(i + 1) * size] for i in range(SUB_PROCESSES)] 
    data = pool.map(merge_sort, data)
    while len(data) > 1:
        extra = data.pop() if len(data) % 2 == 1 else None 
        data = [[data[i] , data[i + 1]] for i in range(0, len(data), 2)]
        data = pool.starmap(merge, data) + ([extra] if extra else []) # -> map will still take data
    pool.close()
    return data[0]
    
def run_merge(data_unsorted):
    start = time.time()
    merge_sort(data_unsorted)
    end = time.time() - start
    print ("original", end)

def run_par_merge(data_unsorted):
    start = time.time()
    data_sorted = merge_sort_parallel(data_unsorted)
    end = time.time() - start
    print ("parallel", end)
    return data_sorted
