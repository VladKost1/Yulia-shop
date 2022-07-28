import os
import string
import random
import threading
import time
from multiprocessing.pool import ThreadPool
import multiprocess

import requests


class timer:
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time.time()
        return None

    def __exit__(self, type, value, traceback):
        elapsed_time = time.time() - self.start
        print(self.message.format(elapsed_time))


# def fetch_pic(num_pic):
#     url = 'https://picsum.photos/400/600'
#     path = os.path.join(os.getcwd(), 'img')
#     for _ in range(num_pic):
#         random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
#         response = requests.get(url)
#         if response.status_code == 200:
#             with open(f'{path}/{random_name}.jpg', 'wb') as f:
#                 f.write(response.content)
#
#
# workers = 50
# DATA_SIZE = 50
#
# with timer("Elapsed {}s"):
#     with ThreadPool(workers) as pool:
#         input_data = [DATA_SIZE // workers for _ in range(workers)]
#         pool.map(fetch_pic, input_data)

DATA_SIZE = 1_000_000
lst = []
workers = 1


def fill_data(n):
    while n > 0:
        n -= 1
        lst.append(random.randint(1, 100))


with timer("Elapsed {}s"):
    with multiprocess.Pool(workers) as pool:
        input_data = [DATA_SIZE // workers for _ in range(workers)]
        pool.map(fill_data, input_data)

print(len(lst), lst[:100])

# with timer("Elapsed {}s"):
#     with ThreadPool(workers) as pool:
#         input_data = [DATA_SIZE // workers for _ in range(workers)]
#         pool.map(fill_data, input_data)
#
# print(len(lst), lst[:10])
