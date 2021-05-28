#!/usr/bin/env python3
import sys

MAX_DIGITS = 8

# Converts a decimal to a binary
def convert(args):
    # result = ""
    decRes = []
    binRes = []
    base = 2
    for i in range(len(args)):
        # Skip the first arg, it is the file name
        if i == 0:
            continue

        # Grab the base we want to convert to
        if i == 1:
            base = int(args[i])
            continue
        
        dec = args[i]

        # If the number is more than 8 decimal digits cut it down to size
        # + 2 to account for the "0" and "."
        if len(dec) > MAX_DIGITS + 2:
            dec = dec[0 : MAX_DIGITS + 2]

        # convert dec to a float and add it to the decRes list
        dec = float(dec.strip(' "'))
        decRes.append(dec)

        # Restrict input to [0, 1)
        if dec >= 1 or dec < 0:
            binRes.append("Outside parameters")
            continue
        # binary = "0."
        result = ""
        print(dec)
        dec = dec * (base ** 5)

        # Multiply by 2 until the decimal digits == 0
        # Each decimal >= 0.5 = binary 1, < 0.5 = binary 0
        while dec > 0:
            mod = int(dec % base)
            
            result += str(mod)
            dec = int(dec / base)
            print('dec:', dec)
            print('result:', result)
            print('result:', result[::-1])
            print('mod:', str(dec % base))
        
        # binRes.append(("0." + result[::-1]).strip('0'))
        
        result = "0." + result[::-1]
        binRes.append(result)

    print(binRes)
    # print('| Base 10 | Base 2 |')
    # print('|---------|--------|')
    # for i in range(len(decRes)):
    #     print('| ', decRes[i], '   | ', binRes[i], '|')
    


convert(sys.argv)