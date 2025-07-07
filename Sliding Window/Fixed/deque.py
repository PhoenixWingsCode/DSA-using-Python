from collections import deque

window_size = 3
data = [1, 2, 3, 4, 5]
window = deque(maxlen=window_size)  # fixed max size, automatically discards oldest

for num in data:
    window.append(num)  # append new element, old one discarded automatically if full
    
    if len(window) == window_size:
        print(list(window))