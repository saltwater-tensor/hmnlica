
from threading import Thread
from threading import Event
from json import JSONDecoder
import logging

def foo(bar, result, index):
    print('hello {0}'.format(bar))
    result[index] = "foo"

threads = [None] * 10
results = [None] * 10

for i in range(len(threads)):
    pr = Thread(target=foo, args=('world!', results, i))
    pr.start()
    threads.append(pr)
