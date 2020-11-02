#第 0003 题： 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。

import redis
import b0001activateCode

def saveDataRedis(name1,value1):
    redis_conn.set(name=name1,value=value1)
    print("Value saved")


redis_conn=redis.Redis(host='localhost',port=6379,password='',db=0)
print('Redis connected successfully')

name0=1
for i in b0001activateCode.activCode(10,10):
    saveDataRedis('name'+str(name0),i)
    name0+=1