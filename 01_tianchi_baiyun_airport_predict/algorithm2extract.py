# -*- coding:utf-8 -*-

import os
import math

def getFileNameList():
	rootPath = ''
	fileNameList = []
	path = 'D:\\workstation\\repositories\\tianchi\\Baiyun_airport_predict\\data\\resultSet\\'
	for root,dirs,files in os.walk(path):
		for fileName in files:
			fileNameList.append(fileName.strip())
		rootPath = root
	return fileNameList,rootPath


def getSortedRecordList(filePath):
	try:
		fr = open(filePath,'r',encoding='utf-8')
		# 初始化截取列表
		interceptedList = []
		while True:
			line = fr.readline()
			if line:
				lineList = line.strip().split(',')
				# 筛选时间戳大于等于1473505200的纪录
				if lineList[4] >= '1473505200':
					# 获取截取时间后的列表
					interceptedList.append(lineList)
			else:
				break
		# 将列表按照timeStamp字段排序
		sortedRecordList = sorted(interceptedList, key=lambda lineList: lineList[4])
		return sortedRecordList
	except Exception as ex:
		print(ex)


def getListNum(sortedRecordList):
	if sortedRecordList[0][4] == '1473505200':
		beginTimeStamp = sortedRecordList[0][4]
		endTimeStamp = sortedRecordList[len(sortedRecordList) - 1][4]
		listNum = math.ceil((int(endTimeStamp) - int(beginTimeStamp)) / 60 / 10)
		print(listNum)
		return listNum


def getAverageCount(tempList):
	sumAccount = 0
	avgAccount = 0
	for item in tempList:
		sumAccount = sumAccount + int(item[1])
	if sumAccount:
		avgAccount = sumAccount / len(tempList)
	return avgAccount


def write2csv(finalInfoList):
	try:
		filePath = os.path.join(os.path.dirname(__file__),'data','wifi_ap_passenger_2ndround_separated.csv')
		fw = open(filePath,'w',encoding='utf-8')
		# 遍历列表
		for itemPort in finalInfoList:
			for itemPer in itemPort:
				fw.writelines(itemPer[0] + ',' + itemPer[1] + ',' + itemPer[2] + ',' + itemPer[3] + ',' + itemPer[4] + '\n')
		fw.close()
	except Exception as ex:
		print(ex)



if __name__ == '__main__':
	# 读取文件名列表
	fileNameList,rootPath = getFileNameList()
	# 总纪录列表
	finalInfoList = []
	for i in range(len(fileNameList)):
		# 获取文件路径
		filePath = os.path.join(rootPath,fileNameList[i])
		# 加载文件数据
		sortedRecordList = getSortedRecordList(filePath)
		# 获取列表个数（用来分割数据记录）
		listNum = getListNum(sortedRecordList)
		# 分割数据
		resultList = []
		endStamp = 1473505140
		for i in range(listNum):
			tempList = []
			startStamp = endStamp + 60
			endStamp = startStamp + (i+1) * 60 * 9
			# 筛选符合条件的记录
			for item in sortedRecordList:
				if int(item[4]) > startStamp and int(item[4]) < endStamp:
					tempList.append(item)
			# 计算平均旅客数量
			avgPasrCount = getAverageCount(tempList)
			#
			if tempList:
				print(str(tempList[0]))
				perRecord = [tempList[0][0],str(int(avgPasrCount)),tempList[0][2],tempList[0][3],tempList[0][4]]
				print(perRecord)
				#
				resultList.append(perRecord)
		finalInfoList.append(resultList)
	# 将结果写入到文本
	write2csv(finalInfoList)


		# j = 1
		# for item in sortedRecordList:
		# 	if j == 100:
		# 		break
		# 	print(str(item),j)
		# 	j += 1
		# exit(0)
