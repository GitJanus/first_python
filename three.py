# from struct import *
#
# #import Module 引入模块
# #from struct import Other 引入模块中的类、函数或者变量
# #from struct import *  引入模块中所有“公开”成员
#
#
# packed_data = pack("iif",6,19,4.73)
# print(packed_data)
# print(calcsize("iif"))
#
# rogin_data = unpack("iif",b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@')
#
# print(rogin_data)
#
#
# income = [10,20,30]
# def double_money(RMB):
#     return RMB*2
#
# print(list(map(double_money,income)))
#
#
# stocks = {
#     'GooG':123,
#     'AAPL':254,
#     'FB':52,
#     'AMZN':82
# }
#
# print(min(stocks))
# print(min(zip(stocks.values(),stocks.keys())))
# print(sorted(zip(stocks.values(),stocks.keys())))
#
#
# import heapq
#
# grad = [1,21,3,9,6,58,4,754]
#
# print(heapq.nlargest(2,grad))
#
# print(heapq.nsmallest(2,grad))
#
#
# stock =[
#     {'ticker':'A','price':123},
#     {'ticker':'B','price':312},
#     {'ticker':'C','price':1223},
#     {'ticker':'D','price':1223},
# ]
#
# print(heapq.nsmallest(2,stock,key=lambda stock:stock['ticker']))
# print(heapq.nlargest(2,stock,key=lambda stock:stock['price']))
#
#
# from collections import Counter
# text = "新西兰 软件工程师 边拿 高新 边移民 无英 语要求 两年 拿绿卡 全家享受福利 xindayi min666 IT行业的 你看过来 只要和 it搭上 边的职 业都可 以移民 新西兰"
#
# results = text.split(" ")
# print(results)
#
# counter = Counter(results)
#
# top_three = counter.most_common(3)
# print(top_three)
#
#
# from operator import itemgetter
#
# stock1 =[
#     {'ticker':'A','price':123},
#     {'ticker':'F','price':312},
#     {'ticker':'D','price':1223},
#     {'ticker':'B','price':1223},
# ]
# for x in sorted(stock1,key=itemgetter('ticker','price')):
#     print(x)
#


from operator import attrgetter

class User:
    def __init__(self,name,id):
        self.name = name
        self.id = id


    def __repr__(self):
        return self.name+':' + str(self.id)


users = [
    User("huang",61),
    User("chen",11),
    User("zhang",15),
    User("zheng",41),
    User("zou",13),
    User("hu",12)
]

# for u in users:
#     print(u)

for u in sorted(users,key=attrgetter("id")):
    print(u)


















