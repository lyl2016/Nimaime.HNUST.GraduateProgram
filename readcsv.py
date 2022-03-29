with open("/Volumes/Seagate/下载/FinacialData/sh600000/sh600000_lrb.csv") as file:
	line_count = 0
	#读取文件每一行
	for line in file:
		varis_count = 0
		if (line_count == 0):
			#首行表头处理
			line_count += 1
		else:
			#按行展开每一列
			varis = line.split(",")
			for vari in varis:
				if (vari.upper().strip() != "NAN"):
					print(vari.upper())
			line_count += 1