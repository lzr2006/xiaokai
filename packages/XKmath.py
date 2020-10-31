#pylint:disable=W0612
#pylint:disable=E0001
#pylint:disable=W0622
#!/usr/bin/env python3
import time
def meaner():
    try:
        N = int(input("请输入要计算数字的个数:"))
        num = 0
        sum =0
        count = 0
        print("请输入{}个数字:".format(N	))
        while count < N:
	           number = float(input())
	           sum = sum + number
	           count = count + 1
        average = sum/N
        print("共计算了{}个数字,总和是{}".format(N, sum))
        print("平均数 = {:.2f}".format(average))

    except ValueError:
        print("老老实实输入一个数字它不香么？")
        e = time.localtime()
        file = open('C:\\Users\Administrator\\Desktop\\xiaokai\\logs\\calcerror' +  '.txt','wb')
        file.write(str(e[0]) + '年' + str(e[1]) + '月' + str(e[2]) + '日' + str(e[3]) + '时' + str(e[4]) + '分' + str(e[5]) + '秒' + '错误：在计算器中输入了非法的信息')


        
class calc:
    class info:
        def andder():
            print("计算加法...")
        def subber():
            print("计算减法...")
        def muller():
            print("计算乘法...")
        def divver():
            print("计算除法...")
        def __init__(*args):
            print("感谢使用我的计算器")
        def __del__(*args):
            print("离开...")
        def error():
            print("请不要乱输入!")
            
   
    class do:
        def andder(num1,num2):
            print(str(int(num1) + int(num2)))
        def sub(num1,num2):
            print(str(int(num1) - int(num2)))
        def mul(num1,num2):
            print(str(int(num1) * int(num2)))
        def div(num1,num2):
            print(str(int(num1) / int(num2)))
        
    def go(*args):
        num1 = input("输入第一个数>")
        num2 = input("输入第二个数>")
        user = input("输入运算类型(加/减/乘/除)>")

        if user == "加":
            calc.info.andder()
            calc.do.andder(num1,num2)
        elif user == "减":
            calc.info.subber()
            calc.do.sub(num1,num2)
        elif user == "乘":
            calc.info.muller()
            calc.do.mul(num1,num2)
        elif user == "除":
           calc.info.divver()
           calc.do.div(num1,num2)
        else:
            calc.info.error()
       
       
if __name__ == "__main__":
    print("Xiao Kai System Error: \nError1:\nCan't do it. \n(The last calling):小恺数学模块:请勿直接调用!")
    
