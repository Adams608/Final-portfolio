#Adam Gboyega-dixon
#Use random.randrange to print an odd integer between 0 and 100.
import random
number = random.randrange(0, 100)
check = 2
if number % check != 0:
    print(number)
