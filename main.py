# -*- coding: UTF-8 -*-

import os
import xlrd

structStr = ""

for dir in os.listdir('.'):                             # 遍历当前目录所有问价和目录
    child = os.path.join('.', dir)                      # 加上路径，否则找不到
    if os.path.isfile(child):                         # 如果是文件，则直接判断扩展名
        fileName = str.split(os.path.basename(child), ".")[0]
        extentName = str.split(os.path.basename(child), ".")[1]
        if extentName == 'xlsx':
            workbook = xlrd.open_workbook(child)
            sheet = workbook.sheet_by_index(0)
            structStr += "struct " + fileName+ "\n"
            structStr += "{\n"
            for Index in range(0, sheet.ncols):
                structStr += "\t" + sheet.row(1)[Index].value + " "
                structStr += sheet.row(0)[Index].value + ";\n"
            structStr += "};\n"

StructFile = open(u"struct.h", "w+")
StructFile.write(structStr)

StructFile.close()

