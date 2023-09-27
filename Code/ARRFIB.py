import time

def fib(n):
    F = [0] * 1000
    F[0] = 0
    F[1] = 1
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]

def main():
    n = int(input("Введите значение n: "))
    start_time = time.time()
    total_duration = 0.0

    for i in range(n + 1):
        iter_start_time = time.time()
        result = 0
        for j in range(10000):
            result = fib(i)

        iter_end_time = time.time()
        iter_duration = iter_end_time - iter_start_time
        total_duration += iter_duration

        print(f"F({i}) = {result} (время выполнения: {iter_duration:.6f} сек, общее время: {total_duration:.6f} сек)")

    total_end_time = time.time()
    total_duration = total_end_time - start_time
    print(f"Общее время выполнения программы: {total_duration:.6f} сек")

if __name__ == "__main__":
    main()
