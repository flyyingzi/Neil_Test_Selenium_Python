#coding: utf-8

"""
@Author: Well
@Date: 2014 - 04 - 19
"""

# threading

import threading
from time import sleep, ctime

loops = [4, 2]

def loop(n_loop, n_sec):
    print "start loop", n_loop, 'at:', ctime()
    sleep(n_sec)
    print "loop", n_loop, 'done at:', ctime()

def main():
    print 'starting at:', ctime()
    threads = None
    n_loops = range(len(loops))
    print "---------"
    print n_loops

    # 创建线程
    for i in n_loops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        print t
        threads.append(t)

    # 开始线程
    for i in n_loops:
        threads[i].start()

    # 等待所有线程结束
    for i in n_loops:
        threads[i].join()

    print "all end:", ctime()

if __name__ == "__main__":
    main()