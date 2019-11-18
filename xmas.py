import termcolor
import random
import time, datetime
import sys, os
from colorama import init
from termcolor import colored

def clear():   
    if sys.platform == 'win32': # if windows 
        return os.system('cls')
    else: #if *nix
        return os.system('clear')
        
        
colors = [
        'red',
        'green',
        'yellow',
        'blue',
        'magenta',
        'cyan',
        'white']

yellowlight = termcolor.colored('o', 'yellow')
magentalight = termcolor.colored('o', 'magenta')
cyanlight = termcolor.colored('o', 'cyan')

lightlist = [yellowlight, cyanlight, magentalight]

init()
while True: #exit with ctrl+C
    print('to exit use a keyboard interrupt (ctrl+c)')
    for i in range(1,30,2): #tree
        tree = ''
        for j in range(i): #make lights
            randNum=random.randint(0,500)
            if (randNum <= 750) and (randNum >=250) :
                tree += lightlist[random.randint(0,2)]
            else:
                tree += termcolor.colored('*', 'green')
        string = '_'*(15-int(i/2))+tree+'_'*(15-int(i/2))+'\n'
        print(string,end='')
    trunk=colored('mWm', 'yellow')
    for k in range(3): #trunk
        outbuffer = '_'*14+trunk+'_'*14+'\n'
        print(outbuffer, end='')
        merry_Christmas =termcolor.colored('Merry Christmas', colors[random.randint(0,len(colors)-1)]) 
    outbuffer2 = '_'*8+merry_Christmas+'_'*8+'\n'
    print(outbuffer2, end='')
    time.sleep(0.4)
    clear()
    
    