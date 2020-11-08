# encoding:utf-8
#https://www.jianshu.com/p/193d2ff17a27
#激活码


import random
import string

# 激活码生成
def activation_code(count, length):    
    # count 数量    
    # length 长度    
    base = string.ascii_uppercase + string.ascii_lowercase + string.digits    # 生成激活码可能包含的字符集（大写字母、小写字母、数字）
    result=[''.join(random.sample(base, length)) for i in range(count)]
    return result
print(activation_code(10, 16))   # 获取10个长度为16个字符的激活码 