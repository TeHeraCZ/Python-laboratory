import random

min = int(input("Zadej počáteční hodnotu: "))
max = int(input("Zadej koncovou hodnotu: "))

rozsah = int(input("Zadej počet čísel na vygenerování: "))

for x in range(rozsah):
    print(random.randint(min, max))
