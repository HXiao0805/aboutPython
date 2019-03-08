# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 14:28:19 2019

@author: Administrator
套接字练习2-创建TCP客户端
"""
from socket import *

#TCP时间戳客户端
#创建TCP客户端伪码
#cs = socket()               # 创建客户端套接字 
#cs.connect()                # 尝试连接服务器 
#comm_loop:                  # 通信循环     
#    cs.send()/cs.recv()     # 对话（发送/接收） 
#cs.close()                  # 关闭客户端套接字 
HOST='127.0.0.1'
PORT=21564
BUFSIZE=1024
ADDR=(HOST,PORT)

tcp_client_socket=socket(AF_INET, SOCK_STREAM) #创建客户端套接字
tcp_client_socket.connect(ADDR) #尝试连接服务器：当连接建立之后，它就可以参与到与服务器的一个对话中

while True:
    data=input('please input something:')
    #发送之前要编码，增加编码转码，send需要的是byte类型的参数，此处为对数据类型的转换
    data = data.encode("utf-8")
    #print(type(data))
    if not data:
        break
    tcp_client_socket.send(data) #发送消息
    data=tcp_client_socket.recv(BUFSIZE)
    if not data:
        break
    #接受之后要解码
    print(data.decode('utf-8'))
    
tcp_client_socket.close() #关闭客户端套接字
