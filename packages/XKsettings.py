#pylint:disable=E0001
#小恺简易配置程序 /玩科光电/玩具世界科技部.
from time import time,sleep
from os import system
print("Toysworld (©2016-2020) Studio. all rights reserved. Unix timestamp:" + str(int(time())) + ".")
i = 0
class do():
    def normal(*args):
        sleep(3)
        print("删除tar文件...")
        system("start C:\\users\\administrator\\desktop\\xiaokai\\setuptools\\deltar.bat")
        sleep(3)
        print("关联文件...")
        system("start C:\\users\\administrator\\desktop\\xiaokai\\setuptools\\files.bat")
        sleep(3)
        print("创建目录...")
        system("start C:\\users\\administrator\\desktop\\xiaokai\\setuptools\\folder.bat")
        sleep(3)
        print("删除开发目录...")
        system("rd /s /q C:\\users\\administrator\\desktop\\xiaokai\\notes")
        sleep(3)
        print("Success!\n恭喜,您可以正常的使用小恺了.")
        sleep(3)
    def developer(*argv):
    	  sleep(3)
    	  print("删除tar文件...")
    	  system("start C:\\users\\administrator\\desktop\\xiaokai\\setuptools\\deltar.bat")
    	  sleep(3)
    	  print("关联文件...")
    	  system("start C:\\users\\administrator\\desktop\\xiaokai\\setuptools\\files.bat")
    	  sleep(3)
    	  print("创建目录...")
    	  system("start C:\\users\\administrator\\desktop\\xiaokai\\setuptools\\folder.bat")
    	  sleep(3)
    	  print("Success!\n恭喜,您可以正常的使用小恺了.")
    	  sleep(3)
    	
while i == 0:
    user = input("The Xiaokai Standard Library>")
    if user == "normal":
        print("自动一般模式处理开始...") 
        do.normal()
        break
    elif user == "developer":
    	print('开发者处理模式开始...')
    	do.developer()
    	break
    else:
        print(f"'{user}'并不是可行的模式,也不是可执行的命令.")
