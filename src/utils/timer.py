import time


def now_time():
    return time.perf_counter()


def calculate_time(t1: float, t2: float):
    return round(t2 - t1, 8) if t2 > t1 else round(t1 - t2, 8)
