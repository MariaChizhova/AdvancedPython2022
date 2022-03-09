import time
from multiprocessing import Queue, Process, Pipe
from datetime import datetime
import codecs
from multiprocessing.connection import Connection


def worker_A(in_queue: Queue, out_pipe: Connection):
    while True:
        msg = in_queue.get()
        time.sleep(5)
        out_pipe.send(msg.lower())


def worker_B(in_pipe: Connection, out_pipe: Connection):
    while True:
        out_pipe.send(codecs.encode(in_pipe.recv(), "rot_13"))


def hard_task():
    messages = []
    a_b, b_a = Pipe()
    b_main, main_b = Pipe()
    main_a = Queue()
    Process(target=worker_A, args=(main_a, a_b), daemon=True).start()
    Process(target=worker_B, args=(b_a, b_main), daemon=True).start()
    while True:
        msg = input('>>> ')
        if msg == 'exit':
            messages.append(f'Exit on {datetime.now()}\n')
            break
        messages.append(f'Received "{msg}" on {datetime.now()}\n')
        main_a.put(msg)
        msg = main_b.recv()
        messages.append(f'Processed "{msg}" on {datetime.now()}\n')
    return messages
