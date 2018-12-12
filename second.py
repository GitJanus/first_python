#zip函数
first = ['a','b','c']
last =  ['x','y','z']


#[('a','x'),('b','y'),('c','z')]
letter = zip(first,last)

for i,j in letter:
    print(i,j)

#lambda函数

answer = lambda x:x*7

print(answer(5))


def oxoxo(answer = lambda x:x*7):
    print(answer(3))

oxoxo()
oxoxo(answer = lambda x:x*3)

tytorial = {"C++","Python","GitHub","Windows","ISO","Python"}

print(tytorial)

if "Python" in tytorial:
    print("Python online")

else:
    print("Python OffLine")


calssmates = {"LengTe":"ZangAiLeng","LiuZiPei":"PiZiLiu","Feng":"FengZheng"}
print(calssmates)

print(calssmates["LengTe"])

for m,n in calssmates.items():
    print(m)
    print(n)

import Tool
import random
Tool.Google()



for a in range(1,100):
    x = random.randrange(1, 1000)
    print(x)