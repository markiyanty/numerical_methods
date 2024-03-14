def thomas_algorithm(a, b, c, d):

    n = len(d)
    c_prime = [c[0] / b[0]]
    d_prime = [d[0] / b[0]]
    for i in range(1, n):
        temp = b[i] - a[i] * c_prime[i-1]
        c_prime.append(c[i] / temp if i < n - 1 else 0)  # No c_prime for the last element
        d_prime.append((d[i] - a[i] * d_prime[i-1]) / temp)
    
    x = [0] * n
    x[-1] = d_prime[-1]
    for i in range(n-2, -1, -1):
        x[i] = d_prime[i] - c_prime[i] * x[i+1]
    
    return x


a = [0, 1, 1, 1]
b = [4, 4, 4, 4]
c = [1, 1, 1, 0]
d = [5, 5, 5, 5]

solution = thomas_algorithm(a, b, c, d)
print(solution)
