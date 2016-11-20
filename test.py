# -*- coding:utf-8 -*-
import time
import math
import os

def findSubStr(substr, str, i):
    count = 0
    while i > 0:                   #循环来查找
        index = str.find(substr)
        if index == -1:
            return -1
        else:
            str = str[index+1:]   #第一次出现该字符串后后面的字符
            i -= 1
            count = count + index + 1   #位置数总加起来
    return count - 1



line = """2,新,"黄,沈",黄家山村,1394040****"""
print(findSubStr('"',line,1))
print(findSubStr('"',line,2))
print(line[findSubStr('"',line,1):findSubStr('"',line,2)+1])
str2 = line[findSubStr('"',line,1):findSubStr('"',line,2)+1]
str1 = line[:findSubStr('"',line,1)]
str3 = line[findSubStr('"',line,2)+1:]
print(str1)
print(str2)
print(str3)

# testLine = """jjjjkjk"""
# print(findSubStr('"',testLine,1))




# testList = ['a','b','c']
# result = ','.join(testList)
# print(result)


# testList = [[2,3,14],[3,5,12],[4,7,11]]
# print(testList)
# testList = sorted(testList,key=lambda item:item[2])
# print(testList)



# st1 = '112'
# st2 = '32'



# path = 'F:\\repositories\\tianchi\\Baiyun_airport_predict\\data\\resultSet\\20161016'
# for root,dirs,files in os.walk(path):
# 	for fileName in files:
# 		print(fileName)
# 	# for dirName in dirs:
# 	# 	print(dirName)
# 	print(dirs)
# 	print(root)



# print(math.ceil((1473836340 - 1473505200) / 60 / 10))
# print(3*24*6 + 19*6 + 6)


# dic = {}
# dic['a'] = ['a1','a2']
# dic['b'] = ['b1','b2']
# print(dic)
# for key,value in dic.items():
# 	print(key,value)


# line = 'E1-1A-1<E1-1-01>,15,2016-09-10-18-55-04'
# lineList = line.strip().split(',')
# print(lineList)
# newTimeStr = lineList[2][0:16]
# print(newTimeStr)
# structTime = time.strptime(newTimeStr,'%Y-%m-%d-%H-%M')
# timeStamp = int(time.mktime(structTime))
# print(type(timeStamp))
# print(timeStamp)


# # py初始化字典
# dic = {}
# dic['a'] = []
# dic['b'] = []
# print(dic)
# print(type(dic))


# # 时间戳以“秒”为单位
# # timeStr = '2016-09-10-18-55-04'
# timeStr1 = '2016-09-10-18-55'
# timeStr2 = '2016-09-11-18-55'
# # structTime = time.strptime(timeStr,'%Y-%m-%d-%H-%M-%S')     # result: 1473504904.0
# structTime1 = time.strptime(timeStr1,'%Y-%m-%d-%H-%M')        # result: 1473504900.0
# structTime2 = time.strptime(timeStr2,'%Y-%m-%d-%H-%M')        # result: 1473504900.0
# timeStamp1 = time.mktime(structTime1)
# timeStamp2 = time.mktime(structTime2)
#
# print(timeStamp2-timeStamp1)    #86400.0
# print(86400/24/60/60)


# timeStamp = 1473504900
# structedTime = time.localtime(timeStamp)
# strTime = time.strftime('%Y-%m-%d-%H-%M',structedTime)
# print(strTime)
