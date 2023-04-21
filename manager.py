import multiprocessing as mp
from typing import List
import os 
import time

from decorate import log

def workers_func(*args, **kwargs):
    print_lock: mp.Lock = kwargs.get("print_lock")

    for i in range(12):
    
        print_lock.acquire()
        try:
            print(f"PPID: {os.getppid()}\tPID: {os.getpid()}: {i}")
            time.sleep(.1)
        finally:
            print_lock.release()

class Manager(object):
    __instance: int = 0
    
    def __init__(self, managers: int, print_lock: mp.Lock, **kwargs):
        self.__workers = managers
        self.__queue = mp.Queue()
        self.__lock = mp.Lock()
        self.__workers_list: List[mp.Process] = []
        self.__func = None
        self.__print_lock = print_lock

    @property
    def workers(self) -> int:
        """
        Get number of workers.
        """    
        return self.__workers
    
    @property
    def print_lock(self) -> mp.Lock:
        return self.__print_lock

    def create_workers(self, func: List, *args, **kwargs) -> None:
        """
        Create workers
        """

        # kwargs update to update print_lock
        kwargs.update({"print_lock": self.__print_lock})

        # Create workers
        for i in range(self.__workers):
            self.__workers_list.append(
                mp.Process(
                    target=func,
                    args=args,
                    kwargs=kwargs
                )
            )
        return

    def start_workers(self) -> None:
        """
        Start workers
        """

        for p in self.__workers_list:
            p.start()

    def join_workers(self) -> None:
        """
        Join workers 
        """
        
        for p in self.__workers_list:
            if p.is_alive():
                p.join()

    def terminate_workers(self) -> None:
        """
        Terminate workers
        """

        for p in self.__workers_list:
            if p.is_alive():
                print(f"Terminating\tPPID: {os.getppid()}\tPID: {p.pid}")
                p.terminate()


def main():
    print_lock: mp.Lock = mp.Lock()
    m: Manager = Manager(managers=1, print_lock=print_lock)

    try:
        m.create_workers(workers_func)
        m.start_workers()
        m.join_workers()
    except KeyboardInterrupt as e:
        m.terminate_workers()

if __name__ == "__main__":
    main()