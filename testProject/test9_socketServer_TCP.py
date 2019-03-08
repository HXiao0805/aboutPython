# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:56:16 2019

@author: Administrator
创建 SocketServer TCP 服务器 
"""
#在使用socketserver时对于python2来说模块名为：SocketServer；对于python3来说是socketserver
from socketserver import (TCPServer as TCP,StreamRequestHandler as SHR)
from time import ctime

HOST='127.0.0.1' #设置服务器主机（与客户端使用同一个地址）
PORT=21567       #设置服务器端口号（与客户端使用同一个地址）
#BUFSIZE=1024     #设置发送/接收的最大字节数
ADDR=(HOST,PORT)

class MyRequestHandler(SHR): # MyRequestHandler，作为 SocketServer 中 StreamRequestHandler 的一个子类
    def handle(self): #重写handle()方法
        print('...connected from:',self.client_address)
        #将使用 readline()来获取客户端消息， 并利用 write()将字符串发送回客户端
        #发送之前要将str类型编码为byte
        data='[%s] %s' % (ctime(),self.rfile.readline().decode("utf-8")) #接收到的消息要解码
        data=data.encode("utf-8") #发送之前要编码
        self.wfile.write(data) 
        
tcpServ=TCP(ADDR,MyRequestHandler) #创建TCP服务器
print('waiting for connection...')

tcpServ.serve_forever() #无限循环的服务于客户端
 

