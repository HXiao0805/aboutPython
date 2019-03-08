# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 13:37:54 2019

@author: Administrator
正则表达式练习2
"""
import re
#1-1  识别后续的字符串： “bat”、“ bit”、“ but”、“ hat”、“ hit”或者“hut”。 
par_1=r'bat|bit|but|hat|hit|hut'
test_str1='this is bat,and that is bat,here is bit and there is but'
test_1=re.findall(par_1,test_str1)
print(test_1)
# out=['bat', 'hat', 'bat', 'bit', 'but']

#1-2  匹配由单个空格分隔的任意单词对，也就是姓和名。
par_2=r' |,'
test_str2='alice chen,bob jhon,kitty han' 
test_2=re.split(par_2,test_str2)
print(test_2)
# out=['alice', 'chen', 'bob', 'jhon', 'kitty', 'han']

#1-3  匹配由单个逗号和单个空白符分隔的任何单词和单个字母，如姓氏的首字母。
par_3=r', '
test_str3='alice chen, bob jhon, kitty han' 
test_3=re.split(par_3,test_str3)
print(test_3) 
# out=['alice chen', 'bob jhon', 'kitty han']

#1-4  匹配所有有效 Python 标识符的集合。
par_4=r'([A-Za-z]\w*)'
test_str4='python,test_1,2test' 
test_4=re.findall(par_4,test_str4)
print(test_4)
# out= ['python', 'test_1', 'test']

#1-5  根据读者当地的格式，匹配街道地址（使你的正则表达式足够通用，来匹配任意数量的街道单词，
#     包括类型名称）。例如，美国街道地址使用如下格式：1180 Bordeaux Drive。
#     使你的正则表达式足够灵活，以支持多单词的街道名称，如 3120 De la Cruz Boulevard。 
par_5=r'((\w* )*\w*)'
test_str5='3120 De la Cruz Boulevarde' 
test_5=re.search(par_5,test_str5)
print(test_5.group()) #3120 De la Cruz Boulevarde
print(test_5.group(1))#3120 De la Cruz Boulevarde
print(test_5.group(2))#Cruz 此处为满足内括号的最后一个串，之前的串被覆盖

#1-6  匹配以“www”起始且以“.com”结尾的简单Web 域名；例如，www://www. yahoo.com/。 
#     选做题：你的正则表达式也可以支持其他高级域名，如.edu、.net 等（例如， http://www.foothill.edu）。
#par_6=r'^www.*\.com$|.*\.edu|net$' #匹配以www开始并且以.com结尾的域名或者是开头无限制但是要以.edu或.net结尾的域名
par_6=r'^(www|.*).*(\.com|edu|net$)' #（）也有类似于先计算归类的意思
test_str6='www://www. yahoo.com,http://www.foothill.edu,www://www. yahoo.net,http://www. yahoo.net' 
#test_6=re.search(par_6,test_str6)
#if test_6 is not None:
#    print(test_6.group()) #www://www. yahoo.com   
test_pre=re.split(',',test_str6)
print(test_pre) #['www://www. yahoo.com', 'http://www.foothill.edu', 'www://www. yahoo.net', 'http://www. yahoo.net']
for i in test_pre:
    test_6=re.search(par_6,i)
    print(test_6.group()) #循环4次依次输出：www://www. yahoo.com
                          #               http://www.foothill.edu
                          #               www://www. yahoo.net
                          #               http://www. yahoo.net
    
 

#1-7  匹配所有能够表示 Python 整数的字符串集。 
#1-8  匹配所有能够表示 Python 长整数的字符串集。 
#1-9  匹配所有能够表示 Python 浮点数的字符串集。 
#1-10  匹配所有能够表示 Python 复数的字符串集。 
#1-11  匹配所有能够表示有效电子邮件地址的集合
#     （从一个宽松的正则表达式开始，然后尝试使它尽可能严谨，不过要保持正确的功能）。
    
data=input('input:')
print(type(data))