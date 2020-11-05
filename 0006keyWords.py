# encoding=utf-8
# 第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
import string

def keyWords():
    fileObject = open('test.txt')
    try:
        fileContext = fileObject.read()
        fileSplit = fileContext.split()

        wordsCounter = dict()
        wordsKeys = wordsCounter.keys()
        for i in fileSplit:
            i = i.lower()
            if i in wordsKeys:
                wordsCounter[i] += 1
            else:
                wordsCounter[i] = 1
    finally:
        wordsCounter1 = sorted(wordsCounter.items(), key=lambda d: d[1], reverse=True)
        print('This is original word list: ', wordsCounter)
        print('This is sorted word list: ', wordsCounter1)
        print('This is the key word: ', wordsCounter1[0])
        fileObject.close()


keyWords()
