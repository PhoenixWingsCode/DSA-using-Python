import random

def monte_carlo_circle_area(num_points=10000):
    inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:  # inside unit circle
            inside_circle += 1

    square_area = 4  # since square side is 2 (-1 to 1)
    estimated_area = (inside_circle / num_points) * square_area
    return estimated_area

# Example run
area = monte_carlo_circle_area()
print(f"Estimated area of circle using Monte Carlo: {area}")
