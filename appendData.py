import os
#设定基准目录
foldPath = "/Volumes/Seagate/下载/FinacialData/"
#遍历股票代码
for stockCode in os.listdir(foldPath):
	lrbPath = foldPath + stockCode + "/" + stockCode + "_lrb.csv"#利润表路径
	xjllbPath = foldPath + stockCode + "/" + stockCode + "_xjllb.csv"#现金流量表
	zcfzbPath = foldPath + stockCode + "/" + stockCode + "_zcfzb.csv"#资产负债表
	lines = str([])
	with open(lrbPath) as lrbContent:
		for line in lrbContent:
			lines.append(line)
	with open(xjllbPath) as xjllbContent:
		for line in xjllbContent:
			lines.append(line)
	with open(zcfzbPath) as zcfzbContent:
		for line in zcfzbContent:
			lines.append(line)
	
	#合并三个文件
	newFileName = foldPath + stockCode + "/" + stockCode + "_full.csv"
	with open(newFileName,"w") as file2Write:
		for line in lines:
			if (line.split(",")[1].strip().upper() != "NAN"):
				file2Write.write(line)
			print("已写入文件" + newFileName)
