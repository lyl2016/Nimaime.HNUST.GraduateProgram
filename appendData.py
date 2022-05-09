# -*- coding: UTF-8 -*-
import os
from func import ProgressBar
# 设定基准目录
foldPath = "/Users/liuyonglin/Desktop/毕业设计/"
# 遍历股票代码
stockCodes = os.listdir(foldPath + "FinacialData/")
print("正在生成Append表：")
progress = ProgressBar(len(stockCodes), fmt=ProgressBar.FULL)
for stockCode in stockCodes:
    if (stockCode[0] == '.'):
        continue
    lrbPath = foldPath + "FinacialData/" + stockCode + "/" + stockCode + "_lrb.csv"  # 利润表路径
    xjllbPath = foldPath + "FinacialData/" + stockCode + "/" + stockCode + "_xjllb.csv"  # 现金流量表
    zcfzbPath = foldPath + "FinacialData/" + stockCode + "/" + stockCode + "_zcfzb.csv"  # 资产负债表
    lines = []
    with open(lrbPath, encoding='utf-8') as lrbContent:
        for line in lrbContent:
            lines.append(line)
    with open(xjllbPath, encoding='utf-8') as xjllbContent:
        xjllbContent.readline()
        for line in xjllbContent:
            lines.append(line)
    with open(zcfzbPath, encoding='utf-8') as zcfzbContent:
        zcfzbContent.readline()
        for line in zcfzbContent:
            lines.append(line)

    # 合并三个文件
    fullTableFileName = foldPath + "FinacialData/" + stockCode + "/" + stockCode + "_full.csv"
    with open(fullTableFileName, "w", encoding='utf-8') as file2Write:
        for line in lines:
            file2Write.write(line)

    progress.current += 1
    progress()
progress.done()
