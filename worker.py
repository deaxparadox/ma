import multiprocessing as mp
from typing import List
import os 
import time

from decorate import log




def workers_func(*args, **kwargs):
    print_lock: mp.Lock = kwargs.get("print_lock")
    queue: mp.Queue = kwargs.get("queue")
    queue_lock: mp.Lock = kwargs.get('queue_lock')

    # global print_lock, queue, queue_lock

    for i in range(120):

        ipt = f"PPID: {os.getppid()} PID: {os.getpid()}: {i}"
        
        # queue_lock.acquire()
        # try:
        #     queue.put(ipt)
        # finally:
        #     queue_lock.release()

        print_lock.acquire()
        try:
            print(ipt)            
        finally:
            print_lock.release()





    
class Workers(object):
    __instance: int = 0
    
    def __init__(self, workers: int, print_lock: mp.Lock, **kwargs):
        self.__workers = workers
        self.__queue = mp.Queue()
        self.__queue_lock = mp.Lock()
        self.__workers_list: List[mp.Process] = []
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
        kwargs.update(
            {
                "print_lock": self.__print_lock,
                "queue": self.__queue,
                "queue_lock": self.__queue_lock
            }
        )

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
            # if p.is_alive():
                p.join()

    def terminate_workers(self) -> None:
        """
        Terminate workers
        """

        for p in self.__workers_list:
            if p.is_alive():
                print(f"Terminating\tPPID: {os.getppid()}\tPID: {p.pid}")
                p.terminate()

    def printer(self) -> None:
        while not self.__queue.empty:
            self.__queue_lock.acquire
            try:
                print(self.__queue.get())
            finally:
                self.__queue_lock.release()

def main():
    # mp.set_start_method('spawn')
    print_lock: mp.Lock = mp.Lock()
    m: Workers = Workers(workers=300, print_lock=print_lock)

    try:
        m.create_workers(workers_func)
        m.start_workers()
        m.join_workers()
        # m.printer()
    except KeyboardInterrupt as e:
        m.terminate_workers()

if __name__ == "__main__":
    main()