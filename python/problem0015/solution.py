def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)


size = 20

print(f"{fac(2*size) // ((x := fac(size)) * x)}")
