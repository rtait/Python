#!/usr/bin/env python
while True:
    C = input("What is the temperature? or 'q' to quit \n")
    if C.lower() == 'q':
        print("See you next time...")
        break
    try:
        C = float(C)
    except ValueError:
        print("Please enter a number in numeric form \n")
        continue
    if C =='':
        continue
    C = float(C)
    F = ((9 * C) / 5) + 32
    print(F)