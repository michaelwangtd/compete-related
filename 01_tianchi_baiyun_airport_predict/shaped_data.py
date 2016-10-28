# -*- coding:utf-8 -*-

import os
import time

def getWifiApTagSetList():
	wifiSetList = []
	try:
		filePath = os.path.join(os.path.dirname(__file__),'data','WIFI_AP_Passenger_Records_chusai_2ndround.csv')
		fr = open(filePath,'r',encoding='utf-8')
		i = 1
		while True:
			line = fr.readline()
			if line.strip() != 'WIFIAPTag,passengerCount,timeStamp':
				if line :
					lineList = line.strip().split(',')
					wifiSetList.append(lineList[0])
					print('已读取第',str(i),'条数据...')
					i += 1
				else:
					break
		fr.close()
	except Exception as err:
		print('读取文本出现问题:',err)
	wifiSetList = sorted(list(set(wifiSetList)))
	return wifiSetList


def writeSetList2Txt(wifiSetList):
	try:
		filePath = os.path.join(os.path.dirname(__file__),'data','wifi_ap_passenger_set_list.txt')
		fw = open(filePath,'a',encoding='utf-8')
		if wifiSetList:
			# 遍历列表
			i = 1
			for item in wifiSetList:
				fw.writelines(item + '\n')
				print('写入第',str(i),'条数据...')
				i += 1
		fw.close()
	except Exception as err:
		print('写入文件出错:',err)


def createWifiPortDict():
	wifiPortDict = {}
	try:
		filePath = os.path.join(os.path.dirname(__file__),'data','wifi_ap_passenger_set_list.txt')
		fw = open(filePath,'r',encoding='utf-8')
		while True:
			line = fw.readline().strip()
			if line:
				# 初始化wifiPort字典
				wifiPortDict[line] = []
			else:
				break
	except Exception as err:
		print('初始化字典出错：',err)
	return wifiPortDict


def createDictObject(wifiPortDict):
	'''
	1 将原始文本信息读入字典
	2 添加处理的时间字段
	3 将时间转换成时间戳
	'''
	# 对文本信息逐条处理
	try:
		i = 1
		filePath = os.path.join(os.path.dirname(__file__),'data','WIFI_AP_Passenger_Records_chusai_2ndround.csv')
		fr = open(filePath,'r',encoding='utf-8')
		while True:
			line = fr.readline().strip()
			if line != 'WIFIAPTag,passengerCount,timeStamp':
				if line:
					# line字符串分割
					lineList = line.strip().split(',')
					# 添加时间字段
					newTimeStr = lineList[2][0:16]
					# 转换成时间戳
					structTime = time.strptime(newTimeStr, '%Y-%m-%d-%H-%M')
					timeStamp = int(time.mktime(structTime))
					# 拼装新的纪录数据
					lineNew = line + ',' + newTimeStr + ',' + str(timeStamp)
					# 将新的纪录数据写入到对应字典
					wifiPortDict[lineList[0]].append(lineNew)
					print('已处理第',str(i),'条数据...')
					i += 1
				else:
					break
		fr.close()
	except Exception as err:
		print('形成字典对象出错：',err)
	return wifiPortDict


def dictObjWrite2Txt(wifiDictObj):
	elementPath = os.path.join(os.path.dirname(__file__),'data','resultSet')
	# 遍历字典
	for key,value in wifiDictObj.items():
		filePath = os.path.join(elementPath , 'wifi_ap_' + str(key).replace('<','_').replace('>','') + '_list.csv')
		print('创建',filePath,'文本...')
		fw = open(filePath,'a',encoding='utf-8')
		for item in value:
			fw.writelines(item.strip()+ '\n')
		fw.close()
		print('写入',filePath,'文本完成...')


def createTxtByFormat():
	try:
		i = 1
		filePath = os.path.join(os.path.dirname(__file__),'data','WIFI_AP_Passenger_Records_chusai_2ndround.csv')
		fr = open(filePath,'r',encoding='utf-8')
		wFilePath = os.path.join(os.path.dirname(__file__),'data','resultSet','WIFI_AP_Passenger_Records_2ndnew.csv')
		fw = open(wFilePath,'a',encoding='utf-8')
		fw.writelines('WIFIAPTag,passengerCount,timeFormat1,timeFormat2,timeStamp' + '\n')
		while True:
			line = fr.readline().strip()
			if line != 'WIFIAPTag,passengerCount,timeStamp':
				if line:
					# line字符串分割
					lineList = line.strip().split(',')
					# 添加时间字段
					newTimeStr = lineList[2][0:16]
					# 转换成时间戳
					structTime = time.strptime(newTimeStr, '%Y-%m-%d-%H-%M')
					timeStamp = int(time.mktime(structTime))
					# 拼装新的纪录数据
					lineNew = line + ',' + newTimeStr + ',' + str(timeStamp)
					fw.writelines(lineNew + '\n')
					print('写入第',str(i),'条数据...')
					i += 1
				else:
					break
		fw.close()
		fr.close()
	except Exception as err:
		print('写入格式文本出错:',err)



if __name__ == '__main__':

	# # # part1
	# # 获取wifi_ap_tag的种类列表
	# wifiSetList = getWifiApTagSetList()
	# # wifiSetList写入到文本
	# writeSetList2Txt(wifiSetList)

	# 初始化wifiPort字典
	wifiPortDict = createWifiPortDict()
	# 形成字典对象
	wifiDictObj = createDictObject(wifiPortDict)
	# 将wifi字典对象持久化
	dictObjWrite2Txt(wifiDictObj)

	## part2
	# 按照格式输出文件
	# createTxtByFormat()