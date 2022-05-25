# -*- coding:utf-8 –*-
import time
import os
import numpy as np
import re
import datetime
import efinance as ef
import datetime as dt
import pandas as pd

# 设定基准目录
foldPath = "/Users/liuyonglin/Desktop/毕业设计/"

def GetCodeList(filename):
    codelist = []
    with open(filename, 'r', encoding="utf-8-sig") as ListFile:
        while True:
            line = ListFile.readline().strip()
            if not line:
                break
            else:
                codelist.append(line)
    return codelist


CodeList = GetCodeList(foldPath + "/GraduateProgram/address_number.txt")
infoList = []
for i in range(len(CodeList)):  # ):
    print(i)
    baseinfo = []
    try:
        baseinfo = ef.stock.getter.get_base_info_single(CodeList[i][2:]).tolist()
    except:
        print("Error at : CodeList[i]")
    if(len(baseinfo) > 0):
        infoList.append(baseinfo)
baseinfo = ef.stock.getter.get_base_info_single(CodeList[1][2:])
OldTable = pd.DataFrame(infoList)
OldTable.columns = baseinfo.index.tolist()
OldTable.to_csv(foldPath + "StockInfo2.csv", mode='w',
                encoding="utf-8", index=0, header=True, na_rep='NAN')
