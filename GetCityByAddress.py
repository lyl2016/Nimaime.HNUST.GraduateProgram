# -*- coding: UTF-8 -*-
import json
import requests
import urllib.request, urllib.parse, urllib.error
import hashlib
import time
import pandas as pd
import csv
filename = "/Users/liuyonglin/Downloads/address_2021.csv"
# get请求：url+params请求参数
url = "https://restapi.amap.com/v3/geocode/geo?parameters"
cnt = 0
with open(filename, encoding='utf-8') as csvfile:
    csvfile.readline()
    for line in csvfile:
        code = line.strip().split(",")[0]
        name = line.strip().split(",")[1]
        addressString = line.strip().split(",")[2]
        # http请求参数
        p = {"key": "fd93bde9cbb20ec74a62efb0d9bbd9ea", "address": addressString}
        # print(addressString)
        httpResponse = requests.get(url, params=p)
        jsonDecodeResult = json.loads(httpResponse.text)
        cnt += 1
        print(cnt)
        if (cnt % 1000 == 0):
            time.sleep(5)
        with open("/Users/liuyonglin/Downloads/address.csv", "a", encoding='utf-8') as file2write:
            file2write.write(code + "," + name + "," + addressString + "," + str(jsonDecodeResult["geocodes"][0]["city"]) + "\r\n")