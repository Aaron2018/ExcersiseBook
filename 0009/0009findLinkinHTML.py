#encoding:utf-8
# 第 0009 题： 一个HTML文件，找出里面的链接。
htmlFile="python/ExcersiseBook/0009/test.html"
def findParainHTML():
    fileObj=open(htmlFile)
    fileContext=fileObj.read()
    fileLines=fileContext.splitlines()
    for line in fileLines:
        line=line.replace(" ",'')
        line=line.replace('\t','')
        if line[0:2]=='<a' and line[-4:]=='</a>':
            print(line)


findParainHTML()