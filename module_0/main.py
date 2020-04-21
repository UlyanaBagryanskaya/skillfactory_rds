import random
starting_point = 1 # to define the range within the number could belong to
ending_point = 100
k = random.randint(starting_point,ending_point) #now we are having the number to be guessed
number = ending_point/2 #to reduce amount of tryings
count = 2
pop = 1 #that is amount of our tryings, which increases with each pass through the cicle
while number != k: #while the number is not guessed
    herochka = ending_point/(2*count) #please do not laugh at the name we call it. herochka sounds quite respectable. 
                                                                        #besides it helps to catch the number
    if herochka < 1:
        herochka = 1
    else:
        herochka = int(herochka)
    if k > number:
        number = int(number + herochka)
    if k < number:
        number = int(number - herochka)
    count = count * 2
    pop = pop + 1
        
print(number, k, pop)
