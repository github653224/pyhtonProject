from socket import *

# 1.创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)
# 2.绑定本地的相关的信息，如果一个网络程序不绑定，则系统会随机分配
# ip地址和端口，ip一般不用写，表示本机的任何一个ip
bindAddr = ("" ,7788)
udpSocket.bind(bindAddr)
# 3.等待接收方发送的数据,1024表示本次接收的最大字节数
recvData = udpSocket.recvfrom(1024)
print(recvData)
udpSocket.close()


