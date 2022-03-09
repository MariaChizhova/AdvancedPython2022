import time
from multiprocessing import Process
from threading import Thread


def get_fib(n):
    fib = [0] * n
    fib[0] = fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib


def easy_task(n, threads_number):
    start = time.time()
    for _ in range(threads_number):
        get_fib(n)
    sync_time = time.time() - start

    threads = [Thread(target=get_fib, args=(n,)) for _ in range(threads_number)]
    start = time.time()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    threads_time = time.time() - start

    procs = [Process(target=get_fib, args=(n,)) for _ in range(threads_number)]
    start = time.time()
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    process_time = time.time() - start
    return sync_time, threads_time, process_time
