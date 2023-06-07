#!/usr/bin/python3
for n in range(0, 10):
    for t in range(n + 1, 10):
        if (n == 8 and t == 9):
            print("{}{}".format(n, t))
            continue
        print("{}{}".format(n, t), end=", ")
