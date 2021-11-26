def fib(n):
  if n - 1 == 0:
    return 0
  if n - 1 == 1:
    return 1
  else:
    return fib(n - 1) + fib(n - 2)
print(fib(7))
