a=1
b=100
import random
k = random.randint(a,b)
noun = b/2
count = 2
pop = 1
while noun != k:
    herochka = b/(2*count)
    if herochka < 1:
        herochka = 1
    else:
        herochka = int(herochka)
    if k > noun:
        noun = noun + herochka
    if k < noun:
        noun = noun - herochka
    count = count * 2
    pop = pop + 1

print(k,pop)
