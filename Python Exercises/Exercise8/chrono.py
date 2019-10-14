import time


class ChronometerStarted:
    """A started chronometer"""
    def __init__(self):
        self._start = time.time()
        self._stop = 0

    def time (self):
        print("The timer has been running for {0} seconds".format(time.time() - self._start))
        return time.time() - self._start

    def start(self):
        self._start = time.time()
        print("Timer started at {0} seconds".format(self._start))

    def stop (self):
        self._stop = time.time()
        print("Timer stopped after {0} seconds".format(self._stop-self._start))
        self.__class__ = ChronometerStopped

#   My solution
    # def change_state(self):
    #     print ("Chronometer started at time {0}".format(time_start))
    #     self.__class__ = ChronometerStopped


class ChronometerStopped:
    """A stopped chronometer"""
    def __init__(self):
        self._start = 0
        self._stop = time.time()

    def time (self):
        return self._stop - self._start

    def start(self):
        self._start = time.time()
        print("Timer started")
        self.__class__ = ChronometerStarted

    def stop (self):
        print("Timer already stopped")
        pass

#   My solution
    # def change_state(self):
    #     time_stop = time.time()
    #     self._stop = time_stop
    #     print("Chronometer stopped at time {0}".format(time_stop))
    #     print("Chronometer running for {0}ms".format(self._stop - self._start))
    #     self.__class__ = ChronometerStarted


if __name__ == "__main__":
    """Sample main to test functionality. Create a timer and toy with it seeing the debug messages prepared in the 
    code """
    timer = ChronometerStarted()
    time.sleep(1)
    timer.time()
    time.sleep(2)
    timer.stop()
    time.sleep(1)
    timer.stop()
    timer.start()
    time.sleep(2)
    timer.time()
