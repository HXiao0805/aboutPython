# -*- coding: utf-8 -*-
"""
正则表达式练习1：re模块涉及方法

@author: x-h
"""
#导入re模块，用来处理正则表达式
import re
#match函数：从字符串的起始部分对模式进行匹配。
#如果匹配成功，就返回一个匹配对象；如果 匹配失败，就返回 None
m=re.match('foo','foofoo') #第一个参数为正则表达式

print(m)

if m is not None:
    print(m.group()) #在正则表达式中没有使用（）进行分组时，该函数返回完整匹配对象
    print(m.groups()) #在正则表达式中没有使用（）进行分组时，该函数返回空的元组
    
#search函数：从任意位置开始匹配
s=re.search('foo','this is food')
print(s)

if s is not None:
    print(s.group())
    print(s.groups())
    

m_2=re.match('(\w\w\w)-(\d\d\d)','qwe-123')
print(m_2)

if m_2 is not None:
    print(m_2.group()) #在正则表达式中使用（）进行分组时，该函数返回完整匹配对象 ->qwe-123
    print(m_2.group(1)) #在正则表达式中使用（）进行分组时，该函数返回第一个括号匹配对象 ->qwe
    print(m_2.group(2)) #在正则表达式中使用（）进行分组时，该函数返回第二个括号匹配对象 ->123
    print(m_2.groups()) #在正则表达式中使用（）进行分组时，该函数返回两个子组对应的元组 ->('qwe', '123')

#此时匹配不上，正则表达式\bthe，用来匹配t在边界并且后面是he，例如：thedog或this the dog 
s_2 = re.search(r'\bthe', 'bitethe dog') 

#findall函数:以列表形式返回全部匹配串，如果没有找到匹配部分，就返回一个空的列表
f_1=re.findall('car','carcarcar carry')
print(f_1)

#finditer函数与findall函数类似但是更节省内存:生成的是一个迭代器
f_2=re.finditer('(a\w+)','carcarcar carry')
print(f_2)
#使用for循环进行迭代取值
for i in f_2:
    print (i.group())
    print (i.group(1)) #由于不存在（）分组，所以在取group（1）报错
    #print (i.group(2)) #由于不存在（）分组，所以在取group（2）报错


#sub函数：某字符串中所有匹配正则表达式的部分进行某种形式的替换
s_1=re.sub('[ae]','X','abcdef') #将字符串abcdef中的a或e替换成X，返回替换成功的字符串
print(s_1)

#subn函数：某字符串中所有匹配正则表达式的部分进行某种形式的替换，替换后的字符串和表示替换总数的数字一起作为一个拥有两个 元素的元组返回
s_2=re.subn('[ae]','X','abcdef') #将字符串abcdef中的a或e替换成X，返回替换成功的字符串与替换总数组成的元组
print(s_2)
#可以使用\N，其中N是分组编号
#在参数3中使用参数1进行匹配，将匹配成功的部分替换成参数2的样式显示（r'\2/\1/\3'的意思是分组2\分组1\分组3的样式显示）
s_3=re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})',r'\2/\1/\3', '2/20/91')
print(s_3)

#扩展符号，扩展正则表达式：通过使用 (?iLmsux) 系列选项；可以进行组合使用
#1. re.I/IGNORECASE忽略大小写(?i)
r_1=re.findall(r'(?i)yes', 'yes? Yes. YES!!') 
print(r_1)
#2. re.M/MULTILINE实现多行混合搜索,在cmd中进入python环境是可以执行成功的；
#但是在集成环境中匹配不成功，不会进行跨行检索？是字符串换行符不正确？
r_2=re.findall(r'(?im)(^th[\w ]+)',"""
               This line is the first,
               another line,
               that line, it's the best
               """)
        
print(r_2)
#3. re.S/DOTALL。该标记表明点号（.）能够用来表示\n 符号（反之其通常 用于表示除了\n 之外的全部字符）
r_3=re.findall(r'(?is)th.+',"""
               The first line,
               the second line,
               the third line
               """)
print(r_3)
#4.re.X/VERBOSE 标记非常有趣；
#该标记允许用户通过抑制在正则表达式中使用空白符（除了在字符类中或者在反斜线转义中）来创建更易读的正则表达式
#有了(?x)正则表达式可以换行
r_4= re.search(r'''(?x)
\((\d{3})\)
[ ]
(\d{3})
-
(\d{4})
''', '(800) 555-1212').groups()
print(r_4)
#5.(?:...)使用该符号可以对正则表达式进行分组，但是并不会保存该分组用于后续的检索或者应用
#在不需要保存今后永远不会使用的多余匹配时，这个符号可以使用
r_5=re.findall(r'http://(?:\w+\.)*(\w+\.com)','http://google.com http://www.google.com http://code.google.com')
print(r_5)
r_6=re.search(r'http://(?:\w+\.)*(\w+\.com)','http://google.com http://www.google.com http://code.google.com')
print(r_6.group(1))