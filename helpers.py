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

