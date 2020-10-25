def __init__():
    print('随机数内核已经启动！')
def math():
    #coding:utf-8
    try:
        l=5
        import random
        from time import sleep
        print("欢迎使用加减法自定义生成器")
        sleep(0.3)
        q=0
        m=100
        print("---------------------------------------------------")
        print("预备区块")
        z=int(input("输入欲生成的题目数量:"))
        l=int(input("请输入每题的时间:"))
        g=int(input("请输入可能出现的最大值:"))
        q=m/z
        print("---------------------------------------------------")
        print("开始生成！")

        i=0
        #加法模块
        while i<z:
            x=str(random.randint(1,g/2))
            y=str(random.randint(1,g/2))
            print(x+"+"+y+"=")
            f=int(x)+int(y)
            qwq=("输入答案:")
        
            sleep(l)
            if qwq==f:
                print("哎呀，粗问题啦，请重试")
            else:
                print("时间到")
                print("本题答案是"+str(f)) 
        
            i=i+1
            sleep(0.2)
        #减法模块
            x=str(random.randint(1,g/2))
            y=str(random.randint(1,g/2))
            while x<y:
                x=int(x)+random.randint(1,4)  
                #防止出现负数
                x=str(x)      
            print(x+"-"+y+"=")
            f=int(x)-int(y)
            qwq=("输入答案:")
            sleep(l)
            if qwq==f:
                print("哎呀，粗问题啦，请重试")
            else:
                print("时间到")
        
            print("本题答案是"+str(f)) 
            sleep(0.2)
            i=i+1
        print("---------------------------------------------------")
        print("程序自检")
        print("已经生成"+str(z)+"道题目")
        print("每题可得"+str(q)+"分")
        time=int(input("请输入分数:"))
        jiyi=100-time
        print("今天推荐做"+str(jiyi)+"道题目")
        print("---------------------------------------------------")
    except ValueError:
        print("请做点人事吧！！！")

def sorting():
    import random
    #获取内容
    i1=input("输入第一个内容")
    i2=input("输入第二个内容")
    i3=input("输入第三个内容")
    i4=input("输入第四个内容")
    i5=input("输入第五个内容")
    i6=input("输入第六个内容")
    i7=input("输入第七个内容")
    i8=input("输入第八个内容")
    i9=input("输入第九个内容")
    i10=input("输入第十个内容")
    #写入列表
    ran=[i1,i2,i3,i4,i5,i6,i7,i8,i9,10]
    #取随机数
    #随机输出
    for j in range(1,11):
        x = random.randint(0,9 )
        print(ran[x])
    def help():
        print("随机数帮助系统...")
        print("输入随机出题可以出加减法题目，输入随机排序可以进行排序。")
if __name__ == '__main__':
    print("请勿直接调用！")


    
