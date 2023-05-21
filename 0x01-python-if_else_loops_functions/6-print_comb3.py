#!/usr/bin/python3

for digitOne in range(0, 10):
    for digitTwo in range(digitOne + 1, 10):
        if digitOne == 8 and digitTwo == 9:
            print("{}{}".format(digitOne, digitTwo))
        else:
            print("{}{}".format(digitOne, digitTwo), end=", ")
