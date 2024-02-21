def bisection_method(f, a, b, epsilon):
    if f(a) * f(b) >= 0:
        print("Функція повинна мати різні знаки на кінцях інтервалу [a, b]")
        return None

    c = a
    while (b - a) / 2.0 > epsilon:
        c = (a + b) / 2.0
        if f(c) == 0:
            break
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c

f = lambda x: x**3 - 3*(x**2) + 9*x + 27
#f = lambda x: x**2 - 4
root = bisection_method(f, -10, 9, 0.01)
print(f"Корінь рівняння: {root}")