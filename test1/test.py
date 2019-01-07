#!/usr/bin/python3
# 注释
print("hello world")  # 注释

import keyword

print(keyword.kwlist)

'''
这是注释
'''

"""
这也是注释
"""

if True:
    print(123)
else:
    print(234)
    print(12)

total = 'asd' + '123' + \
        'dsa' + \
        '321'
print(total)

print(r'this is a line with \n')

print(u'this is an unicode string')

print("""这是一个段落，
这里折行了""")

print('this' ' ' 'is' ' ' 'string')

inputString = input('请输入：')
print('你输入的是：' + inputString)

a = '123'
print(a, type(a))
a = 123
print(a, type(a))
a = 123.123
print(a, type(a))
a = True
print(a, type(a))

b = [1, 2.2, 'asd', False]
print(b)
a = (1, 1.2, 'asd', True, b)
print(a, type(a))
print(a[1], a[4], a[4][2])
a[4][1] = 132  # 数组可以修改
print(a)
# a[0] = 132  # tuple不可以修改
print(a)
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[:5])  # 从index=0开始到index=5-1
print(a[5:])  # 从index=5开始到最后
print(a[-1])  # 倒数第一个
print(a[-3])  # 倒数第三个
print(a[0:5:2])  # 从index=0开始到index=5-1，每隔2取一个
print(a[2:0:-1])  # 从index=2到index=1
print(a[2:0])  # 从index=2到index=0
a = '0123456789'
print(a)
print(a[2:4])
print(a[0:9:2])

print('1+9=', 1 + 9)
print('1*9', '=', 1 * 9)
print('9 % 4', '=', 9 % 4)
print('9 / 4', '=', 9 / 4)

a = 1
if a > 0:
    print('positive a')
    a = a + 1
elif a == 0:
    print('a is 0')
    a = a * 10
else:
    print('negative a')
    a = a - 1
print('new a=', a)

for a in [1, 2.2, 'a', True]:
    print(a)

for a in range(10):
    print(a)

print('now a is ', a)

while a > 1:
    print('a = ', a)
    a = a - 1

print('now a is ', a)

while a < 10:
    if a == 5:
        break
    print('a = ', a)
    a = a + 1

print('noe a is ', a)

for a in range(10):
    if a == 2:
        continue
    print('a = ', a)
    a = a - 1
print('noe a is ', a)


def sum_test(a, b):
    return a + b


print('1 + 2 =', sum_test(1, 2))
print('1.2 + 2 =', sum_test(1.2, 2))
# print('a + 2 =', sum_test('a', 2))  # error
print('True + 2 =', sum_test(True, 2))
print('a + b =', sum_test('a', 'b'))
