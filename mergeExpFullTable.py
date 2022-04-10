# -*- coding: UTF-8 -*-
import os
from func import ProgressBar
# 设定基准目录
foldPath = "/Users/liuyonglin/Desktop/毕业设计/FinacialData/"
if (os.path.isfile(foldPath + "AllInOne.csv")):
    os.remove(foldPath + "AllInOne.csv")
# 键值对列表（多个Full表的键值对字典构成的列表）
KeyValuesPairs = []
# 总表头
AllKeys = []
# 遍历股票代码
stockCodes = os.listdir(foldPath)
print("正在读取Expand表：")
progress = ProgressBar(len(stockCodes), fmt=ProgressBar.FULL)
for stockCode in stockCodes:
    fullExpandTableFileName = foldPath + stockCode + \
        "/" + stockCode + "_full_expand.csv"
    with open(fullExpandTableFileName, encoding='gbk') as fullExpandTable:
        KeyValuePair = {}
        # 键值对
        keys = fullExpandTable.readline().strip().split(",")
        values = fullExpandTable.readline().strip().split(",")
        i = 0
        for key in keys:
            KeyValuePair[key] = values[i]
            AllKeys.append(key)
            i += 1
        KeyValuesPairs.append(KeyValuePair)
    progress.current += 1
    progress()
progress.done()
AllKeys = list(set(AllKeys))
AllKeys.sort(reverse=True)
AllKeys.remove("股票代码")
AllKeys.insert(0, "股票代码")
AllInOneTableFileName = foldPath + "AllInOne.csv"
with open(AllInOneTableFileName, "w", encoding="gbk") as file2Write:
    # 写表头
    print("正在写入表头：")
    progress = ProgressBar(len(AllKeys), fmt=ProgressBar.FULL)
    for key in AllKeys:
        file2Write.write(key + ",")
        progress.current += 1
        progress()
    file2Write.write("\b\r\n")
    progress.done()
    # 按股票写所有值
    print("正在写入键值对：")
    progress = ProgressBar(len(KeyValuesPairs), fmt=ProgressBar.FULL)
    for KeyValuePair in KeyValuesPairs:
        for key in AllKeys:
            if (key in dict(KeyValuePair)):
                file2Write.write(KeyValuePair[key] + ",")
            else:
                file2Write.write("NaN,")
        file2Write.write("\b\r\n")
        progress.current += 1
        progress()
    progress.done()