def moving_average(iterable, window_size):
    from collections import deque
    window = deque(maxlen=window_size)
    averages = []
    
    for num in iterable:
        window.append(num)
        if len(window) == window_size:
            avg = sum(window) / window_size
            averages.append(avg)
    return averages

data = [1, 2, 3, 4, 5]
print(moving_average(data, 3))  # output: [2.0, 3.0, 4.0]