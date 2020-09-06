import time
from gpiozero import LED

out1 = LED(11)
out2 = LED(9)
out3 = LED(10)
ball1 = LED(26)
ball2 = LED(19)
ball3 = LED(13)
ball4 = LED(6)
strike1 = LED(21)
strike2 = LED(20)
strike3 = LED(16)
topInn = LED(12)
botInn = LED(5)

#pass in text to split based on '|' character
def splitter(data):
    splitList=[]
    newStr=''
    for i in data:
        if i != '|':
            newStr += str(i)
        elif i == '|':
            splitList.append(newStr)
            newStr = ''
    #adds the very last string to the list since the string does not start or end with '|'
    if newStr != 0:
        splitList.append(newStr)
    return splitList

def displayStats(balls, strikes, outs):
    displayBalls(balls)
    displayStrikes(strikes)
    displayOuts(outs)
    return

def displayInning(innNum, innTB):
    #handle innNum later
    if innTB == 'Top':
        topInn.on()
        botInn.off()
    elif innTB == 'Bot':
        botInn.on()
        topInn.off()
    else:
        topInn.off()
        botInn.off()
    return

def displayOuts(outs):
    if outs is 0:
        out1.off()
        out2.off()
        out3.off()
    elif outs is 1:
        out1.on()
        out2.off()
        out3.off()
    elif outs is 2:
        out1.on()
        out2.on()
        out3.off()
    elif outs is 3:
        out1.on()
        out2.on()
        out3.on()
    else:
        out1.off()
        out2.off()
        out3.off()
    return

            
def displayBalls(balls):
    if balls is 0:
        ball1.off()
        ball2.off()
        ball3.off()
        ball4.off()            
    elif balls is 1:
        ball1.on()
        ball2.off()
        ball3.off()
        ball4.off()            
    elif balls is 2:
        ball1.on()
        ball2.on()
        ball3.off()
        ball4.off()            
    elif balls is 3:
        ball1.on()
        ball2.on()
        ball3.on()
        ball4.off()            
    elif balls is 4:
        ball1.on()
        ball2.on()
        ball3.on()
        ball4.on()            
    else:
        ball1.off()
        ball2.off()
        ball3.off()
        ball4.off()            
    return
        
            
def displayStrikes(strikes):
    if strikes is 0:
        strike1.off()
        strike2.off()
        strike3.off()
    elif strikes is 1:
        strike1.on()
        strike2.off()
        strike3.off()
    elif strikes is 2:
        strike1.on()
        strike2.on()
        strike3.off()
    elif strikes is 3:
        strike1.on()
        strike2.on()
        strike3.on()
    else:
        strike1.off()
        strike2.off()
        strike3.off()
    return

def displayBases(bases):
    lst = [1,1,1]
    for cnt, i in enumerate(bases):
        if i.find('transparent') != (-1):
           lst[cnt] = 0 
           #turn off a specific led here
    return lst
