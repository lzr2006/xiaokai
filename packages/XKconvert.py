#edit:qpy
#功能:进行部分常见单位转换
print("输入格式:数值+单位(只包括字母).例如在摄氏度和华氏度的转换中输入7F就是把7℉转换为摄氏度.")
def cf(*args):
    TempStr = input ("请输入带有符号的温度值：") 
    if TempStr[-1] in ["f","F"]:
        C = (eval(TempStr[0:-1]) - 32)/1.8 
        print(f"转换后为{C}℃") 
    elif TempStr[-1] in ['C', 'c']:
        F = 1.8*eval(TempStr[0:-1]) + 32 
        print(f"转换后为{F}°F") 
    else: 
        print("输入格式错误")
        
