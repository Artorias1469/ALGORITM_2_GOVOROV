import time
def euclid_gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a
def main():
    a = 3918843
    res = 0
    b = 1653264
    for i in range(1, 13):
        start_time = time.time()
        for j in range(1000001):
            res = euclid_gcd(a, b)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"ITER {i}: Gcd({a}, {b}) = {res}, time: {elapsed_time:.6f} sec")
        b *= 2
if __name__ == "__main__":
    main()