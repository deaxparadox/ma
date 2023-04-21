import multiprocessing as mp


class Shared(object):
    __queue: mp.Queue = mp.Queue()
    __queue_lock: mp.Lock = mp.Lock()
    __queue_locked: bool = False

    __print: mp.Lock = mp.Lock()

    
    def __init__(self, name="") -> None:
        pass 

    @property
    def queue(cls):
        return cls.__queue

    @classmethod
    def lock(cls) -> bool:
        """
        If `__queue_locked` is True, raise `RuntimeError` and return False.
        It means that lock `__queue_lock` is already already acquired.
        
        Otherwise acquire the `__queue_lock` and set `__queue_locked` to True        
        """
         
        try:
            if cls.__queue_locked:
                raise RuntimeError
            cls.__queue_lock.acquire()
            cls.__queue_locked = not cls.__queue_locked
            return True
        except:
            return False

    @classmethod
    def unlock(cls) -> False:
        """
        if `__queue_locked` is True, 
        then release `__queue_lock`, 
        set `__queue_locked` to False
        and return True
        
        
        else return False
        """
        if cls.__queue_locked:
            cls.__queue_lock.release()
            cls.__queue_locked = False
            return True
        else:
            return False
        



class Queue(object):
    __queue: mp.Queue = mp.Queue()
    __queue_lock: mp.Lock = mp.Lock()
    __queue_locked: bool = False

    __print: mp.Lock = mp.Lock()

    
    def __init__(self, name="") -> None:
        pass 

    @property
    def queue(self):
        return self.__queue

    def lock(self) -> bool:
        """
        If `__queue_locked` is True, raise `RuntimeError` and return False.
        It means that lock `__queue_lock` is already already acquired.
        
        Otherwise acquire the `__queue_lock` and set `__queue_locked` to True        
        """
         
        try:
            if self.__queue_locked:
                raise RuntimeError
            self.__queue_lock.acquire()
            self.__queue_locked = not self.__queue_locked
            return True
        except:
            return False

    def unlock(self) -> False:
        """
        if `__queue_locked` is True, 
        then release `__queue_lock`, 
        set `__queue_locked` to False
        and return True
        
        
        else return False
        """
        if self.__queue_locked:
            self.__queue_lock.release()
            self.__queue_locked = False
            return True
        else:
            return False
    