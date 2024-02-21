from sympy import symbols, diff

x = symbols('x')
f = x**3 - x**2 - 3*x + 1
f_prime = diff(f, x)

# Initial approximation
x_n = 3
# Desired precision
epsilon = 1e-5
# Iteration counter
iteration = 0

# Newton's method iteration
while True:
    f_n = f.subs(x, x_n)
    f_prime_n = f_prime.subs(x, x_n)
    x_next = x_n - f_n / f_prime_n  # Newton's formula
    difference = abs(x_next - x_n)
    if difference < epsilon:
        break
    x_n = x_next
    iteration += 1
    print(f"Iteration {iteration}: x = {x_n}, difference = {difference}")

# Final approximation of the root
print(f"Final approximation of the root: x = {x_n}")
