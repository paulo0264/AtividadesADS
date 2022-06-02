from threading import Thread
import random

NUM_VALUES = 1000
values = []
seq_total = 0


for i in range(NUM_VALUES):
    values.append(random.randint(0,100))

for i in range(NUM_VALUES):
        seq_total += values[i]

print(" total: " + str(seq_total))



   