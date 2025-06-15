def run(p):
    digits = 2
    limit = digits * 9**p
    result = 0
    while 10 ** (digits - 1) < limit:
        for number in range(10 ** (digits - 1), min(10**digits - 1, limit)):
            if number == sum(int(d) ** p for d in str(number)):
                result += number
        digits += 1
        limit = digits * 9**p

    print(result)


run(5)
