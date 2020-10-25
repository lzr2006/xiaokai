#powered py paaliaq
from os import system
class Cmd_easy:
    def __init__(self):
        t = ""
        f = ''
        r = ''
        q = ''
    def time(self):
        system('time' + ' ' + self)
    def date(self):
        system('date' + ' ' + self)
    def rebot(self):
        system('shutdown -r -t' + ' ' + self)
    def notoff(self):
        #self随便传
        system('shutdown -a')
    def assoc(self,new):
        system('assoc .' + self + '=' +new)
    def copy(last,new):
        system('copy' + ' ' + last + ' ' + new)
    def move(last,new):
        system('move' + ' ' + last + ' ' + new)
    def kill(self,all = False,cut = False):
        t = ""
        f = ''
        if all == True:
            t = ' /t'
        if cut == True:
            f = ' /f'
        system('taskkill /im' + ' ' + self + t + f)
    def start(file):
        system('start' + ' ' +file)
    def ren(last,new):
        print('ren' + ' ' + last +' '+ new)
        system('ren' + ' ' + last +' '+ new)
    def tree(drive,file):
        #列举drive驱动器中的所有文件，并写入到file中
        system('tree' + ' ' + drive + ' ' + '>>' + file)
    def md(index):
        system('mkdir' + ' ' + index)
    def print(self):
        system('echo' + ' ' + self)
    def attrib(file,zhidu = False,yincang = False,xitong = False):
        zhi = ' -R'
        xi = ' -S'
        yin = ' -H'
        if zhidu == True:
            zhi = ' +R'
        if xitong == True:
            xi = ' +S'
        if yincang == True:
            yin = ' +H'
        print('attrib' + ' ' +file + zhi + xi + yin)
class Cmd_diffculty():
    def rm(file,all = False,Quiet = False):
        r = ''
        q = ''
        system('rmdir' + ' ' + file +r +q)
        if all == True:
            r = ' /S'
        if Quiet == True:
            q = ' /Q'
