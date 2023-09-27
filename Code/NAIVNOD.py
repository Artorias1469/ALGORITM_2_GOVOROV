import time

def naive_gcd(a, b):
    gcd = 1
    MAX = max(a, b)

    for d in range(2, MAX + 1):
        if a % d == 0 and b % d == 0:
            gcd = d

    return gcd

def main():
    a = 3918843
    b = 1653264
    for i in range(1, 13):
        start_time = time.time()
        res = naive_gcd(a, b)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"НОД({a}, {b}) = {res}, Время: {elapsed_time:.6f} sec")
        b *= 2

if __name__ == "__main__":
    main()
