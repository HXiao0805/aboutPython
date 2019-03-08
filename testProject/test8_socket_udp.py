# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 09:27:30 2019

@author: Administrator
套接字练习4-创建UDP客户端
"""
from socket import *

#UDP时间戳客户端
#创建UDP客户端伪码
#cs = socket()               # 创建客户端套接字 
#comm_loop:                  # 通信循环     
#    cs.sendto()/cs.recvfrom()     # 对话（发送/接收） 
#cs.close()                  # 关闭客户端套接字
HOST='127.0.0.1'
PORT=21566
BUFSIZE=1024
ADDR=(HOST,PORT)
udp_client_socket=socket(AF_INET, SOCK_DGRAM) #创建客户端套接字

while True:
    data=input('please input something:')
    #增加编码转码，sendto需要的是byte类型的参数，此处为对数据类型的转换
    data = data.encode("utf-8")
    #print(type(data))
    if not data: #data为空
        break
    udp_client_socket.sendto(data,ADDR) #发送数据，参数包含数据消息与服务器地址和端口号
    data,ADDR=udp_client_socket.recvfrom(BUFSIZE) #接收服务器消息
    data = data.decode("utf-8")
    if not data:
        break
    print(data)
udp_client_socket.close()