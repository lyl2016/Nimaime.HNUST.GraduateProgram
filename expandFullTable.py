import os
from func import ProgressBar
# 设定基准目录
foldPath = "/Volumes/Seagate/下载/FinacialData/"
# 遍历股票代码
stockCodes = os.listdir(foldPath)
progress = ProgressBar(len(stockCodes), fmt=ProgressBar.FULL)
for stockCode in stockCodes:
    # 表头 => 数据
    KeyValuePair = {}
    # 将新生成的full表展开单行
    fullTableFileName = foldPath + stockCode + "/" + stockCode + "_full.csv"
    with open(fullTableFileName, encoding='utf-8') as fullTable:
        headers = fullTable.readline().strip().split(",")
        headers.remove(headers[0])
        seasons = headers
        # 表头：项目A_季度&
        keys = []
        # 数据：ValueOf(项目A_季度&)
        values = []
        for line in fullTable:
            # 单行内所有值
            cells = line.strip().upper().split(",")
            # 行首作为项目名称
            key = cells[0]
            keys.append(key)
            # 单行内所有值移除行首作为所有数据值
            cells.remove(key)
            values = cells

            seasonIndex = 0
            for value in values:
                if (seasonIndex < len(seasons)):
                    KeyValuePair[key + "_" + str(seasons[seasonIndex])] = value
                    seasonIndex += 1

    expandTableHeadersLine = str()
    expandTableValuesLine = str()
    fullExpandTableFileName = foldPath + stockCode + \
        "/" + stockCode + "_full_expand.csv"
    with open(fullExpandTableFileName, "w", encoding='gbk') as file2Write:
        expandTableHeadersLine += "股票代码"
        expandTableValuesLine += str(stockCode)
        for key, value in KeyValuePair.items():
            expandTableHeadersLine += str("," + key)
            expandTableValuesLine += str("," + value)
        file2Write.writelines(expandTableHeadersLine + "\r\n")
        file2Write.writelines(expandTableValuesLine)
    progress.current += 1
    progress()
progress.done()
