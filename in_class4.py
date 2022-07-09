def read_file(primes):
    f = open("primes1000.txt", "r")
    for x in f:
        primes.append(int(x))


def fermat(a, n):
    # True if n is composite and passes the test
    if(pow(a, n-1, n) != 1):
        return True
    return False


def theorem_2(x, n):
    # true if n is composite and passes the test
    if(pow(x, 2, n) == 1):
        return True
    return False


def part_1(primes):
    # returns all of the composite numbers that fail the test
    passes = []
    for n in range(2, 1000):
        for a in range(2, n):
            if(n not in primes and not fermat(a, n) and n not in passes):
                print(f"n={n}, a={a}")
                passes.append(n)
    # return passes


def part_2(primes):
    # returns all of the composite numbers that fail the test
    passes = []
    for n in range(2, 1000):
        if (n not in primes):
            found = False
            for a in range(2, n-1):
                if((not found and a != 1 and a != n-1 and n not in passes and theorem_2(a, n))):
                    found = True
            if not found:
                passes.append(n)
    return passes


if __name__ == "__main__":
    primes = []
    read_file(primes)
    print(fermat(a=2, n=341))
    print((part_1(primes)))
    print((part_2(primes)))
