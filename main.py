import multiprocessing as mp
import logging
import typing

from decorate import log
from argument import argument

@log()
def printer(value: str = "A") -> None:
    print(value)


printer("My name is nitish")



@log()
def main():
    loop: bool = True 
    while loop:
        printer()
        loop = False 



if __name__ == "__main__":
    main()