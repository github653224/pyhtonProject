from socket import *
from time import time


def recview_msg():
    
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    bindAddr = ("", 7788)
    udpSocket.bind(bindAddr)
    
    while 1:
        recv_msg = udpSocket.recvfrom(1024)
        print(recv_msg)
        # print(recv_msg)
        print(f"收到{recv_msg[1][0]}:{recv_msg[1][1]}的消息: {recv_msg[0].decode('gb2312')}")
        if recv_msg[0].decode('gb2312') in ("bye", "byebye", "再见", "q"):
            print("再见")
            break


if __name__ == "__main__":
    recview_msg()
        


