#!/usr/bin/env python
while True:
    C = input("What is the temperature? or 'q' to quit")
    if C.lower() == 'q':
        print("See you next time...")
        break
    if C =='':
        continue
    C = float(C)
    F = ((9 * C) / 5) + 32
    print(F)