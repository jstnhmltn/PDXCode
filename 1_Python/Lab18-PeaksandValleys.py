import random
x = '$'
data = {
    [1, 1]
    [2, 2, 2]
    [3, 3, 3, 3]
    [4, 4, 4, 4, 4]
    [5, 5, 5, 5, 5, 5]
    [6, 6, 6, 6, 6, 6, 6]
    [7, 7, 7, 7, 7, 7, 7, 7]
    [6, 6, 6, 6, 6, 6, 6]
    [5, 5, 5, 5, 5, 5]
    [4, 4, 4, 4, 4]
    [5, 5, 5, 5, 5, 5]
    [6, 6, 6, 6, 6, 6, 6]
    [7, 7, 7, 7, 7, 7, 7, 7]
    [8, 8, 8, 8, 8, 8, 8, 8, 8]
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    [8, 8, 8, 8, 8, 8, 8, 8, 8]
    [7, 7, 7, 7, 7, 7, 7, 7]
    [6, 6, 6, 6, 6, 6, 6]
    [7, 7, 7, 7, 7, 7, 7, ]
    [8, 8, 8, 8, 8, 8, 8, 8, 8]
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
}


def peaks(data):
    peak_indices = []
    for i in range(1, len(data) -1):
        prev = data[i-1]
        mid = data[i]
        post = data[i+1]
        if prev < mid and post < mid:
            peak_indices.append(i)
    return peak_indices

def valleys(data):
    valley_indices = []
    for i in range(1, len(data)-1):
        prev = data[i-1]
        mid = data[i]
        post = data[i+1]
        if prev > mid and post > mid:
            valley_indices.append(i)
    return valley_indices 
