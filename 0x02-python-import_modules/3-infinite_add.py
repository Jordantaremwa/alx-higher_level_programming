#!/usr/bin/python3
if _name_ == "_main_":
    from sys import argv
    sumint = 0
    for i in range(1, len(argv)):
        sumint += int(argv[i])
        print("{}".format(sumint))
