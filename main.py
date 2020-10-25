#usr/bin/python3
#coding:utf-8
#引入轮子
import time as t
import pyautogui as p
import random as s
import os
import webbrowser
import sys
sys.path.append('C:\\users\\administrator\\desktop\\XiaoKai\\packages')
#引入其他轮子
import XKrandom
#定义列表区
hello=['hi','hello','你好','你好啊','你好哇','您好','您好啊','嗨','嘿']

#定义变量区
random_start=1
random_end=10
print("玩具世界科技(2018-2020) toy's world 出品")
print("版权所有 (C) toy's world corporation 。 保留所有权利。") #输出权利文本

#子函数
def restart():
    global i
    i = 0

#程序主体-----------------------------------------程序主体#
while True:
    restart()    
    user_import = input("toy's world>")    # 输入内容
    for hello0 in hello: #问好模块
        if user_import == hello0: #判断模块
            print(hello[s.randint(0,8)])  #随机输出
        elif user_import.endswith('?'):
            webbrowser.open("https://www.sogou.com/sie?hdq=[AQxRG-0000&query="+str(user_import)+"&ie=utf8")
            print(f'为您搜索{user_import}')
            break
        if user_import == "cmd":                   #cmd功能
            print(" 温馨提示:输入'start'打开cmd窗口,输入cmd -s[command]可以运行指定命令行,-s与[command]之间不留空格")
            os.system("cmd.exe")
            break
        elif user_import.startswith("cmd -s"):      #运行指定命令
             cmd_control=user_import.split("-s",1)
             cmd_control_user = cmd_control[1]
             cmd_control_user=str(cmd_control_user)#提取用户输入
             os.system("cmd /C" + cmd_control_user)
             break
        elif user_import == '随机数内核':
            while i == 0:
                user_input = input('toysworld\\random-system>')
                if user_input == '随机排序':
                    XKrandom.sorting()
                elif user_input == '随机出题':
                    XKrandom.math()
                elif user_input == '退出':
                    i = 1
                else:
                    print('没有这个操作...')

            





