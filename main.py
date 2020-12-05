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
sys.path.append('C:\\users\\administrator\\desktop\\XiaoKai\\packages\\games')
#引入其他轮子
import XKrandom
import XKtranslation
import XKsettings
import XKmath
import Chasinggame

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
    global m
    m = 0
    global gs
    gs = 0


#程序主体-----------------------------------------程序主体#
try:
    while True:
        e = t.localtime()
        restart()    
        user_import = input("toy's world>")# 输入内容
        f = open('C:\\users\\administrator\\desktop\\xiaokai\\logs\\input.txt','a')
        f.write(str(e[0]) + '年' + str(e[1]) + '月' + str(e[2]) + '日' + str(e[3]) + '时' + str(e[4]) + '分' + str(e[5]) + '秒' + ':' + (user_import + '\n'))
        for hello0 in hello: #问好模块
            if user_import == hello0: #判断模块
                print(hello[s.randint(0,8)])  #随机输出
            elif user_import.endswith('?'):
                webbrowser.open("https://www.sogou.com/sie?hdq=[AQxRG-0000&query="+str(user_import)+"&ie=utf8")
                print(f'为您搜索{user_import}')
                break
            elif user_import == '随机数内核': #随机数模块.
                while i == 0:
                    user_input = input('toysworld\\random-system>')
                    if user_input == '随机排序':
                        XKrandom.sorting()
                    elif user_input == '随机出题':
                        XKrandom.math()
                    elif user_input == '返回':
                        i = 1
                    elif user_input == '帮助':
                        XKrandom.help()
                    else:
                        print('没有这个操作...')
            elif user_import == '数学':
                while m == 0:
                    user_input = input('toysworld\\math-system>')
                    if user_input == '计算平均数':
                        XKmath.meaner()
                    elif user_input == '计算器':
                        XKmath.calc.go()
                    elif user_input == '返回':
                         m = 1
                         break
                    else:
                        print(f'"{user_input}"并不是小恺数学标准库中的函数,也不是可执行的命令.')
            elif user_import == '翻译':
                print('仅仅是调用接口，如需大批量翻译请勿使用本程序！')
                XKtranslation.main()
                break
            elif user_import == '游戏':
                while gs == 0:
                    user_input = input('toysworld\\game-system>')
                    if user_input == '追逐游戏':
                        Chasinggame.main()
                    else:
                        print("暂时没有这个游戏...")
                        gs = 4
            elif user_import == '配置':
                XKsettings.do.todo()
except ValueError as reason:
    print(str(reason))
    f = open("C:\\users\\administrator\\desktop\\xiaokai\\logs\\Errors.nlg","w")
    f.write("ValueError" + "\n" + str(reason))
    f.close()
