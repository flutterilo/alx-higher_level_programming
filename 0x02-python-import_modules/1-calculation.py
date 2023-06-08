#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as op
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, op.add(a, b)))
    print("{} - {} = {}".format(a, b, op.sub(a, b)))
    print("{} * {} = {}".format(a, b, op.mul(a, b)))
    print("{} / {} = {}".format(a, b, op.div(a, b)))
