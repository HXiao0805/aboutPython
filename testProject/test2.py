# -*- coding: utf-8 -*-

"""
随机骰子游戏：玩家先选Big or Small，选择后开始摇号，计算号码总值，
11<=总值<=18为“Big”，3<=总值<=10为“Small”，然后告诉玩家是否猜测正确

"""
import random
#产生3个随机数
def give_3_number():
    #定义一个列表
    number_list=[]
    #产生3个1~6的随机数
    num1=random.randrange(1,7)
    num2=random.randrange(1,7)
    num3=random.randrange(1,7)
    #将这3个随机数放到列表中
    number_list.append(num1)
    number_list.append(num2)
    number_list.append(num3)
    return number_list

#print(give_3_number())
    
#比较大小函数，返回big或者small
def get_bigOrSmall(number_list):
    #计算列表的和
    sum_list=sum(number_list)
    if 11<=sum_list<=18:
        return "Big"
    elif 3<=sum_list<=10:
        return "Small"
#print(__name__=="__main__")  

#自身运行时，if永远成立
if __name__=="__main__":
    #设置初始金额
    money=1000
    while True:
        #输入猜想值
        input_string=input("please input your think 'Big' or 'Small' :")
        number_list=give_3_number()
        #计算随机值
        count_string=get_bigOrSmall(number_list)
        
        #猜想值与计算值一样，证明猜想正确
        if input_string==count_string:
            print("congratulation,you are winner")
            #正确加500
            money=money+500
        elif input_string!=count_string:
            #错误减去500
            money=money-500
            if input_string=="Big":
                print("sorry,you are wrang,you think is 'Big',but is ",number_list,"is 'Small'")
            else:
                print("sorry,you are wrang,you think is 'Small',but is ",number_list,"is 'Big'")
        
        print("money is",str(money),"元")
        #第一次结束后提示是否继续
        continue_string=input("continue? n/y")
        #选择退出或金额为0即退出
        if continue_string=="n" or money==0:
            break
        
    