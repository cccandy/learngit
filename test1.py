from functools import reduce

def str2float(s):

    left, right = s.split('.')
    t = len(right)

    def char2num(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]

    def fn(x,y):
        return 10*x+y
    L1 = reduce(fn, map(char2num, left))
    L2 = reduce(fn, map(char2num, right)) / 10**t

    return L1+L2
print('str2float(\'123.456\') =', str2float('123.456'))