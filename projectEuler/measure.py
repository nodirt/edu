import datetime
import math

now = datetime.datetime.now

def measure(f, n=1000):
    start = now()
    for i in range(n):
        f()
    return now() - start

if __name__ == "__main__":
    def slow():
        math.sqrt(34234)
    print(measure(slow).microseconds)