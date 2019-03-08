# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 09:12:45 2019

@author: Administrator
套接字练习3-创建UDP服务端
"""
from socket import *
from time import ctime
#创建TCP服务器伪码
#ss = socket()                      # 创建服务器套接字 
#ss.bind()                          # 套接字与地址绑定 
#inf_loop:                          # 服务器无限循环              
#    cs = ss.recvfrom()/ss.sendto() # 关闭（接收/发送）     
#ss.close()                         # 关闭服务器套接字#（可选）
#1.UDP时间戳服务器：接受来自客户端的消息，然后将消息加上时间戳前缀返回给客户端
HOST='127.0.0.1' #设置服务器主机（与客户端使用同一个地址）
PORT=21566       #设置服务器端口号（与客户端使用同一个地址）
BUFSIZE=1024     #设置发送/接收的最大字节数
ADDR=(HOST,PORT)

udp_socket=socket(AF_INET, SOCK_DGRAM) #创建UDP套接字
udp_socket.bind(ADDR) #将套接字绑定到服务器地址
#udp_socket.listen(5) #开启监听，listen() 方法的参数是在连接被转接或拒绝之前，传入连接请求的最大数

while True:
    print('waiting from message......')
    data,address=udp_socket.recvfrom(BUFSIZE) #返回元组，里面包含客户端发送消息data和地址address
    data=data.decode('utf-8')
    #按照给定要求拼装服务器返回样式
    data='[%s] %s' % (bytes(ctime(),'utf-8'),data)
    
    #增加编码转码，sendto需要的是byte类型的参数，此处为对数据类型的转换
    data = data.encode("utf-8")
    udp_socket.sendto(data,address)
        
    print('...received from and return to:',address)
udp_socket.close() #关闭服务端套接字

#总结：
#在python3中，利用套接字传输的内容都以byte形式传输，这时候传送时（send/sendto）需要encode，
#接收（recv）时需要decode。编码与解码的形式要一致，本例中全部使用“utf-8”