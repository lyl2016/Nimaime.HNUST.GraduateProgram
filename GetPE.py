#-*- coding:utf-8 –*-
import time
import os
import re
import datetime
import efinance as ef
import datetime as dt
import pandas as pd

def GetCodeList(filename):
    codelist=[]
    with open(filename, 'r',encoding="utf-8-sig") as ListFile:    #all-mid.txt 341
        while True:
            line = ListFile.readline().replace("\n","").strip()
            if not line:
                break
            else:
                codelist.append(line)
    return codelist
    

CodeList=GetCodeList("address_number.txt")
infoList=[]
for i in range(len(CodeList)):#):
    print(i)
    baseinfo=[]
    try:
        baseinfo=ef.stock.getter.get_base_info_single(CodeList[i][2:]).tolist()
    except:
        print("Error at : CodeList[i]" )
    if(len(baseinfo)>0):
        infoList.append(baseinfo)
baseinfo=ef.stock.getter.get_base_info_single(CodeList[1][2:])
OldTable=pd.DataFrame(infoList)
OldTable.columns=baseinfo.index.tolist()
OldTable.to_csv("StockInfo1.csv", mode='w',encoding="utf-8-sig", index=0, header=True,na_rep='NaN')

