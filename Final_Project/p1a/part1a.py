import random


def generate_prime(numBits, s, exculde):
    x = random.randint(1, pow(2, numBits)-1)
    if (x % 2) == 0:
        x = (x + 1)
    while x == exculde or not miller_rabin(x, s):
        x = (x + 2)
    return x


# returns false if x is not prime
def miller_rabin(x, s):
    # returns true if x is possibly prime
    # x is the number being check for primality
    # s is the number of random bases we are checking for
    # 1 is not a prime number, and we are dealing with positives
    if x <= 1:
        return False
    # 2 is prime and a is between 2 and x-1, x-1=1 so that would cause an error
    # so I added this to prevent the edge case error
    if x == 2:
        return True
    # r and t are only dependent on x so it is more effiecient to calculate them here instead of in the combined test
    r, t = r_and_t(x)
    for _ in range(s):
        a = random.randint(2, x-1)
        if not combined_test(x, a, r, t):
            return False
    return True


def combined_test(n, a, r, t):
    # test n with base a
    if((n % 2) == 0):
        return False
    # initializes x, which is even
    x = (n - 1)
    # (2^t)*r=x
    b = pow(a, r, n)
    for _ in range(1, t+1):
        # roots of unit test
        c = pow(b, 2, n)
        b_mod_n = (b % n)
        if c == 1 and b_mod_n != 1 and b_mod_n != (n - 1):
            return False
        b = c
    if b != 1:
        return False
    return True


def r_and_t(x):
    t = (1)
    # sets r equal to r divided by 2
    r = int(x) >> 1
    while r % 2 == 0:
        r = r >> 1
        t += 1
    return (r), (t)


def extended_euclid(a, b):
    if b == 0:
        return ((a), (1), (0))
    else:
        gcd_, x_, y_ = extended_euclid(b, (a % b))
        gcd, x, y = (gcd_, y_, (x_ - (((a // b)) * y_)))
        return(gcd, x, y)


def message_to_int(M):
    x = 0
    for c in M:
        x = x << 8
        x = x ^ ord(c)
    return x


def int_to_message(D):
    M1 = ""
    while D > 0:
        M1 = chr(D & 0xff) + M1
        D = D >> 8
    return M1


def check_encrypt_and_decrypt(original_mess, e, d, N):
    original_int = message_to_int(original_mess)
    encrypted = encrypt(original_int, e, N)
    decrypted = decrypt(encrypted, d, N)
    print(f"Original Message: {original_mess}")
    print(f"Original message as a integer: {original_int}")
    print(f"Encrypted int representation of message: {encrypted}")
    print(f"Decrypted int representation of message: {decrypted}")
    print(f"Decrypted message as a string: {int_to_message(decrypted)}")


def sign(mess, d, N):
    return pow(mess, d, N)


def unsign_signed(mess, e, N):
    return pow(mess, e, N)


def encrypt(mess, e, N):
    return pow(mess, e, N)


def decrypt(mess, d, N):
    return pow(mess, d, N)


def check_signing(string_mess, e, d, N):
    print(f"----------------------------Signed Message-----------------------------------\n")
    mess = message_to_int(string_mess)
    print(f"Original Message: {string_mess}")
    signed_mess = sign(mess, d, N)
    to_verfy = unsign_signed(signed_mess, e, N)
    print(f"Original message as a integer: {mess}\n")
    print(f"Signed message: {signed_mess}\n")
    print(f"Signed message with signature removed: {to_verfy}\n")
    print(
        f"Signed message with signature removed as a string: {int_to_message(to_verfy)}")


def generate_keys():
    numBits = (int)(input("How many bits? "))
    half_numBits = (numBits // 2)
    # s = mpz(input("What value should s be? "))
    s = 20
    e = pow((2), 16) + 1
    p = generate_prime(half_numBits, s, 0)
    q = generate_prime(half_numBits, s, p)
    phi_N = (p - 1) * (q - 1)
    gcd, a, b = extended_euclid(e, phi_N)
    while gcd != 1:
        p = generate_prime(half_numBits, s, 0)
        q = generate_prime(half_numBits, s, p)
        phi_N = (p - 1) * (q - 1)
        gcd, a, b = extended_euclid(e, phi_N)
    d = (a % phi_N)
    N = (p * q)
    print(f"Public Key:")
    print(f"\tN: {N}")
    print(f"\te: {e}\n")
    print(f"Private Key")
    print(f"\tN: {N}")
    print(f"\td: {d}\n")
    print(f"Factors of Moduli N:")
    print(f"\tp: {p}")
    print(f"\tq: {q}\n")
    print("Other:")
    print(f"\t(p - 1)*(q - 1) aka phi(N): {phi_N}\n")
    return e, d, N


if __name__ == "__main__":
    e, d, N = generate_keys()
    check_signing("I deserve an A", e, d, N)
