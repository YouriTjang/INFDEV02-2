
def exercise2():
    print "==== Exercise 2 ===="
    n = 1
    prev_n = 1
    print "n  prev_n   i    tmp"
    print "{: <5} {: <5} {: <5} {: <5} ".format(n, prev_n, "", "")
    for i in range(0, 7):
        tmp = n
        n = n + prev_n
        prev_n = tmp
        print "{: <5} {: <5} {: <5} {: <5} ".format(n, prev_n, i, tmp)


def exercise3():
    print "==== Exercise 3 ===="

    x = 0.1 * 3
    s = "The answer to life, the universe, and everything, is " + str(42)
    y = int("21") * 2 == 42
    z = 5 % 2 != 1

    print "Type             Value"
    print "{} \t {}".format(type(x), x)
    print "{} \t {}".format(type(s), s)
    print "{} \t {}".format(type(y), y)
    print "{} \t {}".format(type(z), z)

def exercise4():
    print "==== Exercise 4 ===="

    import sys

    for i in range(0,10):
        for j in range(0,10):
            dist = (i - 5) * (i - 5) + (j - 5) * (j - 5)
            if dist < 3:
                sys.stdout.write("#")
            elif dist < 7:
                sys.stdout.write("+")
            elif dist < 10:
                sys.stdout.write(".")
            else:
                sys.stdout.write(" ")
        sys.stdout.write("\n")


# exercise1()
exercise2()
print
print
exercise3()
print
print
exercise4()
