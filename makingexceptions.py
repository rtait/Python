#!/usr/bin/env python
filename = input("C:\\Users\\rtait\\Desktop\\number.txt")

try:
    fn = open("C:\\Users\\rtait\\Desktop\\number.txt")
except(IOError) as err:
    print ("OOPS")
    exit(0)

for line in fn:
    x,y = line.split()
    except:
    print("OOPS2")
    continue

