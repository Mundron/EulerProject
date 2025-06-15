def fac(number):
    if number == 1:
        return 1
    else:
        return fac(number - 1) * number


print(sum(map(int, str(fac(100)))))
