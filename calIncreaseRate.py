# -*- coding: UTF-8 -*-
import os
from func import ProgressBar
# 设定基准目录
foldPath = "/Users/liuyonglin/Desktop/毕业设计/"
# 键值对列表
KeyValuesPairs = []
# 总表头
AllKeys = []
# 全部股票代码
stockCodes = []
# 处理的项目
ItemsToDealList = [
    "营业收入",
    "净利润",
    "固定资产",
    "收取利息、手续费及佣金的现金",
    "利润总额",
    "研发费用",
]
# 年份
years = ["2021", "2020", "2019", "2018", "2017", "2016",
         "2015", "2014", "2013", "2012", "2011", "2010"]

print("正在读取 AllInOne.csv 文件中的数据...")
with open(foldPath + "AllInOne.csv", encoding='gbk') as AllInOneFile:
    KeyValuePair = {}
    # 键值对
    keys = AllInOneFile.readline().strip().split(",")
    keys.remove("股票代码")
    for line in AllInOneFile:
        stockCode = line.strip().split(",")[0]
        stockCodes.append(stockCode)
        values = line.strip().split(",")
        values.remove(stockCode)
        i = 0
        for key in keys:
            KeyValuePair[stockCode + "_" + key] = values[i]
            AllKeys.append(stockCode + "_" + key)
            i += 1
            KeyValuesPairs.append(KeyValuePair)

print("正在计算各指标各年间增长率数据...")
with open(foldPath + "IncreaseRate.csv", "w", encoding='gbk') as file2Write:
    # 填充表头
    file2Write.write("股票代码")
    for key in ItemsToDealList:
        indexOfYears = 0
        for year in years:
            if (indexOfYears < len(years) - 1):
                file2Write.write("," + key + "_" + years[indexOfYears + 1] + "~" + years[indexOfYears])
                indexOfYears += 1
    file2Write.write("\r\n")
    # 填充表头

    # 计算增长率
    progress = ProgressBar(len(stockCodes), fmt=ProgressBar.FULL)
    for stockCode in stockCodes:
        file2Write.write(stockCode)
        # 增长率缓存
        IncreaseRates = []
        for key in ItemsToDealList:
            indexOfYears = 0
            IncreaseRate = {}
            for year in years:
                if (indexOfYears < len(years) - 1):
                    IncreaseRate[stockCode + "_" + key + "_" + years[indexOfYears + 1] + "~" + years[indexOfYears]] = str(\
                        (float(KeyValuePair[stockCode + "_" + key + "_" + years[indexOfYears]]) - \
                        float(KeyValuePair[stockCode + "_" + key + "_" + years[indexOfYears + 1]])) \
                        / float(KeyValuePair[stockCode + "_" + key + "_" + years[indexOfYears + 1]]) * 100) \
                        .upper()
                    IncreaseRates.append(IncreaseRate)
                    file2Write.write("," + IncreaseRate[stockCode + "_" + key + "_" + years[indexOfYears + 1] + "~" + years[indexOfYears]])
                    indexOfYears += 1
        file2Write.write("\r\n")
        progress.current += 1
        progress()
    progress.done()
    # 计算增长率
print("已完成计算，数据已存入 IncreaseRate.csv 文件中")