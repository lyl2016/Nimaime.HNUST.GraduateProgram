from func import ProgressBar
# 设定基准目录
foldPath = "/Users/liuyonglin/Desktop/毕业设计/"
Lies = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",]

with open(foldPath + "Func.txt", "w", encoding="gbk") as file2write:
    A = 2
    while (A <= 36):
        for Lie in Lies:
            file2write.write("=SUMIFS(50_!C2:C1024,50_!A2:A1024,'50%收益统计'!A" + str(A) + ",50_!B2:B1024,'50%收益统计'!" + Lie + "1)\t")
        #file2write.write("=SUMIFS(复权价格!D2:D65535,复权价格!A2:A65535,A" + str(A) + ")\t")
        file2write.write("\r\n")
        A += 1
