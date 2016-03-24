import single
import threading


@single.MakeItSingleton
class SemaphoreContextManager(object):
    """
    this class represent a lock
    """
    def __init__(self):
        self._lock = False

    def __enter__(self):
        while self._lock:
            pass
        self._lock = True

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._lock = False


class MyThread(threading.Thread):
    """
    A simple thread for testing the lock
    """
    def __init__(self, to_print, num_of_itr):
        threading.Thread.__init__(self)
        self._to_print = to_print
        self._num_of_itr = num_of_itr

    def run(self):
        with SemaphoreContextManager():
            for i in range(1, self._num_of_itr):
                print(self._to_print, self.getName())


if __name__ == '__main__':

    t1 = MyThread("x", 1000)
    t2 = MyThread("y", 1000)

    t1.start()
    t2.start()
    t1.join()
    t2.join()






