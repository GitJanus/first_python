import random
import urllib.request
#
# def download_web_image(url):
#     name = random.randrange(1,1000)
#     full_name = str(name) +".jpg"
#
#     urllib.request.urlretrieve(url,full_name)
#
# download_web_image("https://p3.pstatp.com/weili/l/462080962967896215.jpg")


#向文件写入数据
fw = open("simple.txt",'w')
fw.write("writing some stuff in my text file \n"
         "I Love ")
fw.close()


#读取文件
fr= open("simple.txt",'r')

text = fr.read()
print(text)
fr.close()

