import time
import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import concurrent
from datetime import datetime

logs = []


def integrate(f, a, b, job=0, n_jobs=1, n_iter=1000, logging=False):
    start = datetime.now()
    acc = 0
    step = (b - a) / n_iter
    left = n_iter // n_jobs * job
    right = min(n_iter // n_jobs * (job + 1), n_iter)
    for i in range(left, right):
        acc += f(a + i * step) * step
    end = datetime.now()
    if logging:
        logs.append((start, end, left, right))
    return acc


def medium_task(n_jobs):
    threads = []
    start = time.time()
    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        threads_result = 0
        for i in range(n_jobs):
            threads.append(executor.submit(integrate, math.cos, 0, math.pi / 2, i, n_jobs, logging=True))
        for t in concurrent.futures.as_completed(threads):
            threads_result += t.result()
        threads_time = time.time() - start

    procs = []
    start = time.time()
    with ProcessPoolExecutor(max_workers=n_jobs) as executor:
        process_result = 0
        for i in range(n_jobs):
            procs.append(executor.submit(integrate, math.cos, 0, math.pi / 2, i, n_jobs, logging=False))
        for p in concurrent.futures.as_completed(procs):
            process_result += p.result()
        process_time = time.time() - start
    return threads_time, threads_result, process_time, process_result
