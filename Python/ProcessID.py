import os

def main():
    print("PID of running process is :", os.getpid())
    print("PID of parent process is :", os.getppid())
    #print("PID of parent process is :", os.getpgid(os.getpid()))
    #print("PID of parent process is :", os.getpgrp())

if __name__ == "__main__":
    main()