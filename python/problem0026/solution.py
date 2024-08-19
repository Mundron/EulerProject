def cycle_length(number):
    nom, rems, pos = 1, {}, 0
    while nom:
        nom, pos = nom * 10 % number, pos + 1
        if nom == 0:
            return 0
        if nom in rems:
            return pos - rems[nom]
        if nom < number:
            rems[nom] = pos


best_num, best_cyc = 2, 0

for num in range(1, 1000):
    if (new_cyc := cycle_length(num)) > best_cyc:
        best_num, best_cyc = num, new_cyc

print(best_num)
