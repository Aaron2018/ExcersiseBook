# encoding:utf-8
# 第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
import os


def CountCodeLines(path):
    for home, dirs, files in os.walk(path):
        for fileName in files:
            if fileName[-3:] == '.py':
                print(os.path.join(home, fileName))
path1="/Users/carey/Library/Mobile Documents/com~apple~CloudDocs/Documents/vscode/python"
CountCodeLines(path1)