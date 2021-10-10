from socket import *

# 1、创建udp套接字 
udpSocket = socket(AF_INET, SOCK_DGRAM)
# 2.绑定本地的相关的信息，如果一个网络程序不绑定，则系统会随机分配
# ip地址和端口，ip一般不用写，表示本机的任何一个ip
# bindAddr = ("" ,7788)
# udpSocket.bind(bindAddr)

# 2、准备接受方的地址
sendAddr = ("192.168.0.105", 8080)

# 3、从键盘获取数据
sendData = input("请输入要发送的数据：")
# 4、发送数据到指定的电脑上
udpSocket.sendto(sendData.encode("utf-8"), sendAddr)
udpSocket.close()

