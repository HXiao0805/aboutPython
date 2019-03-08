# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 13:36:14 2019

@author: Administrator
套接字练习1-创建TCP服务器
"""
import socket
from time import ctime

#socket.socket(socket_family, socket_type, protocol=0)函数用来创建套接字
#其中，socket_family是AF_UNIX或AF_INET（如前所述）
#socket_type是SOCK_STREAM 或 SOCK_DGRAM（也如前所述）
#protocol通常省略，默认为 0
#1.创建TCP/IP套接字
#tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#2.创建UDP/IP套接字 
#udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#创建TCP服务器伪码
#ss = socket()               # 创建服务器套接字 
#ss.bind()                   # 套接字与地址绑定 
#ss.listen()                 # 监听连接 
#inf_loop:                   # 服务器无限循环     
#    cs = ss.accept()        # 接受客户端连接     
#    comm_loop:              # 通信循环         
#        cs.recv()/cs.send() # 对话（接收/发送）     
#    cs.close()              # 关闭客户端套接字 
#ss.close()                  # 关闭服务器套接字#（可选）

#1.TCP时间戳服务器：接受来自客户端的消息，然后将消息加上时间戳前缀返回给客户端
HOST='127.0.0.1' #设置服务器主机（与客户端使用同一个地址）
PORT=21564       #设置服务器端口号（与客户端使用同一个地址）
BUFSIZE=1024     #设置发送/接收的最大字节数
ADDR=(HOST,PORT)

tcp_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #创建TCP套接字
tcp_socket.bind(ADDR) #将套接字绑定到服务器地址
tcp_socket.listen(5) #开启监听，listen() 方法的参数是在连接被转接或拒绝之前，传入连接请求的最大数

while True:
    print('waiting for connection......')
    tcp_client_socket,address=tcp_socket.accept() #返回元组，里面包含客户端socket->tcp_client_socket和地址address
    print('...connected from:',address)
    
    while True:
        data=tcp_client_socket.recv(BUFSIZE)
        if not data:
            break
        #接收之后先解码
        data=data.decode('utf-8')
        #按照给定要求拼装服务器返回样式
        data='[%s] %s' % (bytes(ctime(),'utf-8'),data)
        #发送之前要编码，增加编码转码，send需要的是byte类型的参数，此处为对数据类型的转换
        data = data.encode("utf-8")
        tcp_client_socket.send(data)
        
    tcp_client_socket.close() #关闭客户端套接字
tcp_socket.close() #关闭服务端套接字

#总结：
#1.在运行程序时要注意，先运行服务器代码，后运行客户端代码
#2.在运行时可能会遇到OSError: [WinError 10048] 通常每个套接字地址(协议/网络地址/端口)只允许使用一次
#  这个原因是虽然把运行窗口中运行状态终结了，在执行的python程序实际上还没有结束，解决这个问题也简单，
#  打开windows任务管理器，把名为python的进程结束再重启就行了，如果你运行了好几个，那就把名为python的进程全部关掉。
#3.在运行程序时可能会遇到send() argument 1 must be string or buffer,not str 错误
#  此时需要对send的参数进行编码转码，例如上面写的：data = data.encode("ascii")    