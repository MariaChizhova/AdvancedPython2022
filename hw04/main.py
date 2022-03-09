import os
from multiprocessing import cpu_count

from hw04.easy import easy_task
from hw04.hard import hard_task
from hw04.medium import medium_task, logs

if __name__ == '__main__':
    if not os.path.exists('artifacts'):
        os.mkdir('artifacts')

    # easy task
    with open('artifacts/easy.txt', 'w') as file:
        sync_time, threads_time, process_time = easy_task(100000, 10)
        file.write('Synchronous time: ' + str(sync_time) + ' seconds\n')
        file.write('Threads time: ' + str(threads_time) + ' seconds\n')
        file.write('Processes time: ' + str(process_time) + ' seconds\n')

    # medium task
    cpu_num = cpu_count()
    with open('artifacts/medium.txt', 'w') as file:
        for n_jobs in range(1, 2 * cpu_num + 1):
            threads_time, threads_result, process_time, process_result = medium_task(n_jobs)
            file.write(f'Running with {n_jobs} threads:\n')
            file.write(f'\tTime: {threads_time} seconds\n')
            file.write(f'\tResult: {threads_result}\n')

            file.write(f'Running with {n_jobs} processes:\n')
            file.write(f'\tTime: {process_time} seconds\n')
            file.write(f'\tResult: {process_result}\n')

    with open("artifacts/log_integrate.txt", "w") as file:
        for log in logs:
            file.write("Integrate from {} to {} part from {} to {}\n".format(*log))

    # hard task
    messages = hard_task()
    with open('artifacts/hard.txt', 'w') as file:
        for msg in messages:
            file.write(msg)
