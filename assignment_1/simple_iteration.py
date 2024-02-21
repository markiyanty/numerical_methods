import math

def simple_iteration(f, x0, epsilon, max_iter=10000000, max_value=1e10, relaxation_factor=0.1):
    phi = lambda x: x - relaxation_factor * f(x)

    x1 = phi(x0)
    iteration_count = 0
    while abs(x1 - x0) > epsilon:
        if abs(x1) > max_value:
            print('Value too large, method does not converge')
            return None
        x0 = x1
        x1 = phi(x0)
        iteration_count += 1
        if iteration_count > max_iter:
            print('Iteration limit reached, solution may not have converged')
            return None
    return x1


f = lambda x: x**2 - 16
x0 = 2
epsilon = 0.001

root = simple_iteration(f, x0, epsilon)
if root is not None:
    print(f'Root found: {root}')
else:
    print('Failed to find a root')
