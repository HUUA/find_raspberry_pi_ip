# -*- coding:utf8 -*-
import os
print ('--------------脚本环境----------------\n' + \
       '系统    ubuntu\n' + \
       'python版本    3\n' + \
       '--------------------------------------')
an = input('请问你的树莓派和你的电脑是否在同一网络内？(yes/no)')
while an != 'yes':
    print ('走点心行不行？！(╬▔＾▔)凸检查下环境再来！')
    break
else:
    print (' ')
    print ('让我们继续吧！ \n' + \
            '检测树莓派的ip需要nmap工具')
    if os.system('sudo dpkg -l | grep -i nmap') != 0:
        print ('#############################################################')
        print ('你未安装nmap,将为你安装nmap软件')
        print ('#############################################################')
        os.system('sudo apt-get install nmap -y')
    else:
        print ('############################################################')
        print ('你已安装nmap软件,直接进行下一步')
        print ('############################################################')
    print (' ')
    IP = input("请以'192.168.1.0/24'的格式输入你的网段以及子网掩码：")
    while IP == None:
        print ('没有检测到你输入的网段，请确认输入！')
        break
    else:
        print (' ')
        print ("ok,你的输入为：'%s' \n"%IP + \
               '###################树莓派的信息如下##########################\n' + \
               ' ')
        os.system("sudo nmap -sP '%s'| grep Raspber -B 2"%IP)
        print (' ')
        print ('#############################################################\n' + \
               ' ')
        print ('Come on！让我们开始开始愉快地玩耍吧~')
