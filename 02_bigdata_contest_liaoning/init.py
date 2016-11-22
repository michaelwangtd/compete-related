# -*- coding:utf-8 -*-

#-------------------
# Author:CaptWang
# Source:Bigdata LiaoNing
# Date:2016/11/21
#-------------------

from math import *

"""
    1 fault_set一共18列，complaint_set一共32列
    2 纬度(latitude)   经度(longitude)
"""


def findSubStr(substr, str, i):
    '''
        找出第i个字串位置
    '''
    count = 0
    while i > 0:                   
        index = str.find(substr)
        if index == -1:
            return -1
        else:
            str = str[index+1:]   
            i -= 1
            count = count + index + 1   
    return count - 1


def getDistance(Lat_A,Lng_A,Lat_B,Lng_B): 
    '''
        get distance by lat and lng
    '''
    ra=6378.140 #赤道半径
    rb=6356.755 #极半径 
    flatten=(ra-rb)/ra  #地球偏率
    rad_lat_A=radians(Lat_A)
    rad_lng_A=radians(Lng_A)
    rad_lat_B=radians(Lat_B)
    rad_lng_B=radians(Lng_B)
    pA=atan(rb/ra*tan(rad_lat_A))
    pB=atan(rb/ra*tan(rad_lat_B))
    xx=acos(sin(pA)*sin(pB)+cos(pA)*cos(pB)*cos(rad_lng_A-rad_lng_B))
    c1=(sin(xx)-xx)*(sin(pA)+sin(pB))**2/cos(xx/2)**2
    c2=(sin(xx)+xx)*(sin(pA)-sin(pB))**2/sin(xx/2)**2
    dr=flatten/8*(c1-c2)
    distance=ra*(xx+dr)
    return distance



def readTxt2List(filePath):
    '''
        load data from txt
    '''
    resultList = []
    fr = open(filePath,'r',encoding='utf-8')
    i = 1
    while True:
        try:
            line = fr.readline()
            if line:
                tempStr = line.strip().replace('\ufeff','')
                if findSubStr('"',tempStr,1) != -1 and findSubStr('"',tempStr,2) != -1:
                    str2 = line[findSubStr('"', line, 1):findSubStr('"', line, 2) + 1]
                    str1 = line[:findSubStr('"', line, 1)]
                    str3 = line[findSubStr('"', line, 2) + 1:]
                    str2 = str2.replace(',','，')
                    tempStr = str1 + str2 + str3
                lineList = tempStr.split(',')
                # print(i,len(lineList),lineList)
                # print(lineList)
                resultList.append(lineList)
                i += 1
            else:
                break
        except Exception as ex:
            print(ex)
    if resultList:
        return resultList


def createLinkList(complaintRecord,faultList):
    '''
        找出符合条件的记录
    '''
    resultSet = []
    dayTime = 86400.0
    endTime = complaintRecord[len(complaintRecord)-1]
    startTime = str(float(endTime) - dayTime)
    # dayTime范围内的故障纪录
    for item in faultList:
      if item[len(item)-2] <endTime and item[len(item)-2] > startTime:
          # 计算两者经纬度距离
            try:
                tempItem = []
                # print('----',float(complaintRecord[14]),float(complaintRecord[13]),float(item[9]),float(item[8]))
                if float(complaintRecord[14]) == float(item[9]) and float(complaintRecord[13]) == float(item[8]):
                    tempItem.extend(item)
                    tempItem.append(str(0.0))
                else:
                    distanceFloat = getDistance(float(complaintRecord[14]),float(complaintRecord[13]),float(item[9]),float(item[8]))
                    # print(distanceFloat)
                    tempItem.extend(item)
                    tempItem.append(str(distanceFloat))
                    # item.append(str(distanceFloat))
                    # print('new item:',str(item))
                resultSet.append(tempItem)
            except Exception as ex:
                print(ex)
    sortedResultSet = sorted(resultSet,key=lambda item:item[len(item)-1])
    if sortedResultSet:
        complaintRecord.extend(sortedResultSet[0])
        print(len(complaintRecord),complaintRecord)
    return complaintRecord



if __name__ == '__main__':


    complaintSet = readTxt2List('complaint_set.csv')
    faultSet = readTxt2List('fault_set.csv')


    fw = open('result_set.csv','w',encoding='utf-8')
    title = "工单流水号,主题,完成时间,反馈区县,反馈地市,建单时间,投诉分类,用户归属地,故障号码,故障时间,反馈区县1,故障地点,故障地点1,经度,纬度,客户姓名,故障号码.1,客户品牌,客户级别,投诉时间,是否大面积投诉,工单性质,网络标识,用户类型,投诉场景,1问题原因,处理措施,网络口建议投诉分类,网络口建议投诉原因,疑难投诉,处理结果,投诉时间1,|网管告警流水号,告警标题,告警级别,告警发生时间,告警清除时间,告警网元,设备类型,告警对象名称,x,y,告警对象类型,设备厂家,所属城市,所属区县,是否派单,基站覆盖类型,告警发生时间1,告警清除时间1,基站距离"
    fw.writelines(title + '\n')

    i = 1
    for item in complaintSet:
        print('complaintSet',i,item)
        finalList = createLinkList(item,faultSet)
        outputLine = ','.join(finalList)
        # print(type(outputLine),outputLine)
        fw.writelines(outputLine + '\n')
        i += 1
    fw.close()


