import time
from gpiozero import LED

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

def displayStats(balls, strikes, outs):
    displayBalls(balls)
    displayStrikes(strikes)
    displayOuts(outs)
    return

def displayOuts(outs):
    if outs is 0:
        print('No outs')
        out1.off()
        out2.off()
        out3.off()
    elif outs is 1:
        print('1 outs')
        out1.on()
        out2.off()
        out3.off()
    elif outs is 2:
        print('2 outs')
        out1.on()
        out2.on()
        out3.off()
    elif outs is 3:
        print('3 outs')
        out1.on()
        out2.on()
        out3.on()
    else:
        print('Outs != 0,1,2, or 3')
        out1.off()
        out2.off()
        out3.off()
    return

            
def displayBalls(balls):
    if balls is 0:
        print('No Balls')
        ball1.off()
        ball2.off()
        ball3.off()
        ball4.off()            
    elif balls is 1:
        print('1 balls')
        ball1.on()
        ball2.off()
        ball3.off()
        ball4.off()            
    elif balls is 2:
        print('2 balls')
        ball1.on()
        ball2.on()
        ball3.off()
        ball4.off()            
    elif balls is 3:
        print('3 balls')
        ball1.on()
        ball2.on()
        ball3.on()
        ball4.off()            
    elif balls is 4:
        print('4 balls')
        ball1.on()
        ball2.on()
        ball3.on()
        ball4.on()            
    else:
        print('Balls != 0,1,2,3,4')
        ball1.off()
        ball2.off()
        ball3.off()
        ball4.off()            
    return
        
            
def displayStrikes(strikes):
    if strikes is 0:
        print('No Strikes')
        strike1.off()
        strike2.off()
        strike3.off()
    elif strikes is 1:
        print('1 strikes')
        strike1.on()
        strike2.off()
        strike3.off()
    elif strikes is 2:
        print('2 strikes')
        strike1.on()
        strike2.on()
        strike3.off()
    elif strikes is 3:
        print('3 strikes')
        strike1.on()
        strike2.on()
        strike3.on()
    else:
        print('Strikes != 0,1,2,3')
        strike1.off()
        strike2.off()
        strike3.off()
    return


