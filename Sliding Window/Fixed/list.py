window_size = 3
data = [1, 2, 3, 4, 5]
window = []

for i in range(len(data)):
    # Add new element
    window.append(data[i])
    
    # If window size exceeded, remove oldest element
    if len(window) > window_size:
        window.pop(0)
    
    # Use the window once it reaches full size
    if len(window) == window_size:
        print(window)
