import sys
import time


def F(n, plus_one=False):
    assert n >= 0 and isinstance(n, int), \
        'n should be a non-negative integer'
    if n == 0: 
        result = 1
    else:
        result = n * F(n-1)
    return result + (1 if plus_one else 0)


if __name__ == '__main__':
    time.sleep(200)
    if len(sys.argv) == 1:
        num = 5
    else:
        assert len(sys.argv) == 2, \
            'factorial.py takes zero or one argument'
        num = int(sys.argv[1])
    print(F(num))
