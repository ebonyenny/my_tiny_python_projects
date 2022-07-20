#!\Users\Dorcas\AppData\Local\Microsoft\WindowsApps\python3.exe
"""Purpose: Say hello"""
import argparse
def get_args():
    """Get the command line"""

    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name',
    default='World', help='Name to greet')
    return parser.parse_args() 
def main():
 args = get_args() 
 print('Hello, ' + args.name + '!')
 
if __name__ == '__main__':
    main()