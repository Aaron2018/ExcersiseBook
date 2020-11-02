#第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。
import string

def countWords(text1):
    if text1 in string.punctuation or text1=='':
        counter=0
    else:
        counter=1
    letter0=text1[0]
    for letter1 in text1:
        if (letter0 in string.punctuation or letter0==' ') and (letter1 not in string.punctuation and letter1!=' '):
            counter+=1
        letter0=letter1
    return counter

print(countWords(input('please input some text: ')))