from time import sleep
import sys
import time


def display_bar(n, size, bar_size, start_time):
    normalize_n = int(n / size * bar_size)
    percentage = int(n / size * 100)
    end = time.perf_counter()

    result = '\r'
    if (n == 0):
        result += f"\rETA: {0.00:.2}s "
    else:
        result += f"\rETA: {(size - n) / (n / (end - start_time)):.2f}s "
    result += "[" + str(percentage).rjust(3, ' ') + "%]"
    result += f"[{'=' * (normalize_n)}"
    if normalize_n > 0 and normalize_n < bar_size:
        result += f"\b>"
    result += f"{' ' * (bar_size - normalize_n)}]"
    result += f" {n}/{size}"
    result += f" | elapsed time {end - start_time:.2f}s"
    print(result, end='', flush=True)


def ft_progress(listy):
    min_value = 0
    size = len(listy)
    bar_size = 100

    start_time = time.perf_counter()
    display_bar(0, size, bar_size, start_time)
    for i in range(size):
        yield i
        display_bar(i + 1, size, bar_size, start_time)
