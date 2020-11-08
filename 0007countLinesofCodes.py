# encoding:utf-8
# 第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
import os

path = "/Users/carey/Library/Mobile Documents/com~apple~CloudDocs/Documents/vscode/python/"
def countLinesOfPyFiles():
    def CountLines(pyfile):
        pyfileObj = open(path+pyfile)
        pyfileContext = pyfileObj.read()
        pyfileSplit = pyfileContext.splitlines()
        print(pyfile + " " + str(len(pyfileSplit)))
    for home, dirs, files in os.walk(path):
        for fileName in files:
            if fileName[-3:] == '.py':
                CountLines(fileName)

countLinesOfPyFiles()
