# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:33:15 2019

@author: hx
选择某一路径下图片进行识别
识别后生成文本放在某一路径下
将文本内容显示到页面对应的位置
"""

# 举个栗子，添加输入框，将验证码图片打印出来
# coding= utf-8

from PIL import ImageTk
from tkinter import filedialog as fd
#from tkinter import *
import PIL
import tkinter as tk
import pytesseract
#import os
import time

class GetCode(object):

    def __init__(self):
        self.root = tk.Tk()
        
        # 设置整个顶层GUI页面长宽可拉伸
        self.root.resizable(width=True,height=True)   
        self.path = tk.StringVar()
        self.text_path = tk.StringVar()
        #grid布局管理器，与pack功能类似：https://www.cnblogs.com/ruo-li-suo-yi/p/7425307.html
        tk.Label(self.root,text = "待识别图片路径:").grid(row = 0, column = 0) 
        #输入、输出框存放选择路径
        tk.Entry(self.root, textvariable = self.path, width=113).grid(row = 0, column = 1)
        tk.Button(self.root, text = "待识别图片选择", command = self.selectPath).grid(row = 0, column = 2)
        
        tk.Label(self.root,text = "识别后生成文件路径:").grid(row = 1, column = 0) 
        #输入、输出框存放识别后生成文件路径
        tk.Entry(self.root, textvariable = self.text_path, width=113).grid(row = 1, column = 1)
        #保留后续根据图片识别图片，且将生成的识别文件存于某个路径
        tk.Button(self.root,text="识别图片文字",command=self.image_to_text).grid(row = 1, column = 2) # 按键
        tk.Button(self.root,text="关闭识别插件",command=self.close_code).grid(row = 3, column = 2) # 按键
        
        self.root.mainloop()

    def close_code(self):
        self.root.destroy()           # 关闭窗体
        #os.remove(self.path.get())   # 删除图片，先不进行删除，方便与识别结果对比
        
        
    def selectPath(self):
        path_ = fd.askopenfilename()
        self.path.set(path_)
        #选测路径之后进行图片展示
        self.showPhoto(self.path.get())
    
    #重置图片（按要求缩放）
    def resize(self, w_box, h_box, pil_image): #参数是：要适应的窗口宽、高、Image.open后的图片
        w, h = pil_image.size #获取图像的原始大小   
        f1 = 1.0*w_box/w 
        f2 = 1.0*h_box/h    
        factor = min([f1, f2])   
        width = int(w*factor)    
        height = int(h*factor)    
        return pil_image.resize((width, height), PIL.Image.ANTIALIAS) 
    #open_path为选择图片的路径
    def showPhoto(self,open_path):
        #期望图像显示的大小  
        w_box = 800  
        h_box = 800 
        # get the size of the image  
       
        #根据选择的路径显示图片
        im=PIL.Image.open(open_path)
        
        # resize the image so it retains its aspect ration  
        # but fits into the specified display box  
        #缩放图像让它保持比例，同时限制在一个矩形框范围内  
        im_resize = self.resize(w_box, h_box, im)
        
        img=ImageTk.PhotoImage(im_resize)

        tk.Label(self.root,image=img).grid(row = 2, column = 1) # 布局控件
        self.root.mainloop() #显示图片
        
    #根据路径执行文字识别
    def image_to_text(self):
        #设置识别引擎地址
        pytesseract.pytesseract.tesseract_cmd = 'E:/Tesseract-OCR/tesseract.exe'
        #识别图片成文本，改成分割形式保存,调用image_to_excel.py中方法
        text = pytesseract.image_to_string(PIL.Image.open(self.path.get()))
        print(text)
        #text = text.encode("utf-8")
        #获取当前时间戳整数部分，用来拼装生成文件的文件名使用，防止文件重名
        current_time=str(int(time.time()))
        #在指定路径打开指定名字文件（若在该路径下不存在改文件，则会新建文件）
        #mode模式如下：
        #w 只能操作写入  r 只能读取   a 向文件追加
        #w+ 可读可写   r+可读可写    a+可读可追加
        #wb+写入进制数据
        #w模式打开文件，如果而文件中有数据，再次写入内容，会把原来的覆盖掉
        text_path='E:/testText/image_to_text'+current_time+'.txt'
        
        #在编写文件时设置编码格式，否则出现字符时会报错
        file_handle=open(text_path,mode='w',encoding= 'utf8')
        #将识别后的文本text写入指定文件
        file_handle.write(text)
        #写完之后关闭文件
        file_handle.close()
        #记录生成的文本的路径
        self.text_path.set(text_path)

        


if __name__ == '__main__':
    GetCode()
