# Solution with Python
# lists
from rich import print

TITULO = "[bold magenta=] Multiples of 3 or 5 [/bold magenta]"
# clean screen
print("\033c", end="")
print("🍉 " + TITULO + " 🍍")
print("[bold green=]==========================================[/bold green]")
multiple_3_list = []
multiple_5_list = []
for i in range(1000):
    if (i % 3) == 0:
        multiple_3_list.append(i)
    if (i % 5) == 0 and (i % 3) == 0:
        multiple_3_list.pop()
        multiple_5_list.append(i)
    if (i % 5) == 0 and (i % 3) != 0:
        multiple_5_list.append(i)
partial_sum_3 = sum(multiple_3_list)
partial_sum_5 = sum(multiple_5_list)
sum_total = partial_sum_3 + partial_sum_5
print("Multiples of 3: [")
for element in multiple_3_list:
    print(element, end=" ")
print("]")
print("Multiples of 5: [")
for element in multiple_5_list:
    print(element, end=" ")
print("]")
lista_total = sorted(multiple_3_list + multiple_5_list)
print("All Multiples: [")
for element in lista_total:
    print(element, end=" ")
print("]")
print("Sum multiples of 3: ", partial_sum_3)
print("Sum multiples of 5: ", partial_sum_5)
print("Sum All multiples: ", sum_total)
