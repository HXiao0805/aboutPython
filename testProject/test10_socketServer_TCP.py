# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 16:17:47 2019

@author: Administrator
创建 SocketServer TCP 客户端
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
PORT=21567
BUFSIZE=1024
ADDR=(HOST,PORT)

tcp_client_socket=socket(AF_INET, SOCK_STREAM) #创建客户端套接字
tcp_client_socket.connect(ADDR) #尝试连接服务器：当连接建立之后，它就可以参与到与服务器的一个对话中

while True:
    data=input('please input something:')
    #因为这里使用的处理程序类对待套 接字通信就像文件一样，所以必须发送行终止符（回车和换行符）。
    #而服务器只是保留并重用 这里发送的终止符。当得到从服务器返回的消息时，用 strip()函数对其进行处理并使用由 print 声明自动提供的换行符。 
    data='%s\r\n' % data #在data还是字符串类型时，设置格式
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
    print(data.decode('utf-8').strip()) # strip()函数对其进行处理并使用由 print 声明自动提供的换行符
    
tcp_client_socket.close() #关闭客户端套接字

#注意：
#1.在发送之前要编码，在接受之后要解码，原因是python3的发送与接受方法只接收byte参数
#2.SocketServer 请求处理程序的默认行为是接受连接、获取请求，然后关闭连接；每次向服务器发送消息时， 都需要创建一个新的套接字
#  即使用socketserver作为服务端，客户端每次发送请求都要重新执行代码，不会一次执行，无限发送
