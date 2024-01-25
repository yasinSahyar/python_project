##Tehtävä6

import random

## Generate a random 3-digit code (numbers between 0 and 9)
code_3_digit = [random.randint(0, 9) for _ in range(3)]

## Generate a random 4-digit code (numbers between 1 and 6)
code_4_digit = [random.randint(1, 6) for _ in range(4)]

## Print the generated codes
print("Random 3-digit combination:", "".join(map(str, code_3_digit)))
print("Random 4-digit combination:", "".join(map(str, code_4_digit)))
