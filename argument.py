import argparse
import typing



def __argument() -> argparse.Namespace:
    parser = argparse.ArgumentParser("Multprocessing architecture")
    parser.add_argument("-n", "--name", help="Specify name")
    subparsers = parser.add_subparsers(help="Process subcommand arguments")
    
    process = subparsers.add_parser("process", help="help of limit")
    process.add_argument('-m', '--manager', default=1, type=int, help="bar help")
    process.add_argument('-w', '--worker', default=3, type=int, help="bar help")

    

    return parser.parse_args()

argument = __argument()