import single
import threading
import time

# threading.Condition() - wait, notify


@single.MakeItSingleton
class SemaphoreContextManagerWithEvent(object):
    """
    the event object sync the threads.
    when a thread try to run the code, it first checks for the
    state of the flag (during the enter method).
    if the flag is set to true, then the thread can run the code, and also sets the
    flag to be false. because the flag is now set to false, other threads that will try
    to run the code will get blocked on the __enter__ method
    """
    def __init__(self):
        self.event = threading.Event()
        self.event.set()

    def __enter__(self):
        self.event.wait()
        self.event.clear()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.event.set()


@single.MakeItSingleton
class SemaphoreContextManagerBusyWaiting(object):
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
    def __init__(self, to_print, time_to_sleep, num_of_itr, cm):
        threading.Thread.__init__(self)
        self._to_print = to_print
        self._num_of_itr = num_of_itr
        self.cm = cm
        self.time_to_sleep = time_to_sleep

    def run(self):
        with self.cm:
            for i in range(1, self._num_of_itr):
                print(self._to_print, self.getName())
                time.sleep(self.time_to_sleep)


if __name__ == '__main__':

    t1 = MyThread("x", 0.02, 200, SemaphoreContextManagerWithEvent())
    t2 = MyThread("y", 0.02,  200, SemaphoreContextManagerWithEvent())

    t1.setDaemon(True)
    t2.setDaemon(True)

    t1.start()
    t2.start()
    t1.join()
    t2.join()






