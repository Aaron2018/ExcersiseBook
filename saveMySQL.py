#第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

import b0001activateCode
import pymysql

def createDB():
    db=pymysql.connect(host='localhost',user='root',password='Newme2020',port=3306)
    cursor=db.cursor()
    try:
        cursor.execute("CREATE DATABASE test_db DEFAULT CHARACTER SET utf8")
        print("Database created")
    except:
        print("Database already exists")
    db.close()
    

def createTable():
    db=pymysql.connect(host='localhost',user='root',password='Newme2020',port=3306,db='test_db')
    cursor=db.cursor()
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS test_table(id VARCHAR(255) NOT NULL, code VARCHAR(255) NOT NULL, PRIMARY KEY (id))")
        print("Table created")
    except:
        print("Table already exists")
    db.close()
    

def insertData(value):
    db=pymysql.connect(host='localhost',user='root',password='Newme2020',port=3306,db='test_db')
    cursor=db.cursor()
    sql="INSERT INTO test_table(id, code) values(%s, %s)"
    try:
        cursor.execute(sql,value)
        db.commit()
        print('insert successfully')
    except:
        db.rollback()
        print('insert failed')
    db.close()

createDB()
createTable()
codes=b0001activateCode.activCode(10,10)
id0=0
for code in codes:
    insertData((str('id'+str(id0)),code))
    id0+=1