from time import sleep
import sys
import time


def display_bar(n, size, bar_size, start_time):
    normalize_n = int(n / size * bar_size)
    percentage = int(n / size * 100)
    print("\r[" + str(percentage).rjust(3, ' ') + "%]", end='', flush=True)
    print(f"[{'=' * (normalize_n)}", end='', flush=True)
    # print(f"!!{normalize_n}!!")
    print(f"\b>", end='', flush=True) if normalize_n > 0 and normalize_n < bar_size else None
    print(f"{' ' * (bar_size - normalize_n)}]", end='', flush=True)
    print(f" {n}/{size}", end='', flush=True)
    # end = time.time()
    end = time.perf_counter()
    print(f" | elapsed time {end - start_time:.2f}s", end='', flush=True)


def ft_progress(listy):
    min_value = 0
    size = len(listy)
    bar_size = 33

    # start_time = time.time()
    start_time = time.perf_counter()
    display_bar(0, size, bar_size, start_time)
    for i in range(size):
        yield i
        display_bar(i + 1, size, bar_size, start_time)


# listy = range(0, 100, 1)
listy = range(0, 3333, 1)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    # sleep(0.01)
    # sleep(1)
    # ret += elem
    sleep(0.0005)
print()
print(ret)

# 0 1 2
# [ - - - - - - - - - - ]

# eta = 0
# eta = 1 * 10 = 10s