import math
import numpy as np

print(11 // 2)

nd = 'dertgbvc'
print(nd[-1])
print(nd[1])
print("AB\nC\nDE")
"hello Mike".find("Mike")
print(3 + 2 * 2)
type(int(12.3))
print(str(1) + str(1))
"123".replace("12", "ab")
A = (1, 2, 3, 4, 5)
print(A[1:4])
print(len(A))
B = [1, 2, [3, 'a'], [4, 'b']]
print(B[3][1])

print([1, 2, 3] + [1, 1, 1])

print("Hello Mike".split())
var = {"a": 1, "b": 2}
print(var)
Dict = {"A": 1, "B": "2", "C": [3, 3, 3], "D": (4, 4, 4), 'E': 5, 'F': 6}
print(Dict["D"])

print(type({1, 2, 3}))
va = {'a', 'b'} & {'a'}
print(va)

A = ((11, 12), [21, 22]),
print(A[0][1])

AB = ["hard rock", 10, 1.2]
del (AB[0])
print(AB)

print(len(("disco", 10, 1.2, "hard rock", 10)))

print({"The Bodyguard": "1992", "Saturday Night Fever": "1977"})

vr = '1' in {'1', '2'}
print(vr)

A = (1, [2, 3], [4])
print(A[2])

t = 5 != 5
print(t)

r = 'a' == 'A'
print(r)

for x in range(0, 3):
    print(x)

for x in ['A', 'B', 'C']:
    print(x + 'A')

for i, x in enumerate(['A', 'B', 'C']):
    print(i, x)

print('hey')
print(len(['A', 'B', 1]))

print(len([sum([0, 0, 1])]))

L = [1, 3, 2]

print(sorted(L))

print(type["a"])

x = "Go"

if x == "Go":

    print('Go ')

else:

    print('Stop')

print('Mike')

x = 5
while x != 2:
    print(x)
    x = x - 1


class Points(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print('x=', self.x, ' y=', self.y)


for i, x in enumerate(['A', 'B', 'C']):
    print(i, 2 * x)


class Points(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print('x=', self.x, ' y=', self.y)


p2 = Points(1, 2)

p2.x = 2

p2.print_point()


def step(xx):
    if x > 0:
        y = 1
    else:
        y = 0
    return y


a = 1


def do(x):
    return x + a


print(do(1))
print('hey')

m = np.array([-1, 1])
b = np.array([1, 1])
print(np.dot(m, b))

print('yo')

X = np.array([[1, 0, 1], [2, 2, 2]])
out = X[0, 1:3]
print(out)

print('next')
X = np.array([[1, 0], [0, 1]])
Y = np.array([[2, 2], [2, 2]])
print(np.dot(X, Y))

print('next')
X = np.array([[1, 0], [0, 1]])
Y = np.array([[2, 1], [1, 2]])
print(np.dot(X, Y))
print('r')
Name = "ABCDE"
print(Name.find("B"))

print('r')

A = ['1', '2', '3']
for a in A: print(2 * a)

A = [1, 2, 3]
for a in A: print(3 * a)

print('netx')
for i in range(1, 5):
    if i == 2: print(i)

print('mm')

a = np.array([0, 1, 0, 1, 0])
b = np.array([1, 0, 1, 0, 1])
print(a * b)

print('ew')

a = np.array([1, 2, 1, 1, 1])
print(a + 10)

print('dd')
a = np.array([1, 1, 1, 1, 1])
print(a + 10)

print('ddd')

for n in range(0, 2):
    print(file1.readline())
