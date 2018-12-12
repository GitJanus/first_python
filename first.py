
#函数
def index():
    print("work")
index()


def rmb_to_use(rmb):
    amount = rmb / 7
    print(amount)

rmb_to_use(7)

#这段代码用于介绍break语句
number = 26
for n in range(100):
    if n is number:
        print(n,"is number")
        continue
    else:
        print(n)



print("设置循环次数 range函数")
for x in range(5):
    print(x)

count = 5
while count < 10:
    print(count)
    count +=1



print("循环列表")
words = ['a','as','asd','asdf','asdfg','asdfgh']
for w in  words:
    print(w + "的长度是")
    print(len(w))


name = 'aa'
if name is 'Janus':
    print('客官您来啦')
elif name is 'Lucy':
    print('你不可以来')
else:
    print("Can not Know this!")


print("今天天气好晴朗")
age = 13
if age < 18:
    print('你给我滚')


def prdeict_gf_age(my_age):
    gf_age  = my_age / 2 + 8
    return gf_age


print(prdeict_gf_age(29))


def keyword(a = 'v',b = 'p', c = 'n'):
    print(a,b,c)

keyword()
keyword('www.','baidu.','com')
keyword(c='ased')

#可变参数
def add_numbers(*args):
    toto = 0
    for a in args:
        toto += a
    print(toto)
add_numbers(1)
add_numbers(1,2)
add_numbers(1,2,3)


#参数解包
def health_cacl(age,apple_ate,cige_smocked):
    value = (100+age+apple_ate*3.5)-(cige_smocked*2)
    print(value)

janus=[27,1,1]
health_cacl(janus[0],janus[1],janus[2])

health_cacl(*janus)





