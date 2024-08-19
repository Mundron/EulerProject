def run(al, au, bl, bu):
    print(len({a**b for a in range(al, au + 1) for b in range(bl, bu + 1)}))


run(2, 100, 2, 100)
