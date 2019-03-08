# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:17:49 2019

@author: Administrator
FTP客户端
"""
import logging
from ftplib import FTP

class MyFtp():
    def __init__(self):
        self.ftp_client = FTP()
        self.ftp_client.encoding = 'utf-8' #为ftp设置编码避免中文乱码

    # 些函数实现ftp登录
    def ftp_login(self,host_ip,username,password):
        try:
            #与服务器进行连接，此处timeout可以设置大一些，否则可能在还没有交互完就断开
            #可能会出现ConnectionAbortedError: [WinError 10053] 你的主机中的软件中止了一个已建立的连接。
            self.ftp_client.connect(host_ip,port=21,timeout=10)
        except :
            logging.warning('network connect time out')
            return 1001
        try:
            #使用用户名密码进行登录
            self.ftp_client.login(user=username, passwd=password)
        except:
            logging.warning('username or password error')
            return 1002
        return 1000

    # 此函数执行ftp命令，并打印命令执行结果
    #romatepath远程ftp目录,根目录向下的目录
    #filename文件名称,想要下载或上传的ftp上文件的名称（包含文件类型），
    #localpath保存在本地的本地路径，不包含文件名的
    def execute_some_command(self,romatepath,filename,localpath): 
       # # 通运sendcmd方法形式执行pwd命令，为使用形式统一起见不推荐使用此种形式，而且其实大多数命令都是支持这种形式的
       # command_result = self.ftp_client.sendcmd('pwd')
       # logging.warning('command_result:%s'% command_result)
       # # 通过直接使用pwd方法执行pwd命令，推荐统一使用此种形式
       # command_result = self.ftp_client.pwd()
       # logging.warning('command_result:%s' % command_result)
       # # 上传文件；'stor ftp_client.py'告诉服务端将上传的文件保存为ftp_client.py，open()是以二进制读方式打开本地要上传的文件
       # command_result = self.ftp_client.storbinary('stor ftp_client.py',open("ftp_client.py",'rb'))
       # logging.warning('command_result:%s' % command_result)
       
        # 下载文件；'RETR bash_profile'告诉服务端要下载服务端当前目录下的bash_profile文件，open()是以二进制写方式打开本地要存成的文件
       # self.ftp_client.cwd(romatepath)#选择操作目录,切换到对应目录下
       
        #根据下载文件大小设置，此大小要大于下载文件的大小，否则文件下载失败
        bufsize = 1024
        open_file=open(localpath+filename,'wb') #以写模式在本地打开文件
        
        command_result = self.ftp_client.retrbinary('RETR %s' % filename,open_file.write,bufsize)
        #command_result = self.ftp_client.retrbinary('retr .bash_profile', open('local_bash_profile', 'wb').write)
        logging.warning('command_result:%s' % command_result)
        
        open_file.close() #传输完成之后关闭释放资源


    # 此函数实现退出ftp会话
    def ftp_logout(self):
        logging.warning('now will disconnect with server')
        self.ftp_client.close()

if __name__ == '__main__':
    # 要连接的主机ipS
    host_ip = '192.168.129.254'
    # 用户名
    username = 'sbsj'
    # 密码
    password = 'sbsj123'
    # 实例化
    my_ftp = MyFtp()
    # 如果登录成功则执行命令，然后退出
    if my_ftp.ftp_login(host_ip,username,password) == 1000:
        logging.warning('login success , now will execute some command')
        name='新员工入职须.doc'
        localpath='E:/studyMyself/aboutPython/testProject/'
        #下载ftp根目录下的“新员工入职须.doc”到本地E:/studyMyself/aboutPython/testProject/路径下
        my_ftp.execute_some_command('',name,localpath)
        my_ftp.ftp_logout()
