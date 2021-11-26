def power(a, n):
  if n == 1:
    return a
  if n % 2 == 0:
    return power(a, n // 2) * power(a, n // 2)
  if n % 2 != 0:
    return power(a, n - 1) * power(a, 1)
print(power(3, 3))
