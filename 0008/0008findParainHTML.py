# encoding:utf-8
# 第 0008 题： 一个HTML文件，找出里面的正文。

htmlFile="python/ExcersiseBook/0008/test.html"
def findParainHTML():
    fileObj=open(htmlFile)
    fileContext=fileObj.read()
    fileLines=fileContext.splitlines()
    for line in fileLines:
        line=line.replace(" ",'')
        line=line.replace('\t','')
        if line[0:3]=='<p>' and line[-4:]=='</p>':
            print(line)


findParainHTML()